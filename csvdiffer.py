# -*- coding:utf-8 -*-
import csv
import os


class csvread():
    def __init__(self, filename, lstname):
        self.lstname = lstname  # lstname 用于比对csv中相同列
        self.filename = filename
        self.header = self.fields()
        self.data = self.getdata()
        self.dataset = self.getset()

    # test update
    # 以字典方式获取csv数据
    def getdata(self):
        data = []
        with open(self.filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data

    # 获取序列
    def getset(self):
        lst = set()
        for row in self.data:
            lst.add(row.get(self.lstname))

        return lst

    # 获取表头
    def fields(self):
        with open(self.filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            fields = reader.__next__()

            return fields

    def __sub__(self, other):
        # diff表示公共序列的差集，即表1中存在而表2不存在的列
        diff = self.dataset - other.dataset
        rdata = []
        # 根据diff生产基于表1的记录
        for row in self.data:
            if row[self.lstname] in diff:
                rdata.append(row)

        f1 = os.path.basename(self.filename)
        f2 = os.path.basename(other.filename)
        f1 = f1.split('.')[0]
        f2 = f2.split('.')[0]

        filename = f1 + '_' + f2 + '.csv'
        filename = os.path.join(os.path.dirname(self.filename), filename)
        # 写入csv文件
        with open(filename, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.header)
            writer.writeheader()
            writer.writerows(rdata)
        return filename


if __name__ == '__main__':
    import sys
    # print(sys.argv[0])
    # for i in sys.argv:

    filename1 = sys.argv[1]
    print filename1
    filename2 = sys.argv[2]

    print filename1, filename2

    file1 = csvread(filename1)
    file2 = csvread(filename2)
    file1 - file2
    file2 - file1
