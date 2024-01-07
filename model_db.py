import sqlite3

class ModelBanco:
    # ----------------------  CRIA BANCO ---------------------------------------
    
    def __init__(self):
        self.conn = sqlite3.connect("academia.db")
        self.criar_tabelas()

    def __del__(self):
        self.conn.close()
        
    # ----------------------  CRIA TABELAS ---------------------------------------
    def criar_tabelas(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS tb_aluno (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                matricula INTEGER NOT NULL UNIQUE,
                nome TEXT,
                tipo_documento TEXT,
                num_documento VARCHAR(10) NOT NULL UNIQUE,
                telefone VARCHAR(12),
                genero VARCHAR(1),
                status TEXT,
                dt_cadastro DATE,
                dt_nascimento DATE,
                FOREIGN KEY(matricula) REFERENCES tb_usuario(id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tb_usuario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                matricula INTEGER NOT NULL UNIQUE,
                usuario VARCHAR(15),
                senha VARCHAR(10),
                nome VARCHAR(15),
                email VARCHAR(15),
                tipo_documento TEXT,
                num_documento VARCHAR(10) UNIQUE,
                status TEXT,
                dt_nascimento DATE,
                dt_cadastro DATE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tb_funcionario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                tipo_documento TEXT,
                num_documento VARCHAR(10) UNIQUE,
                telefone VARCHAR(12),
                email VARCHAR(15),
                dt_nascimento DATE,
                genero VARCHAR(1),
                matricula INTEGER,
                status TEXT,
                dt_contratacao DATE,
                dt_desligamento DATE,
                cargo_id INTEGER,
                dt_cadastro DATE,
                FOREIGN KEY(cargo_id) REFERENCES tb_cargo(id),
                FOREIGN KEY(matricula) REFERENCES tb_usuario(matricula)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tb_cargo (
                id INTEGER NOT NULL PRIMARY KEY,
                codigo INTEGER NOT NULL UNIQUE,
                nome TEXT,
                setor TEXT,
                salario_base FLOAT,
                dt_cadastro DATE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tb_plano (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                codigo INTEGER NOT NULL UNIQUE,
                descricao TEXT NOT NULL,
                nivel TEXT NOT NULL,
                valor FLOAT,
                status TEXT,
                dt_cadastro DATE,
                FOREIGN KEY(codigo) REFERENCES tb_aluno(matricula)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS tb_endereco (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                matricula INTEGER,
                nome TEXT,
                rua TEXT,
                numero VARCHAR(10),
                complemento TEXT,
                cep VARCHAR(8),
                bairro TEXT,
                cidade TEXT,
                estado TEXT,
                FOREIGN KEY(matricula) REFERENCES tb_aluno(matricula),
                FOREIGN KEY(matricula) REFERENCES tb_funcionario(matricula)
            );
            """
        ]

        with self.conn:
            for query in queries:
                self.conn.execute(query)

        print("Banco de dados criado com sucesso!")
        print("Tabelas Aluno, Usuario, Funcionario, Cargo, Plano, Endereço criadas!")