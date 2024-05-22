import requests
url = "http://localhost:8000"

response = requests.get(f"{url}/posts")
print(response.text)
response = requests.get(f"{url}/post/2")
print(response.text)
post={"title":"Mi experiencia como dev","content":"nothing"}
response = requests.post(f"{url}/posts",post)
print(response)
response = requests.get(f"{url}/posts")
print(response.text)
response=requests.put(f"{url}/post/3",{"content":"En progreso"})
print(response)
response=requests.delete(f"{url}/post/2")
response = requests.get(f"{url}/posts")
print(response.text)

