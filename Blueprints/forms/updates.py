from flask import Blueprint, render_template, request, url_for, redirect

update_bp = Blueprint('update', __name__)

@update_bp.route('/upd_ocorrencia/<int:id>', methods=['GET','POST'])
def upd_ocorrencia(id):

    # ocorrencia = "Miro passa o caminho p a table de ocorrencias aqui"

    ocorrencia = {
            "id": 1,
            "data_registro": "2026-06-06 12:00",
            "estado": "PB",
            "cidade": "Cajazeiras",
            "tipo_crime": "Furto",
            "cpf_vitima": "123.456.789-00",
            "descricao": "Exemplo de relato de teste.",
            "status": "Em Andamento"
        }

    if request.method == 'POST':

        # ocorrencia.estado = request.form.get("estado") COLOCA TODOS A BAIXO NESSE PADRÂO

        estado = request.form.get("estado")
        cidade = request.form.get("cidade")
        tipo_crime = request.form.get("tipo_crime")
        cpf = request.form.get("cpf_vitima")
        relato = request.form.get("descricao")
        status = request.form.get("status")

        if estado and cidade and tipo_crime and cpf and relato and status:
            print(estado, cidade,tipo_crime,cpf,relato,status)
            return redirect(url_for('lista.list_ocorrencia'))

    return render_template('editar_ocorrencia.html', ocorrencia=ocorrencia)