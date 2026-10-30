"""The character encoding of a response, as the HTML Living Standard determines it with the
Encoding Standard (filter-alfa.md): the BOM, then the charset of the HTTP Content-Type, then the
prescan of the first 1024 bytes for a <meta charset> or <meta http-equiv=content-type>.

Without any of them the HTML standard leaves the choice to the user agent (autodetection or the
locale's default, windows-1252 for Spanish). Alfa decides it the same way every time: UTF-8 if
the bytes are valid UTF-8, else windows-1252, and the output says so ("detectada").

Labels and names are the table of the Encoding Standard, §4.2 "Names and labels" (version frozen
in references/, whatwg-encoding). Decoding replaces an invalid sequence with U+FFFD, as the
Encoding Standard does; windows-1252 maps its five undefined bytes to the C1 code points.
"""
from __future__ import annotations

import codecs
import re

# Encoding Standard §4.2: name → labels (each label is ASCII case-insensitive)
LABELS = {
    "UTF-8": "unicode-1-1-utf-8 unicode11utf8 unicode20utf8 utf-8 utf8 x-unicode20utf8",
    "IBM866": "866 cp866 csibm866 ibm866",
    "ISO-8859-2": "csisolatin2 iso-8859-2 iso-ir-101 iso8859-2 iso88592 iso_8859-2 iso_8859-2:1987 l2 latin2",
    "ISO-8859-3": "csisolatin3 iso-8859-3 iso-ir-109 iso8859-3 iso88593 iso_8859-3 iso_8859-3:1988 l3 latin3",
    "ISO-8859-4": "csisolatin4 iso-8859-4 iso-ir-110 iso8859-4 iso88594 iso_8859-4 iso_8859-4:1988 l4 latin4",
    "ISO-8859-5": "csisolatincyrillic cyrillic iso-8859-5 iso-ir-144 iso8859-5 iso88595 iso_8859-5 iso_8859-5:1988",
    "ISO-8859-6": "arabic asmo-708 csiso88596e csiso88596i csisolatinarabic ecma-114 iso-8859-6 iso-8859-6-e "
                  "iso-8859-6-i iso-ir-127 iso8859-6 iso88596 iso_8859-6 iso_8859-6:1987",
    "ISO-8859-7": "csisolatingreek ecma-118 elot_928 greek greek8 iso-8859-7 iso-ir-126 iso8859-7 iso88597 "
                  "iso_8859-7 iso_8859-7:1987 sun_eu_greek",
    "ISO-8859-8": "csiso88598e csisolatinhebrew hebrew iso-8859-8 iso-8859-8-e iso-ir-138 iso8859-8 iso88598 "
                  "iso_8859-8 iso_8859-8:1988 visual",
    "ISO-8859-8-I": "csiso88598i iso-8859-8-i logical",
    "ISO-8859-10": "csisolatin6 iso-8859-10 iso-ir-157 iso8859-10 iso885910 l6 latin6",
    "ISO-8859-13": "iso-8859-13 iso8859-13 iso885913",
    "ISO-8859-14": "iso-8859-14 iso8859-14 iso885914",
    "ISO-8859-15": "csisolatin9 iso-8859-15 iso8859-15 iso885915 iso_8859-15 l9",
    "ISO-8859-16": "iso-8859-16",
    "KOI8-R": "cskoi8r koi koi8 koi8-r koi8_r",
    "KOI8-U": "koi8-ru koi8-u",
    "macintosh": "csmacintosh mac macintosh x-mac-roman",
    "windows-874": "dos-874 iso-8859-11 iso8859-11 iso885911 tis-620 windows-874",
    "windows-1250": "cp1250 windows-1250 x-cp1250",
    "windows-1251": "cp1251 windows-1251 x-cp1251",
    "windows-1252": "ansi_x3.4-1968 ascii cp1252 cp819 csisolatin1 ibm819 iso-8859-1 iso-ir-100 iso8859-1 "
                    "iso88591 iso_8859-1 iso_8859-1:1987 l1 latin1 us-ascii windows-1252 x-cp1252",
    "windows-1253": "cp1253 windows-1253 x-cp1253",
    "windows-1254": "cp1254 csisolatin5 iso-8859-9 iso-ir-148 iso8859-9 iso88599 iso_8859-9 iso_8859-9:1989 "
                    "l5 latin5 windows-1254 x-cp1254",
    "windows-1255": "cp1255 windows-1255 x-cp1255",
    "windows-1256": "cp1256 windows-1256 x-cp1256",
    "windows-1257": "cp1257 windows-1257 x-cp1257",
    "windows-1258": "cp1258 windows-1258 x-cp1258",
    "x-mac-cyrillic": "x-mac-cyrillic x-mac-ukrainian",
    "GBK": "chinese csgb2312 csiso58gb231280 gb2312 gb_2312 gb_2312-80 gbk iso-ir-58 x-gbk",
    "gb18030": "gb18030",
    "Big5": "big5 big5-hkscs cn-big5 csbig5 x-x-big5",
    "EUC-JP": "cseucpkdfmtjapanese euc-jp x-euc-jp",
    "ISO-2022-JP": "csiso2022jp iso-2022-jp",
    "Shift_JIS": "csshiftjis ms932 ms_kanji shift-jis shift_jis sjis windows-31j x-sjis",
    "EUC-KR": "cseuckr csksc56011987 euc-kr iso-ir-149 korean ks_c_5601-1987 ks_c_5601-1989 ksc5601 ksc_5601 "
              "windows-949",
    "replacement": "csiso2022kr hz-gb-2312 iso-2022-cn iso-2022-cn-ext iso-2022-kr replacement",
    "UTF-16BE": "unicodefffe utf-16be",
    "UTF-16LE": "csunicode iso-10646-ucs-2 ucs-2 unicode unicodefeff utf-16 utf-16le",
    "x-user-defined": "x-user-defined",
}
BY_LABEL = {label: name for name, labels in LABELS.items() for label in labels.split()}

