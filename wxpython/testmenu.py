# -*- coding: UTF-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Simple Menu Example")
        p = wx.Panel(self)
        menuBar = wx.MenuBar()      # 创建一个菜单栏
        menu = wx.Menu()        # 创建一个菜单
        menuBar.Append(menu, "Left Menu")   # 添加菜单到菜单栏
        menu2 = wx.Menu()
        menuBar.Append(menu2, "Middle Menu")
        menu3 = wx.Menu()
        menuBar.Append(menu3, "Right Menu")
        self.SetMenuBar(menuBar)

if __name__=="__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
