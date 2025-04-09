nome = input('Digite o seu nome: ')
nomeM = nome.upper()
nomem = nome.lower()
nomeseparado = nome.split() #separa o nome em uma lista
nomejunto = ''.join(nome.split())
encontrar1 = nome.find('silva')
emcontrar2 = nome.find('a')
contar = nome.count('a')


print('O seu nome em maiúsculo',nomeM)
print('O seu nome em minúsculo',nomem)
print('Total de letras em seu nome',len(nomejunto))
print('Seu primeiro nome tem',len(nomeseparado[0]),' letras')
print('Seu último nome é',nomeseparado[-1])
print('Seu nome tem Silva?',encontrar1)
print('Seu nome onde aparece a primeira letra "a"',emcontrar2)
print('Quantas veses aparece a letra "a"',contar)