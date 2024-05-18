from app import app, db
from flask import render_template, url_for, redirect, flash
from app.controllers.forms import ProfessorForm
from app.models.tables import Professor

@app.route('/professores/adicionar', methods=['GET', 'POST'])
def add_professor():
    form = ProfessorForm()
    if form.validate_on_submit():
        novo_professor = Professor(
            nome=form.nome.data
        )
        db.session.add(novo_professor)
        db.session.commit()
        flash('Professor adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('add_professor.html', form=form)

@app.route('/professores/lista')
def lista_de_professores():
    professores = Professor.query.all()
    return render_template('lista_de_professores.html', professores=professores)

@app.route('/professores/lista/<int:id>')
def perfil_professor(id):
    professor = Professor.query.get_or_404(id)
    return render_template('perfil_professor.html', professor=professor)