class TestCli:
    # content of test_sample.py
    def func(self, x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 4