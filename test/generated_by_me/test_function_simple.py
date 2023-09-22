from pytest import CaptureFixture
from src.interpreter import process_file


def test_function_simple1(capfd: CaptureFixture):
    process_file("./files/generated_by_me/functionSimple1.rinha.json")
    assert "4\n" == capfd.readouterr().out


def test_function_simple2(capfd: CaptureFixture):
    process_file("./files/generated_by_me/functionSimple2.rinha.json")
    assert "6\n" == capfd.readouterr().out


def test_function_simple3(capfd: CaptureFixture):
    process_file("./files/generated_by_me/functionSimple3.rinha.json")
    assert "6\n" == capfd.readouterr().out
