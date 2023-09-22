from pytest import CaptureFixture
from src.interpreter import process_file


def test_tuple1(capfd: CaptureFixture):
    process_file("./files/generated_by_me/tuple1.rinha.json")
    assert "1\n2\n" == capfd.readouterr().out


def test_tuple2(capfd: CaptureFixture):
    process_file("./files/generated_by_me/tuple2.rinha.json")
    assert "1\n2\n" == capfd.readouterr().out
