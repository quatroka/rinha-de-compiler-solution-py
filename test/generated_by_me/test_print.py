from pytest import CaptureFixture
from src.interpreter import process_file


def test_print1(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print1.rinha.json")
    assert "10\n" == capfd.readouterr().out

def test_print2(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print2.rinha.json")
    assert "oi\na\n2\ntrue\n(1, 2)\n(3, 4)\n" == capfd.readouterr().out

def test_print3(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print3.rinha.json")
    assert "prefix: oi\nprefix: a\nprefix: 2\nprefix: true\nprefix: 1\n" == capfd.readouterr().out

def test_print4(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print4.rinha.json")
    assert "true\nfalse\nfalse\ntrue\n---\ntrue\nfalse\nfalse\ntrue\n" == capfd.readouterr().out

def test_print5(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print5.rinha.json")
    assert "4: sufix\n" == capfd.readouterr().out

def test_print6(capfd: CaptureFixture):
    process_file("./files/generated_by_me/print6.rinha.json")
    assert "1\n2\n3\n" == capfd.readouterr().out