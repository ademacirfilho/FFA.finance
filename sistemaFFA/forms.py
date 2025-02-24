from django import forms
from .models import Contato, Categoria, Transacao, ContaBancaria
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'contatoNome', 'categoriaNome', 'tipo', 'valor', 'tipoPagamento', 'data', 'pago']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.data:
            self.initial['data'] = self.instance.data.strftime('%Y-%m-%d')
        
        self.fields['data'].widget = forms.DateInput(attrs={'type': 'date'})

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
                Column('tipo', css_class='col-12 form-label'),
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
        if self.instance.data:
            self.initial['data'] = self.instance.data.strftime('%Y-%m-%d')
        
        self.fields['data'].widget = forms.DateInput(attrs={'type': 'date'})
    
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
        if self.instance.data:
            self.initial['data'] = self.instance.data.strftime('%Y-%m-%d')
        
        self.fields['data'].widget = forms.DateInput(attrs={'type': 'date'})

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