from .drawMap import CreateMapSurface
from .drawPlayer import drawCharacter
from .drawMouse import drawMouse
# from map import CreateMap
from ..config.screen import screen

# Mouse
mouseSurfaces = {
    'basic' : drawMouse()
}

# Maps
map1 = CreateMapSurface(screen.get_width(), screen.get_height())
map1.createRamp( 400, 700, 150, 3)
map1.createRamp( 100, 900, 300, 3)
map1.createRamp( 700, 500, 500, 3)
map1.createRamp( 300, 200, 500, 3)
map1_surface = map1.getMapSurface()

# Players
player1 = drawCharacter()
player2 = drawCharacter( '#00ff00')