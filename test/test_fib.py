from pytest import CaptureFixture
from src.interpreter import process_file


def test_fib5(capfd: CaptureFixture):
    process_file("./files/fib5.json")
    assert "5\n" == capfd.readouterr().out

def test_fib10(capfd: CaptureFixture):
    process_file("./files/fib10.json")
    assert "55\n" == capfd.readouterr().out

def test_fib15(capfd: CaptureFixture):
    process_file("./files/fib15.json")
    assert "610\n" == capfd.readouterr().out

def test_fib20(capfd: CaptureFixture):
    process_file("./files/fib20.json")
    assert "6765\n" == capfd.readouterr().out

def test_fib25(capfd: CaptureFixture):
    process_file("./files/fib25.json")
    assert "75025\n" == capfd.readouterr().out

def test_fib30(capfd: CaptureFixture):
    process_file("./files/fib30.json")
    assert "832040\n" == capfd.readouterr().out
