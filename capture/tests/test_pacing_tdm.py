import random
from datetime import datetime

from capture import tdm
from capture.pacing import Pacer, Pacing, draw


def pacing(**over):
    return Pacing.from_plan({"pacing": over})


def test_draw_stays_within_bounds():
    rng = random.Random(1)
    values = [draw(rng, (20, 60)) for _ in range(2000)]
    assert min(values) >= 20 and max(values) <= 60
    assert sum(values) / len(values) < 40  # skewed towards the lower bound


def test_long_pause_every_n_pages():
    p = Pacer(pacing(pause_s=[1, 1], long_every=[3, 3], long_pause_s=[100, 100]), random.Random(1))
    assert [round(p.pause()) for _ in range(6)] == [1, 1, 101, 1, 1, 101]


def test_crawl_delay_raises_the_pause():
    p = Pacer(pacing(pause_s=[1, 2], long_every=[99, 99]), random.Random(1), crawl_delay=10)
    assert p.pause() == 10


def test_hours():
    p = pacing(hours=[9, 21])
    assert p.within_hours(datetime(2026, 10, 25, 9, 0))
    assert not p.within_hours(datetime(2026, 10, 25, 21, 0))


def test_tdmrep_most_specific_location_decides():
    items = tdm.entries('[{"location": "/", "tdm-reservation": 1}, {"location": "/guias/*", "tdm-reservation": 0}]', 200)
    assert tdm.reserved_by_entries(items, "https://x.es/sabanas")
    assert not tdm.reserved_by_entries(items, "https://x.es/guias/elegir-sabanas")
    assert tdm.entries("no json", 200) == [] and tdm.entries("[]", 404) == []


def test_reservation_in_header_or_meta():
    assert tdm.reserved_by_response({"TDM-Reservation": "1"}, None)
    assert tdm.reserved_by_response({}, {"tdm": "1"})
    assert not tdm.reserved_by_response({"tdm-reservation": "0"}, {"tdm": None})
