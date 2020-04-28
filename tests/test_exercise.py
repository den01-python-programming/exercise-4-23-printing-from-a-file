import pytest
import src.exercise

def test_exercise():
    main()
    out, err = capsys.readouterr()
    assert out == "In a\nworld\n"
