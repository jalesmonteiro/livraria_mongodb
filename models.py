from pymongo import MongoClient
from bson.objectid import ObjectId
import os

# Configuração da conexão com o MongoDB Atlas
MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client.livraria  # nome do banco de dados

# Coleções
livros = db.livros
usuarios = db.usuarios
pedidos = db.pedidos

class Livro:
    def __init__(self, titulo, preco, categoria, tags, autores, mais_recente_edicao, numero_autores, data_publicacao, editora, descricao, isbn, estoque, imagem_capa):
        self.titulo = titulo
        self.preco = preco
        self.categoria = categoria
        self.tags = tags
        self.autores = autores
        self.mais_recente_edicao = mais_recente_edicao
        self.numero_autores = numero_autores
        self.data_publicacao = data_publicacao
        self.editora = editora
        self.descricao = descricao
        self.isbn = isbn
        self.estoque = estoque
        self.imagem_capa = imagem_capa

    def salvar(self):
        # Todo
        pass

    @staticmethod
    def buscar_por_id(id_livro):
        # Todo
        pass

    @staticmethod
    def buscar_todos():
        # Todo
        pass
    
    @staticmethod
    def buscar_livros(filtros=None, pagina=1, por_pagina=12):
        # Todo
        pass

    @staticmethod
    def buscar_por_id(id_livro):
        # Todo
        pass

    @staticmethod
    def categorias_disponiveis():
        # Todo
        pass

    @staticmethod
    def tags_disponiveis():
        # Todo
        pass

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha  # Importante: criptografar antes de salvar!

    def salvar(self):
        # Todo
        pass

    @staticmethod
    def buscar_por_email(email):
        # Todo
        pass

    @staticmethod
    def buscar_por_id(id_usuario):
        # Todo
        pass

class Pedido:
    def __init__(self, id_usuario, livros, data, total, status="pendente"):
        self.id_usuario = id_usuario
        self.livros = livros  # lista de dicionários com id_livro, quantidade, preco
        self.data = data      # data do pedido (ex: datetime.now())
        self.total = total
        self.status = status

    def salvar(self):
        # Todo
        pass

    @staticmethod
    def buscar_por_usuario(id_usuario):
        # Todo
        pass

    @staticmethod
    def buscar_por_id(id_pedido):
        # Todo
        pass
