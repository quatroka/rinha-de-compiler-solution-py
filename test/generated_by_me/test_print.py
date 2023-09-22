from pytest import CaptureFixture
from src.interpreter import process_file


def test_print1(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print1.rinha.json")
    assert "10\n" == capfd.readouterr().out
