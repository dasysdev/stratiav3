import pytest


@pytest.fixture(autouse=True)
def paa_dirs(tmp_path, monkeypatch):
    """Each test keeps its seed sets and its output in temporary PAA_SETS and PAA_VAR."""
    monkeypatch.setenv("PAA_SETS", str(tmp_path / "sets"))
    monkeypatch.setenv("PAA_VAR", str(tmp_path / "var"))
    (tmp_path / "sets").mkdir()
    return tmp_path
