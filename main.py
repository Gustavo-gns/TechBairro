# Importando a pasta utils (com funções do sistema);
# O client para a classe client;
# O database para a classe gerenciadora;
# O tkinter para fazer a aplicação desktop;
# O sqlite3 para o banco de dados;
# E o os para criar o caminho certo para o banco
import system.utils as ut, tkinter as tk, sqlite3 as sqlt, os
from system.client import Client
from tkinter import messagebox
from system.database import ClientManager

# Versão do sistema
VERSION = '3.3.2'

# __file__ é o caminho deste arquivo .py.
# Assim o techbairro.db fica SEMPRE na mesma pasta do projeto,
# não importa de onde o VS Code rodar o programa.
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(PROJECT_FOLDER, "techbairro.db")
# Mostra no terminal qual banco está em uso
print(f'Banco em uso: {DATABASE_PATH}')
# Gerenciador de clientes
try:
    manager = ClientManager(DATABASE_PATH)
except sqlt.Error as error:
    print(f'Erro ao acessar o banco: {error}')
    exit()

# Criar janela
root = tk.Tk()
root.title('TechBairro - Cadastro de Cliente')
root.geometry('500x370')
root.config(bg="#D8D8D8")
root.resizable(False,False)

# Janelas novas que abrem
consult_window = None
edit_window = None

# Cabeçalho
header = tk.Frame(root, bg="#2C3E50")
header.pack(side='top',fill='x')
tk.Frame(root,height=1.5,bg="#223141").pack(fill='x')

tk.Label(header, text='Cadastro de Cliente', bg="#2C3E50", font=('Arial',25,'bold'), fg="#D6D6D6", pady=5).pack()

# Formulário
form_frame = tk.Frame(root, bg="#D8D8D8")
form_frame.pack(pady=20)

# Campos para serem criados com um ciclo de repetição
fields = {'name':'Nome', 'tel':'Telefone', 'email':'Email', 'address':'Endereço'}
text_box_inputs = {}
items_row = 0

# Cria as labels e entrys de cada um dos campos de fields
for text_box, entry_label in fields.items():
    tk.Label(form_frame,text=f'{entry_label}:',bg='#D8D8D8').grid(row=items_row, column=0, sticky="e", pady=4, padx=3)
    text_box_input = tk.Entry(form_frame,width=30)
    text_box_input.grid(row=items_row,column=1)
    items_row += 1
    text_box_inputs[text_box] = text_box_input

# Botões
buttons_frame = tk.Frame(root, bg="#D8D8D8")
buttons_frame.pack()

# Funcão para usar no botão de salvar
def on_button_salvar_click(event=None,inputs=text_box_inputs,selection=None,window=None,label=None):
    if label is None:
        label = label_status
    # Classe recebe os Entry
    user_regist = Client(*(input.get() for label_input, input in inputs.items()))

    # Configura a cor de todos os entry para branco
    for label_input, input in inputs.items():
        input.config(bg='#FFFFFF')
    # Mudança da label de validação
    invalid = ut.check_info(user_regist)
    if invalid[0] != []:
        label.config(text=invalid[1],fg='red')
        for i in invalid[0]:
            if inputs == text_box_inputs:
                inputs[i].delete(0,tk.END)
            inputs[i].config(bg='#FFBCBC')
    else:
        try:
            # Valida as entradas e dá um retorno positivo
            if inputs == text_box_inputs:
                manager.add_client(user_regist)
                label_qntd_status.config(text=f'Quantidade de clientes do sistema: {manager.total_clients()}')
                label_status.config(text=f'O cadastro de {user_regist.name} foi feito com sucesso!',fg="#267128")
                main_clean_all_entry(False)
                # Se a janela de consulta já estiver aberta, atualiza a lista
                if consult_window is not None and consult_window.winfo_exists():
                    update_list()
            else:
                manager.update(selection.id,user_regist)
                label_qntd_status.config(text=f'Quantidade de clientes do sistema: {manager.total_clients()}')
                label_status.config(text=f'Edição de {user_regist.name} feita com sucesso!',fg="#267128")
                window.destroy()
        except sqlt.Error as erro:
            label_status.config(text=f'Erro ao acessar o banco: {erro}',fg='red')
            if not inputs == text_box_inputs:
                window.destroy()

# Limpa todos os entry
def main_clean_all_entry(confirm=True):
    # Apaga os campos e redefine a label de validação
    for label_input, input in text_box_inputs.items():
        input.delete(0,tk.END)
        input.config(bg='#FFFFFF')
    if confirm:
        label_status.config(text='')

