# author:ImHash-101
# Github:https://github.com/ImHash-101/Script.git
# description:删除PNG图片中的空白行和列

import numpy as np
from PIL import Image

# 打开PNG文件
image = Image.open('original_image.png')
data = np.array(image)

# 删除空白行
drop_list = []
for line in range(data.shape[0]):
    if np.all(data[line, :, :] == [255, 255, 255, 0]):
        drop_list.append(line)

data = np.delete(data,drop_list, axis=0)


# 删除空白列

drop_list = []
for column in range(data.shape[1]):
    if np.all(data[:, column, :] == [255, 255, 255, 0]):
        drop_list.append(column)

data = np.delete(data,drop_list, axis=1)

# 保存图片
new_image = Image.fromarray(data)
new_image.save('new_image.png')
new_image.show()