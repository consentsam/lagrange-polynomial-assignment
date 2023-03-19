from csv_writer import CSVWriter
import itertools


"""
    Returns inverse for a given prime number field `prime_number` => TESTED
"""
def inverse(number,prime_number):
    return pow(number,prime_number-2,prime_number)

"""
    Returns the denominator part of the lagrange l_i(x) => TESTED
"""
def get_denominator(x_points_list_removed_current_point,deleted_x): 
    mult = 1;    
    for i in range(len(x_points_list_removed_current_point)):
        mult *= (deleted_x - x_points_list_removed_current_point[i]);
    return mult;

"""
    Returns the multiplications of a tuple
"""
def get_multiplication_of_a_list(subtuple):
    mult =1;
    for i in range(len(subtuple)):
        mult*=subtuple[i];
    return mult;


"""
    Returns the multiplication of all possible combinations of x at a time 
"""
def x_at_a_time(x_points_list_removed_current_point,x_at_a_time):
    sum_of_x_at_a_time = 0;
    permutations = list(itertools.combinations(x_points_list_removed_current_point, x_at_a_time))
    
    for i in permutations:
        sum_of_x_at_a_time += get_multiplication_of_a_list(i)
    return sum_of_x_at_a_time

"""
    Returns out the numerator coefficients for the polynomial ( x-x_1)( x-x_2)*(x-x_3).... by treating `x_1`,`x_2` as roots
"""
def get_numerator(x_points_list_removed_current_point):
    number_of_points = len(x_points_list_removed_current_point)
    # print("number_of_points => ",number_of_points)
    coefficient_value_list = [1] * (number_of_points+1)
    
    # print(x_points_list_removed_current_point)
    for i in range(1,number_of_points+1):
        sign_of_coefficient = pow(-1,i)
        coefficient_value_list[i] = x_at_a_time(x_points_list_removed_current_point,i) * sign_of_coefficient;
    return list(reversed(coefficient_value_list));

def calculate_lagrange_polynomial(points):
    """
    Calculate lagrange polynomial.

    Consider the example below
    Given points = [[1, 3], [4, 4], [16, 5], [13, 9]], the returned value calculated on base field of 17
    should be list - [1, 13, 3, 3]

    :param points: List of elements of form [x, y]. The returned polynomial should pass through these points

    :return: List[int] - coefficients of lagrange polynomial. The coefficient of lowest power of x
    should be the first element of list
    """
    numerator_list_list = []
    x_points_list = [point[0] for point in points]
    PRIME_NUMBER = 17

    for i in range(len(x_points_list)):
        x_points_list_removed_current_point = x_points_list.copy();
        
        x_to_be_deleted = x_points_list_removed_current_point[i];
        
        del x_points_list_removed_current_point[i];
        
        numerator = get_numerator(x_points_list_removed_current_point);
        
        denominator = get_denominator(x_points_list_removed_current_point,x_to_be_deleted)

        y_to_multiply = points[i][1];
        
        numerator_coefficient_multiplier = (y_to_multiply * inverse(denominator,PRIME_NUMBER))%PRIME_NUMBER

        numerator = [i * numerator_coefficient_multiplier for i in numerator]
        numerator_list_list.append(numerator);
        
    coefficient_sums = [0] * len(numerator_list_list[0]);
    for i in range(len(numerator_list_list)):
        for j in range(len(numerator_list_list[0])):
            coefficient_sums[j] = (coefficient_sums[j] + numerator_list_list[i][j])%PRIME_NUMBER;
    return coefficient_sums;


csv_writer = CSVWriter()
all_polynomial_points = csv_writer.get_points()

lp_coeffs_lst = []
for polynomial_points in all_polynomial_points:
    lp_coeffs = calculate_lagrange_polynomial(polynomial_points)
    lp_coeffs_lst.append(lp_coeffs)

csv_writer.write(lp_coeffs_lst)
