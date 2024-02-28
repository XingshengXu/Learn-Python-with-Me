import concurrent.futures
import multiprocessing
import os
import time
from PIL import Image, ImageFilter

# 1. 利用multiprocessing模块并行执行程序

start = time.perf_counter()


def my_function(second):
    print(f'睡眠 {second} 秒...')
    time.sleep(second)
    print('完成睡眠...')


if __name__ == '__main__':
    # my_function(1)
    # my_function(1)
    p1 = multiprocessing.Process(target=my_function, args=[1])
    p2 = multiprocessing.Process(target=my_function, args=[1])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'总共耗时 {round(finish-start, 2)} 秒')

# 2. 利用进程池管理器，并行执行程序
# start = time.perf_counter()


# def my_function(second):
#     print(f'睡眠 {second} 秒...')
#     time.sleep(second)
#     return '完成睡眠...'


# if __name__ == '__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = [executor.submit(my_function, 1) for _ in range(10)]

#         # 这种方式不会按照任务提交的顺序来获取结果，而是按照任务完成的顺序
#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

#     finish = time.perf_counter()

#     print(f'总共耗时 {round(finish-start, 2)} 秒')

# 3. 多进程并行图像处理任务
# 图片名称列表

# img_names = [
#     'photo-1532009324734-20a7a5813719.jpg',
#     'photo-1524429656589-6633a470097c.jpg',
#     'photo-1530224264768-7ff8c1789d79.jpg',
#     'photo-1564135624576-c5c88640f235.jpg',
#     'photo-1541698444083-023c97d3f4b6.jpg',
#     'photo-1522364723953-452d3431c267.jpg',
#     'photo-1493976040374-85c8e12f0c0e.jpg',
#     'photo-1504198453319-5ce911bafcde.jpg',
#     'photo-1530122037265-a5f1f91d3b99.jpg',
#     'photo-1516972810927-80185027ca84.jpg',
#     'photo-1550439062-609e1531270e.jpg',
#     'photo-1549692520-acc6669e2f0c.jpg',
#     'photo-1605140316783-b43dfc1df270.jpg',
#     'photo-1681687495469-0d9cf33a3b59.jpg',
#     'photo-1572478966407-4d50f39e23d6.jpg',
#     'photo-1559511124-aaccf50b90d5.jpg',
#     'photo-1616645728806-838c6bf184af.jpg',
#     'photo-1564381714144-049e9f7aa06a.jpg',
#     'photo-1604557835456-3b81c783cadd.jpg',
#     'photo-1608440037200-97cedc9805a6.jpg'
# ]


# start = time.perf_counter()

# size = (1200, 1200)

# # 检查保存文件夹是否存在，否则新建文件夹
# if not os.path.exists('processed'):
#     os.makedirs('processed')

# for img_name in img_names:

#     # def process_image(img_name):
#     img = Image.open(img_name)

#     img = img.filter(ImageFilter.GaussianBlur(15))

#     img.thumbnail(size)
#     img.save(f'processed/{img_name}')
#     print(f'{img_name} 正在处理...')


# # if __name__ == '__main__':
# #     with concurrent.futures.ProcessPoolExecutor() as executor:
# #         executor.map(process_image, img_names)

# finish = time.perf_counter()

# print(f'总共耗时 {round(finish-start, 2)} 秒')
