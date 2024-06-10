import sqlite3 as sql
from colorama import Fore, Style, init
import time
from tabulate import tabulate

# Inicializa o colorama
init(autoreset=True)

def color_text(text, color):
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE
    }
    
    # Pega a cor desejada do dicionário ou usa branco se a cor não for válida
    chosen_color = colors.get(color.lower(), Fore.WHITE)
    
    # Imprime o texto com a cor escolhida
    print(f"{chosen_color}{text}{Style.RESET_ALL}")

def logo():
    color_text("""
░██████╗░█████╗░██╗░░██╗░█████╗░░█████╗░██╗░░░░░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░░░░░░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
╚█████╗░██║░░╚═╝███████║██║░░██║██║░░██║██║░░░░░█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
░╚═══██╗██║░░██╗██╔══██║██║░░██║██║░░██║██║░░░░░╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
██████╔╝╚█████╔╝██║░░██║╚█████╔╝╚█████╔╝███████╗░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░░╚██╗
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝

Contato para erros e sugestões [+55 21-99885-7949]""", "blue")

def MENU():
    color_text("[01] Adicionar alunos;", 'green')
    color_text("[02] Dar uma(1) advertência ao aluno;", "red")
    color_text("[03] Remover uma(1) advertência do aluno;", 'blue')
    color_text("[04] Adicionar nota ao aluno;", 'yellow')
    color_text("[05] Ver lista com todos os alunos;", "white")
    color_text("[06] Ver um aluno em específico", "blue")
    color_text("[07] Remover um aluno", "red")
    color_text('[00] sair', 'cyan')
    o = input("escolha a opção: ")
    if o == '01' or o == '1':
        add()
    elif o == '02' or o == '2':
        adv()
    elif o == '03' or o == '3':
        Radv()
    elif o == '04' or o == '4':
        nta()
    elif o == '05' or o == '5':
        ver()
    elif o == '06' or o == '6':
        ver_Es()
    elif o == '07' or o == '7':
        dele()
    elif o == '00' or o == '0':
        quit()

def add():
    connect = sql.connect('data.db')
    cursor = connect.cursor()
    id_aluno = input("Digite o ID do aluno: ")
    nm = input("Digite o nome do aluno a ser matriculado: ")
    ns = input("Digite a data de nascimento do aluno (YYYY-MM-DD): ")
    hi = input("De que escola ele veio? ")
    nt = input("Qual a nota dele? ")
    ad = input("Quantas advertências ele tem? ")
    tr = input("Qual o turno? ")
    sx = input("Qual o sexo? ")
    tu = input("Qual a turma? ")

    try:
        cursor.execute('''
        INSERT INTO alunos (id, nome, nascimento, escola_de_origem, nota, advertencia, turno, sexo, turma)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_aluno, nm, ns, hi, nt, ad, tr, sx, tu))
        
        connect.commit()
        print(Fore.YELLOW + f"Aluno {nm} foi matriculado com sucesso!")
    except sql.Error as e:
        print(Fore.RED + f"Erro ao matricular aluno: {e}")
    finally:
        connect.close()
        time.sleep(3)
        logo()
        MENU()

def adv():
    def add(advertencias_id):
        connect = sql.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''
        UPDATE alunos
        SET advertencia = advertencia + 1
        WHERE id = ?
        ''', (advertencias_id,))
        connect.commit()
        connect.close()
    num = input("Qual o numero do aluno que irá levar advertência? ")
    add(num)
    color_text(f"Advertência adicionada ao aluno com ID {num}.", "yellow")
    time.sleep(2)
    logo()
    MENU()

def Radv():
    def unadd(advertencias_id):
        connect = sql.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''
        UPDATE alunos
        SET advertencia = advertencia - 1
        WHERE id = ?
        ''', (advertencias_id,))
        connect.commit()
        connect.close()
    
    num = input("Qual o numero do aluno que irá perder uma advertência? ")
    unadd(num)
    color_text(f"Advertência removida do aluno com ID {num}.", "yellow")
    time.sleep(3)
    logo()
    MENU()

def nta():
    def update_nota(aluno_ID, nova_Nota):
        connect = sql.connect("data.db")
        cursor = connect.cursor()
        cursor.execute('''
            UPDATE alunos
            SET nota = ?
            WHERE id = ?
        ''',        (nova_Nota, aluno_ID))
        connect.commit()
        connect.close()
        color_text(f"A nota do aluno com número {aluno_ID} foi atualizada para {nova_Nota}.", "yellow")
    
    v = input("Qual o número do aluno? ")
    n = input("Qual a nova nota do aluno? ")
    update_nota(v, n)
    time.sleep(3)
    logo()
    MENU()


def quit():
    color_text("Deseja realmente sair? [S/N]", "red")
    e = input("> ")
    if e == 's' or e == 'S': 
        color_text("[+] Um momento...", "magenta")
        time.sleep(3)
        exit()
    else:
        logo()
        MENU()

def ver():
    connect = sql.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM alunos")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    connect.close()
    print(tabulate(rows, headers=col_names, tablefmt="pretty"))
    input("pressione enter para voltar ao menu: ")
    logo()
    MENU()

def ver_Es():
    num = input("Qual o número do aluno que você deseja ver? ")
    connect = sql.connect("data.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (num,))
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    connect.close()
    print(tabulate(rows, headers=col_names, tablefmt="pretty"))
    time.sleep(3)
    logo()
    MENU()

def delete(l):
    connect = sql.connect('data.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?', (l,))
    connect.commit()
    connect.close()
    color_text(f"Aluno com id {l} foi removido", 'yellow')
    time.sleep(3)
    logo()
    MENU()

def dele():
    t = input("Qual o número do aluno que você deseja remover? ")
    delete(t)
    time.sleep(3)
    logo()
    MENU()

# Inicializa o programa
logo()
MENU()
