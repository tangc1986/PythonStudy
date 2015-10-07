# -*- coding: UTF-8 -*-
import wx
from blockwindow import BlockWindow

labels = "one two three four five six seven eight nine".split()

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Basic Grid Sizer")
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)    # 创建grid sizer
        for label in labels:
            bw = BlockWindow(self, label=label)
            sizer.Add(bw, 0, 0)     # 添加窗口部件到sizer
        self.SetSizer(sizer)    # 把sizer与框架关联起来
        self.Fit()

app = wx.PySimpleApp()
GridSizerFrame().Show()
app.MainLoop()
