# -*- coding: UTF-8 -*-
__author__ = 'tangchao'

import wx
import treedata


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
                          title='simple tree with icons', size=(400, 500))

        # 创建一个图像列表
        il = wx.ImageList(16, 16)

        # 添加图像到列表
        self.fldridx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_FOLDER,
                                     wx.ART_OTHER, (16, 16)))
        self.fldropenidx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,
                                     wx.ART_OTHER, (16, 16)))
        self.fileidx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE,
                                     wx.ART_OTHER, (16, 16)))

        # 创建树
        self.tree = wx.TreeCtrl(self)
        # 给树分配图像列表
        self.tree.AssignImageList(il)
        root = self.tree.AddRoot("wx.Object")
        self.tree.SetItemImage(root, self.fldridx,
                               wx.TreeItemIcon_Normal)  # 设置根的图像
        self.tree.SetItemImage(root, self.fldropenidx,
                               wx.TreeItemIcon_Expanded)

        self.AddTreeNodes(root, treedata.tree)
        self.tree.Expand(root)

    def AddTreeNodes(self, parentItem, items):
        for item in items:
            if type(item) == str:
                newItem = self.tree.AppendItem(parentItem, item)
                self.tree.SetItemImage(newItem, self.fldridx,
                                       wx.TreeItemIcon_Normal)  # 设置数据图像
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.tree.SetItemImage(newItem, self.fldridx,
                                       wx.TreeItemIcon_Normal)  # 设置结点的图像
                self.tree.SetItemImage(newItem, self.fldropenidx,
                                       wx   .TreeItemIcon_Expanded)

                self.AddTreeNodes(newItem, item[1])

    def GetItemText(self, item):
        if item:
            return self.tree.GetItemText(item)
        else:
            return ""

app = wx.PySimpleApp(redirect=True)
frame = TestFrame()
frame.Show()
app.MainLoop()