# The Python codec of each encoding (replacement and x-user-defined are decoded by hand)
CODECS = {
    "UTF-8": "utf-8", "IBM866": "cp866", "ISO-8859-2": "iso8859_2", "ISO-8859-3": "iso8859_3",
    "ISO-8859-4": "iso8859_4", "ISO-8859-5": "iso8859_5", "ISO-8859-6": "iso8859_6", "ISO-8859-7": "iso8859_7",
    "ISO-8859-8": "iso8859_8", "ISO-8859-8-I": "iso8859_8", "ISO-8859-10": "iso8859_10",
    "ISO-8859-13": "iso8859_13", "ISO-8859-14": "iso8859_14", "ISO-8859-15": "iso8859_15",
    "ISO-8859-16": "iso8859_16", "KOI8-R": "koi8_r", "KOI8-U": "koi8_u", "macintosh": "mac_roman",
    "windows-874": "cp874", "windows-1250": "cp1250", "windows-1251": "cp1251", "windows-1252": "cp1252",
    "windows-1253": "cp1253", "windows-1254": "cp1254", "windows-1255": "cp1255", "windows-1256": "cp1256",
    "windows-1257": "cp1257", "windows-1258": "cp1258", "x-mac-cyrillic": "mac_cyrillic", "GBK": "gbk",
    "gb18030": "gb18030", "Big5": "big5hkscs", "EUC-JP": "euc_jp", "ISO-2022-JP": "iso2022_jp",
    "Shift_JIS": "cp932", "EUC-KR": "cp949", "UTF-16BE": "utf-16-be", "UTF-16LE": "utf-16-le",
}
BOMS = ((b"\xef\xbb\xbf", "UTF-8"), (b"\xfe\xff", "UTF-16BE"), (b"\xff\xfe", "UTF-16LE"))
WS = " \t\n\f\r"


def _c1(error: UnicodeDecodeError):
    """windows-1252 in the Encoding Standard: 0x81, 0x8D, 0x8F, 0x90 and 0x9D are U+0081… itself."""
    byte = error.object[error.start]
    return (chr(byte) if 0x80 <= byte <= 0x9F else "�"), error.start + 1


