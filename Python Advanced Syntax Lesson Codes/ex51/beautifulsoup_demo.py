from bs4 import BeautifulSoup
import requests
import csv

# 简单网页解析
with open('sample.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.prettify())

# 爬取单个文章信息
article = soup.find('div', class_='article')
print(article.prettify())

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

# 批量爬取所有文章信息
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    summary = article.p.text

    print(headline)
    print(summary)
    print()

# 赛博红兔博客爬取（请手下留情）
url = 'https://cyberhongtu.com/'
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

article = soup.find('li', class_='wp-block-post')
print(article.prettify())

# 标题爬取
headline = article.h2.text
print(headline)

# 图片爬取
figure = article.figure.img
figure_url = figure['src']
response = requests.get(figure_url)
with open('cover.jpg', 'wb') as f:
    f.write(response.content)

# 简介爬取
summary = article.find('div', class_='wp-block-post-excerpt').p.text
print(summary)

# 批量爬取
csv_file = open('blog_scrape.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['标题', '简介', '图片链接'])

index = 1
for article in soup.find_all('li', class_='wp-block-post'):

    headline = article.h2.text
    print(headline)

    figure = article.figure.img
    figure_url = figure['src']
    response = requests.get(figure_url)
    with open(f'cover_{index}.jpg', 'wb') as f:
        f.write(response.content)
    print(figure_url)

    summary = article.find('div', class_='wp-block-post-excerpt').p.text
    print(summary)

    print()
    index += 1

    csv_writer.writerow([headline, summary, figure_url])

csv_file.close()
