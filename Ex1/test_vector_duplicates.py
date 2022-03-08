import pytest
from vector_duplicates import VectorDuplicates

class TestVectorDuplicates:
    """
    A test class to verify the methods implemented in vector_duplicates.py.
    
    ...
    
    Methods
    -------
    test_unique_values_dict()
        Tests the unique values dictionary of the vector 2, giving an example and expecting always a dictionary as a result.
    test_find_first_repeated_value_multivalues(vector1, vector2, expected)
        Method to test several different cases for both vectors, including limit values, negatives and floats. The type of the result must not be a list.   
    """
    
    def test_unique_values_dict(self):
        """Every unique value of the vector 2 should be stored in a dictionary only once"""
        result_dict = VectorDuplicates.generate_unique_values_dict (self, [1,2,3])
        assert result_dict == {1:True, 2:True, 3:True}
        assert type(result_dict) is dict

    @pytest.mark.parametrize(
        "vector_a, vector_b, expected",
        [
            ([9, 3], [3, 5, 3, 7, 5, 3, 4, 9], 9),
            ([1, 2, 9, 3], [3, 5, 3, 7, 5, 3, 4, 9, 2], 2),
            ([0], [3, 5, 3, 7, 5, 3, 4, 9], None),
            ([-5, 9, 3], [3, 5, 3, 7, 5, -5, 3, 4], -5),
            ([-5, 9, 3], [], None),
            ([2.7, -5, 3], [4, 10, 2.7], 2.7),
            ([], [10, 100, 4, 6, 2, 23], None)
        ]
    )
    def test_find_first_repeated_value_multivalues(self, vector_a, vector_b, expected):
        """The first repeated value of vector_a in vector_b should be expected, and it should not be a list"""
        result = VectorDuplicates.find_first_repeated_value(self, vector_a, vector_b)
        assert result == expected
        assert type(result) is not list