from _2_pytest import add

# def test_case_1():
#     assert add(3,1) == 4 , "LHS != RHS"

# def test_case_2():
#     assert add("a","b") == "abc" , "both left and right side are not equal"


class Test_sample:
    def test_case_1(self):
        assert add(3,1) == 4 , "LHS != RHS"

    def test_case_2(self):
        assert add("a","b") == "ab" , "both left and right side are not equal"