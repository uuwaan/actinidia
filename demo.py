import time
import actinidia

print("Pacman: ", end="")
indicator = actinidia.Pacman(10)
for _ in range(0, 100):
    indicator.update()
    time.sleep(0.3)
indicator.clear()
print("finished!")
