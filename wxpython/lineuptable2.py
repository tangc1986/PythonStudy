import wx
import wx.grid

class LineupEntry:
    
    def __init__(self, pos, first, last):
        self.pos = pos
        self.first = first
        self.last = last
        
class LineupTable(wx.grid.PyGridTableBase):
    
    colLabels = ("First", "Last")   # �б�ǩ
    colAttrs = ("first", "last")    #1 ������
    
    def __init__(self, entries):    #2 ��ʼ��ģ��
        wx.grid.PyGridTableBase.__init__(self)
        self.entries = entries
        
    def GetNumberRows(self):
        return len(self.entries)
        
    def GetNumberCols(self):
        return 2
    
    def GetColLabelValue(self, col):
        return self.colLabels[col]  # ���б�ǩ
    
    def GetRowLabelValue(self, col):
        return self.entries[row].pos    #3 ���б�ǩ
    
    def IsEmptyCell(self, row, col):
        return False
    
    def GetValue(self, row, col):
        entry = self.entries[row]
        return getattr(entry, self.colAttrs[col])   #4 ������ֵ
    
    def SetValue(self, row, col, value):
        pass
    
    