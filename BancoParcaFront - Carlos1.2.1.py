import tkinter as tk
from tkinter import messagebox
#from BancoParcaBack import BancoDB  
from tkinter import *
from PIL import Image, ImageTk

# contas criadas
# ('Cliente', 'paulo', 'paulo'),
# ('Cliente', 'rafaela', 'rafaela'),
# ('Cliente', 'carlos', 'carlos'),
# ('Cliente', 'gabriel', 'gabriel'),
# ('Cliente', 'davi', 'davi')
# ('Gerente Geral', 'admpaulo', 'paulo'),
# ('Gerente Geral', 'admrafaela', 'rafaela'),
# ('Gerente Geral', 'admcarlos', 'carlos'),
# ('Gerente Geral', 'admgabriel', 'gabriel'),
# ('Gerente Geral', 'admdavi', 'davi')



class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bem Vindo ao Banco Parça")
        self.root.geometry("1920x1080")
        #self.root.attributes('-fullscreen',True)
        self.root.resizable(False, False)
        #self.db = BancoDB()
        self.root.configure(bg='#FFFAFA')
        self.carregar_imagens()


        
        self.create_login_widgets()

    
    def carregar_imagens(self):
    #imagem usuário cinza 
     imagem_usuario = Image.open(r"TRABALHO OUTUBRO\do-utilizador.png")
     imagem_redimensionada = imagem_usuario.resize((134, 122), Image.Resampling.LANCZOS)
     self.img1 = ImageTk.PhotoImage(imagem_redimensionada)
    #logo banco invertida
     imagem_logo = Image.open(r"TRABALHO OUTUBRO\logo banco invert.png")
     imagem_redimensionada_logo = imagem_logo.resize((462, 462), Image.Resampling.LANCZOS)
     self.img2 = ImageTk.PhotoImage(imagem_redimensionada_logo)
    


    def create_login_widgets(self):
        
        frame1 = tk.Frame(self.root, bg='#FFFAFA')
        frame1.place(relx=0.03, rely=0.5, anchor='w')
        
        self.label_bemvindo = tk.Label(text="Faça seu login", font=('SourceSansPro-Bold 40 bold'), bg ="#FFFAFA", fg = "#4270A8")
        self.label_bemvindo.place(x=150 ,y=70)

        self.label_titular_login = tk.Label(frame1, text="CPF:",font=('SourceSansPro-Bold 24 bold'),  bg='#FFFAFA')
        self.label_titular_login.place(x=0 ,y=0)
        self.entry_titular_login = tk.Entry(frame1, font=('SourceSansPro-Bold 20 bold'),bg='#c6d1e1',fg ='#000000', width=30)
        self.entry_titular_login.place(x=0,y=20)

        self.label_senha_login = tk.Label(frame1, text="Senha:",bg='#FFFAFA',font=('SourceSansPro-Bold 24 bold'))
        self.label_senha_login.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_senha_login = tk.Entry(frame1, show="*",font=('SourceSansPro-Bold 20 bold'))
        self.entry_senha_login.grid(row=1, column=1, padx=10, pady=5)

        self.button_login = tk.Button(text="Login", command=self.login, font=('SourceSansPro-Bold 20 bold'), bg='#4270A8', fg='#FFFAFA' )
        self.button_login.place(x=250 , y=800)
        
        self.framelogin = Frame(self.root, bd=4, bg='#4270A8', highlightbackground='#4270A8', highlightthickness=3)
        self.framelogin.place(relx=0.35, rely=0, relwidth=1, relheight=1)

        self.label_cadastro = tk.Label(text ="Não tem cadastro ainda? Clique aqui!",font=('SourceSansPro-Bold 14 bold') )
        self.label_cadastro.place(x=300 , y=200)
        #textos da logo
        self.label_textologo1 = tk.Label(text="BancoParça", font=('SourceSansPro-Bold 64 bold'), bg ="#4270A8", fg = "#FFFAFA")
        self.label_textologo1.place(x=1070 ,y=70)

        self.label_textologo1 = tk.Label(text='''Ajudando pessoas com \n um banco online!''', font=('SourceSansPro 36'), bg ="#4270A8", fg = "#FFFAFA")
        self.label_textologo1.place(x=1050 ,y=800)

        #somente imagens
        self.label_imagem = tk.Label(self.root, image=self.img1, bg='#FFFAFA' )
        self.label_imagem.place(relx=0.12, rely=0.2, anchor='nw')
        
        self.label_imagem2 = tk.Label(self.root, image=self.img2, bg='#4270A8' )
        self.label_imagem2.place(relx=0.675, rely=0.45, anchor='center')


    def login(self):
        titular = self.entry_titular_login.get()
        senha = self.entry_senha_login.get()
        perfil = self.db.autenticar_usuario(titular, senha)
        if perfil:
            messagebox.showinfo("Sucesso", f"Usuário autenticado como: {perfil}")
            self.create_main_widgets(perfil)
        else:
            messagebox.showerror("Erro", "Falha na autenticação.")

    def create_main_widgets(self, perfil):
        
        for widget in self.root.winfo_children():
            widget.destroy()

        
        if perfil == 'Cliente':
            self.create_cliente_widgets()
        elif perfil == 'Gerente Geral':
            self.create_gerente_widgets()
        elif perfil == 'Chefe de Setor':
            self.create_chefe_widgets()
        elif perfil == 'Funcionário':
            self.create_funcionario_widgets()

    def create_cliente_widgets(self):
        
        self.label_titular = tk.Label(self.root, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.root)
        self.entry_titular.grid(row=0, column=1)

        self.label_valor = tk.Label(self.root, text="Valor:")
        self.label_valor.grid(row=1, column=0)
        self.entry_valor = tk.Entry(self.root)
        self.entry_valor.grid(row=1, column=1)

        self.label_titular_destino = tk.Label(self.root, text="Titular Destino:")
        self.label_titular_destino.grid(row=2, column=0)
        self.entry_titular_destino = tk.Entry(self.root)
        self.entry_titular_destino.grid(row=2, column=1)

        self.button_deposito = tk.Button(self.root, text="Depositar", command=self.depositar)
        self.button_deposito.grid(row=3, column=0)

        self.button_saque = tk.Button(self.root, text="Sacar", command=self.sacar)
        self.button_saque.grid(row=3, column=1)

        self.button_transferir = tk.Button(self.root, text="Transferir", command=self.transferir)
        self.button_transferir.grid(row=4, column=0, columnspan=2)

        self.button_consultar_saldo = tk.Button(self.root, text="Consultar Saldo", command=self.consultar_saldo)
        self.button_consultar_saldo.grid(row=5, column=0, columnspan=2)

    def create_gerente_widgets(self):
        
        self.label_titular = tk.Label(self.root, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.root)
        self.entry_titular.grid(row=0, column=1)

        self.button_criar_conta = tk.Button(self.root, text="Criar Conta", command=self.criar_conta)
        self.button_criar_conta.grid(row=1, column=0, columnspan=2)

        self.button_listar_contas = tk.Button(self.root, text="Listar Contas", command=self.listar_contas)
        self.button_listar_contas.grid(row=2, column=0, columnspan=2)

    def create_chefe_widgets(self):
        
        self.label_titular = tk.Label(self.root, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.root)
        self.entry_titular.grid(row=0, column=1)

        self.button_criar_funcionario = tk.Button(self.root, text="Criar Funcionário", command=self.criar_funcionario)
        self.button_criar_funcionario.grid(row=1, column=0, columnspan=2)

    def create_funcionario_widgets(self):
        
        self.label_titular = tk.Label(self.root, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.root)
        self.entry_titular.grid(row=0, column=1)

        self.button_autorizar_movimentacao = tk.Button(self.root, text="Autorizar Movimentação", command=self.autorizar_movimentacao)
        self.button_autorizar_movimentacao.grid(row=1, column=0, columnspan=2)

    
    def depositar(self):
        titular = self.entry_titular.get()
        valor = float(self.entry_valor.get())
        if self.db.depositar(titular, valor):
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao realizar depósito.")

    def sacar(self):
        titular = self.entry_titular.get()
        valor = float(self.entry_valor.get())
        if self.db.sacar(titular, valor):
            messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao realizar saque ou saldo insuficiente.")

    def transferir(self):
        titular_origem = self.entry_titular.get()
        titular_destino = self.entry_titular_destino.get()
        valor = float(self.entry_valor.get())
        if self.db.transferir(titular_origem, titular_destino, valor):
            messagebox.showinfo("Sucesso", "Transferência realizada com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao realizar transferência.")

    def consultar_saldo(self):
        titular = self.entry_titular.get()
        saldo = self.db.consultar_saldo(titular)
        if saldo is not None:
            messagebox.showinfo("Saldo", f"O saldo da conta é: R${saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Falha ao consultar saldo.")

    def criar_conta(self):
        titular = self.entry_titular.get()
        if self.db.criar_conta(titular):
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao criar conta.")

    def listar_contas(self):
        contas = self.db.listar_contas()
        contas_str = "\n".join([f"Titular: {c[1]}, Saldo: R${c[2]:.2f}" for c in contas])
        messagebox.showinfo("Contas", contas_str)

    def criar_funcionario(self):
        
        pass

    def autorizar_movimentacao(self):
        
        pass


root = tk.Tk()
app = BancoApp(root)
root.mainloop()
