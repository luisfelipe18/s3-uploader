from tornado.web import Application, url, StaticFileHandler
from tornado_swagger.setup import setup_swagger

from handlers.HealtService import HealtService
from handlers.FileManager import FileManagerService


class App(Application):
    rutas = [
        url(r'/test-filemanager/health$', HealtService),
        url(r'/test-filemanager/forecast', FileManagerService),
        url(r'/(favicon.ico)', StaticFileHandler, {"path": "static/"})
    ]

    def __init__(self):
        configuracion = dict(
            debug=False
        )
        setup_swagger(
            self.rutas,
            swagger_url='/test-filemanager/swagger',
            api_base_url='/',
            description='Lundero - Equipo de Inteligencia Artificial.',
            title='FileManager',
            api_version='0.1.0',
            contact='soporte@lundero.com'
        )
        super(App, self).__init__(self.rutas, **configuracion)
