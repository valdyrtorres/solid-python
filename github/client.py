import requests
import json


class GithubClient():

    API_BASE_URL = 'https://api.github.com'

    @classmethod
    def get_repos_by_user(self):
        response = requests.get(f'{self.API_BASE_URL}/users/{self._user}/repos')
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "Error while getting repos"}

            

