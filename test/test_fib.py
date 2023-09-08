from pytest import CaptureFixture
from src.interpreter import process_file

def test_fib(capfd: CaptureFixture):
    process_file('./files/fib.json')
    assert '55\n' == capfd.readouterr().out