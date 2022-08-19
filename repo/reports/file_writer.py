#Simulando um banco de dados
class ReportFileWriter():

    @staticmethod
    def write(report):
        file = open('report.txt', 'w')
        file.write(report)
        file.close()
