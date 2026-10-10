###############################
# Loading Icon Animation Test #
###############################

from menudoodle import MenuDoodle
import turtle
import time
from multiprocessing import Process

doodler = MenuDoodle()

loader = doodler.Loader(0, 0, 20, loaderColor="black", eraserColor="white")
loader.run()

doodler.getScreen().tracer(1)

doodler.mainloop()


 
