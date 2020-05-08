import unittest
import app


class flaskmaintest(unittest.TestCase):

 

    def testIndex(self):
        response = tester.post('/api/v1.0/getData',  follow_redirects=True)
        self.assertIn(response.data)

 


if __name__ == '__name__':
    unittest.main()