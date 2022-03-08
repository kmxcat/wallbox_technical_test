import pytest
from coin_flips import CoinFlips

class TestCoinFlips:
    """
    A test class to verify the methods implemented in coin_flips.py.
    
    ...
    
    Methods
    -------
    test_wrong_values_dict()
        Tests the wrong values dictionary, which should store the position and value of the values that does not match with the expected vector. The type of the result must be a dictionary.
    test_find_min_coin_permutations_multivalues(cf_vector, expected)
        Method to test several cases for different coin flips sequences, including large sequences, small onces and mixed differently. The type of the result must be an integer.   
    """

    def test_wrong_values_dict(self):
        """Every wrong value should be stored in a dict using a key-value syntax, and the result of this function should be a dictionary"""
        result_dict = CoinFlips.get_wrong_values_dict (self, [0, 1, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1])
        assert result_dict == {2:1, 7:0}
        assert type(result_dict) is dict
    
    @pytest.mark.parametrize(
        "cf_vector, expected",
        [
            ([1], 0),
            ([0, 1, 1], 1),
            ([0], 0),
            ([0, 1, 0], 0),
            ([1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0], 13)
        ]
    )
    def test_find_min_coin_permutations_multivalues(self, cf_vector, expected):
        """The minimum amount of permutations in the given cf_vectotr should be equal as expected value, and should always be an integer"""
        result = CoinFlips.find_min_coin_permutations(self, cf_vector)
        assert result == expected
        assert type(result) is int