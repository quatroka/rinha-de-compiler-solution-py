from pytest import CaptureFixture
from src.interpreter import process_file


def test_first_second1(capfd: CaptureFixture):
    process_file("./files/generated_by_me/first_second1.rinha.json")
    assert (
        "Error: first method only accepts tuple as parameter\n"
        == capfd.readouterr().out
    )


def test_first_second2(capfd: CaptureFixture):
    process_file("./files/generated_by_me/first_second2.rinha.json")
    assert (
        "Error: second method only accepts tuple as parameter\n"
        == capfd.readouterr().out
    )
