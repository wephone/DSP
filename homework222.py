# 之前以2.2.2.py命名后面发现这样导入有问题 所以改成了现在的homework222命名
import matplotlib.pyplot as plt
import numpy as np
# 单位取样序列 n1n2为始末 n0为冲激点
def impseq(n0,n1,n2):
    # 定义一个一维数组 从n1开始到n2 一共n2-n1+1个 即间隔为1 arrange不知为何无法用
    x=np.linspace(n1,n2,(n2-n1+1))
    y=np.zeros((n2-n1+1))
    y[n0-n1]=1
    return [x,y]

# 单位取样序列 n1n2为始末 n0起始点
def stepseq(n0,n1,n2):
    x = np.linspace(n1,n2,(n2-n1+1))
    y1 =np.zeros((n0-n1))
    y2 =np.ones((n2-n0+1))
    y=np.hstack((y1,y2))
    return [x,y]

# 带噪声的余弦函数
def nosieCos(n):
    x=np.linspace(0,n,n)
    y=np.cos(0.04*np.pi*x)+0.2*np.random.random(size=n)
    return [x,y]

# 线状图
def plot(arr):
    plt.plot(arr[0],arr[1])
    plt.show()

# 火柴梗图
def stem(arr):
    plt.stem(arr[0], arr[1])
    plt.show()

# 书上例题 2.2(1)
def ex221():
    x=np.linspace(-5,5,11)
    y=3*impseq(-3,-5,5)[1]-impseq(3,-5,5)[1]
    return [x,y]

# 书上例题 2.2(2)
def ex222():
    x = np.linspace(0, 20, 21)
    y=x*(stepseq(0,0,20)[1]-stepseq(10,0,20)[1])+10*(stepseq(10,0,20)[1]-stepseq(20,0,20)[1])*np.exp(-0.3*(x-10))
    return [x,y]

def ex23():
    x = np.linspace(-10, 10, 21)
    # 复数直接用后缀j表示
    y=np.exp((-0.08+0.3j)*x)
    res=[x,y]
    # 分成2x2，占用第一个，即第一行第一列的子图
    # plt.subplot(221)
    # 分成2x2，占用第二个，即第一行第二列的子图
    # plt.subplot(222)
    # 分成2x1，占用第二个，即第二行一整行
    # plt.subplot(212)

    plt.subplot(221)
    # 实部
    plt.stem(x, np.real(y))# 或者plt.stem(x, y)
    plt.subplot(222)
    # 虚部
    plt.stem(x,np.imag(y))
    plt.subplot(223)
    # 幅度
    plt.stem(x, np.abs(y))
    plt.subplot(224)
    # 相位
    plt.stem(x, np.angle(y))
    plt.show()

# ex23()
# print(3*[1,2,3,4,5])
# 得到的是[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]看来numpy还得多看看文档