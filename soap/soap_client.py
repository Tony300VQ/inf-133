from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Jhon")
result2= client.service.SumaDosNumeros(num1=2,num2=3)
result3 = client.service.CadenaPalindromo(cadena="HHH")
print(result)
print(result2)
print(result3)