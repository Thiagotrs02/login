lista = []
while True:
    try:
       
        nome = input('Digite seu nome: ').strip()
        if not nome:
            print('Em "nome" Digite algo')
            continue 
        elif len(nome) < 3:
            print('Digite um nome com 3 ou mais letras')
            continue 
  
        
    
        
        idade = input('Digite sua idade: ').strip()
        if not idade:
            print('a opção "idade" deve ser preenchida')
            continue 
        elif not idade.isdigit():
            print('Digite apenas números')
            continue 
        idade =int(idade)
        
        if idade >= 18:
            cnh = input('possui habilitação? [s]im [n]ão: ').strip()
            if not cnh:
                print('o espaço "cnh" não pode estar vazio')
                continue 
        email = input('digite seu email: ').strip()
        if not email:
            print('O espaço não pode estar em branco')
            continue
        elif "@" not in email or ".com" not in email:
            print('Digite um email válido')
            continue 
            
        cpf = input('Digite seu cpf: ').strip()
        if not cpf:
            print('em "cpf" o espaço deve ser preenchido')
            continue 
        elif len(cpf) < 11:
            print('Digite um cpf válido')
            continue 
        elif not cpf.isdigit():
            print('Digite apenas números')
            continue
            
    except Exception as erro:
        print(f'algo deu errado{erro}')
        
    sair = input ('Deseja sair [s]im [n]ão: ').lower()
    if sair.startswith('s'):
        print('saindo')
        break