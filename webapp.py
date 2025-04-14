from flask import Flask, request, jsonify, render_template
import app

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return render_template('index.html')

@app_flask.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(app.list_tasks())

@app_flask.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({'error': 'Falta el nombre de la tarea'}), 400
    app.add_task(data['nombre'])
    return jsonify({'mensaje': 'Tarea agregada correctamente'}), 201

@app_flask.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    try:
        app.remove_task(index)
        return jsonify({'mensaje': 'Tarea eliminada'})
    except:
        return jsonify({'error': 'Índice inválido'}), 400

@app_flask.route('/tasks/<int:index>/complete', methods=['PATCH'])
def complete_task(index):
    try:
        app.complete_task(index)
        return jsonify({'mensaje': 'Tarea completada'})
    except:
        return jsonify({'error': 'Índice inválido'}), 400

@app_flask.route('/tasks/<int:index>', methods=['PUT'])
def edit_task(index):
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({'error': 'Falta el nuevo nombre'}), 400
    try:
        app.edit_task(index, data['nombre'])
        return jsonify({'mensaje': 'Tarea editada'})
    except:
        return jsonify({'error': 'Índice inválido'}), 400

if __name__ == '__main__':
    app_flask.run(debug=True)
