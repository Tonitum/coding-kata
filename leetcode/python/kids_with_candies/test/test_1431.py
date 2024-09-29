from leetcode.python.kids_with_candies.solution_1431 import kids_with_candies
def test_case_one():
    """
    Input: candies = [2,3,5,1,3], extraCandies = 3
    Output: [true,true,true,false,true]
    Explanation: If you give all extraCandies to:
    - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
    - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
    - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
    - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
    """
    candies = [2, 3, 5, 1, 3]
    extra_candies = 3
    expected = [True, True, True, False, True]
    assert kids_with_candies(candies, extra_candies) == expected

def test_case_two():
    """
    Input: candies = [4,2,1,1,2], extraCandies = 1
    Output: [true,false,false,false,false]
    Explanation: There is only 1 extra candy.
    Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
    """
    candies: list[int] = [4,2,1,1,2]
    extraCandies: int = 1
    expected: list[bool] = [True,False,False,False,False]
    assert kids_with_candies(candies, extraCandies) == expected

def test_case_three():
    """
    Input: candies = [12,1,12], extraCandies = 10
    Output: [true,false,true]
    """
    candies: list[int] = [12,1,12]
    extraCandies: int = 10
    expected: list[bool] = [True,False,True]
    assert kids_with_candies(candies, extraCandies) == expected

