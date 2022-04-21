from flask import Flask, jsonify, request
import json

app = Flask(__name__)

entradas = [
    {
        'id':'0',
        'responsável':'Vinicius',
        'tarefa':'Desenvolver método GET',
        'status':'concluído'
    },
    {
        'id':'1',
        'responsável':'Lima',
        'tarefa':'Desenvolver método POST',
        'status':'Pendente'
    }
]

@app.route('/tarefa/<int:id>/',methods=['GET','PUT','DELETE'])
def gerencia_tarefas(id):
    if request.method == 'GET':
        try:
            response = entradas[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não registrada'.format(id)
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        entradas[id]['status']= dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        entradas.pop(id)
        return jsonify({'status':'sucesso','mensagem':'entrada excluída'})
    
@app.route('/tarefa/', methods=['POST','GET'])
def lista_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(entradas)
        dados['id'] = posicao
        entradas.append(dados)
        return jsonify(entradas[posicao])
    elif request.method == 'GET':
        return jsonify(entradas)

if __name__ == '__main__':
    app.run(debug='True')