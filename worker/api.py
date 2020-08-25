from flask import Flask, request
import flask_restful



app = Flask('UP')
api = flask_restful.Api(app)

todos={}


class HelloWorld(flask_restful.Resource):
    def get(selfself):
        return {'hello': 'world'}

# Method 1: add resource
class TodoSimple(flask_restful.Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

#api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')
# api.add_resource(HelloWorld, '/', '/hello')


# Method 2: route
@app.route('/', methods=['get'])
def test():
    return 'hi'

@app.route('/test', methods=['get'])
def hitest():
    return 'hi test'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
