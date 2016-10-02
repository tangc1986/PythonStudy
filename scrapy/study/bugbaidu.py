import string
import urllib2
import re

#----------- 处理页面上的各种标签 -----------
class HTML_Tool:
    # 用非贪婪模式匹配\t或者\n或者空格或者超链接或者图片
    BgnCharToNoneRex = re.compile("(\t|\n\ \<a.*?>|<img.*?>)")

    # 用非贪婪模式匹配任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")

    # 用非贪婪模式匹配任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html的符号实体转变为原始符号
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]

    def Replace_Char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub("\n    ", x)
        x = self.CharToNewLineRex.sub("\n", x)
        x = self.CharToNextTabRex.sub("\t", x)
        x = self.EndCharToNoneRex.sub("", x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x