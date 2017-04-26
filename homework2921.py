# 导入2.2.2作为基类 调用2.2.2方法时无需在引入这两个库
from numpy import *
from matplotlib.pyplot import *
# python的数字信号库 可以用一些filter这样的滤波器方法
import scipy.signal as signal
import homework222 as base

# 卷积convolve函数
# numpy.convolve(a, v, mode=’full’)
# （http://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html#r17）
# a，v是两个算子(array_like)，mode有三种情况，
# ’full‘ : 默认值，将计算每个点的卷积，即若a，v长度为n，m。最终输出图形x长度为（n+m-1），在边界处信号不完全重叠，即存在边界效应。
# ‘same‘：返回长度为max（n,m），仍然有边界效应。
# ‘valid‘：返回长度为max（n,m）-min(n,m)+1。其中只会显示两个信号重叠的部分，不会有边界效应。

def homework230():
    # 输入序列 arange linspace这些都是数组 需要用mat转为矩阵 不然得下都得手动加shape
    n = arange(-1, 4)
    # print(mat(n))
    # print(type(mat(n)))
    # print(mat(n).shape)
    # 每个序列对应的值
    x = arange(1, 6)
    # 在横坐标上分点
    k=arange(0,501)
    w=(pi/500)*k
    # 不可以直接转置 这时n的shape还是(5,)
    # print(transpose(n))
    # 需要这样转置
    n.shape=(1,5)
    x.shape=(1,5)
    k.shape=(1,501)
    # 计算DTFT 用矩阵相乘代替连加
    # (5, 501)
    # print(((exp(-1j*pi/500))**(transpose(n)*k)).shape)
    # 用*时 operands could not be broadcast together with shapes (1,5) (5,501)
    # 使用array时，运算符 * 用于计算数量积（点乘），函数dot() 用于计算矢量积（叉乘）
    # 与array不同的是，使用matrix时，运算符 * 用于计算矢量积，函数multiply()用于计算数量积
    X = dot(x,((exp(-1j*pi/500))**(dot(transpose(n),k))))
    X.shape=(501,)
    magX=abs(X)
    angX=angle(X)
    subplot(211)
    plot(w/pi,magX)
    subplot(212)
    plot(w/pi,angX)
    show()

# a = array( [(1,2),(-1,5)] )
# b=array( [(7,2),(1,0)] )
# c=2
# print(a.shape)
# print(b)
# print(a**b)

# [[ 2  4]
#  [ 0 32]]
# print(2**a)

# [[128   4]
#  [  2   1]]
# print(2**b)

def homework231():
    # 这道我实在看不懂书上在讲啥
    b=array([0.0181,0.0543,0.0543,0.0181])
    a=array([1.0000,-1.7600,1.1829,-0.2781])
    m=arange(0,len(b))
    m.shape=(1,len(b))
    l=arange(0,len(a))
    l.shape=(1,len(a))
    K=500
    k=arange(0,K+1)
    w=(pi*k)/K
    w.shape=(1,501)
    b.shape=(1,4)
    num=dot(b,exp(-1j*dot(transpose(m),w)))
    den=dot(a,exp(-1j*dot(transpose(l),w)))
    H=num/den
    magH=abs(H)
    angH=angle(H)
    base.plot([w/pi,magH])
    base.plot([w/pi,angH])

def homework231freqz():
    b=array([0.0181,0.0543,0.0543,0.0181])
    a=array([1.0000,-1.7600,1.1829,-0.2781])
    result=signal.freqz(b,a,500)
    magH=abs(result[1])
    angH=angle(result[1])
    # base.plot([result[0],magH])
    # base.plot([result[0],angH])
    subplot(2,1,1)
    plot(result[0] , magH)
    subplot(2,1,2)
    plot(result[0] , angH)
    show()
# homework231()
homework230()
homework231freqz()
# print(arange(1,5).shape)