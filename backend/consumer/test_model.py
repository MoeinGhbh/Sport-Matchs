import unittest
from model import Team,Matches,Tournament,Scores,Title, turnamentError
import random, string
import pytest


def make_suite():

    

    class sport_test(unittest.TestCase):
        

        def randomString(self, stringLength=10):
            """Generate a random string of fixed length """
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))

        # @pytest.mark.string
        def test_title(self):
            title_name = sport_test.randomString(self)
            assert Title.Insert(title_name,"1")== 'add Title'

        def test_Tournement(self):
            assert  Tournament.Insert(sport_test.randomString(self),"overcooked","2020-01-0714:30:00")
            with pytest.raises(turnamentError) as context:
                result =Tournament.Insert(sport_test.randomString(self),"null","2020-01-0714:30:00")
            print(str(context.value))

        def test_Team(self):
            assert 1==1

        def test_matches(self):
            assert 1==1
        
        def test_score(self):
            assert 1==1



       

    suite = unittest.TestSuite()
    suite.addTest(sport_test('test_title'))
    suite.addTest(sport_test('test_Tournement'))
    suite.addTest(sport_test('test_Team'))
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