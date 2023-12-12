from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request, jsonify , render_template
from datetime import datetime

# Configuração do Flask
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')



# Inicialização do SQLAlchemy e do Migrate
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

# Importações do banco de dados



class Eventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ativo = db.Column(db.String(20), nullable=False)
    emissor = db.Column(db.String(20))
    data_base = db.Column(db.DateTime, default=datetime.today())
    data_liquidacao = db.Column(db.DateTime, default=datetime.today())






@app.route("/")
def home():
    eventos = Eventos.query.filter(db.func.extract("month",Eventos.data_liquidacao) == datetime.today().month)\
        .filter(db.func.extract("year",Eventos.data_liquidacao) == datetime.today().year)\
            .filter(db.func.extract("day",Eventos.data_liquidacao) >= datetime.today().day).order_by(Eventos.data_liquidacao.asc()).all()
    return render_template("main_eventos.html" , eventos = eventos)



@app.route('/adicionar_eventos' , methods=['POST'])
def adicionar_eventos():
    dados = request.get_json()
    evento = Eventos(ativo=dados['ativo']  ,  emissor = 'na'  , 
                    data_base = datetime.today() ,  
                    data_liquidacao = datetime.strptime(dados['data_liquidacao'] , "%d/%m/%Y" ))
    db.session.add(evento)
    db.session.commit()
    return jsonify({"message": "Eventos Adicionados com sucesso"})



@app.route("/listar_ativos" )
def listar_ativos():
    eventos = Eventos.query.all()
    ativos = []
    for item in eventos:
        if item.ativo not in ativos:
            ativos.append(item.ativo)

    dados = {"ativos": ativos}

    return render_template("ativos_cadastrados.html" , ativos=dados['ativos'])


@app.route("/atualizar_emissores")
def atualizar_emissores():
    return jsonify({"message": "Emissores Atualizados"})





if __name__ == '__main__':
    app.run(debug=True)







