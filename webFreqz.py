#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from numpy import *
from matplotlib.pyplot import *
import scipy.signal as signal
import time
import shutil
import os
import wave
import json

app = Flask(__name__)
# 调试模式 修改代码后不用重启flask
app.debug = True
@app.route('/freqz', methods=['GET','POST'])
def FreqzPrint():
    # 前面记得加个b Python对bytes类型的数据用带b前缀的单引号或双引号表示
    imgtime=int(time.time())
    imgName=str(imgtime)+'.png'
    imgPath='static/img/'+imgName
    imgDir='static/img/'
    staticPath='static/'
    if(not os.path.exists(staticPath)):
        os.mkdir(staticPath, 755)
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
        os.mkdir(imgDir,755)
        savefig(imgPath)
        # 记得清除之前画过的 不然会有两次画的重复
        close('all')

    return render_template('freqz.html',b=b,a=a,N=N,img='static/img/'+imgName)

@app.route('/DTMF', methods=['GET','POST'])
def DTMF():
    resPath = "static/res/"
    if (not os.path.exists(resPath)):
        os.mkdir(resPath)
    # 解决vue和jinja模板的冲突
    app.jinja_env.variable_start_string = '{{ '
    app.jinja_env.variable_end_string = ' }}'
    if (request.method == 'POST'):
        # 取样频率
        framerate = 44100
        # 时间10s
        time = 10
        # 时间轴
        t = np.arange(0, time, 1.0 / framerate)

        key = request.form['key']
        dtmf_freqs = {'1': (1209, 697), '2': (1336, 697), '3': (1477, 697), 'A': (1633, 697),
                      '4': (1209, 770), '5': (1336, 770), '6': (1477, 770), 'B': (1633, 770),
                      '7': (1209, 852), '8': (1336, 852), '9': (1477, 852), 'C': (1633, 852),
                      '*': (1209, 941), '0': (1336, 941), '#': (1477, 941), 'D': (1633, 941)}
        dtmf_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#', 'A', 'B', 'C', 'D']
        # wave_data=sine_sine_wave(dtmf_freqs[key][0], dtmf_freqs[key][1], 10, framerate)
        frames = []
        frames.append(sine_sine_wave(dtmf_freqs[key][0], dtmf_freqs[key][1], 1, framerate))
        # 之前太小声一直听不到 后来乘了一万 音效就很明显 奇怪DTMF.py那边的怎么没看到放大倍数
        wave_data = concatenate(frames) * 0.25*10000
        # print(len(wave_data))
        wave_data = wave_data.astype(np.short)
        # 打开WAV文档
        fileName="DTMF"+key+".wav"
        f = wave.open(r"static/res/"+fileName, "wb")
        # 配置声道数、量化位数和取样频率
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(framerate)
        # 将wav_data转换为二进制数据写入文件
        f.writeframes(wave_data.tostring())
        f.close()
        result={
            'statusCode':200,
            'message':"成功",
            'path':"static/res/"+fileName
        }
        return json.dumps(result)
    return render_template('DTMF.html')
# 将两个sin波混叠
def sine_sine_wave(f1, f2, length, rate):
    s1 = sine_wave(f1, length, rate)
    s2 = sine_wave(f2, length, rate)
    ss = s1 + s2
    # divide点除 数组里每个数除以2
    sa = divide(ss, 2.0)
    return sa


# 根据按键位置得到频率,长度和取样频率 得到正弦波 lenth代表声音持续的时间
def sine_wave(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return sin(arange(length) * factor)


if __name__ == '__main__':
    # 加上0.0.0.0.0才能所有ip都可以访问 不然只能本地访问
    app.run(host='0.0.0.0')
