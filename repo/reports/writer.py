#Simulando uma classe de alto nível
from .file_writer import ReportFileWriter


class ReportWriter():

    # Devemos usar a injeção de dependência para aplicar o princípio [D]ependency Inversion Principle
    @staticmethod
    def write(report, writer=ReportFileWriter):
        # Lógica...
        # Lógica...
        # report = faz alguma operacao
        writer.write(report)
