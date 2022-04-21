#!python2
# coding:utf8
import csv

data = [["American", "美国人"], ["Chinese", "中国人"]]

with open("chinese_data.csv", "wb") as f:
    f.write("\ufeff".encode("utf8"))
    w = csv.writer(f)
    for row in data:
        w.writerow([item.encode("utf8") for item in row])
