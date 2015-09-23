#-*- coding: UTF-8 -*-
import os
import cPickle
import wx
import wx.html
from sketchwindow import SketchWindow
from wx.lib import buttons

class SketchAbout(wx.Dialog):
    text = '''
<html>
<body bgcolor="#ACAA60">
<center><table bgcolor="#455481" width="100%" cellspacing="0"
cellpadding="0" border="1">
<tr>
    <td align="center"><h1>Sketch!</h1></td>
</tr>
</table>
</center>
<p><b>Sketch</b> is a demonstration program for <b>wxPython In Action</b>
Chapter 7.  It is based on the SuperDoodle demo included with wxPython,
available at http://www.wxpython.org/
</p>

<p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by
<b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright
&copy; 1997-2006.</p>
</body>
</html>
'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About Sketch',
                           size=(440, 400))

        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "Okay")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()

class ControlPanel(wx.Panel):

    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4

    colorList = ('Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',
                 'Brown', 'Aquamarine', 'Forest Green', 'Light Blue',
                 'Goldenrod', 'Cyan', 'Orange', 'Navy', 'Dark Grey',
                 'Light Grey')
    maxThickness = 16

    def __init__(self, parent, ID, sketch):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.sketch = sketch
        buttonSize = (self.BMP_SIZE + 2*self.BMP_BORDER, self.BMP_SIZE + 2*self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent, buttonSize)
        thicknessGrid = self.createThicknessGrid(buttonSize)
        self.layout(colorGrid, thicknessGrid)

    def createColorGrid(self, parent, buttonSize):  #1 创建颜色网络
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for eachColor in self.colorList:
            bmp = parent.MakeBitmap(eachColor)
            b = buttons.GenBitmapToggleButton(self, -1, bmp, size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
            colorGrid.Add(b, 0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid

    def createThicknessGrid(self, buttonSize):   #2 创建线条粗细网络
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for x in range(1, self.maxThickness+1):
            b = buttons.GenToggleButton(self, -1, str(x), size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
            thicknessGrid.Add(b, 0)
            self.thicknessIdMap[b.GetId()] = x
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid

    def layout(self, colorGrid, thicknessGrid):     #3 合并网格
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(colorGrid, 0, wx.ALL, self.SPACING)
        box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

    def OnSetColour(self, event):
        color = self.colorMap[event.GetId()]
        if color != self.sketch.color:
            self.colorButtons[self.sketch.color].SetToggle(False)
        self.sketch.SetColor(color)

    def OnSetThickness(self, event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.sketch.thickness:
            self.thicknessButtons[self.sketch.thickness].SetToggle(False)
        self.sketch.SetThickness(thickness)

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        self.title = "Sketch Frame"
        wx.Frame.__init__(self, parent, -1, self.title,
                          size=(800, 600))
        self.filename = ""
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.initStatusBar()    #1 这里因重构有点变化
        self.createMenuBar()
        #self.createToolBar()
        self.createPanel()

    def createPanel(self):
        controlPanel = ControlPanel(self, -1, self.sketch)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(controlPanel, 0, wx.EXPAND)
        box.Add(self.sketch, 1, wx.EXPAND)
        self.SetSizer(box)

    def SaveFile(self):     #1 保存文件
        if self.filename:
            data = self.sketch.GetLinesData()
            f = open(self.filename, 'w')
            cPickle.dump(data, f)
            f.close()

    def ReadFile(self):     #2 读文件
        if self.filename:
            try:
                f = open(self.filename, 'r')
                data = cPickle.load(f)
                f.close()
                self.sketch.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a sketch file."%self.filename, "oops!", style=wx.OK|wx.ICON_EXCLAMATION)

    wildcard = "Sketch files (*.sketch)|*.sketch|All files (*.*)|*.*"

    def OnOpen(self, event):    #3 弹出打开对话框
        dlg = wx.FileDialog(self, "Open sketch file...",
                            os.getcwd(), style=wx.OPEN,
                            wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.title+'--'+self.filename)
        dlg.Destroy()

    def OnSave(self, event):    #4 保存文件
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self, event):  #5 弹出保存对话框
        dlg = wx.FileDialog(self, "Save sketch as...",
                            os.getcwd(),
                            style=wx.SAVE|wx.OVERWRITE_PROMPT,
                            wildcard=self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]:   #6 确保文件后缀名
                filename = filename + '.sketch'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title+'--'+self.filename)
        dlg.Destroy()

    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1, -2, -3])
        
    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos:%s"%
                                     str(event.GetPositionTuple()), 0)
        self.statusbar.SetStatusText("Current Pts:%s"%
                                     len(self.sketch.curLine), 1)
        self.statusbar.SetStatusText("Line Count:%s"%
                                     len(self.sketch.lines), 2)
        event.Skip()

    def menuData(self):     #2 菜单数据
        return [("&File", (("&New", "New Sketch file", self.OnNew),
                           ("&Open", "Open sketch file", self.OnOpen),
                           ("&Save", "Save sketch file", self.OnSave),
                           ("", "", ""),
                           ("&Color", (("&Black", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Red", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Green", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Blue", "", self.OnColor, wx.ITEM_RADIO),
                                       ("&Other...", "", self.OnOtherColor, wx.ITEM_RADIO))),
                           ("", "", ""),
                           ("&About", "About", self.OnAbout),
                           ("", "", ""),
                           ("&Quit", "Quit", self.OnCloseWindow)))]

    def OnOtherColor(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)     # 创建颜色数据对象
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColor(dlg.GetColourData().GetColour())   # 根据用户的输入设置颜色
        dlg.Destroy()

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        #3 创建子菜单
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, label, status, handler,
                       kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)     #4 使用kind创建菜单项
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnNew(self, event): pass
    #def OnOpen(self, event): pass
    #def OnSave(self, event): pass

    def OnColor(self, event):   #5 处理颜色的改变
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnCloseWindow(self, event):
        self.Destroy()

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

    def OnAbout(self, parent):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

class SketchApp(wx.App):

    def OnInit(self):
        bmp = wx.Image("splash.png").ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTER_ON_SCREEN|wx.SPLASH_TIMEOUT,
                        1000, None, -1)
        wx.Yield()

        frame = SketchFrame(None)
        frame.Show()
        self.SetTopWindow(frame)
        return True

if __name__ == '__main__':
    #app = wx.PySimpleApp()
    #frame = SketchFrame(None)
    #frame.Show()
    app = SketchApp()
    app.MainLoop()
