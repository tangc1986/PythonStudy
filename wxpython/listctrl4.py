# -*- coding: UTF-8 -*-
__author__ = 'tangchao'

import wx
import sys, glob, random
import data


class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          "wx.ListCtrl in wx.LC_REPORT mode",
                          size=(600, 400))

        # load some images into an image list
        il = wx.ImageList(16, 16, True)     # 创建图像列表
        for name in glob.glob("icon\\smicon??.png"):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        # create the list control
        # 创建列表窗口部件
        self.list = wx.ListCtrl(self, -1,
                                style=wx.LC_REPORT)

        # assign the image list to it
        self.list.AssignImageList(il, wx.IMAGE_LIST_SMALL)

        # Add some columns
        for col, text in enumerate(data.columns):   # 增加列
            self.list.InsertColumn(col, text)

        # add the rows
        for item in data.rows:  # 增加行
            index = self.list.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)

            # give each item a random image
            img = random.randint(0, il_max)
            self.list.SetItemImage(index, img, img)

        # set the width of the columns in varous ways
        self.list.SetColumnWidth(0, 120)    # 设置列的宽度
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)


app = wx.PySimpleApp()
frame = DemoFrame()
frame.Show()
app.MainLoop()
