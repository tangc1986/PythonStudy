# -*- coding: UTF-8 -*-
__author__ = 'tangchao'

import wx
import sys, glob

class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          "wx.ListCtrl in wx.LC_LIST mode",
                          size=(600, 400))

        # load some images into an image list
        il = wx.ImageList(16, 16, True)     # 创建图像列表
        for name in glob.glob("icon\\smicon??.png"):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        # create the list control
        # 创建列表窗口部件
        self.list = wx.ListCtrl(self, -1,
                                style=wx.LC_LIST)

        # assign the image list to it
        self.list.AssignImageList(il, wx.IMAGE_LIST_SMALL)

        # create some items for the list
        # 为列表创建一些项目
        for x in range(25):
            img = x % (il_max+1)
            self.list.InsertImageStringItem(x,
                                      "this is item %02d"%x, img)

app = wx.PySimpleApp()
frame = DemoFrame()
frame.Show()
app.MainLoop()
