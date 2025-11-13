nome = 'Anderson'

'''criando uma lista para guardar as cores e acessar via nome'''
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'Preto':'\033[30m',
         'Vermelho':'\033[31m',
         'Verde':'\033[32m',
         'Amarelo':'\033[33m',
         'Azul':'\033[34m',
         'Magenta':'\033[35m',
         'Cyan':'\033[36m',
         'Cinza Claro':'\033[37m',
         'Cinza Escuro':'\033[90m',
         'Vermelho Claro':'\033[91m',
         'Verde Claro':'\033[92m',
         'Amarelo Claro':'\033[93m',
         'Azul Claro':'\033[94m',
         'Magenta Claro':'\033[95m',
         'Cyan Claro':'\033[96m',
         'Branco':'\033[97m',
}

'''Negrito	\033[;1m	-
Inverte	\033[;7m	-
Reset (remove formatação)	\033[0;0m	-'''

print(f'Olá! Muito prazer em te conhecer, {cores['azul']} {nome} {cores['limpa']}')

#tambem pode ser feito dessa maneira
#print(f'Olá! Muito prazer em te conhecer, \033[;32m{nome}\033[m')