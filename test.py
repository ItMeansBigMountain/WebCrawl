import requests



print( "text/html" in requests.get("https://www.google.com").headers.get("Content-Type").lower()    )


import requests

response = requests.get("https://www.google.com")
response.encoding = 'utf-8'  # set the encoding to UTF-8
content_utf8 = response.text
print(content_utf8)
