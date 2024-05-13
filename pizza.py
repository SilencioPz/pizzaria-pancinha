from flask import Flask, render_template, request, redirect, url_for

class Pizza:
    def __init__(self, nome, sabor, tamanho):
        self.nome = nome
        self.sabor = sabor
        self.tamanho = tamanho

pizza1 = Pizza('Margherita', 'Tomate e Mozzarella', 'Grande')
lista = [pizza1]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Listagem de Pizzas', pizzas=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Cadastro de Pizza')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    sabor = request.form['sabor']
    tamanho = request.form['tamanho']
    pizza = Pizza(nome, sabor, tamanho)
    lista.append(pizza)
    return redirect(url_for('index'))

app.run(debug=True)