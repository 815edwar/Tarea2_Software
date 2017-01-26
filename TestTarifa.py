'''
Created on Jan 25, 2017

@author: Melanie Gomes
'''
import unittest
from Tarifa import *

class TarifaTest(unittest.TestCase):
    
    def setUp(self):
        self.t = Servicio()
    
    def testminHourService(self): 
        self.t=Servicio(10,100,[datetime(2017,1,1,12,0),datetime(2017,1,1,12,15)])
        self.assertEquals(100, self.t.calcularServicio())
        

    def testmaxHourService(self):
        self.t=Servicio(10,100,[datetime(2017,1,1,12,0),datetime(2017,1,8,12,0)])
        self.assertEquals(6000,self.t.calcularServicio())
    def testcasoFinSemana(self):
        self.t=Servicio(10,100,[datetime(2017,1,6,23,59),datetime(2017,1,8,23,59)])
        self.assertEquals(4710,self.t.calcularServicio())
        
    def testcasoFinSemanamas(self):
        self.t=Servicio(10,100,[datetime(2017,1,6,23,59),datetime(2017,1,9,0,1)])
        self.assertEquals(4810,self.t.calcularServicio())
    
    def testCasoBorde(self):
        self.t=Servicio(10,100,[datetime(2017,1,6,23,45),datetime(2017,1,7,0,0)])
        self.assertEquals(10,self.t.calcularServicio())
    
    def testCasoBorde1(self):
        self.t=Servicio(10,100,[datetime(2017,1,29,23,45),datetime(2017,1,30,0,0)])
        self.assertEquals(100,self.t.calcularServicio())
    
    def testDiaSemana(self):
        self.t=Servicio(10,100,[datetime(2017,1,2,0,0),datetime(2017,1,6,23,59)])
        self.assertEquals(1200,self.t.calcularServicio())
        
    def testCasoMalicioso(self):
        self.t=Servicio(10,100,[datetime(2017,1,7,0,0),datetime(2017,1,8,23,59)])
        self.assertEquals(4800,self.t.calcularServicio())
    
    def testCasoMalicioso1(self):
        self.t=Servicio(10,100,[datetime(2017,1,7,23,59),datetime(2017,1,8,0,14)])
        self.assertEquals(100,self.t.calcularServicio())
        
    def testCasoSemanaEmpezandoLunes(self):
        self.t=Servicio(10,100,[datetime(2017,1,2,0,0),datetime(2017,1,9,0,0)])
        self.assertEquals(6000,self.t.calcularServicio())
        
    
    
    
if __name__ == "__main__":
    unittest.main()