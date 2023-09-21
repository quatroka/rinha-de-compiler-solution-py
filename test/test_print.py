from pytest import CaptureFixture
from src.interpreter import process_file


def test_print1(capfd: CaptureFixture):
    process_file("./files/print1.json")
    assert "10\n" == capfd.readouterr().out