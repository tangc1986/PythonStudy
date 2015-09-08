__author__ = 'tangchao'

import wx               #1

class App(wx.App):      #2

    def OnInit(self):   #3
        frame = wx.Frame(parent=None, id=-1, title='Bare')
        frame.Show()
        return True

app = App()             #4
app.MainLoop()          #5