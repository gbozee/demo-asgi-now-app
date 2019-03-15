# import json
# import bottle
# from bottle import response

# application = bottle.Bottle()

# @application.get('/')
# def home():
#     return {'hello': 'world'}

# @application.get("/hello")
# def hello():
#     return {'new-hello':'world'}

from starlette.applications import Starlette
from starlette.responses import JSONResponse

application = Starlette()

@application.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})


@application.route("/post-call", methods=['POST'])
async def postCall(request):
    json = await request.json()
    return JSONResponse(json)