import datetime
from datetime import datetime,timedelta

class Servicio:
    
    def __init__(self,semana=1,fin_de_semana=2,rango_servicio=[datetime(2017,1,1,12,1),datetime(2017,1,1,12,1)]):
        self.tarifaSemana = semana
        self.tarifa_fin_de_semana = fin_de_semana
        self.inicio = rango_servicio[0]
        self.fin = rango_servicio[1]

    def tarifaDelDia(self,fecha):
        dia = fecha.strftime("%a")
        
        if (dia =="Sat" or dia =="Sun"):
            return self.tarifa_fin_de_semana
        
        return self.tarifaSemana
