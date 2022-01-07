from classes import Mode, Player, Point, Board
from ui_game import pick_mode
import pytest


def test_pick_mode(monkeypatch):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pick_mode() == 1


def test_pick_mode_letter(monkeypatch):
    inputs = iter(['e', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pick_mode() == 2

def test_pick_mode_float(monkeypatch):
    inputs = iter(['3.5', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pick_mode() == 2


