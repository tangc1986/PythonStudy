#-*- coding: UTF-8 -*-
import os
import cPickle
import wx
from sketchwindow import SketchWindow

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
        colorGrid = wx.GridSize(cols=self.NUM_COLS, hgap=2, vgap=2)
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
        self.SetSize(box)

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
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show()
    app.MainLoop()
