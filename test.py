# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
menu = {
        '1': dict(name=u'草莓冰淇淋', price=20),
        '2': dict(name=u'香草冰淇淋', price=10),
        '3': dict(name=u'香蕉冰淇淋', price=15),
        '5': dict(name=u'巧克力冰淇淋', price=30),
    }

def showmenu(menu):
    for k, item in sorted(menu.items()):
        print "%(key)s: %(name)s 价格%(price).2f" % dict(key=k, **item)

def menuchoice(menu):
    while True:
        showmenu(menu)
        c = raw_input("Your Choice('.' for end): ")
        if c == '.':
            break
        else:
            yield menu.get(c)

customerchoice = filter(None, menuchoice(menu))

print "Total: %.2f" % sum(map(lambda x: x["price"], customerchoice))