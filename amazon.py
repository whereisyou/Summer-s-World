import requests
try:
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
	r = requests.get('https://www.amazon.cn/', headers = headers)
	r.raise_for_status()
	with open('amazon.html','wb') as f:
		f.write(r.content)
except:
	print('请求错误.')