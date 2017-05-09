from numpy import *
import scipy.signal as signal

# 书P84
def residuez():
    b=[1,-0.5]
    a=[1,0.75,0.125]
    RPC=signal.residuez(b,a)
    print(RPC)

residuez()