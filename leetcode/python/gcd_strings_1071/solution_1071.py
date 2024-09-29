import math
def is_a_string_divisor(str1: str, divisor: str) -> bool:
    if str1.count(divisor) * len(divisor) == len(str1):
        return True
    return False

def gcd_of_strings(str1: str, str2: str) -> str:
    prefix_source: str = min(str1, str2)
    prefix_target: str = max(str1, str2)
    prefix_source_len = len(prefix_source)

    # find divisors of prefix source
    divisor_list: list[int] = [1]
    prefix_len_sqrt = math.sqrt(prefix_source_len)

    for i in range(2, math.ceil(prefix_len_sqrt) + 1):
        if prefix_source_len % i == 0:
            divisor_list.append(i)
            divisor_list.append(int(prefix_source_len / i))
    divisor_list.append(prefix_source_len)
    divisor_list.sort()

    for d in reversed(divisor_list):
        prefix_slice = prefix_source[:d]
        if is_a_string_divisor(prefix_target, prefix_slice) and is_a_string_divisor(prefix_source, prefix_slice):
            return prefix_slice

    return ""
