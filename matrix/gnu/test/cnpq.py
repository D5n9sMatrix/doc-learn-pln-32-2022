import unittest


class MyTestCase(unittest.TestCase):
    def partial(self, /, *args, **keywords):
        def newfunc(*fargs, **fkeywords):
            newkeywords = {**keywords, **fkeywords}
            return self(*args, *fargs, **newkeywords)

        newfunc.func = self
        newfunc.args = args
        newfunc.keywords = keywords
        return newfunc


if __name__ == '__main__':
    unittest.main()
