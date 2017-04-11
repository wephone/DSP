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
    # FIR 设置a=1 signal.lfilter(b,1,x1)
    # b和a是滤波器的系数，x是输入
    # 套上述公式得出书上的题目
    # 得再去看看lfilter文档
    h=signal.lfilter(b,a,x1)
    s=signal.lfilter(b,a,x2)
    # roots(p) 多项式求根 返回具有在p中给出的系数的多项式的根。 多项式为p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]
    # 我测试后的例子 多项式 x平方-2x+1 即roots(1,-2,1) 得到[ 1.  1.]
    # x平方-6x+8 roots([1,-6,8])得到 [ 4.  2.]
    # 其次解的每个特征根模都小于1时系统稳定
    z=roots(a)
    # 得到极点的模制
    magz=abs(z)
    print(z)
    print(magz)
    subplot(211)
    stem(n,h)
    subplot(212)
    stem(n,s)
    show()

def Convolution():
    b=[1,0.5]
    a=[1,-0.8,0.6]
    x=base.impseq(0,0,20)[1]
    n=base.impseq(0,0,20)[0]
    # 冲激响应
    h=signal.lfilter(b,a,x)
    subplot(211)
    stem(n, h)
    title("冲激响应")
    # 卷积求系统对x(n)的响应
    # 为防止卷积的两个序列不对齐,导致出现卷积值无法确定,而计算错误(即边界效应)
    # 需要对冲激响应进行周期延拓 保证每个x都能对应上正确的h
    # 用法：numpy.tile(a, reps)
    # 其中a为数组，reps为重复的次数 结果和书上有点不太一样 最后还是没做延拓
    # 这个可能也不需要延拓 都是0开始 一个到10一个到20
    # nh = tile(h,2)
    # subplot(412)
    # stem(linspace(0,41,42), nh)
    # title("周期延拓后的冲激响应")

    # 两个星号表示几次方
    x1=0.8**linspace(0,10,11)
    y1=convolve(x1,h)
    subplot(212)
    stem(linspace(0, size(y1)-1, size(y1)), y1)
    title("卷积后")
    show()

# ImpulseStepresponse()
Convolution()