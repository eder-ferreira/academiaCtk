import sqlite3
from tkinter import messagebox, ttk
from model_formata import Formata

import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
from customtkinter import CTkImage
from tkinter import messagebox
from model_formata import Formata

janela = ctk.CTk()


class Aplicacao:
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.tela_login()
        janela.mainloop()

    def tema(self):
        # ctk.set_appearance_mode("dark")
        # ctk.set_default_color_theme("dark-blue")
        
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    def tela(self):
        janela.geometry("700x450")
        janela.title("Sistema de Academia")
        janela.iconbitmap("img/gym2.ico")
        janela.resizable(False, False)
        
    def tela_login(self):
        # Imagens
        img = PhotoImage(file="img/logo1.png")
        label_img = ctk.CTkLabel(master=janela, image=img)
        label_img.place(x=10, y=90)


        label_titulo = ctk.CTkLabel(master=janela,text="Seja bem vindo ao sistema da \n Academia Marombinha",font=("Roboto", 25),text_color="#00B0F0")
        label_titulo.place(x=25, y=10)

        # Frame do login
        login_frame = ctk.CTkFrame(master=janela, width=340, height=400)
        login_frame.pack(side=RIGHT)
    
        # Frame logo menu
        label = ctk.CTkLabel(master=login_frame, text=f"Sistema de Login", font=("Roboto",30))
        label.place(x=25, y=15)
        
        # Insere data
        date = Formata.obter_data_formatada(self)
        data = ctk.CTkLabel(master=login_frame, text=f"Data: {date}", font=("Roboto",12))
        data.place(x=25, y=70)
        
        # Frame Usuario e Senha
        usuario_entry = ctk.CTkEntry(master=login_frame,placeholder_text="Digite o usuario",width=300,font=("Roboto", 14))
        usuario_entry.place(x=25, y=105)

        usuario_label = ctk.CTkLabel(master=login_frame,text="O campo usuario é de preenchimento obrigatório",text_color="#238E23",font=("Roboto", 10))
        usuario_label.place(x=25, y=135)

        senha_entry = ctk.CTkEntry(master=login_frame,placeholder_text="Digite a senha",width=300,font=("Roboto", 14),show="*")
        senha_entry.place(x=25, y=175)

        senha_label = ctk.CTkLabel(master=login_frame,text="O campo senha é de preenchimento obrigatório",text_color="#238E23",font=("Roboto", 10))
        senha_label.place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembre-me")
        checkbox.place(x=25, y=230)

        def logar():
            msg = messagebox.showinfo(title="Estado do Login", message="Usuário Logado com sucesso!")
                
        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=logar)
        login_button.place(x=25, y=280)

        cadastrar_span = ctk.CTkLabel(master=login_frame, text="Novo Usuário ?", text_color="#238E23")
        cadastrar_span.place(x=25, y=330)

        def tela_cadastro():
            # Remove a tela de login
            login_frame.pack_forget()
            
            # Cria a tela de cadastro
            cadastra_frame = ctk.CTkFrame(master=janela, width=340, height=450)
            cadastra_frame.pack(side=RIGHT)
            
            label = ctk.CTkLabel(master=cadastra_frame, text="Cadastrar Usuário", font=("Roboto",30))
            label.place(x=25, y=15)
            
            label_span = ctk.CTkLabel(master=cadastra_frame, text="Todos os campos são de preenchimento obrigatório", text_color="#238E23", font=("Roboto", 10))
            label_span.place(x=25, y=55)
            
            usuario_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Digite um usuario",width=300,font=("Roboto", 14))
            usuario_entry.place(x=25, y=85)
            
            email_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Digite uma senha",width=300,font=("Roboto", 14), show="*")
            email_entry.place(x=25, y=125)
            
            nome_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Digite o nome completo",width=300,font=("Roboto", 14))
            nome_entry.place(x=25, y=165)
            
            senha_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Digite um e-mail",width=300,font=("Roboto", 14))
            senha_entry.place(x=25, y=205)
            
            # tdocumento_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Tipo do doc RG-CPF-Passaporte-Outros",width=300,font=("Roboto", 14))
            # tdocumento_entry.place(x=25, y=245)
            
            opcoes_tdocumento = ["RG", "CPF", "Passaporte", "Outros"]
            tdocumento_entry = ttk.Combobox(master=cadastra_frame, values=opcoes_tdocumento, font=("Roboto", 14))
            tdocumento_entry.place(x=25, y=245)
            
            ndocumento_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Digite o numero do documento",width=300,font=("Roboto", 14))
            ndocumento_entry.place(x=25, y=285)
            
            dtaniversario_entry = ctk.CTkEntry(master=cadastra_frame,placeholder_text="Digite a data de nascimento dd/mm/aaaa",width=300,font=("Roboto", 14))
            dtaniversario_entry.place(x=25, y=325)


            checkbox = ctk.CTkCheckBox(master=cadastra_frame, text="Aceitar termos e politicas")
            checkbox.place(x=25, y=365)
            
            def voltar():
                # Remove a tela de cadastrar
                cadastra_frame.pack_forget()
                
                # Devolve a tela de login
                login_frame.pack(side=RIGHT)
                
            voltar_button = ctk.CTkButton(master=cadastra_frame, text="Voltar", width=145, fg_color="gray",hover_color="#333333", command=voltar)
            voltar_button.place(x=25, y=400)
            
            def salvar():
                # Verifica se os campos obrigatórios estão preenchidos
                if not usuario_entry.get() or not senha_entry.get() or not nome_entry.get() or not email_entry.get():
                    messagebox.showerror("Erro de Cadastro", "Todos os campos obrigatórios devem ser preenchidos.")
                    return
                
                formata_instance = Formata()
                try:
                    conn = sqlite3.connect("academia.db")
                    with conn:
                        c = conn.cursor()
                        
                        matricula = Formata.gerar_matricula()
                        status = "ativo"
                        dt_cadastro = formata_instance.obter_data_formatada()

                        c.execute("INSERT INTO tb_usuario VALUES (null,?,?,?,?,?,?,?,?,?,?)",
                                (matricula, usuario_entry.get(), senha_entry.get(), nome_entry.get(),
                                email_entry.get(), tdocumento_entry.get(), ndocumento_entry.get(),
                                status, dtaniversario_entry.get(), dt_cadastro))
                    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
                    
                    # Limpa os campos após salvar no banco
                    usuario_entry.delete(0, END)
                    senha_entry.delete(0, END)
                    nome_entry.delete(0, END)
                    email_entry.delete(0, END)
                    tdocumento_entry.delete(0, END)
                    ndocumento_entry.delete(0, END)
                    dtaniversario_entry.delete(0, END)

                except Exception as e:
                    messagebox.showerror("Erro de Cadastro", f"Erro ao cadastrar usuário: {str(e)}")

            cadastra_button = ctk.CTkButton(master=cadastra_frame, text="Cadastrar", width=145,fg_color="#238E23", hover_color="#014B05", command=salvar)
            cadastra_button.place(x=180, y=400)
            
        cadastrar_button = ctk.CTkButton(master=login_frame,text="Cadastre-se",width=200,fg_color="green",hover_color="#238E23", command=tela_cadastro)
        cadastrar_button.place(x=124, y=330)


# Crie uma instância da classe Aplicacao
app = Aplicacao()