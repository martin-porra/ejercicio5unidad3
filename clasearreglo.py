from numpy import  *
from zope.interface import implementer
from claseinterface import intermanejo
from clasenodo import nodo
@implementer(intermanejo)
class coleccion:
    __cabeza = None

    def __init__(self):
       self.__cabeza = None
    def insertarElemento(self,objeto,indice):
      '''codigo para instertar un objeto'''
    def agregarElemento(self,objeto):
      '''codigo para agregar un objeto al final'''
    def mostrarElemento(self,indice):
     '''''codigo para mostrar un objeto'''