# Função para atualizar a lista dentro do consultar
def update_list(search=''):
    # Primeiro limpa a lista visual
    client_list.delete(0, tk.END)
    try:
        clients = manager.list_clients(search)
        # Exibe os clientes encontrados
        for pos, user in enumerate(clients, start=1):
            text = f'{pos}. {user.summary()}'
            client_list.insert(tk.END, text)
        # Informa quando não há resultados
        if not clients:
            client_list.insert(tk.END, 'Nenhum cliente encontrado.')
    except sqlt.Error as error:
        consult_window.destroy()
        label_status.config(text=f'Erro ao acessar o banco: {error}',fg='red')

# Função para editar um registro
def on_button_editar_click(event=None):
    global consult_window, edit_window, client_list

    # Descobre qual tarefa foi selecionada
    selected = client_list.curselection()

    # Verifica se há clientes na listagem
    if not manager.list_clients(search_bar.get()):
        return

    # Verifica se alguma tarefa foi selecionada
    if not selected:
        messagebox.showwarning('Atenção','Selecione algum registro para prosseguir!')
        return
    
    # Cria a janela
    edit_window = tk.Toplevel(root,bg='#D8D8D8')
    edit_window.title('Editar Registro')
    edit_window.geometry('300x300')
    edit_window.resizable(False,False)
    edit_header = tk.Frame(edit_window, bg="#2C3E50")
    edit_header.pack(side='top',fill='x')
    tk.Frame(edit_window,height=1.5,bg="#223141").pack(fill='x')
    tk.Label(edit_header, text='Edição de Cliente', bg="#2C3E50", font=('Arial',15,'bold'), fg="#D6D6D6", pady=5).pack()
    consult_window.destroy()
    consult_window = None
    
    # Formulário de edição
    edit_frame = tk.Frame(edit_window, bg="#D8D8D8")
    edit_frame.pack(pady=2)

    # Campos para serem criados com um ciclo de repetição
    text_box_edit_inputs = {}
    items_row = 0

    # Cria as labels e entrys de cada um dos campos de fields
    for text_box, entry_label in fields.items():
        tk.Label(edit_frame,text=f'{entry_label}:',bg='#D8D8D8').grid(row=items_row, column=0, sticky="e", pady=4, padx=3)
        text_box_input = tk.Entry(edit_frame,width=30)
        text_box_input.grid(row=items_row,column=1)
        try:
            exec(f'text_box_input.insert(0,manager.list_clients()[selected[0]].{text_box})')
        except sqlt.Error as error:
            edit_window.destroy()
            label_status.config(text=f'Erro ao acessar o banco: {error}',fg='red')
            return
        items_row += 1
        text_box_edit_inputs[text_box] = text_box_input

    def edit_save(event=None):
        on_button_salvar_click(
            inputs=text_box_edit_inputs,
            selection=manager.list_clients()[selected[0]],
            window=edit_window,
            label=label_edit_status)

    # Cria os Botões
    buttons_edit_frame = tk.Frame(edit_window,bg='#D8D8D8')
    buttons_edit_frame.pack(pady=1)
    label_edit_status = tk.Label(edit_window,text='', bg='#D8D8D8')
    label_edit_status.pack(pady=1)
    tk.Button(buttons_edit_frame, text='Salvar', width=15, command=edit_save).grid(column=0, row=0,padx=2)
    tk.Button(buttons_edit_frame, text='Cancelar', width=15, command=edit_window.destroy).grid(column=1, row=0, padx=2)
    edit_window.bind('<Return>', edit_save)

# Função para excluir um registro
def on_button_excluir_click(event=None):
    # Descobre qual tarefa foi selecionada
    selected = client_list.curselection()
    # Verifica se há clientes na listagem
    if not manager.list_clients(search_bar.get()):
        return
    # Verifica se alguma tarefa foi selecionada
    if not selected:
        messagebox.showwarning('Atenção','Selecione algum registro para prosseguir!')
        return
    # Descobre o índice da tarefa
    index = selected[0]
    try:
        client = manager.list_clients()[index]
    except sqlt.Error as error:
        consult_window.destroy()
        label_status.config(text=f'Erro ao acessar o banco: {error}',fg='red')
        return
    # Confirma que o usuário quer excluir, e se o usuário confirmar exclui
    check = messagebox.askyesno(
        "Confirmar exclusão",
        f"Deseja realmente excluir o registro de {manager.list_clients()[index].name}? \nEmail: {manager.list_clients()[index].email} \nTelefone: {manager.list_clients()[index].tel}")
    if check:
        # Remove a tarefa
        manager.remove(client.id)
        # Atualiza a lista na tela
        if manager.total_clients() == 0:
            consult_window.destroy()
        else:
            update_list()
        label_qntd_status.config(text=f'Quantidade de clientes do sistema: {manager.total_clients()}')
        label_status.config(text='')
        messagebox.showinfo("Sucesso",f"Registro de {client.name} excluído!")

