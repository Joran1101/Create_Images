#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021.2.25
# @Author  : Joran
# @Github    ：https://github.com/Joran1101

# 需求：按照模板图片，在指定位置写入文本
# 功能：通过模板图片 写入文字到指定位置，并分别保存成新的图片
# 功能说明：根据";"间隔,根据","换行（也可以根据"\n"换行）
# 环境：PyDev 6.5.0   Python3.6.0
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

if __name__=="__main__":
    # 初始化字符串
    strs = "张三"
    # 打开模板图片
    imageFile = "2.png"
    # 新文件保存路径
    file_save_dir = "D:\\Code\\Create_Images\\"

    # 初始化参数
    x = 628 # 横坐标（左右）
    y = 648  # 纵坐标（上下）
    word_size = 18  # 文字大小
    word_css = "HYZhongSongJ.ttf"  # 字体文件
    r = 0  # 画笔字体颜色
    g = 0  # 画笔字体颜色字体颜色
    b = 0  # 画笔字体颜色字体颜色  (0,0,0)黑色
    direction = 0  # 文字方向  0横向（默认）  1竖向
    row_hight = 0  # 行高设置（文字行距,可以小于0） 竖向时设置
    word_dir = 0  # 文字间距    竖向时设置

    # 设置字体，如果没有，也可以不设置
    font = ImageFont.truetype(word_css, word_size)

    # 功能：竖向画笔写入文字
    # 参数：x,y 坐标   i,s编号及文字，im1图片  font字体  im1模板图片   row_hight行高（行距）  word_dir文字间距
    def draw_2(x, y, i, s, font, im1, row_hight, word_dir):
        draw = ImageDraw.Draw(im1)
        # draw.text((x, y),s.replace(",","\n"),(r,g,b),font=font) #设置位置坐标 文字 颜色 字体
        right = 0  # 往右位移量
        down = 0  # 往下位移量
        w = 100  # 文字宽度（默认值）
        h = 100  # 文字高度（默认值）
        # row_hight = -50 #行高设置（文字行距）
        # word_dir = 0; #文字间距
        for k, s2 in enumerate(s):
            if k == 0:
                w, h = font.getsize(s2)  # 获取第一个文字的宽和高
            if s2 == "," or s2 == "\n":
                right = right + w + row_hight
                down = 0
                continue
            else:
                down = down + h + word_dir
            draw.text((x + right, y + down), s2, (r, g, b), font=font)  # 设置位置坐标 文字 颜色 字体
        # 定义文件名 数字需要用str强转
        new_filename = file_save_dir + s.replace(",", "-").replace("\n", "-") + ".png"
        im1.save(new_filename)
        del draw  # 删除画笔


    # 功能：横向画笔写入文字
    # 参数：x,y 坐标    i,s编号及文字  font字体   im1模板图片
    def draw_1(x, y, i, s, font, im1):
        draw = ImageDraw.Draw(im1)
        draw.text((x, y), s.replace(",", "\n"), (r, g, b), font=font)  # 设置位置坐标 文字 颜色 字体

        # 定义文件名 数字需要用str强转
        new_filename = file_save_dir + s.replace(",", "-").replace("\n", "-") + ".png"
        im1.save(new_filename)
        del draw  # 删除画笔


    # 分割得到数组
    strs2 = strs.split(";")
    if direction == 0:  # 横向
        for i, ss in enumerate(strs2):
            print(i + 1, ss)
            im1 = Image.open(imageFile)
            draw_1(x, y, i + 1, ss, font, im1)
            im1.close()
    # elif direction == 1 :  #竖向
    else:  # 竖向
        print("竖向文字")
        for i, ss in enumerate(strs2):
            print(i + 1, ss)
            im1 = Image.open(imageFile)
            draw_2(x, y, i + 1, ss, font, im1, row_hight, word_dir)
            im1.close()


