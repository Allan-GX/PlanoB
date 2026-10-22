from flask import Flask
from Blueprints.auth.login import login_bp
from Blueprints.hubs.hubs import hub_bp
from Blueprints.admin.admin import admin_bp

app = Flask(__name__)

app.register_blueprint(login_bp)
app.register_blueprint(hub_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    # debug=True reinicia o servidor automaticamente ao salvar alterações no código
    # host="0.0.0.0" torna o servidor acessível na sua rede local (opcional)
    # port=5000 define a porta padrão do Flask
    app.run(debug=True)