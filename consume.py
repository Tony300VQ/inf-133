from zeep import Client
client=Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result = client.service.NumberToWords(5)
result2 = client.service.NumberToDollars(10)
print(result)
print(result2)