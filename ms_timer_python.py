'''
用win32api.GetSystemTime()不是太精确，值15毫秒才变一下，最好用time.clock()，这个能到毫秒级，
最精确的办法是用QueryPerformanceFrequency()函数和QueryPerformanceCounter()函数。
用CPU周期计时，很精确。
win32api里没定义，调用办法如下：
import time,ctypesfreq = ctypes.c_longlong(0)
ctypes.windll.kernel32.QueryPerformanceFrequency(ctypes.byref(freq))
f=freq.value
print f
ctypes.windll.kernel32.QueryPerformanceCounter(ctypes.byref(freq))
n1=freq.value
print n1
time.sleep(1)
ctypes.windll.kernel32.QueryPerformanceCounter(ctypes.byref(freq))
n2=freq.value
print n2
print (n2-n1)/(f+0.)

'''
