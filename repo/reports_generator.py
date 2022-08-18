from .reports.html_generator import HTMLGenerator
from .reports.markdown_generator import MarkdowGenerator

class ReportsGenerator():
    @classmethod
    def build(cls, type, repos):
        if type == 'HTML':
            return HTMLGenerator.build(repos)
        elif type == 'MARKDOWN':
            return MarkdowGenerator.build(repos)
        else:
            return "Invalid report type!"