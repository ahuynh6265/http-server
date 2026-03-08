url = "search?q=hello&limit=10"
path, _, query = url.partition("?")

results = {}
split = query.split("&")
print(split)


for s in split: 
  key, value = s.split("=")
  results[key] = value 

for result in results.items():
  print(result)

