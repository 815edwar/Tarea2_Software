import datetime
from datetime import datetime,timedelta

class Servicio:
    
    def __init__(self,semana=1,fin_de_semana=2,rango_servicio=[datetime(2017,1,1,12,1),datetime(2017,1,1,12,1)]):
        self.tarifaSemana = semana
        self.tarifa_fin_de_semana = fin_de_semana
        self.inicio = rango_servicio[0]
        self.fin = rango_servicio[1]

    def calcularServicio(self):
        try:
            assert((self.fin - self.inicio)> timedelta(minutes=15) and (self.fin - self.inicio)<timedelta(days=7))
        except:
            print("Las precondiciones no se cumplen")
            exit()
        
        totalServicio = 0
        while (self.inicio<self.fin):
            self.inicio = self.inicio + timedelta(hours = 1)
            totalServicio += self.tarifaDelDia(self.inicio)
    
        return totalServicio