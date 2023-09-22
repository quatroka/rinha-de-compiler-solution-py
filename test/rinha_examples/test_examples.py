from pytest import CaptureFixture
from src.interpreter import process_file


def test_combination(capfd: CaptureFixture):
    process_file("./files/rinha_examples/combination.rinha.json")
    assert "45\n" == capfd.readouterr().out


def test_fib(capfd: CaptureFixture):
    process_file("./files/rinha_examples/fib.rinha.json")
    assert "55\n" == capfd.readouterr().out


def test_print(capfd: CaptureFixture):
    process_file("./files/rinha_examples/print.rinha.json")
    assert "Hello world\n" == capfd.readouterr().out


def test_sum(capfd: CaptureFixture):
    process_file("./files/rinha_examples/sum.rinha.json")
    assert "15\n" == capfd.readouterr().out
