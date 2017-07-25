# encoding=utf-8
'''
创建者：liu
作用：更改图片尺寸大小
使用方法：放一张图片到同目录。filein:  输入图片
          fileout: 输出图片
          width: 输出图片宽度
          height:输出图片高度
          type:输出图片类型（png, gif, jpeg...）
创建日期：2017/7/21
'''

import os
import os.path
from PIL import Image
'''

'''
__dir__ = os.path.dirname(os.path.abspath(__file__))
def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
    out.save(fileout, type)

if __name__ == "__main__":
    filein = __dir__+'\\banma.png'
    fileout = __dir__+'\\b.png'
    width = 120
    height = 160
    type = 'png'
    ResizeImage(filein, fileout, width, height, type)
