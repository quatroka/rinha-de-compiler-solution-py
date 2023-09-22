from pytest import CaptureFixture
from src.interpreter import process_file


def test_simple(capfd: CaptureFixture):
    process_file("./files/generated_by_me/simple.rinha.json")
    assert "20\n2\n" == capfd.readouterr().out


def test_simple2(capfd: CaptureFixture):
    process_file("./files/generated_by_me/simple2.rinha.json")
    assert "20\n2\nNone\n" == capfd.readouterr().out


def test_simple3(capfd: CaptureFixture):
    process_file("./files/generated_by_me/simple3.rinha.json")
    assert "5\n1\n" == capfd.readouterr().out


def test_simple4(capfd: CaptureFixture):
    process_file("./files/generated_by_me/simple4.rinha.json")
    assert "olar\n" == capfd.readouterr().out


def test_simple5(capfd: CaptureFixture):
    process_file("./files/generated_by_me/simple5.rinha.json")
    assert "True\n" == capfd.readouterr().out
