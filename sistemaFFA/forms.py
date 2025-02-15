from django import forms
from django.core.exceptions import ValidationError
from .models import Contato, Categoria, Transacao, ContaBancaria
from usuarios.models import User, Empresa
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'contatoNome', 'categoriaNome', 'valor', 'tipoPagamento', 'data', 'pago']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('descricao', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('contatoNome', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('categoriaNome', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('valor', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('tipoPagamento', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('data', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('pago', css_class='col-12 form-label'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-success')
        )

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'tipo', 'cpf_cnpj', 'email', 'telefone', 'data']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('tipo', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('cpf_cnpj', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('data', css_class='col-12 form-label'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-success')
        )
    
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo', 'data']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('tipo', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('data', css_class='col-12 form-label'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-success')
        )

class ContaBancariaForm(forms.ModelForm):
    class Meta:
        model = ContaBancaria
        fields = ['nome', 'tipoConta', 'agenciaConta', 'banco', 'numeroConta', 'saldo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('tipoConta', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('agenciaConta', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('banco', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('numeroConta', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('saldo', css_class='col-12 form-label'),
                css_class='row'
            ),
            Submit('submit', 'Enviar', css_class='btn btn-success')
        )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'cpf', 'telefone', 'username', 'avatar']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='col-6 form-label'),
                Column('last_name', css_class='col-6 form-label'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='col-6 form-label'),
                Column('cpf', css_class='col-6 form-label'),
                css_class='row'
            ),
            Row(
                Column('telefone', css_class='col-6 form-label'),
                Column('username', css_class='col-6 form-label'),
                css_class='row'
            ),
            Row(
                Column('avatar', css_class='col-12 form-label'),
                css_class='row'
            ),
            Submit('submit', 'Editar', css_class='btn btn-success')
        )

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'endereco', 'numero', 'complemento', 'bairro', 'pais', 'estado', 'cidade', 'cep', 'cnpj']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('nome', css_class='col-12 form-label'),
                css_class='row'
            ),
            Row(
                Column('endereco', css_class='col-6 form-label'),
                Column('numero', css_class='col-2 form-label'),
                Column('complemento', css_class='col-4 form-label'),
                css_class='row'
            ),
            Row(
                Column('bairro', css_class='col-6 form-label'),
                Column('pais', css_class='col-6 form-label'),
                css_class='row'
            ),
            Row(
                Column('estado', css_class='col-6 form-label'),
                Column('cidade', css_class='col-6 form-label'),
                css_class='row'
            ),
            Row(
                Column('cep', css_class='col-6 form-label'),
                Column('cnpj', css_class='col-6 form-label'),
                css_class='row'
            ),
            Submit('submit', 'Cadastrar', css_class='btn btn-success')
        )