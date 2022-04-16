
#from cliente import Cliente
#from loja import Loja

class Loja:
    def __init__(self):
        self.bicicletas = {
                        1: ['branca', 'infantil', '-', 'Não', '-'],
                        2: ['branca', 'corrida', '-', 'Não', '-'],
                        3: ['branca', 'infantil', '-', 'Não', '-'],
                        4: ['branca', 'passeio', '-', 'Não', '-'], 
                        5: ['vermelha', 'passeio', '-', 'Não', '-'],
                        6: ['vermelha', 'corrida', '-', 'Não', '-'],
                        7: ['vermelha', 'passeio', '-', 'Não', '-'],
                        8: ['azul', 'infantil', '-', 'Não', '-'],
                        9: ['azul', 'corrida', '-', 'Não', '-'], 
                        10: ['azul', 'infantil', '-', 'Não', '-']}

        self.valores = {
                        'hora':5.0, 
                        'dia':25.0, 
                        'semana':100.0} 
    
    def add_bicicleta(self, cor, modelo):
        cod = (len(self.bicicletas)) + 1
        self.bicicletas[cod] = [cor, modelo, '-', 'Não', '-']

    def aluga_bicicleta(self, cliente):
        print()
        codigo = int(input('digite o código da biciclete que você deseja alugar? '))
        if self.bicicletas[codigo][2] == '-':
            print('***Bicicleta disponível!***')
        else:
            while self.bicicletas[codigo][2] != '-':
                print('Bicicleta já alugada. Por favor, escolha uma bicicleta livre')
                codigo = int(input('digite o código da biciclete que você deseja alugar? '))
        print()
        print('Escolha um dos pĺanos abaixo:')
        print(f' {"":_>10} {"":_>19}')
        for p in self.valores:
            print(f'|{p:>10}|valores:{self.valores[p]:>10}|')
        print(f' {"":_>10} {"":_>19}')
        print('''
************************** 
* Digite 'h' para hora,  *
* Digite 'd' para dia e  * 
* Digite 's' para semana.*
**************************
        ''')
        tempo = input('Digite aqui a sua opção: ')
        if tempo == 'h' or tempo == 'd' or tempo == 's':
            if tempo == 'h':
                tempo = 'hora'
            if tempo == 'd':
                tempo = 'dia'
            if tempo == 's':
                tempo = 'semana'
            print(f'Você escolheu {tempo}')
        else:
            opcao = True
            while opcao == True:
                print('Opção inválida. Favor escolher a opção correta:')
                print(f' {"":_>10} {"":_>19}')
                for p in self.valores:
                    print(f'|{p:>10}|valores:{self.valores[p]:>10}|')
                print(f' {"":_>10} {"":_>19}')
                tempo = input('Digite aqui a sua opção: ')            
                if tempo == 'h':
                    tempo = 'hora'
                    opcao = False
                if tempo == 'd':
                    tempo = 'dia'
                    opcao = False
                if tempo == 's':
                    tempo = 'semana'
                    opcao = False

            print(f'Você escolheu: {tempo}')

        if self.bicicletas[codigo][2] == '-':
            self.bicicletas[codigo][2] = cliente.email
            self.bicicletas[codigo][3] = 'sim'
            self.bicicletas[codigo][4] = tempo
        else:
            print('Bicicleta já alugada.')
            loja1.aluga_bicicleta(cliente1)

    def calcula_conta(self, cliente):
        cli = cliente1.email
        
        lista_preco = []
        for k in self.bicicletas:
            self.bicicletas[k][2]
            if self.bicicletas[k][2] == cliente.email:
                lista_preco.append(self.bicicletas[k][4])
        
        contador_hora = 0
        contador_dia = 0
        contador_semana = 0
        valor_hora = 0
        valor_dia = 0
        valor_semana = 0
        print()
        print(f'Empréstimos feitos por {cliente.nome} = {lista_preco}')

        for tempo in lista_preco:
            if 'hora' in tempo:
                contador_hora += 1
                valor_hora = contador_hora * 5.0

            if 'dia' in tempo:
                contador_dia += 1
                valor_dia = contador_dia * 25.0 

            if 'semana' in tempo:
                contador_semana += 1
                valor_semana = contador_semana * 100.0

        contador_total = contador_hora + contador_dia + contador_semana

        if contador_total >= 3:
            valor_desconto = (valor_hora + valor_dia + valor_semana) * 7/10
            print(f'valor com desconto = {valor_desconto} de {cliente.nome}')
        else:
            valor_normal = (valor_hora + valor_dia + valor_semana)
            print(f'valor sem desconto = {valor_normal} de {cliente.nome}')
            print()

    def devolve_bicicletas(self, cliente):
        for devolve in self.bicicletas:
            if self.bicicletas[devolve][2] == cliente.email:
                self.bicicletas[devolve][2] = '-'
                self.bicicletas[devolve][3] = 'não'
                self.bicicletas[devolve][4] = '-'
                print('Devolução realizada com sucesso!')
            
    



class Cliente:
    id = 0
    def __init__(self, nome, email):
        Cliente.id += 1
        self.id = Cliente.id
        self.nome = nome
        self.email = email
    
    def consulta_bicicletas(self, loja):
        consulta = loja.bicicletas
        print(f' {"":_<4} {"":_<10} {"":_<10} {"":_<20} {"":_<8} {"":_<8}')
        print(f'|{"cod":^4}|{"cor":^10}|{"modelo":^10}|{"email":^20}|{"alugado":^8}|{"plano":^8}|')
        print(f'|{"":_<4}|{"":_<10}|{"":_<10}|{"":_<20}|{"":_<8}|{"":_<8}|')
        for ch in consulta:
            print(f'|{ch:<4}|{consulta[ch][0]:<10}|{consulta[ch][1]:<10}|{consulta[ch][2]:^20}|{consulta[ch][3]:^8}|{consulta[ch][4]:^8}|')


loja1 = Loja()
cliente1 = Cliente('Fulvio', 'fulvio@fulvio')
cliente2 = Cliente('Fatima', 'fatima@fatima')
cliente3 = Cliente('lara', 'lara@lara')
cliente4 = Cliente('livia', 'livia@livia')

# cliente1 visualiza estoque:
print(loja1.bicicletas)
print()
loja1.add_bicicleta('verde', 'corrida')

cliente1.consulta_bicicletas(loja1)


# Sequência de pedidos
loja1.aluga_bicicleta(cliente1)
cliente1.consulta_bicicletas(loja1)
loja1.aluga_bicicleta(cliente1)
cliente1.consulta_bicicletas(loja1)
loja1.aluga_bicicleta(cliente2)
cliente1.consulta_bicicletas(loja1)
loja1.aluga_bicicleta(cliente1)
cliente1.consulta_bicicletas(loja1)
loja1.aluga_bicicleta(cliente2)
cliente1.consulta_bicicletas(loja1)

loja1.calcula_conta(cliente1)
loja1.calcula_conta(cliente2)

loja1.devolve_bicicletas(cliente1)
cliente1.consulta_bicicletas(loja1)
loja1.devolve_bicicletas(cliente2)
cliente1.consulta_bicicletas(loja1)

