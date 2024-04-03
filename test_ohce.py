import pytest
from ohce import Ohce

@pytest.fixture
def ohce():
    return Ohce()

def test_saludo_buenas_noches(ohce, monkeypatch):
    monkeypatch.setattr("ohce.Ohce.get_hora_actual", lambda self: 1)
    #ohce.name = "Juan"
    #ohce.start("ohce Juan")
    assert ohce.response == "¡Buenas noches Juan!"

def test_saludo_buenos_dias(ohce, monkeypatch):
    monkeypatch.setattr("ohce.Ohce.get_hora_actual", lambda self: 8)
    #ohce.name = "Maria"
    #ohce.start("ohce Maria")
    assert ohce.response == "¡Buenos días Maria!"

def test_saludo_buenas_tardes(ohce, monkeypatch):
    monkeypatch.setattr("ohce.Ohce.get_hora_actual", lambda self: 15)
    #ohce.name = "Pedro"
    #ohce.start("ohce Pedro")
    assert ohce.response == "¡Buenas tardes Pedro!"

def test_reverse_string(ohce):
    assert ohce.reverse_string("hola") == "aloh"

def test_is_palindrome(ohce):
    assert ohce.is_palindrome("radar") == True
    assert ohce.is_palindrome("hello") == False

def test_process_input_stop(ohce):
    ohce.name = "Juan"
    assert ohce.process_input("Stop!") == "Adios Juan!"

def test_process_input_palindrome(ohce):
    assert ohce.process_input("radar") == "radar ¡Bonita palabra!"

def test_process_input_reverse(ohce):
    assert ohce.process_input("hello") == "olleh"



