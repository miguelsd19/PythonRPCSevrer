
from xmlrpc.server import SimpleXMLRPCServer
def suma(x, y):
  return x + y
def resta(x, y):
  return x - y
def multiplicacion(x, y):
  return x * y
def division(x, y):
  if y == 0:
    return "Error: División por cero."
  return x / y
def potencia(x, y):
  return x ** y
def concatenar_cadenas(str1, str2):
  return str1 + str2
# Crear servidor XML-RPC
servidor = SimpleXMLRPCServer(("localhost", 4242))
# Registrar funciones
servidor.register_function(suma, 'suma')
servidor.register_function(resta, 'resta')
servidor.register_function(multiplicacion, 'multiplicacion')
servidor.register_function(division, 'division')
servidor.register_function(potencia, 'potencia')
servidor.register_function(concatenar_cadenas, 'concatenar_cadenas')
print("Escuchando por el puerto 4242")
servidor.serve_forever()