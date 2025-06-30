import requests

# 检查网站响应状态
url = "https://books.toscrape.com"
response = requests.get(url)
print(response.status_code)
print(response.ok)

if response.status_code == 200:
    print(response.text)
else:
    print("请求失败，状态码：", response.status_code)

# 爬取图片
url = "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
response = requests.get(url)
print(response.content)

with open('bookcover.jpg', 'wb') as f:
    f.write(response.content)

# 爬取图片信息
url = "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
response = requests.get(url)
print(response.headers)

# GET请求带参数
parameters = {'page': 2, 'count': 25}
url = "https://httpbin.org/get"
response = requests.get(url, params=parameters)
print(response.text)

# POST请求提交表单数据
parameters = {'username': 'Hongtu', 'password': '12345'}
url = "https://httpbin.org/post"
response = requests.post(url, data=parameters)
print(response.text)
response_dict = response.json()
print(response_dict['form'])

# 基本身份验证请求
url = "https://httpbin.org/basic-auth/Hongtu/12345"
response = requests.get(url, auth=('Hongtu', '12345'))
print(response.status_code)
print(response.text)
