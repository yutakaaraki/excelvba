#!/bin/python36

import datetime

t=datetime.date.today()

fname=t.strftime("%Y-%m-%d") + ".txt"

with open(fname,"w",encoding="utf-8") as f:
        f.write("書き込みました。\n改行しました。\n")