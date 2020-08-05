from render import Render, V2, V3

from obj import Obj

from utils import color

my_bmp_file = Render()
my_bmp_file.glInit()
my_bmp_file.glCreateWindow(1000,1000)
my_bmp_file.glClear()

 
my_bmp_file.loadModel('./models/pato.obj', V3(500,500,0), V3(300,300,300))

my_bmp_file.glFinish('polygons.bmp')
