from wtiproj03.wtiproj03_API import app
import cherrypy

cherrypy.tree.graft(app.wsgi_app, '/')
cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 5000,
                        'engine.autoreload.on': False,
                        })

if __name__ == '__main__':
    cherrypy.engine.start()