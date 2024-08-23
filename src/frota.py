class Carro:
    modelo: str
    marca: str
    cor: str
    odometro = 0.0
    motor_on = False
    tanque: float
    consumo_medio: float

    def __init__(self, modelo: str, marca: str, cor: str, motor: bool, tanque: float, cm: float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        #self.odometro = odometro
        self.motor_on = motor
        self.tanque = tanque
        self.consumo_medio = cm

    def ligar(self):
        if not self.motor_on and self.tanque > 0:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")
            '''print se comunica com o usuario final, enquanto o objetivo do programa
            é rodar as coisas por trás dos panos'''

    def acelerar(self, velocidade: float, tempo: float):
        if self.motor_on:
            km = velocidade * tempo
            litros = km / self.consumo_medio
            if self.tanque >= litros:
                self.odometro += km
                self.tanque -= litros
            else:
                km = self.tanque * self.consumo_medio
                self.tanque = 0
                self.desligar()
            self.odometro += km
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}, distancia {self.odometro} Km, '
                f'motor {self.motor_on}, consumo {self.consumo_medio} km/l, nível do tanque em {self.tanque:.2f} L')
        return info





