from leetcode.python.can_place_flowers_605.solution_605 import canPlaceFlowers

def test_case_one():
    """
    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: true
    """
    flowerbed = [1,0,0,0,1]
    n = 1
    assert canPlaceFlowers(flowerbed, n)

def test_case_two():
    """
    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: false
    """
    flowerbed = [1,0,0,0,1]
    n = 2
    assert not canPlaceFlowers(flowerbed, n)

def test_case_three():
    flowerbed = [1,0,0,0,0,1]
    n = 2
    assert not canPlaceFlowers(flowerbed, n)

def test_case_four():
    flowerbed = [0,0,1,0,1]
    n = 1
    assert canPlaceFlowers(flowerbed, n)
    
def test_case_five():
    flowerbed = [0]
    n = 1
    assert canPlaceFlowers(flowerbed, n)

def test_case_six():
    flowerbed = [1]
    n = 0
    assert canPlaceFlowers(flowerbed, n)
