#!/usr/bin/env python
# -*- coding:utf-8 -*-

import wx

class DoubleEventFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame With Button',
                          size=(300, 100))
        self.panel = wx.Panel(self, -1)
        self.button = wx.Button(self.panel, -1, "Click Me", pos=(100, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick,
                  self.button)      #1 绑定按钮敲击事件
        self.button.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)    #2 绑定鼠标左键按下事件

    def OnButtonClick(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()

    def OnMouseDown(self, event):
        self.button.SetLabel("Again!")
        event.Skip()        #3 确保继续处理

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = DoubleEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
