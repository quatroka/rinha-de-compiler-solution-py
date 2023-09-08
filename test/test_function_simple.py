from pytest import CaptureFixture
from src.interpreter import process_file


def test_function_simple1(capfd: CaptureFixture):
    process_file("./files/functionSimple1.json")
    assert "4\n" == capfd.readouterr().out


def test_function_simple2(capfd: CaptureFixture):
    process_file("./files/functionSimple2.json")
    assert "6\n" == capfd.readouterr().out


def test_function_simple3(capfd: CaptureFixture):
    process_file("./files/functionSimple3.json")
    assert "6\n" == capfd.readouterr().out
