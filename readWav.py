# http://bigsec.net/b52/scipydoc/wave_pyaudio.html
import wave
import pylab as pl
import numpy as np

# 打开WAV文档 "rb"(二进制模式)
f = wave.open("okoutput.wav", "rb")
# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
# getparams：一次性返回所有的WAV文件的格式信息，它返回的是一个组元(tuple)：
# 声道数, 量化位数（byte单位）, 采样频率, 采样点数,
# 压缩类型, 压缩类型的描述。wave模块只支持非压缩的数据，因此可以忽略最后两个信息
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
# 传递一个参数指定需要读取的长度（以取样点为单位）
# readframes返回的是二进制数据（一大堆bytes) 在Python中用字符串表示二进制数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转换为数组 根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
wave_data = np.fromstring(str_data, dtype=np.short)
# 通过fromstring函数将字符串转换为数组，通过其参数dtype指定转换后的数据格式，
# 由于我们的声音格式是以两个字节表示一个取样值，因此采用short数据类型转换。现在我们得到的wave_data是一个一维的short类型的数组，
# 但是因为我们的声音文件是双声道的，因此它由左右两个声道的取样交替构成：LRLRLRLR....LR（L表示左声道的取样值，R表示右声道取样值）。
# 修改wave_data的sharp之后
# wave_data.shape = -1, 2
# print(wave_data)
# wave_data = wave_data.T
# print(wave_data)

time = np.arange(0, nframes) * (1.0 / framerate)
pl.plot(time, wave_data)
pl.show()

# 绘制波形
# pl.subplot(211)
# pl.plot(time, wave_data[0])
# pl.subplot(212)
# pl.plot(time, wave_data[1], c="g")
# pl.xlabel("time (seconds)")
# pl.show()

# 奇怪我得把time长度砍一半才正常  断点调试后发现我这个音频时单声道的nchannels=1 所以去掉wavedata的shape和转置就行
# 最后通过取样点数和取样频率计算出每个取样的时间
# time = np.arange(0, nframes) * (1.0 / framerate)
# time = np.arange(0, nframes/2) * (1.0 / framerate)
# print(len(time))
# print(len(wave_data[0]))
# pl.subplot(211)
# pl.plot(time, wave_data[0])
# pl.subplot(212)
# pl.plot(time, wave_data[1], c="g")
# pl.xlabel("time (seconds)")
# pl.show()