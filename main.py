from render import Render

from obj import Obj

from utils import color

my_bmp_file = Render()
my_bmp_file.glInit()
my_bmp_file.glCreateWindow(800,600)
my_bmp_file.glClearColor(0,0,0)
my_bmp_file.glColor(1,1,1)




my_bmp_file.glFinish('polygons.bmp')
