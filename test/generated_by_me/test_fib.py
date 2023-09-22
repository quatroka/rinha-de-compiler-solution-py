from pytest import CaptureFixture
from src.interpreter import process_file


def test_fib5(capfd: CaptureFixture):
    process_file("./files/generated_by_me/fib5.rinha.json")
    assert "5\n" == capfd.readouterr().out


def test_fib10(capfd: CaptureFixture):
    process_file("./files/generated_by_me/fib10.rinha.json")
    assert "55\n" == capfd.readouterr().out


def test_fib15(capfd: CaptureFixture):
    process_file("./files/generated_by_me/fib15.rinha.json")
    assert "610\n" == capfd.readouterr().out


def test_fib20(capfd: CaptureFixture):
    process_file("./files/generated_by_me/fib20.rinha.json")
    assert "6765\n" == capfd.readouterr().out


def test_fib25(capfd: CaptureFixture):
    process_file("./files/generated_by_me/fib25.rinha.json")
    assert "75025\n" == capfd.readouterr().out


def test_fib30(capfd: CaptureFixture):
    process_file("./files/generated_by_me/fib30.rinha.json")
    assert "832040\n" == capfd.readouterr().out
