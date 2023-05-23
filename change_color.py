# author:ImHash-101
# Github:https://github.com/ImHash-101/Script.git
# description:修改Png图片颜色
from PIL import Image

# 打开PNG文件并将其转换为图像对象
img = Image.open("transparent_image.png").convert("RGBA")

# 获取图像数据
data = img.load()

# 遍历每个像素并修改其颜色
for x in range(img.size[0]):
    for y in range(img.size[1]):
        # 检查当前像素是否透明
        if data[x, y][3] > 0:
            # 修改非透明像素的颜色
            # data[x, y] = (255, 0, 0, 255)  # 将像素设置为红色
            #改为白色
            data[x,y]=(255,255,255,255)

# 保存修改后的图像为新的PNG文件
img.save("modified_image.png")
img.show()
print("Finished")