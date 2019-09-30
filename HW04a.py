import requests
import unittest
import json
from unittest import mock
from unittest.mock import Mock,patch

def getRepoInfo(username):
    repoInfo=[]
    response=requests.get('https://api.github.com/users/'+username+'/repos')

    repos=response.json()
    
    for repo in repos:
        repoName = repo.get('name')
        repoInfo.append(repoName)
    return repoInfo

def getCommitCount(username,repoName):
    response =requests.get('https://api.github.com/repos/'+username+'/'+repoName+'/commits')
    commits = response.json()
    return len(commits)


class GitApiTest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_GitApiRepoInfo(self,mockVal):
        repoInfo = [{'name': 'Test'}]

        mockVal.return_value.json.return_value = repoInfo
        response = getRepoInfo('abc')
        self.assertEqual(response, ['Test'])

    @mock.patch('requests.get')
    def test_GitApiRepoCount(self,mockVal):
        repocommits = [{'0': {'commit': '1'}},{'1': {'commit': '2'}},{'2': {'commit': '3'}}]
        mockVal.return_value.json.return_value = repocommits
        response = getCommitCount('abc', 'Test')
        self.assertEqual(response, 3)  
        
if __name__ == '__main__':
    unittest.main()