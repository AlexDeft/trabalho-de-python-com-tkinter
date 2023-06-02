import tkinter as tk
import sqlite3
import tkinter.ttk as ttk
# Função para criar o banco de dados e tabela
def criar_banco_de_dados():
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE contatos
                 (nome TEXT, telefone INTEGER, data_nascimento DATE)''')
    cursor.execute("SELECT COUNT(*) FROM contatos")
    contador = cursor.fetchone()[0]

    if contador == 0:
        
        contatos = [
            ("Tadeu", 123456789, "01-01-1991"),
            ("João", 78955552, "20-01-1991"),
            ("Maria", 111111111, "10-05-1992"),
            ("Pedro", 123457896, "15-12-1988"),
            ("Alisson", 52486516, "03-01-1991"),
            ("Adryelson", 35465898, "19-05-1999"),
            ("Robson", 55555555, "19-12-1782"),
            ("João Pedro", 7777777, "05-09-2004"),
            ("João Lucas", 2222222, "19-01-2004"),
            ("Lucas", 34354355, "19-01-2003"),
             ("Maicon", 45842669, "11-09-1999"),
            ("Vitoria", 46888466, "01-01-1902"),
            ("Pamela", 484455455, "19-05-1000"),
            ("Camila", 7816128, "29-12-1959"),
            ("Amanda", 12359899, "30-10-2003"),
            ("David", 9001555, "04-07-1099"),
            ("Matheus", 0000000, "19-12-1970"),
            ("Yasmin", 123404560, "10-11-2004"),
            ("Rian", 12500419, "19-04-1904"),
            ("Rennan", 454006789, "27-08-1945"),
        ]
        cursor.executemany("INSERT INTO contatos VALUES (?, ?, ?)", contatos)

    conexao.commit()
    conexao.close()

# listar todos os contatos em ordem alfabética
def listar_contatos():
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()

    # contatos ordenados pelo nome
    cursor.execute("SELECT * FROM contatos ORDER BY nome")
    contatos = cursor.fetchall()


    resultado.delete(1.0, tk.END)
    for contato in contatos:
        resultado.insert(tk.END, f"Nome: {contato[0]}\nTelefone: {contato[1]}\nData de Nascimento: {contato[2]}\n\n")

    conexao.close()

#função para buscar um contato por telefone
def buscar_contato():
    telefone = buscar.get()
    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()

    #nome do contato correspondente ao numero de telefone
    cursor.execute("SELECT nome FROM contatos WHERE telefone=?", (telefone,))
    resultado_busca = cursor.fetchone()


    resultado.delete(1.0, tk.END)
    if resultado_busca is not None:
        resultado.insert(tk.END, f"Nome: {resultado_busca[0]}\n")
    else:
        resultado.insert(tk.END, "Contato não encontrado.")

    conexao.close()

#função para listar os aniversariantes do mês específico
def aniversariantes_mes():
    
    mes_atual = int(mes.get())

    conexao = sqlite3.connect('contatos.db')
    cursor = conexao.cursor()

    #recupera os contatos com data de nascimento no mês específico
    cursor.execute("SELECT nome, telefone, data_nascimento FROM contatos")
    contatos = cursor.fetchall()

    #filtra os contatos pelo mês de nascimento
    contatos_filtrados = []
    for contato in contatos:
        data_nascimento = contato[2]
        mes_nascimento = int(data_nascimento.split('-')[1])
        if mes_nascimento == mes_atual:
            contatos_filtrados.append(contato)

    #ordena os contatos pelo nome em ordem crescente
    contatos_filtrados = sorted(contatos_filtrados, key=lambda x: x[0])

    
    resultado.delete(1.0, tk.END)
    for contato in contatos_filtrados:
        resultado.insert(tk.END, f"Nome: {contato[0]}\nTelefone: {contato[1]}\nData de Nascimento: {contato[2]}\n\n")

    conexao.close()

# Cria a janela principal do Tkinter
janela = tk.Tk()
janela.title("Pesquisa de Contatos")
janela.geometry("1000x500")


buscar_label = ttk.Label(janela, text="Buscar por Telefone:")
buscar_label.pack()

buscar = ttk.Entry(janela)
buscar.pack()

buscar_button = ttk.Button(janela, text="Buscar", command=buscar_contato)
buscar_button.pack()

listar_button = ttk.Button(janela, text="Listar Contatos", command=listar_contatos)
listar_button.pack()

mes_label = ttk.Label(janela, text="Mês (1-12):")
mes_label.pack()

mes = ttk.Entry(janela)
mes.pack()

aniversariantes_button = ttk.Button(janela, text="Aniversariantes do Mês", command=aniversariantes_mes)
aniversariantes_button.pack()

resultado = tk.Text(janela)
resultado.pack()
criar_banco_de_dados()
janela.mainloop()
