from leetcode.python.merge_strings_1768.solution_1768 import merge_alternate

class TestSolution1768:
    def test_case_one(self):
        input_word1 = "abc"
        input_word2 = "pqr"
        assert (merge_alternate(input_word1, input_word2) == "apbqcr")

    def test_case_two(self):
        input_word1 = "ab"
        input_word2 = "pqrs"
        assert (merge_alternate(input_word1, input_word2) == "apbqrs")

    def test_case_three(self):
        input_word1 = "abcd"
        input_word2 = "pq"
        assert (merge_alternate(input_word1, input_word2) == "apbqcd")
