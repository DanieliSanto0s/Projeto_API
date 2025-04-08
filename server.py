from flask import Flask
import usuarios

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return usuarios.get()

@app.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    return usuarios.getBy(id)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    return usuarios.post()

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    return usuarios.alterar(id)

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    return usuarios.apagar(id)

@app.route('/usuarios/auth', methods=['POST'])
def autenticar_usuario():
    return usuarios.auth()

if __name__ == '__main__':
    app.run(debug=True)
