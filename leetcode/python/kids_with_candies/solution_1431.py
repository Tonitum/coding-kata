def kids_with_candies(candies: list[int], extraCandies: int) -> list[bool]:
    """
    There are n kids with candies. You are given an integer array candies,
    where each candies[i] represents the number of candies the ith kid has,
    and an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after
    giving the ith kid all the extraCandies, they will have the greatest number
    of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
    """
    results: list[bool] = []
    
    # find the largest number in the list
    largest = max(candies)
    for i in candies:
        if i + extraCandies >= largest:
            results.append(True)
            continue
        results.append(False)

    return results

