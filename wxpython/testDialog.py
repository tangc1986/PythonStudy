# -*- coding: UTF-8 -*-


import wx

if __name__=="__main__":
    app = wx.PySimpleApp()

    # # 方法一，使用类
    # dlg = wx.MessageDialog(None, "Is this explanation OK?",
    #                        'A Message Box',
    #                        wx.YES_NO | wx.ICON_QUESTION)
    #
    # retCode = dlg.ShowModal()
    # if retCode == wx.ID_YES:
    #     print "yes"
    # else:
    #     print "no"
    # dlg.Destroy()
    #
    # #1 方法二，使用函数
    # retCode = wx.MessageBox("Is this way easier?", "Via Function",
    #                         wx.YES_NO | wx.ICON_QUESTION)


    # dialog = wx.TextEntryDialog(None,
    #                             "What kind of text would you like to enter?",
    #                             "Text Entry", "Default Value", style=wx.OK | wx.CANCEL)
    # if dialog.ShowModal() == wx.ID_OK:
    #     print "You entered: %s" % dialog.GetValue()
    #
    # dialog.Destroy()


    # choices = ["Alpha", "Baker", "Charlie", "Delta"]
    # dialog = wx.SingleChoiceDialog(None, "Pick A Word", "Choices",
    #                                choices)
    # if dialog.ShowModal() == wx.ID_OK:
    #     print "You selected: %s\n" % dialog.GetStringSelection()
    #
    # dialog.Destroy()


    # progressMax = 100
    # dialog = wx.ProgressDialog("A progress box", "Time remaining", progressMax,
    #                            style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
    # keepGoing = True
    # count = 0
    # while keepGoing and count<progressMax:
    #     count += 1
    #     wx.Sleep(1)
    #     keepGoing = dialog.Update(count)
    #
    # dialog.Destroy()


    # import os
    #
    # wildcard = "Python source (*.py)|*.py|"\
    #            "Compiled Python (*.pyc)|*.pyc|"\
    #            "All file (*.*)|*.*"
    # dialog = wx.FileDialog(None, "Choose a file", os.getcwd(),
    #                        "", wildcard, wx.OPEN)
    # if dialog.ShowModal() == wx.ID_OK:
    #     print dialog.GetPath()
    #
    # dialog.Destroy()


    # dialog = wx.DirDialog(None, "Choose a directory:",
    #                       style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    # if dialog.ShowModal() == wx.ID_OK:
    #     print dialog.GetPath()
    # dialog.Destroy()


    # dialog = wx.FontDialog(None, wx.FontData())
    # if dialog.ShowModal() == wx.ID_OK:
    #     data = dialog.GetFontData()
    #     font = data.GetChosenFont()
    #     colour = data.GetColour()
    #     print 'You selected:"%s", %d points\n' % (
    #         font.GetFaceName(), font.GetPointSize())
    # dialog.Destroy()


    # dialog = wx.ColourDialog(None)
    # dialog.GetColourData().SetChooseFull(True)
    # if dialog.ShowModal() == wx.ID_OK:
    #     data = dialog.GetColourData()
    #     print 'You selected: %s\n' % str(data.GetColour().Get())
    # dialog.Destroy()


    # import wx.lib.imagebrowser as imagebrowser
    #
    # dialog = imagebrowser.ImageDialog(None)
    # if dialog.ShowModal() == wx.ID_OK:
    #     print "You Selected File:" + dialog.GetFile()
    # dialog.Destroy()


    provider = wx.CreateFileTipProvider("tips.txt", 0)
    wx.ShowTip(None, provider, True)








