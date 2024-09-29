def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    """
    You have a long flowerbed in which some of the plots are planted, and some
    are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty
    and 1 means not empty, and an integer n, return true if n new flowers can be
    planted in the flowerbed without violating the no-adjacent-flowers rule and
    false otherwise.
    """
    total_free_plots = 0
    total_plots = len(flowerbed)

    if n == 0:
        return True

    if n > total_plots:
        return False

    if total_plots == 1:
        if flowerbed[0] == 0:
            return True
        return False

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        total_free_plots = total_free_plots + 1

    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        total_free_plots = total_free_plots + 1

    for plot_index in range(1, total_plots - 1):
        if flowerbed[plot_index] == 1:
            continue

        if flowerbed[plot_index - 1] == 0 and flowerbed[plot_index + 1] == 0:
            total_free_plots = total_free_plots + 1
            flowerbed[plot_index] = 1

    return total_free_plots >= n
