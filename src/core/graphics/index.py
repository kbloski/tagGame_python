from .drawMap import CreateMapSurface
from .drawPlayer import drawCharacter
from ..map import CreateMap
from ...config.screen import screen

SURFACE = CreateMapSurface(screen.get_width(), screen.get_height())
SURFACE.createRamp( 400, 700, 150, 3)
SURFACE.createRamp( 100, 900, 300, 3)
SURFACE.createRamp( 700, 500, 500, 3)

MAP1 = CreateMap( SURFACE.getMapSurface() )

player1 = drawCharacter()
player2 = drawCharacter( '#00ff00')