import mysql.connector
from tarifa import Tarifa

class TarifaDao():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="telzir",
            password="123mudar",
            database="TELZIR"
        )

    def getTarifas(self):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT dddOrigem, dddDestino, tarifa FROM tarifas")

        myresult = mycursor.fetchall()

        tarifas = []

        for row in myresult:
            tarifas.append(Tarifa(row[0], row[1], row[2]))

        return tarifas
