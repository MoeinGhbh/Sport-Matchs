import unittest
from model import Team,Matches,Tournament,Scores,Title
import random, string


def make_suite():
    class TeamTest(unittest.TestCase):
        strName = ''

        def randomString(stringLength=10):
            """Generate a random string of fixed length """
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))

        def test_title(self):
            response = Title.Insert("title_test,1")
            self.assertEqual(response, 200)

       

    suite = unittest.TestSuite()
    suite.addTest(TeamTest('test_title'))
    return suite


suite = make_suite()


class T(unittest.TestCase):
    counter = 0

    def __call__(self, *args, **kwargs):
        res = suite._tests[T.counter](*args, **kwargs)
        T.counter += 1
        return res


for t in suite._tests:
    name = "{}${}".format(t._testMethodName, t.__class__.__name__)
    setattr(T, name, t)