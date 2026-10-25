import pytest


@pytest.fixture(autouse=True)
def var_dir(tmp_path, monkeypatch):
    """Each test writes its studies and its corpus in temporary MPIR_STUDIES and MPIR_VAR."""
    monkeypatch.setenv("MPIR_STUDIES", str(tmp_path / "studies"))
    monkeypatch.setenv("MPIR_VAR", str(tmp_path / "var"))
    return tmp_path / "var"
