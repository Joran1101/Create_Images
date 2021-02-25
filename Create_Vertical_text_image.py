#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021.2.25
# @Author  : Joran
# @Github    ：https://github.com/Joran1101

# 功能：竖排文字 通过模板图片 写入文字到指定位置，并分别保存成新的图片
# 功能说明：根据","换行（也可以根据"\n"换行）

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

if __name__=="__main__":
    # 初始化字符串
    strs ="往后余生,风雪是你,平淡是你,清贫也是你,荣华是你,心底温柔是你,目光所致,也是你。"
    # 模板图片
    imageFile = "1.png"
    # 新文件保存路径
    file_save_dir = "D:\\Code\\Create_Images\\"

    # 初始化参数
    x = 100  # 横坐标（左右）
    y = 20  # 纵坐标（上下）
    word_size = 50  # 文字大小
    word_css = "HYZhongSongJ.ttf"  # 字体文件

    # 设置字体，如果没有，也可以不设置
    font = ImageFont.truetype(word_css, word_size)

    # 分割得到数组
    im1 = Image.open(imageFile)  # 打开图片
    draw = ImageDraw.Draw(im1)
    print(font.getsize(strs))
    print("竖向文字")
    #
    im1 = Image.open(imageFile)
    draw = ImageDraw.Draw(im1)
    # draw.text((x, y),s.replace(",","\n"),(r,g,b),font=font) #设置位置坐标 文字 颜色 字体
    right = 0  # 往右位移量
    down = 0  # 往下位移量
    w = 500  # 文字宽度（默认值）
    h = 500  # 文字高度（默认值）
    row_hight = 0  # 行高设置（文字行距）
    word_dir = 0  # 文字间距
    # 一个一个写入文字
    print(strs)
    for k, s2 in enumerate(strs):
        if k == 0:
            w, h = font.getsize(s2)  # 获取第一个文字的宽和高
        if s2 == "," or s2 == "\n":  # 换行识别
            right = right + w + row_hight
            down = 0
            continue
        else:
            down = down + h + word_dir
        print("序号-值", k, s2)
        print("宽-高", w, h)
        print("位移", right, down)
        print("坐标", x + right, y + down)
        draw.text((x + right, y + down), s2, (255, 255, 0), font=font)  # 设置位置坐标 文字 颜色 字体
    # 定义文件名 数字需要用str强转
    new_filename = file_save_dir + strs.replace(",", "-").replace("\n", "-") + ".png"
    im1.save(new_filename)
    del draw  # 删除画笔
    im1.close()
