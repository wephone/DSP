#-*- coding: utf-8 -*-
from numpy import *
from matplotlib.pyplot import *

def DFT(xn,N):
    n=arange(0,N)
    n.shape=(1,N)
    k=arange(0,N)
    k.shape=(1,N)
    WN=exp(-2j*pi/N)
    # 和前面DTFT一样 用矩阵叉乘实现连加
    nk=dot(transpose(n),k)
    WNnk=WN**nk
    XK=dot(xn,WNnk)
    return XK

N=6
x=array([1,1,1,1,1,1])
x.shape=(1,N)
X=DFT(x,N)
magX=abs(X)
phaX=angle(X)*180/pi
k=arange(0,N)
subplot(211)
stem(k,magX[0])
title(u'DFT mag')
subplot(212)
stem(k,phaX[0])
title(u'DFT pha')
xlabel('k')
show()
# numpy的shape感觉是个坑，每次都得设置shape 而且还要phaX[0] 取0
# 得再查查矩阵生成的问题