# from flask import Blueprint, render_template, request
# import db_fake
#
# login_bp = Blueprint('login', __name__)
#
# @login_bp.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#        cpf = request.form["cpf"]
#        senha = request.form["password"]
#        "__table__ = db.metadata.tables['tabela']"
#        "usuario = db.session.get(Tabela,id)"
#        "senha_db = usuaria.c.senha"
#         if senha == senha_db:
#            return render_template("index.html")
#     return render_template('login.html')