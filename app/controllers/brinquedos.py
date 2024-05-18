from flask import flash, redirect, render_template, url_for
from app import app, db
from app.controllers.forms import BrinquedoForm
from app.models.tables import Brinquedo

@app.route('/brinquedos/adicionar', methods=['GET', 'POST'])
def add_brinquedo():
    form = BrinquedoForm()
    if form.validate_on_submit():
        novo_brinquedo = Brinquedo(
            nome=form.nome.data,
            categoria=form.categoria.data
        )
        db.session.add(novo_brinquedo)
        db.session.commit()
        flash('Brinquedo adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('add_brinquedo.html', form=form)

@app.route('/brinquedos/lista')
def lista_de_brinquedos():
    brinquedos = Brinquedo.query.all()
    return render_template('lista_de_brinquedos.html', brinquedos=brinquedos)

@app.route('/brinquedos/<int:id>')
def detalhes_brinquedo(id):
    brinquedo = Brinquedo.query.get_or_404(id)
    emprestimos = brinquedo.emprestimos
    return render_template('detalhes_brinquedo.html', brinquedo=brinquedo, emprestimos=emprestimos)
