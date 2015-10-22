# -*- coding: UTF-8 -*-
__author__ = 'tangchao'

import wx
import wx.html


class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(600, 400))
        html = wx.html.HtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()

        wx.CallAfter(
            html.LoadPage, "http://www.wxpython.org/")

app =wx.PySimpleApp()
frame = MyHtmlFrame(None, "Simple HTML Browser")
frame.Show()
app.MainLoop()
