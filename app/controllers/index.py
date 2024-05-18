from datetime import datetime
from flask import flash, render_template, request, redirect, url_for
from app import app, db
from app.controllers.forms import EmprestimoForm
from app.models.tables import Professor, Brinquedo, Emprestimo


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmprestimoForm()
    
    if form.validate_on_submit():
        professor = Professor.query.filter((Professor.nome == form.nome_do_professor_ou_id.data) |
                                           (Professor.id == form.nome_do_professor_ou_id.data)).first()
        brinquedo = Brinquedo.query.filter((Brinquedo.nome == form.nome_do_brinquedo_ou_id.data) |
                                           (Brinquedo.id == form.nome_do_brinquedo_ou_id.data)).first()

        if professor and brinquedo and brinquedo.disponivel:
            emprestimo = Emprestimo(professor_id=professor.id, brinquedo_id=brinquedo.id)
            db.session.add(emprestimo)
            
            brinquedo.disponivel = False
            brinquedo.ultima_alteracao = datetime.utcnow()
            
            db.session.commit()
            flash('Empréstimo realizado com sucesso!', 'success')
        else:
            flash('Professor ou brinquedo não encontrados, ou brinquedo indisponível.', 'danger')
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form)