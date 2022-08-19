from github.client import GithubClient
from repo.parser import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator

from models.member import Member
from models.manager import Manager

if __name__ == '__main__':
    username = 'valdyrtorres'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
        html_report = ReportsGenerator.build(HTMLGenerator, repos)

        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])

    member = Member('valdyrtorres', 'valdyr@test.com')
    manager = Manager('manager', 'manager@test.com')

    print(member.members())
    print(manager.members())
