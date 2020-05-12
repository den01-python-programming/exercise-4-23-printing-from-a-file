import pytest
from src.exercise import main
import os

def test_exercise(capsys):
    os.chdir('src')
    main()
    out, err = capsys.readouterr()
    assert out == "In a\nworld\n"
