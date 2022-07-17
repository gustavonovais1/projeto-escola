from cProfile import label
from cgi import test
from cgitb import text
from email import header
from logging import root
from tkinter import messagebox
from tkinter import *
from turtle import width
from unicodedata import name
import pymysql
from setuptools import Command
from tkinter import ttk
import matplotlib.pyplot as plt

class aluno():

    def alunoFrnt(self):
        
        self.aluno = Tk()
        self.aluno.title('Aluno')
        self.aluno.geometry('550x250')

        Label(self.aluno, text='Consulte suas notas').grid(row=0, column=0)

        self.consulta = Button(self.aluno,  bg='#00CED1', text='Consultar', command= self.consultaNota).grid(row=1, column=0, padx=5, pady=5)
        self.consulta = Button(self.consulta)

        Label(self.aluno, text='Veja seu desempenho\n vizualmente').grid(row=2, column=0)

        self.consulta = Button(self.aluno,  bg='#00CED1', text='Gráfico de notas', command= self.graficos).grid(row=3, column=0, padx=5, pady=5)
        self.consulta = Button(self.consulta)

        self.tree = ttk.Treeview(self.aluno, selectmode='browse', column=('coluna1', 'coluna2', 'coluna3', 'coluna4'), show='headings')

        self.tree.column('coluna1', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Prmeiro bimestre')

        self.tree.column('coluna2', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Segundo bimestre')

        self.tree.column('coluna3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Terceiro bimestre')

        self.tree.column('coluna4', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Quarto bimestre')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.aluno.mainloop()

    def consultaNota(self):
        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select  nota1, nota2, nota3, nota4 from aluno where id = %s', (id1))
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []

        for linha in resultados:
            linhav.append(linha['nota1'])
            linhav.append(linha['nota2'])
            linhav.append(linha['nota3'])
            linhav.append(linha['nota4'])

            self.tree.insert('', END ,values=linhav, tag='1')

            linhav.clear()

    def graficos(self):

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select nome, nota1, nota2, nota3, nota4 from aluno where id = %s', (id1))
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        linhav = []

        for linha in resultados:
            linhav.append(linha['nota1'])
            linhav.append(linha['nota2'])
            linhav.append(linha['nota3'])
            linhav.append(linha['nota4'])
            
        x = linhav


        plt.plot(x, label= nome)
        plt.ylabel('Notas')
        plt.xlabel('período')
        plt.title('Relação de desempenho da notas durante o ano')
        plt.legend()

        plt.show()

        linhav.clear()

class professor():

    def professorFrnt(self):
        
        self.professor = Tk()
        self.professor.title('Professor')
        self.professor.geometry('570x300')
        Label(self.professor, text='Lançar as notas no sistema').grid(row=0, column=0)

        Label(self.professor, text='Cadastrar nota 1').grid(row=1, column=0)
        self.nota1 = Entry(self.professor)
        self.nota1.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.professor, text='Cadastrar nota 2').grid(row=2, column=0)
        self.nota2 = Entry(self.professor)
        self.nota2.grid(row=2, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.professor, text='Cadastrar nota 3').grid(row=3, column=0)
        self.nota3 = Entry(self.professor)
        self.nota3.grid(row=3, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.professor, text='Cadastrar nota 4').grid(row=4, column=0)
        self.nota4 = Entry(self.professor)
        self.nota4.grid(row=4, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.professor, text='Digite o id do aluno').grid(row=5, column=0)
        self.id = Entry(self.professor)
        self.id.grid(row=5, column=1, columnspan=2, padx=5 ,  pady=5)

        self.lancar = Button(self.professor,width=10, bg='#FFD700', text='Lançar', command=self.professorBack).grid(row=6, column=1, padx=5, pady=5, columnspan=2)
        self.lancar = Button(self.lancar)

        self.tree = ttk.Treeview(self.professor, selectmode='browse', column=('coluna1', 'coluna2', 'coluna3'), show='headings')

        self.tree.column('coluna1', width=70, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Id do aluno')

        self.tree.column('coluna2', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Nome do aluno')

        self.tree.column('coluna3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Senha do aluno')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.updateBackAnd()    

        self.professor.mainloop()

    def professorBack(self):
        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')

        nota1 = float(self.nota1.get())
        nota2 = float(self.nota2.get())
        nota3 = float(self.nota3.get())
        nota4 = float(self.nota4.get())
        id = int(self.id.get())

        try:
            with conexao.cursor() as cursor:
                cursor.execute('''UPDATE aluno SET nota1 = %s, nota2 = %s, nota3 = %s, nota4 = %s where id = %s''', (nota1 , nota2, nota3, nota4, id))
                messagebox.showinfo('Success', message=f"Notas lançadas com sucesso")
                conexao.commit()
        except:
            print('Não foi possivel fazer o insert no bd')

    def updateBackAnd(self):

        try: 
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select * from aluno')
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []

        for linha in resultados:
            linhav.append(linha['id'])
            linhav.append(linha['nome'])
            linhav.append(linha['senha'])

            self.tree.insert('', END ,values=linhav, iid=linha['id'],  tag='1')

            linhav.clear()

class Altenticacao(aluno, professor):
    
    def __init__(self):
        self.root = Tk()
        self.root.title('teste')
        self.root.geometry('370x230')

        Label(self.root, text='Faça seu cadstro').grid(row=0, column=0, columnspan=3)

        Label(self.root, text='Digite um nome de usuario').grid(row=1, column=0)
        self.nome = Entry(self.root)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.root, text='Digite uma senha').grid(row=2, column=0)
        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Label(self.root, text='Digite 1 para professor ou 2 para aluno').grid(row=3, column=0, padx=5, pady=5)
        self.nivel = Entry(self.root) 
        self.nivel.grid(row=3, column=1, padx=5, pady=5)

        self.cadastrar = Button(self.root,  bg='#32CD32', text='Cadastrar',command=self.cadastroBack).grid(row=4, column=0, padx=5, pady=5, columnspan=3)
        self.cadastrar = Button(self.cadastrar)

        self.logarAluno = Button(self.root,  bg='#00CED1', text='Logar como aluno', command=self.logarAlunoFront).grid(row=5, column=0, padx=5, pady=5, columnspan=2)
        self.logarAluno = Button(self.logarAluno)

        self.logarProfessor = Button(self.root, bg='#FFD700', text='Logar como professor', command=self.logarProfessorFront).grid(row=6, column=0, padx=5, pady=5, columnspan=2)
        self.logarProfessor = Button(self.logarProfessor)

        self.root.mainloop()

    def cadastroBack(self):   

        nome = self.nome.get()
        senha = self.senha.get()
        nivel = int(self.nivel.get())

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')
        

        try:
            with conexao.cursor() as cursor:
                if nivel == 1:
                    cursor.execute('''insert into professor (nome, senha, nivel) values (%s, %s, %s)''', (nome , senha, nivel))
                    messagebox.showinfo('Success', message=f"Professor {nome} cadastrado")
                elif nivel == 2:
                    cursor.execute('''insert into aluno (nome, senha, nivel) values (%s, %s, %s)''', (nome , senha, nivel))
                    messagebox.showinfo('Success', message=f"Aluno {nome} cadastrado")
                else:
                    messagebox.ERROR('ERROR', message="Numero tem que ser 1 ou 2")
                conexao.commit()
        
        except:
            print('Não foi possivel fazer o insert no bd')

    def logarProfessorFront(self):
        self.root.destroy()
        self.login = Tk()
        self.login.title('teste')
        self.login.geometry('350x130')

        Label(self.login, text='Faça login').grid(row=0, column=0, columnspan=3)

        Label(self.login, text='Digite seu nome de usuario').grid(row=1, column=0)
        self.nome = Entry(self.login)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.login, text='Digite sua senha').grid(row=2, column=0)
        self.senha = Entry(self.login, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        self.logar = Button(self.login, width=10, bg='#FFD700', text='Logar', command=self.logarProfessorBack).grid(row=3, column=1, padx=5, pady=5)
        self.logar = Button(self.logar)

        self.login.mainloop()

    def logarProfessorBack(self):

        autenticado = False

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')

        nome = self.nome.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from professor')
                resultado  = cursor.fetchall()
        except:
            print('Não foi possível fazer a consulta')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                autenticado = True
                break
            else:
                autenticado = False
        
        if autenticado == False:
            messagebox.showinfo('Aviso', 'Usuário ou senha inválidos')
        else:
            self.login.destroy()
            self.professorFrnt()

    def logarAlunoFront(self):
        self.root.destroy()
        self.login = Tk()
        self.login.title('teste')
        self.login.geometry('350x210')

        Label(self.login, text='Faça login').grid(row=0, column=0, columnspan=3)

        Label(self.login, text='Digite seu nome de usuario').grid(row=1, column=0)
        self.nome = Entry(self.login)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.login, text='Digite sua senha').grid(row=2, column=0)
        self.senha = Entry(self.login,  show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)

        Label(self.login, text='Informe seu id de aluno').grid(row=3, column=0)
        self.id = Entry(self.login)
        self.id.grid(row=3, column=1, padx=5, pady=5)

        self.logar = Button(self.login, width=10, bg='#00CED1', text='Logar', command=self.logarAlunoBack).grid(row=4, column=1, padx=5, pady=5)
        self.logar = Button(self.logar)

        Label(self.login, text='Não sabe seu id?').grid(row=5, column=0)

        self.consultaID = Button(self.login,  bg='#00CED1', text='Visualize seu id ', command=self.consultaID_Front).grid(row=6, column=0, padx=5, pady=5)
        self.consultaID = Button(self.consultaID) 

        self.logar.destroy() 

        self.login.mainloop()

    def consultaID_Front(self):
        self.id = Tk()
        self.id.title('teste')
        self.id.geometry('400x250')

        Label(self.id, text='Verifique seu id').grid(row=0, column=0)

        Label(self.id, text='Digite seu nome de usuario').grid(row=1, column=0)
        self.nomeid = Entry(self.id)
        self.nomeid.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.id, text='Digite sua senha').grid(row=2, column=0)
        self.senhaid = Entry(self.id, show='*')
        self.senhaid.grid(row=2, column=1, padx=5, pady=5)

        self.verificaId = Button(self.id,  bg='#00CED1', text='Visualize seu id ', command=self.consultaID_Back).grid(row=3, column=1, padx=5, pady=5)
        self.verificaId = Button(self.verificaId) 

        self.tree = ttk.Treeview(self.id, selectmode='browse', column=('coluna1'), show='headings')

        self.tree.column('coluna1', width=70, minwidth=1, stretch=NO)
        self.tree.heading('#1', text='Id do aluno')

        self.tree.grid(row=0, column=3, padx=10, pady=10, columnspan=3, rowspan=6)

        self.id.mainloop()

    def consultaID_Back(self):
        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')

        nome = self.nomeid.get()
        senha = self.senhaid.get()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from aluno')
                resultado  = cursor.fetchall()
        except:
            print('Não foi possível fazer a consulta')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                x = nome

                try:
                    with conexao.cursor() as cursor:
                        cursor.execute("select id from aluno where nome = %s", (x))
                        resultado2  = cursor.fetchall()
                except:
                    print('Não foi possível fazer a consulta')

                self.tree.delete(*self.tree.get_children())
                
                linhav = []
                
                for linha in resultado2:
                    linhav.append(linha['id'])


                self.tree.insert('', END ,values=linhav, iid=linha['id'],  tag='1')


                linhav.clear()

    def logarAlunoBack(self):

        autenticado = False

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='escola',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Não foi possivel conectar-se ao banco de dados')

        global nome
        nome = self.nome.get()
        senha = self.senha.get()
        global id1
        id1 = int(self.id.get())

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from aluno')
                resultado  = cursor.fetchall()
        except:
            print('Não foi possível fazer a consulta')

        for linha in resultado:
            if id1 == linha['id'] and nome == linha['nome'] and senha == linha['senha']:
                autenticado = True
                break
            else:
                autenticado = False
        
        if autenticado == False:
            messagebox.showinfo('Aviso', 'Usuário ou senha inválidos')
        else:
            self.alunoFrnt()
        self.login.destroy()

Altenticacao()