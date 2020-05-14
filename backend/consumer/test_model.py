import unittest
from model import Team,Matches,Tournament,Scores,Title, turnamentError, teamError,matchesError,scoresError
import random, string
import pytest
from sqlalchemy import text


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
            with pytest.raises(teamError) as context:
                result =  Team.Insert(1,"Team-Socer")
            print(str(context.value))


        def test_matches(self):
            with pytest.raises(matchesError) as context:
                result = Matches.Insert("new-match",1,1)
            print(str(context.value))
        
        def test_score(self):
            with pytest.raises(scoresError) as context:
                result = Scores.Insert("turnamnet","team1","1","true","team1","team2")
            print(str(context.value))



       

    suite = unittest.TestSuite()
    suite.addTest(sport_test('test_title'))
    suite.addTest(sport_test('test_Tournement'))
    suite.addTest(sport_test('test_Team'))
    suite.addTest(sport_test('test_matches'))
    suite.addTest(sport_test('test_score'))
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