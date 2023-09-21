from pytest import CaptureFixture
from src.interpreter import process_file


def test_fib10(capfd: CaptureFixture):
    process_file("./files/fib10.json")
    assert "55\n" == capfd.readouterr().out
