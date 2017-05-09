# http://blog.csdn.net/hankhanti/article/details/49902441
from numpy import *
from matplotlib.pyplot import *
import scipy.signal as signal
import time,threading
import shutil
import os
# apt-get install python3-pyaudio
import pyaudio
import wave
import sys

resPath="static/res/"
if(not os.path.exists(resPath)):
    os.mkdir(resPath)

# 录音函数 在子线程使用
def recorder():
    print('thread %s start.' % threading.current_thread().name)
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "static/res/output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print('thread %s ended.' % threading.current_thread().name)
    return


#播音 向PC的扩音器或耳机播出
def play_tone(digits):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)

    play_dtmf_tone(stream, digits)
    stream.close()
    p.terminate()


def play_dtmf_tone(stream, digits, length=0.20, rate=44100):
    dtmf_freqs = {'1': (1209, 697), '2': (1336, 697), '3': (1477, 697), 'A': (1633, 697),
                  '4': (1209, 770), '5': (1336, 770), '6': (1477, 770), 'B': (1633, 770),
                  '7': (1209, 852), '8': (1336, 852), '9': (1477, 852), 'C': (1633, 852),
                  '*': (1209, 941), '0': (1336, 941), '#': (1477, 941), 'D': (1633, 941)}
    dtmf_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#', 'A', 'B', 'C', 'D']
    if type(digits) is not type(''):
        digits = str(digits)[0]
        # 将数字拼接成字符串 等下字符串循环出来单个字符
    digits = ''.join([dd for dd in digits if dd in dtmf_digits])

    def sine_sine_wave(f1, f2, length, rate):
        s1 = sine_wave(f1, length, rate)
        s2 = sine_wave(f2, length, rate)
        ss = s1 + s2
        # divide点除 数组里每个数除以2
        sa = divide(ss, 2.0)
        return sa

    def sine_wave(frequency, length, rate):
        length = int(length * rate)
        factor = float(frequency) * (math.pi * 2) / rate
        return sin(arange(length) * factor)

    # 循环出单个字符
    for digit in digits:
        digit = digit.upper()
        frames = []
        frames.append(sine_sine_wave(dtmf_freqs[digit][0], dtmf_freqs[digit][1], length, rate))
        # concatenate数组拼接
        chunk = concatenate(frames) * 0.25
        # 向pyaudio.open的流写入即播放出来
        stream.write(chunk.astype(float32).tostring())
        time.sleep(0.2)


print('thread %s start.' % threading.current_thread().name)
threads = []
t = threading.Thread(target=recorder)
threads.append(t)
t.start()

# give some time to bufer
time.sleep(1)

if len(sys.argv) != 2:
    digits = "12"
else:
    digits = sys.argv[1]
play_tone(digits)
print('thread %s ended.' % threading.current_thread().name)





