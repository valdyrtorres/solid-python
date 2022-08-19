#Simulando uma classe de alto nível
from .file_writer import ReportFileWriter


class ReportWriter():

    @staticmethod
    def write(report):
        # Lógica...
        # Lógica...
        # report = faz alguma operacao
        ReportFileWriter.write_file(report)
