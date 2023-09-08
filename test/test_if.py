from pytest import CaptureFixture
from src.interpreter import process_file


def test_if1(capfd: CaptureFixture):
    process_file("./files/if1.json")
    assert "3\n" == capfd.readouterr().out


def test_if2(capfd: CaptureFixture):
    process_file("./files/if2.json")
    assert "10\nNone\n" == capfd.readouterr().out


def test_if3(capfd: CaptureFixture):
    process_file("./files/if3.json")
    assert "55\nfoi false\n" == capfd.readouterr().out
