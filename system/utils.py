# Verifica se os dados colocados são válidos
def check_info(regist):
    label_status = ''
    invalid_things = []
    # Verifica se o campo do nome é vazio ou não
    check = regist.name.strip()
    if check == '':
        label_status += 'Nome inválido\n'
        invalid_things.append('name')
    # Verifica se o telefone é inválido (se tem caractere, se é vazio ou se não tem a quantidade de números
    # o suficiente para ser um número de telefone)
    tel = regist.tel.replace(' ','')
    tel = tel.replace('(','').replace(')','')
    tel = tel.replace('-','')
    tel = tel.replace('+','')
    if not tel.isdigit() or not (15 >= len(tel) >= 6):
        label_status += 'Telefone inválido\n'
        invalid_things.append('tel')
    # Valida o email verificando se ele possui @ ou não e outras coisas
    email = regist.email.strip()
    check = ((' ' in email) or
    ('@.' in email) or
    ('.@' in email) or
    ('..' in email) or
    (not '@' in email) or
    (email == '') or
    (email.endswith(".")) or
    (email.endswith("@")) or
    (email.count("@") != 1) or
    (email.startswith("@")) or
    (email.startswith(".")))
    if check or not '.' in email.split('@')[1]:
        label_status += 'Email inválido\n'
        invalid_things.append('email')
    # Valida o endereço da mesma forma do nome
    check = regist.address.strip()
    if check == '':
        label_status += 'Endereço inválido\n'
        invalid_things.append('address')
    return (invalid_things, label_status)