# FFA .finance

## Sobre o Projeto

O **FFA .finance** é um gerenciador de finanças microempresariais, desenvolvido como parte do Projeto Integrador do curso de **Informática para Internet** no **IFRN**. Este sistema foi idealizado para ajudar microempresários a organizarem e controlarem suas finanças de forma prática e eficiente, permitindo que eles mantenham uma visão clara da saúde financeira de seus negócios.

## Funcionalidades

- Monitoramento de receitas e despesas.
- Controle centralizado de finanças.
- Interface amigável e responsiva.

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django
- **Outras Tecnologias**: AJAX para atualização dinâmica de telas

## Integrantes do Projeto

- **Ademacir Filho**
- **Francisco Cledson**
- **Francisco Guilherme**

## Configuração do Projeto

Siga as instruções abaixo para configurar o ambiente do projeto após clonar o repositório.

### 1. Clonando o Repositório

```bash
git clone <URL_DO_REPOSITORIO>  
cd ffa_finance  
```

### 2. Criando e Ativando o Ambiente Virtual

```bash
python -m venv venv  
venv\Scripts\Activate.ps1
```

### 3. Instalando as Dependências

```bash
pip install -r requirements.txt  
```

### 4. Aplicando as Migrações

```bash
python manage.py migrate  
```

### 5. Criando um Superusuário

```bash
python manage.py createsuperuser  
```

Siga as instruções e defina um nome de usuário, e-mail e senha.

### 6. Executando o Servidor

```bash
python manage.py runserver  
```

### 7. Acessando o Django Admin

Abra o navegador e acesse:

```
http://127.0.0.1:8000/admin/
```

Faça login com o superusuário criado anteriormente.

### 8. Adicionando Dados Iniciais no Admin

Após acessar o Django Admin, adicione os seguintes registros nas respectivas categorias:

#### Pagamentos

- Cartão
- À vista
- PIX
- Boleto

#### Tipo de Transação

- Todas
- Receita
- Despesa

#### Tipo de Contato

- Todos
- Associados
- Cliente
- Colaborador
- Fornecedor
- Sócio
- Outros

#### Tipo de Categoria

- Todas
- Fixas
- Variáveis
- Impostos
- Rendimentos

#### Tipo de Conta

- Corrente
- Poupança
- Salário

Agora o **FFA .finance** está pronto para ser utilizado!