codecs.register_error("alfa-windows-1252", _c1)


def get_encoding(label: str | None) -> str | None:
    """Encoding Standard, "get an encoding": the name of a label, or None (failure)."""
    if label is None:
        return None
    return BY_LABEL.get(label.strip(WS).lower())


def charset_param(content_type: str | None) -> str | None:
    """The charset parameter of a Content-Type header, unquoted."""
    if not content_type:
        return None
    m = re.search(r";\s*charset\s*=\s*(\"?)([^\";]*)\1", content_type, re.I)
    return m.group(2).strip() if m else None


def _charset_from_content(content: str) -> str | None:
    """HTML: the algorithm for extracting a character encoding from a meta element."""
    i, low = 0, content.lower()
    while True:
        i = low.find("charset", i)
        if i < 0:
            return None
        i += 7
        while i < len(content) and content[i] in WS:
            i += 1
        if i >= len(content) or content[i] != "=":
            continue
        i += 1
        while i < len(content) and content[i] in WS:
            i += 1
        if i >= len(content):
            return None
        if content[i] in "\"'":
            end = content.find(content[i], i + 1)
            return content[i + 1:end] if end > 0 else None
        m = re.match(r"[^\t\n\f\r ;]+", content[i:])
        return m.group(0) if m else None


TAG = re.compile(r"<!--.*?-->|<meta[\t\n\f\r /](?P<meta>[^>]*)>|</?[A-Za-z][^>]*>|<[!/?][^>]*>", re.S | re.I)
ATTR = re.compile(r"([^\t\n\f\r />=][^\t\n\f\r />=]*)(?:[\t\n\f\r ]*=[\t\n\f\r ]*(\"[^\"]*\"|'[^']*'|[^\t\n\f\r >]*))?")


def prescan(head: bytes) -> str | None:
    """HTML: prescan a byte stream to determine its encoding (the first 1024 bytes)."""
    text = head[:1024].decode("latin-1")
    for m in TAG.finditer(text):
        if m.group("meta") is None:
            continue
        attrs: dict[str, str] = {}
        for a in ATTR.finditer(m.group("meta")):
            value = a.group(2) or ""
            if value[:1] in "\"'" and value[-1:] == value[:1] and len(value) > 1:
                value = value[1:-1]
            attrs.setdefault(a.group(1).lower(), value)
        if "charset" in attrs:
            name = get_encoding(attrs["charset"])
        elif "content" in attrs and attrs.get("http-equiv", "").lower() == "content-type":
            name = get_encoding(_charset_from_content(attrs["content"]))
        else:
            continue
        if name is None:
            continue
        if name in ("UTF-16BE", "UTF-16LE"):
            return "UTF-8"
        return "windows-1252" if name == "x-user-defined" else name
    return None


def sniff(raw: bytes, content_type: str | None = None) -> tuple[str, str, int]:
    """(encoding, where it comes from, bytes of BOM to skip): "bom", "http", "meta" or "detectada"."""
    for bom, name in BOMS:
        if raw.startswith(bom):
            return name, "bom", len(bom)
    name = get_encoding(charset_param(content_type))
    if name:
        return name, "http", 0
    name = prescan(raw)
    if name:
        return name, "meta", 0
    try:
        raw.decode("utf-8", errors="strict")
        return "UTF-8", "detectada", 0
    except UnicodeDecodeError:
        return "windows-1252", "detectada", 0


def decode(raw: bytes, content_type: str | None = None) -> tuple[str, str, str]:
    """(text, encoding, where it comes from) of the bytes of a response."""
    name, source, skip = sniff(raw, content_type)
    body = raw[skip:]
    if name == "replacement":
        text = "�" if body else ""
    elif name == "x-user-defined":
        text = "".join(chr(b) if b < 0x80 else chr(0xF780 + b - 0x80) for b in body)
    else:
        text = body.decode(CODECS[name], errors="alfa-windows-1252" if name == "windows-1252" else "replace")
    return text, name, source
