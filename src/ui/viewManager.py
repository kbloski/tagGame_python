import pygame # type: ignore
from ..config.screen import screen
from ..errors.error import throwError

class CreateViewManager:
    __INSTANCE = None
    def __new__(cls):
        if not CreateViewManager.__INSTANCE:
            CreateViewManager.__INSTANCE = super(CreateViewManager, cls).__new__(cls)
        return cls.__INSTANCE
    
    def __init__(self):
        self.__activeView = False
        self.views = { }

    def __trimStringName(self, name = 'view-name'):
        return name.replace(' ','')

    def __viewExist(self, viewName):
        for key in self.views:
            if key == self.__trimStringName( viewName ):
                return True
        return False
        
    def createView(self, name='view-name', view=None):
        if not self.__viewExist(name):
            self.views[ self.__trimStringName(name) ] = view
            return
        throwError("createView - duplicate view name: " + name )

    def setActiveView(self, viewName):
        if self.__viewExist( viewName):
            if self.views[ str( viewName ) ]:
                self.__activeView = viewName

    def render(self):
        if self.__activeView:
            self.views[self.__activeView].render()


viewManager = CreateViewManager()
