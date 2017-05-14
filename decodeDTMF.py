import numpy as np
import wave
import math

THRESHOLD = 328
CHUNK = 1024
hi_freqs = [1209, 1336, 1477, 1633]
lo_freqs = [697, 770, 852, 941]

dtmf_freqs = {'1': (1209, 697), '2': (1336, 697), '3': (1477, 697), 'A': (1633, 697),
              '4': (1209, 770), '5': (1336, 770), '6': (1477, 770), 'B': (1633, 770),
              '7': (1209, 852), '8': (1336, 852), '9': (1477, 852), 'C': (1633, 852),
              '*': (1209, 941), '0': (1336, 941), '#': (1477, 941), 'D': (1633, 941)}


def find_digit(hi, lo):
    for key in dtmf_freqs:
        if (dtmf_freqs[key][0] == hi) and (dtmf_freqs[key][1] == lo):
            return key

def IsSilent(samples):
    if max(np.absolute(samples)) <= THRESHOLD:
        return True
    return False


def goertzel_mag(numSamples, target_freq, sample_rate, data):
    '''''
    int k, i
    float floatnumSamples
    float omega, sine, cosine, coeff, q0, q1, r2, magnitude, real, imag
    '''
    # floatnumSamples = (float)numSamples

    scalingFactor = numSamples / 2.0
    k = (int)(0.5 + ((numSamples * target_freq) / sample_rate))
    omega = (2.0 * math.pi * k) / numSamples
    sine = math.sin(omega)
    cosine = math.cos(omega)
    coeff = 2.0 * cosine
    q0 = 0
    q1 = 0
    q2 = 0

    for i in range(0, (int)(numSamples)):
        # print("Hello")
        q0 = (coeff * q1) - q2 + data[i]
        q2 = q1
        q1 = q0

        # real = (q1 - (q2 * cosine)) / scalingFactor
    # imag = (q2 * sine) / scalingFactor

    # magnitude = math.sqrt((real * real) + (imag * imag))
    magnitude = (q2 * q2) + (q1 * q1) - (coeff * q1 * q2)
    return magnitude

if __name__ == '__main__':
    sample_rate = 44100

    CHUNK_SIZE = 1024
    NOISE_CHUNK_COUNT = 4
    MAX_CHUNK_COUNT = 16

    wav = wave.open('okoutput.wav', 'rb')
    n = wav.getnframes()

    # n = 440320
    # 样本数
    print("样本数： %d" % n)

    # debug = wav.readframes(1)


    c = 0  # 计数

    channels = wav.getnchannels()
    sample_width = wav.getsampwidth()

    chunk_sample_count = (int)(CHUNK_SIZE / channels / sample_width)

    digits = []  # 记录digit出现的次数及顺序，每个元素由{digit: count}组成
    pre_digit = ''  # 记录前一次出现的digit
    while (c * CHUNK_SIZE < n * channels * sample_width):
        data_chunk_string = wav.readframes(chunk_sample_count)
        chunk_data = np.fromstring(data_chunk_string, dtype=np.int16)
        if (not IsSilent(chunk_data)):
            max_mag_hi_freq = 0
            maxvalue_mag_hi_freq = 0
            for freq in hi_freqs:
                mag = goertzel_mag(chunk_sample_count, freq, sample_rate, chunk_data)
                # if c == 277:
                #    print("(%d)CHUNK %d magnitude with higher frequency (%d) = %f" % \
                #          (max_mag_hi_freq, c, freq, mag))
                if (mag > maxvalue_mag_hi_freq):
                    maxvalue_mag_hi_freq = mag
                    max_mag_hi_freq = freq

                    # if c == 277:
            # print("CHUNK %d maximal magnitude located high frequency(%d) " % \
            #              (c, max_mag_hi_freq))
            max_mag_lo_freq = 0
            maxvalue_mag_lo_freq = 0
            for freq in lo_freqs:
                mag = goertzel_mag(chunk_sample_count, freq, sample_rate, chunk_data)
                # print("CHUNK %d magnitude with lower frequency (%d) = %f" % \
                #      (c, freq, mag))
                if (mag > maxvalue_mag_lo_freq):
                    maxvalue_mag_lo_freq = mag
                    max_mag_lo_freq = freq

                    # print("CHUNK %d maximal magnitude located (%d, %d) " % \
            # (c, max_mag_hi_freq, max_mag_lo_freq))
            digit = find_digit(max_mag_hi_freq, max_mag_lo_freq)

            # 判断 digit 是否前一次出现过，若是则相对应次数加一, 否则新增元素
            digits_element = dict()
            if (pre_digit != digit):
                digits_element[digit] = 1
            else:
                digits_element = digits.pop()
                digits_element[digit] += 1

            digits.append(digits_element)

            pre_digit = digit

            # print("CHUNK %d: %c" % (c, digit))

        c = c + 1
    wav.close()

    for i in range(0, len(digits)):
        for k in digits[i]:
            if digits[i][k] > NOISE_CHUNK_COUNT:
                t = 0
                while (t < digits[i][k]):
                    t += MAX_CHUNK_COUNT
                    print(k)