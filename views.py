from app import app , db 
from flask import render_template , jsonify , request
from models.models import Eventos





@app.route("/")
def home():
    return render_template("main_template.html")



@app.route('/adicionar_eventos' , methods=['POST'])
def adicionar_eventos():
    dadoa = request.get_json()
    evento = Eventos(ativo=dados['ativo']  ,  emissor = 'na'  , 
                    data_base = datetime.today() ,  data_liquidacao = dados['data_liquidacao'] )
    db.session.add(evento)
    db.session.commit()

    return jsonify({"message": "Eventos Adicionados com sucesso"})



@app.route("/listar_ativos" )
def listar_ativos():
    return render_template("ativos_cadastrados.html")


@app.route("/atualizar_emissores")
def atualizar_emissores():
    return jsonify({"message": "Emissores Atualizados"})