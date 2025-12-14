import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random as ran
import keyboard



style.use("fivethirtyeight")

graf = plt.figure()
dimen = graf.add_subplot(1, 1, 1)

def animar(i):
    xs = []
    ys = []
    for j in range(30):    
        xs.append(j)
        ys.append(ran.randint(16, 19))
    if keyboard.is_pressed('t'):
        ys[:] = [40] * len(ys)
    dimen.clear()
    dimen.plot(xs, ys)
    

ani = animation.FuncAnimation(graf, animar, interval=1000)
plt.show()