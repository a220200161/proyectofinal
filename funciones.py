import csv
from passlib.hash import sha256_crypt
import datetime

class funciones:
    def diccionarioUsuarios():
        pass
    def lee_archivo_csv(archivo:str)->list:
        '''
        Lee un archivo csv y regresa una lista de renglones 
        (y campos dentro de los renglones)
        '''
        lista = []
        try:
            with open(archivo,"r",encoding="utf-8") as fh: #fh: file handle
                csv_reader = csv.reader(fh)
                for linea in csv_reader:
                    lista.append(linea)
        except IOError:
            print(f"No se pudo abrir el archivo {archivo}")

        return lista
    def lee_diccionario_usuarios(archivo:str)->dict:
        diccionario = {}
        try:
            with open(archivo,"r",encoding="utf-8") as fh: #fh: file handle
                csv_reader = csv.DictReader(fh)
                for renglon in csv_reader:
                    llave = renglon['usuario']
                    diccionario[llave] = renglon
        except IOError:
            print(f"No se pudo abrir el archivo {archivo}")
        return diccionario
    def lee_diccionario_servicios(archivo:str)->dict:
        diccionario = {}
        try:
            with open(archivo,"r",encoding="utf-8") as fh: #fh: file handle
                csv_reader = csv.DictReader(fh)
                for renglon in csv_reader:
                    llave = renglon['numero']
                    diccionario[llave] = renglon
        except IOError:
            print(f"No se pudo abrir el archivo {archivo}")
        return diccionario
