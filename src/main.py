from frota import *

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)  # invoca o método str
    print("\n")

if __name__ == "__main__":
    '''for i in range(0, 2):
        print(f'Cadastro Carro {i + 1}')
        nm_modelo = input('Modelo: ')
        nm_marca = input('Marca: ')
        nm_cor = input('Cor: ')
        if i == 0:
            carro1 = Carro(nm_modelo, nm_marca, nm_cor, motor=False)
        else:
            carro2 = Carro(nm_modelo, nm_marca, nm_cor, motor=False)'''
    print('Cadastro Carro 1')
    nm_modelo = input('Modelo: ')
    nm_marca = input('Marca: ')
    nm_cor = input('Cor: ')
    cm = float(input('Consumo médio: '))
    litros = float(input('Tanque: '))
    carro1 = Carro(nm_modelo, nm_marca, nm_cor, False, litros, cm)

    print('Cadastro Carro 2')
    nm_modelo = input('Modelo: ')
    nm_marca = input('Marca: ')
    nm_cor = input('Cor: ')
    cm = float(input('Consumo médio: '))
    litros = float(input('Tanque: '))
    carro2 = Carro(nm_modelo, nm_marca, nm_cor, False, litros, cm)


    while carro1.odometro < 600 and carro2.odometro < 600 and (carro1.tanque > 0 or carro2.tanque > 0):
        try:
            escolha = 0
            while escolha not in (1, 2):
                escolha = int(input("Qual carro deseja operar? [1/2]\n"))

            if escolha == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)
        except Exception as e: # a exceção q foi capturada (pode ser qualquer uma)
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    if carro1.odometro > carro2.odometro:
        print("O primeiro carro alcançou 600 km primeiro!")
    else:
        print("O segundo carro alcançou 600 km primeiro!")

