import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure() # 获取matplotlib的绘图figure对象

def f(x, y): # 函数定义
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120) 
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

im = plt.imshow(f(x, y), animated=True) # 调用imshow实现绘图.这里参数animated=True很重要

def updatefig(*args): # FuncAnimation会将updatefig中的数据传递给绘图句柄,从而更新绘图
    global x, y
    x += np.pi / 15.
    y += np.pi / 20.
    im.set_array(f(x, y))
    return im,  # 这里的,很重要.

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
