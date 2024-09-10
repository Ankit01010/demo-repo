from flask import Flask,request
                app = Flask(__name__)
                @app.route('/', methods=['GET'])
                def hello():
                    return f'Hello World from v1!\n'
