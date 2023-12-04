
from xmlrpc.client import ServerProxy

servidor = ServerProxy('http://localhost:4242')

print("Suma:", servidor.suma(2, 6))
print("Resta:", servidor.resta(8, 3))
print("Multiplicación:", servidor.multiplicacion(4, 5))
print("División:", servidor.division(10, 2))
print("Potencia:", servidor.potencia(2, 3))
print("Concatenación de Cadenas:", servidor.concatenar_cadenas("Hola, ", "Mundo!"))