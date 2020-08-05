from render import Render, V2, V3

from obj import Obj

from utils import color

my_bmp_file = Render()
my_bmp_file.glInit()
my_bmp_file.glCreateWindow(1000,1000)
my_bmp_file.glClear()

 
my_bmp_file.loadModel('./models/hand.obj', V3(375,500,0), V3(50,50,50))

my_bmp_file.glFinish('polygons.bmp')
