from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BrinquedoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    categoria = StringField('Categoria', validators=[DataRequired()])
    submit = SubmitField('Adicionar Brinquedo')

class ProfessorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    submit = SubmitField('Adicionar Professor')

class EmprestimoForm(FlaskForm):
    nome_do_professor_ou_id = StringField('Nome do professor ou ID', validators=[DataRequired()])
    nome_do_brinquedo_ou_id = StringField('Nome do brinquedo ou ID', validators=[DataRequired()])
    submit = SubmitField('Realizar Empréstimo')
