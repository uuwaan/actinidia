import time
import actinidia

print("Pacman: ", end="")
indicator = actinidia.Pacman(10)
for i in range(0, 100):
    indicator.update("doing stuff {0}/{1}".format(i, 100))
    time.sleep(0.3)
indicator.clear()
print("finished!")
