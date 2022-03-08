class CoinFlips:   
    """
    A class used to handle multiple sequences of coin flips, given as 1(heads) and 0(tails).
    
    ...
    
    Attributes
    ----------
    cf_vector : list
        a vector/list which contains the sequence of 0s and 1s to be analyzed and efficiently interspersed.
        
    Methods
    -------
    get_opposite_element(current_element)
        Given a 1 returns a 0, and the other way around. This function is used to retrieve the required opposite value when a permutation must be done.
    get_final_expected_vector(original_vector)
        Given any sequence of 1s and 0s, this function calculates the expected output vector which we must acquire. This can be done since we can know the total amount of 0s and 1s, and a requirement is to make them interspersed.
    get_wrong_values_dict(original_vector, expected_vector)
        Given the original and the expected vector, this function compares both vectors and fills a dictionary with the position-value of the wrong values. This dictionary will be used to permutate only those positions that are wrong, making it more efficient.
    find_next_value_in_a_dict(v_dict, value)
        Given which value must be found in a dict, this function finds the expected value in the wrong values dict and return its position, to furtherly be permutated.
    find_min_coin_permutations(coin_flips_vector)
        Main function holding the permutations logic. This method first calculates the expected final vector, then builds the dictionary containing only the wrong values and finally iterates the original vector fixing the wrong values found by an opposite value in the wrong values dict.
        This process should be the most efficient since it is never switching positions which are correctly placed, and only focus on the wrong ones. As a matter of fact, it is only executed if the number of 0s and 1s are the same or different by one, otherwise permutations will not be
        possible to leave the sequence fully interspersed.
    """
    
    def __init__(self, cf_vector):
        print ("\nThis class has been created to find the minimum number of permutations in order to make the given vector interspersed.")
        self.cf_vector = cf_vector

    def get_opposite_element (self, current_element):
        if current_element == 0:
            return 1
        else:
            return 0

    def get_final_expected_vector (self, original_vector):
        if original_vector.count(1) == original_vector.count(0):
            if original_vector[0] == 1:
                expected_vector = [1, 0] * original_vector.count(1)
            else:
                expected_vector = [0, 1] * original_vector.count(0)
        elif original_vector.count(1) > original_vector.count(0):
            expected_vector = [1] + [0, 1] * original_vector.count(0)
        else:
            expected_vector = [0] + [1, 0] * original_vector.count(1)
        return expected_vector
        
    def get_wrong_values_dict (self, original_vector, expected_vector):
        wrong_values_dict = {}
        for i in range(len(original_vector)):
            if original_vector[i] != expected_vector[i]:
                wrong_values_dict[i] = original_vector[i]
        print("\nWrong values dictionary has: " + str(len(wrong_values_dict)) + " items.")
        return wrong_values_dict

    def find_next_value_in_a_dict (self, v_dict, value):
        found_value_pos = -1
        for key, val in v_dict.items():
            if val == value:
                found_value_pos = key
                break
        return found_value_pos
        
    def find_min_coin_permutations (self, coin_flips_vector):
        permutations_counter = 0
        opposite_value_pos = 0
        expected_vector = c.get_final_expected_vector(coin_flips_vector)
        wrong_values_dict = c.get_wrong_values_dict (coin_flips_vector, expected_vector)
        for i in range(len(coin_flips_vector)):
            if i in wrong_values_dict:
                opposite_value_pos = c.find_next_value_in_a_dict(wrong_values_dict, c.get_opposite_element(coin_flips_vector[i]))
                coin_flips_vector[i], coin_flips_vector[opposite_value_pos] = coin_flips_vector[opposite_value_pos], coin_flips_vector[i]
                wrong_values_dict.pop(i)
                wrong_values_dict.pop(opposite_value_pos)
                permutations_counter+=1
        return permutations_counter

#coin_flips_vector = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
coin_flips_vector = list(map(int, input("\nInput the coin flips vector as comma-separated 1s and 0s: ").split(',')))
#coin_flips_vector = [1, 1, 0, 1]
print("\nInitial vector: " + "\n" + str(coin_flips_vector))
print("\nAmount of 1s at initial vector: " + "\n" + str(coin_flips_vector.count(1)))
print("\nAmount of 0s at initial vector: " + "\n" + str(coin_flips_vector.count(0)))

#In order to be permutable, the difference between the total amount of 0s and 1s cannot be higher than 1.
if (coin_flips_vector.count(1) - coin_flips_vector.count(0)) in (-1, 0, 1):
    c = CoinFlips(coin_flips_vector)
    coin_permutations = c.find_min_coin_permutations(coin_flips_vector)
    print("\n\nFinal result: " + "\n" + str(coin_flips_vector))
    print("\nTotal permutations: " + "\n" + str(coin_permutations))
else:
    print ("\nThis list cannot be fully permuted since the amount of '1' and '0' are disaligned by 2 or more.")
