# -*- coding: UTF-8 -*-
import wx


class HelpFrame(wx.Frame):

    def __init__(self):
       pre = wx.PreFrame()     #1 预购建对象
       pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)
       pre.Create(None, -1, "Help Context", size=(300, 100),
                  style=wx.DEFAULT_FRAME_STYLE ^
                        (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))   #2 创建框架
       self.PostCreate(pre)    #3 底层C++指针的传递

    # def __init__(self, parent, ID, title,
    #              pos=wx.DefaultPosition, size=(100, 100),
    #              style=wx.DEFAULT_DIALOG_STYLE):
    #     twoStepCreate(self, wx.PreFrame, self.preInit, parent,
    #                   id, title, pos, size, style)
    #
    # def preInit(self, pre):
    #     pre.SetExtraStyle(wx.FRAME_EX_CONTEXTHELP)





if __name__ == '__main__':
    app = wx.PySimpleApp()
    HelpFrame().Show()
    app.MainLoop()
