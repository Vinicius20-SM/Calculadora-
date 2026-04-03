

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (- + / *): ')

    numeros_validos = True

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
    except:
        numeros_validos = False

    if not numeros_validos:
        print('Um ou ambos números são inválidos')
        continue

    operadores_permitidos = '-+/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador=='+':
        print(num_1_float + num_2_float)
    elif operador=='-':
        print(num_1_float - num_2_float)
    elif operador=='/':
        print(num_1_float / num_2_float)
    elif operador=='*':
        print(num_1_float * num_2_float)

    
    sair=input('Quer sair? [s]im ').lower().startswith('s')


    if sair is True:
        print('Você saiu')
        break


   


            
