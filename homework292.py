# 导入2.2.2作为基类 调用2.2.2方法时无需在引入这两个库
from numpy import *
from matplotlib.pyplot import *
# python的数字信号库 可以用一些filter这样的滤波器方法
import scipy.signal as signal
import homework222 as base

# 例2.28 冲激和阶跃响应
def ImpulseStepresponse():
    # 获取冲击函数返回值作为x1 并把生成的序列作为n
    n=base.impseq(0,0,20)[0]
    x1=base.impseq(0,0,20)[1]
    # 获取阶跃函数返回值作为x2
    x2 = base.stepseq(0, 0, 20)[1]
    b=[1]
    a=[1,-0.8,0.5]
    # FIR滤波器 y(n)=b[0]x[n]+b[1]x[n-1]+...+b[P]x[n-P]
    # IIR滤波器 y(n)=b[0]x[n]+b[1]x[n-1]+...+b[P]x[n-P]-a[1]y[n-1]-a[2]y[n-2]-...-a[Q]y[n-Q]
    # b和a是滤波器的系数，x是输入
    # 套上述公式得出书上的题目
    # 得再去看看lfilter文档
    h=signal.lfilter(b,a,x1)
    s=signal.lfilter(b,a,x2)
    subplot(211)
    stem(n,h)
    subplot(212)
    stem(n,s)
    show()

ImpulseStepresponse()
