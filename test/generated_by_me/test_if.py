from pytest import CaptureFixture
from src.interpreter import process_file


def test_if1(capfd: CaptureFixture):
    process_file("./files/generated_by_me/if1.rinha.json")
    assert "3\n" == capfd.readouterr().out


def test_if2(capfd: CaptureFixture):
    process_file("./files/generated_by_me/if2.rinha.json")
    assert "10\nNone\n" == capfd.readouterr().out


def test_if3(capfd: CaptureFixture):
    process_file("./files/generated_by_me/if3.rinha.json")
    assert "55\nfoi false\n" == capfd.readouterr().out
