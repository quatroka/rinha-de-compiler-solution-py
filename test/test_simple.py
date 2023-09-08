from pytest import CaptureFixture
from src.interpreter import process_file


def test_simple(capfd: CaptureFixture):
    process_file("./files/simple.json")
    assert "20\n2\n" == capfd.readouterr().out


def test_simple2(capfd: CaptureFixture):
    process_file("./files/simple2.json")
    assert "20\n2\nNone\n" == capfd.readouterr().out


def test_simple3(capfd: CaptureFixture):
    process_file("./files/simple3.json")
    assert "5\n1\n" == capfd.readouterr().out


def test_simple4(capfd: CaptureFixture):
    process_file("./files/simple4.json")
    assert "olar\n" == capfd.readouterr().out


def test_simple5(capfd: CaptureFixture):
    process_file("./files/simple5.json")
    assert "True\n" == capfd.readouterr().out
