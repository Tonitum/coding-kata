from leetcode.python.two_sum.two_sum import Solution


class TestSolution:
    def test_two_sum_case_one(self):
        nums = [2,7,11,15]
        target = 9
        desired_target = [0,1]
        handle = Solution()
        res = handle.two_sum(nums, target)
        assert res == desired_target

    def test_two_sum_case_two(self):
        nums = [3,2,4]
        target = 6
        desired_target = [1,2]
        handle = Solution()
        res = handle.two_sum(nums, target)
        assert res == desired_target

    def test_two_sum_case_three(self):
        nums = [3,3]
        target = 6
        desired_target = [0,1]
        handle = Solution()
        res = handle.two_sum(nums, target)
        assert res == desired_target