# Função para abrir uma janela com a lista de clientes
def open_consult():
    global client_list, consult_window, edit_window, search_bar

    # Se a janela de edição estiver aberta, não permite consultar
    if edit_window is not None and edit_window.winfo_exists():
        label_status.config(text='Termine de editar primeiro!',fg='red')
        return

    # Se a janela de consulta já estiver aberta, não cria outra
    if consult_window is not None and consult_window.winfo_exists():
        label_status.config(text='Tela de consulta já aberta!',fg='red')
        return

    try:
        # Verifica se a janela pode ser aberta (se não tiver clientes cadastrados, não abre)
        if manager.list_clients() == []:
            label_status.config(text='Nenhum cliente cadastrado', fg='red')
            return
    except sqlt.Error as error:
        label_status.config(text=f'Erro ao acessar o banco: {error}',fg='red')
        return

    consult_window = tk.Toplevel(root)
    consult_window.title('Consulta de Clientes')
    consult_window.geometry('500x350')
    consult_window.resizable(False,False)
    client_list = tk.Listbox(consult_window, width=40)

    # Barra de pesquisa
    search_frame = tk.Frame(consult_window, bg='#2C3E50', height=30)
    search_frame.pack(fill='x')
    tk.Frame(consult_window, height=1.5, bg="#223141").pack(fill='x', pady=(0, 5))
    search_frame.pack_propagate(False)

    tk.Label(search_frame, text='Pesquisar...', bg='#2C3E50', fg='#D8D8D8', font=('Arial', 11, 'bold')).pack(side='left', padx=1, anchor='center')

    # Variável que acompanha o conteúdo da pesquisa
    search_text = tk.StringVar()

    search_bar = tk.Entry(search_frame, width=66, textvariable=search_text)
    search_bar.pack(side='left', padx=1, anchor='center')

    # Atualiza a lista sempre que o texto mudar
    search_text.trace_add('write', lambda *args: update_list(search_text.get()))

    # Configura corretamente a lista
    client_list.pack(fill='both', expand=True)

    # Cria a scrollbar
    scrollbar = tk.Scrollbar(client_list)
    scrollbar.pack(side='right', fill='y')

    # Frame para os botões
    buttons_frame = tk.Frame(consult_window)
    buttons_frame.pack(pady=5)

    # Botões 
    tk.Button(buttons_frame, text='Editar', width=15, command=on_button_editar_click).pack(side='left', padx=5, anchor='center')
    tk.Button(buttons_frame, text='Excluir', width=15, command=on_button_excluir_click).pack(side='left', padx=5, anchor='center')

    # Faz com que ao apertar um cliente duas vezes abre a aba de edição dele
    client_list.bind("<Double-Button-1>", on_button_editar_click)

    # Faz com que ao apertar um cliente e depois clicar em delete, abra uma aba de confirmação para apagar ele
    client_list.bind("<Delete>", on_button_excluir_click)
    
    client_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=client_list.yview)

    # Adiciona os itens na lista
    update_list()

# Faz com que ao apertar Enter faz o mesmo do botão salvar
root.bind('<Return>', on_button_salvar_click)

tk.Button(buttons_frame, text='Salvar', width=15, command=on_button_salvar_click).grid(row=0, column=0, sticky='e', padx=2, pady=2)
tk.Button(buttons_frame, text='Limpar', width=15, command=main_clean_all_entry).grid(row=0, column=1, sticky="e", padx=2, pady=2)
tk.Button(root, text='Consultar clientes', width=15, command=open_consult).pack(pady=5)

label_qntd_status = tk.Label(root, text=f'Quantidade de clientes do sistema: {manager.total_clients()}', bg='#D8D8D8')
label_qntd_status.pack()

label_status = tk.Label(root, text= '', bg="#D8D8D8")
label_status.pack()

# Versão
versao = tk.Label(root, text=f'v{VERSION}', fg="gray", bg="#D8D8D8")
versao.place(rely=0.95, relx=0.97, anchor='e')

# Deixa a janela aberta de maneira constante
root.mainloop()