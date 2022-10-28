import sys

from tornado.ioloop import IOLoop

from urls import App

if __name__ == '__main__':
    print(f'Python: {sys.version}')
    print('iniciando...')
    app = App()
    app.listen(8000, '0.0.0.0')
    IOLoop.current().start()
