class VectorDuplicates:
    """
    A class used to handle 2 different vectors and operate between them.
    
    ...
    
    Attributes
    ----------
    v1 : list
        a vector/list taken as reference to compare with a second one and get repeated data.
    v2 : list
        a vector/list which will be iterated to find values which also appeared in the reference vector.
        
    Methods
    -------
    generate_unique_values_dict(vector2)
        Transforms vector 2 into a dictionary with unique values assigned to boolean 'True'. This approach is done to improve the performance of the execution and only iterate the vector 2 once.
    find_first_repeated_value(vector1, vector2)
        Main function to handle the logic of finding the first repeated value in both vectors. Vector 1 is taken as reference.    
    """

    def __init__(self, v1, v2):
        print ("\nThis class has been created to find the first repeated integer number given 2 vectors.")
        self.v1 = v1
        self.v2 = v2
        
    def generate_unique_values_dict (self, vector2):
        v2_dict = {}
        for i in range (len(vector2)):
            if not vector2[i] in v2_dict:
                v2_dict[vector2[i]] = True
        return v2_dict

    def find_first_repeated_value (self, vector1, vector2):
        vector2_dict = v.generate_unique_values_dict (vector2)
        first_repeated_value = None
        for i in range (len(vector1)):
            if vector1[i] in vector2_dict:
                first_repeated_value = vector1[i]
                break
        return first_repeated_value

a = list(map(int, input("\nInput the vector number 1 as comma-separated integers: ").split(',')))
b = list(map(int, input("Input the vector number 2 as comma-separated integers: ").split(',')))

v = VectorDuplicates(a, b)
first_rep_value = v.find_first_repeated_value (a, b)

if first_rep_value is not None:
    print ("\nThe first repeated number is: " + str(first_rep_value))
else:
    print ("\nNone of the values is repeated")