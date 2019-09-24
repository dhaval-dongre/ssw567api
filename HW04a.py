import requests
import unittest
import json

def getRepoInfo(username):
    repoInfo={}
    response=requests.get('https://api.github.com/users/'+username+'/repos')
    

    if response.status_code != 200:
        return 'Not Exists'

    repos=json.loads(response.text)
    
    for repo in repos:
        url='https://api.github.com/repos/'+username+'/'+repo['name']+'/commits'

        response=requests.get(url)

        if response.status_code != 200:
            repoInfo[repo['name']]=len(json.loads(response.text))
            continue

        repoInfo[repo['name']]=len(json.loads(response.text))

    # print(json.dumps(repoInfo, indent = 4))

    return repoInfo

class GitApiTest(unittest.TestCase):

    def test_GitApiPositive(self):
        actual=getRepoInfo('dhaval-dongre')['CS-546']
        self.assertEqual(actual, 30, 'Unequal amount of commits '+'actual:['+str(actual)+']'+' expected:[30]')
        

    def test_GitApiNegative(self):
        actual=getRepoInfo('dhaval-abcdef')
        self.assertEqual(actual, 'Not Exists', 'Expected the repository to be non existent')
        
if __name__ == '__main__':
    unittest.main()