import bottle
from bottle import route,error,run,request,response

from placeholder import Placeholder

@route('/',method='GET')
def index():
    width = request.query.getone('width')
    height = request.query.getone('height') or width 
    color = request.query.getone('color') or 'grey'
    response.content_type= 'image/png'
    try:
        width = int(width)
        height = int(height)
    except:
        width = 320
        height = 240
        color = 'grey'
    print color

    return Placeholder(width=width,height=height,color=color).get_binary()

@error(404)
def error404(error):
    return '404'

run(host="localhost",port=8080)
