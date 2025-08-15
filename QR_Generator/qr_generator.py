import qrcode
from PIL import Image  # 用来处理图片

# 用户输入要生成的 QR 码内容和文件名
data = input("请输入要生成QR码的文本或网址: ").strip()
filename = input("请输入保存文件名: ").strip() + ".png"

# 创建二维码对象
qr = qrcode.QRCode(
    box_size=10,     # 每个小方块的像素大小
    border=4         # 边框宽度（单位：方块数）
)
qr.add_data(data)
qr.make(fit=True)  # 自动调整大小

# 生成二维码图片（黑白）
img = qr.make_image(fill_color='black', back_color='white').convert('RGB')

# 嵌入Logo
logo_path = "logo.png"
try:
    logo = Image.open(logo_path)

    # 计算Logo显示大小
    qr_width, qr_height = img.size
    logo_size = qr_width // 5
    logo = logo.resize((logo_size, logo_size))

    # 计算Logo放置位置
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    # logo=logo.convert('RGBA') # 如果Logo没有透明通道先使用这段代码
    img.paste(logo, pos, mask=logo)
except FileNotFoundError:
    print("未找到logo.png, 将生成无Logo的二维码")

# 保存最终二维码
img.save(filename)
print(f'二维码已保存为 {filename}')
