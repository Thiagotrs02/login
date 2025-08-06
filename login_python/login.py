llista = []

while True:
    try:
        tentativa = 0
        while tentativa < 3:
            nome = input('Digite seu nome: ').strip()
            if not nome:
                print('Em "nome" Digite algo')
                tentativa += 1
                continue
            elif len(nome) < 3:
                print('Digite um nome com 3 ou mais letras')
                tentativa += 1
                continue
            else:
                break
        else:
            print('suas tentativas acabaram')
            continue

        tentativa = 0
        while tentativa < 3:
            idade = input('Digite sua idade: ').strip()
            if not idade:
                print('a opção "idade" deve ser preenchida')
                tentativa += 1
                continue

            elif not idade.isdigit():
                print('Digite apenas números')
                tentativa += 1
                continue
            else:
                break
        else:
            print('tente novamente')
            continue

        idade =int(idade)

        tentativa = 0
        while tentativa < 3:
            if idade >= 18:
                cnh = input('possui habilitação? [s]im [n]ão: ').strip()
                if not cnh:
                    print('o espaço "cnh" não pode estar vazio')
                    tentativa += 1
                    continue
                else:
                    break
        else:
            print('tente novamente')
            continue

        tentativa = 0
        while tentativa < 3:
            email = input('digite seu email: ').strip()
            if not email:
                print('O espaço não pode estar em branco')
                tentativa += 1
                continue
            elif "@" not in email and ".com" not in email:
                print('Digite um email válido')
                tentativa += 1
                continue
            else:
                break
        else:
            print('tente novamente')
            continue

        tentativa = 0
        while tentativa < 3:
            cpf = input('Digite seu cpf: ').strip()
            if not cpf:
                print('em "cpf" o espaço deve ser preenchido')
                tentativa += 1
                continue
            elif len(cpf) < 11:
                print('Digite um cpf válido')
                tentativa += 1
                continue
            elif not cpf.isdigit():
                print('Digite apenas números')
                tentativa += 1
                continue
            else:
                break
        else:
            print('tente novamente')
            continue

        lista.append(f'nome:{nome}, idade:{idade}, cpf:{cpf}, email:{email}')

        sair = input('Deseja sair [s]im [n]ão: ').lower()
        if sair.startswith('s'):
            print('saindo')
            break


    except Exception as erro:
        print(f'algo deu errado{erro}')

print('Resumo de cadastros:')
for item in lista:
    print(item)