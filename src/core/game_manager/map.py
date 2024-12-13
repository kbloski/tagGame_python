from ...assets.drawMap import CreateMapSurface
from ..map import CreateMap
from ...config.screen import screen

SURFACE = CreateMapSurface(screen.get_width(), screen.get_height())
SURFACE.createRamp( 400, 700, 150, 3)
SURFACE.createRamp( 100, 900, 300, 3)
SURFACE.createRamp( 700, 500, 500, 3)

MAP1 = CreateMap( SURFACE.getMapSurface() )