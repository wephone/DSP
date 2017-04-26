#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from numpy import *
from matplotlib.pyplot import *
import scipy.signal as signal
import time
import shutil
import os

app = Flask(__name__)

@app.route('/freqz', methods=['GET','POST'])
def FreqzPrint():
    # 前面记得加个b Python对bytes类型的数据用带b前缀的单引号或双引号表示
    imgtime=int(time.time())
    imgName=str(imgtime)+'.png'
    imgPath='static/img/'+imgName
    imgDir='static/img/'
    b=''
    a=''
    N=''
    if(request.method=='POST'):
        b = request.form['b']
        a = request.form['a']
        N = request.form['N']
        bArr=b.split(',')
        # 将数组里的字符串转为数字
        bArr=[float(x) for x in bArr]
        aArr=a.split(',')
        aArr = [float(x) for x in aArr]
        # print(bArr)
        # print(type(array([0.0181,0.0543,0.0543,0.0181])))
        # print(type(array(bArr)))
        # print(array(bArr))
        # print(array([0.0181, 0.0543, 0.0543, 0.0181]))
        result = signal.freqz(bArr, aArr, int(N))
        magH = abs(result[1])
        angH = angle(result[1])
        subplot(2, 1, 1)
        plot(result[0], magH)
        subplot(2, 1, 2)
        plot(result[0], angH)
        if(os.path.exists(imgDir)):
            shutil.rmtree('static/img/')
        os.mkdir(imgDir)
        savefig(imgPath)
        # 记得清除之前画过的 不然会有两次画的重复
        close('all')

    return render_template('freqz.html',b=b,a=a,N=N,img='static/img/'+imgName)

if __name__ == '__main__':
    app.run()