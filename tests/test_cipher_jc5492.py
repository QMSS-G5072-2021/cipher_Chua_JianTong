from cipher_jc5492 import cipher_jc5492 as pkg
import pytest

##part a
def test_word():
    example = "test"
    actual = pkg.cipher(example, 1)
    expected = "uftu"
    assert actual == expected

##part b
def test_negative_shift():
    example = "test"
    actual = pkg.cipher(example, -1)
    expected = "sdrs"
    assert actual == expected
    
##part c
def test_symbols():
    example = "@lphabet"
    actual = pkg.cipher(example,1)
    expected = "@mqibcfu"
    assert actual == expected
    
##part d
def test_shift_string():
    example = "test"
    with pytest.raises(AssertionError):
        pkg.cipher(example, "one")