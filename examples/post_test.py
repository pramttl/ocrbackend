import requests

url = 'http://localhost:8000/'
files = {'photo': open('sample-image.jpg', 'rb')}
r = requests.post(url, files=files, data={})
f = open('debug.html', 'w')
f.write(r.text)
f.close()
print r.text