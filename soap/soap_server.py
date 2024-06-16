from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler
def saludar(nombre):
    return "Hola, {}".format(nombre)
dispatcher = SoapDispatcher(
    "ejemplo.soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
def sumaDosNumeros(num1,num2):
    return "La suma es,{}".format(num1+num2)
def sumaRestaNumeros(num1,num2):
    return "La resta es,{}".format(num1-num2)
def sumaMultiplicacionNumeros(num1,num2):
    return "La multiplicacion es,{}".format(num1*num2)
def sumaDivisionNumeros(num1,num2):
    if num2!=0:
        return "La division es,{}".format(num1/num2)
    return "No se puede dividir entre 0"
def cadenaPalindromo(cadena):
    if(cadena==cadena[::-1]):
        return True
    else:
        return False
dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo":str},
    args={"nombre":str}
)
dispatcher.register_function(
    "SumaDosNumeros",
    sumaDosNumeros,
    returns={"suma":str},
    args={"num1":int,"num2":int}
)
dispatcher.register_function(
    "CadenaPalindromo",
    cadenaPalindromo,
    returns={"verifica":bool},
    args={"cadena":str}
)
server=HTTPServer(("0.0.0.0",8000), SOAPHandler)
server.dispatcher=dispatcher
print("Servidor iniciado http://localhost:8000/")
server.serve_forever()
