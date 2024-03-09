import concurrent.futures
import threading
import time
import requests

# 1. 利用threading模块并发执行程序

start = time.perf_counter()


def my_function(second):
    print(f'睡眠 {second} 秒...')
    time.sleep(second)
    print('完成睡眠...')


# my_function(1)
# my_function(1)
t1 = threading.Thread(target=my_function, args=[1])
t2 = threading.Thread(target=my_function, args=[1])

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'总共耗时 {round(finish-start, 2)} 秒')

# 2. 利用线程池管理器，并发执行程序

# start = time.perf_counter()


# def my_function(second):
#     print(f'睡眠 {second} 秒...')
#     time.sleep(second)
#     return '完成睡眠...'


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(my_function, 1) for _ in range(10)]

#     # 这种方式不会按照任务提交的顺序来获取结果，而是按照任务完成的顺序
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# finish = time.perf_counter()

# print(f'总共耗时 {round(finish-start, 2)} 秒')

# 3. 多线程并发处理网站图像爬取任务

# 图片链接列表
# img_urls = [
#     'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#     'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#     'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#     'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#     'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#     'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#     'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#     'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#     'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#     'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#     'https://images.unsplash.com/photo-1550439062-609e1531270e',
#     'https://images.unsplash.com/photo-1549692520-acc6669e2f0c',
#     'https://images.unsplash.com/photo-1605140316783-b43dfc1df270',
#     'https://images.unsplash.com/photo-1681687495469-0d9cf33a3b59',
#     'https://images.unsplash.com/photo-1572478966407-4d50f39e23d6',
#     'https://images.unsplash.com/photo-1559511124-aaccf50b90d5',
#     'https://images.unsplash.com/photo-1616645728806-838c6bf184af',
#     'https://images.unsplash.com/photo-1564381714144-049e9f7aa06a',
#     'https://images.unsplash.com/photo-1604557835456-3b81c783cadd',
#     'https://images.unsplash.com/photo-1608440037200-97cedc9805a6'
# ]

# t1 = time.perf_counter()

# for img_url in img_urls:

#     # def download_image(img_url):
#     img_bytes = requests.get(img_url).content
#     img_name = img_url.split('/')[3]
#     img_name = f'{img_name}.jpg'
#     with open(img_name, 'wb') as img_file:
#         img_file.write(img_bytes)
#         print(f'{img_name} 正在下载...')


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(download_image, img_urls)

# t2 = time.perf_counter()

# print(f'总共耗时 {round(finish-start, 2)} 秒')
