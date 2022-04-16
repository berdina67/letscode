import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_de_categorias = []

    for id in dados:
        lista_de_categorias.append(id['categoria'])

    lista_de_categorias.sort()
    # return lista_de_categorias
    
    # Eliminar as duplicatas
    contador = 1
    lista_categorias_nova = []

    while contador < len(lista_de_categorias):
        if lista_de_categorias[0] == lista_de_categorias[1]:
            lista_de_categorias.pop(0)
            
        else:
            lista_categorias_nova.append(lista_de_categorias[0])
            lista_de_categorias.pop(0)

        contador + 1
    
    #lista_categorias_nova.append(dados[0])    
    
    return lista_categorias_nova 
    


def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    tam = len(dados)
    id = []
    for cat in range(tam):
        if dados[cat]['categoria'] == categoria:
            id.append(dados[cat]['id'])
    
    return id
    
 

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    tam_lista = len(dados)
    dicio_maior = {}
    max_valor = 0.1
    for i in range(tam_lista):
        if categoria == dados[i]['categoria']:
            #print(dados[i]['preco'])
            preco = float(dados[i]['preco'])
            if preco > max_valor:
                produto = dados[i]['id']
                max_valor = preco

    return produto, max_valor


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    tam_lista = len(dados)
    dicio_maior = {}
    min_valor = maior_valor_total(d)
    for i in range(tam_lista):
        if categoria == dados[i]['categoria']:
            #print(dados[i]['preco'])
            preco = float(dados[i]['preco'])
            if preco < min_valor:
                produto = dados[i]['id']
                min_valor = preco

    return produto, min_valor

# Essa função retorna o menor preco do Banco de Dados. 
def menor_valor_total(dados):
    tam_lista = len(dados)
    lista_valores_total = []
    for i in range(tam_lista):
        numero = float(dados[i]['preco']) 
        lista_valores_total.append(numero)
    preco_minimo = min(lista_valores_total)
    
    return preco_minimo

# Essa função retorna o maior preço do Banco de dados.
def maior_valor_total(dados):
    tam_lista = len(dados)
    lista_valores_total = []
    for i in range(tam_lista):
        numero = float(dados[i]['preco']) 
        lista_valores_total.append(numero)
    preco_maximo = max(lista_valores_total)
    
    return preco_maximo


def top_10_caros(dados):

    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_preco = []

    for i in range(len(dados)):
        f = float(dados[i]['preco'])
        dados[i].update({'preco':f})
        lista_preco.append(dados[i]['preco'])
          
    lista_preco.sort()
    lista_max_10 = lista_preco[990:]
    
    lista_id_max = []

    for p in lista_max_10:
        for k in range(len(dados)):
            if p == dados[k]['preco']:
                lista_id_max.append(dados[k]['id'])

    lista_dicio_max = []

    for i in range(10):
        lista_dicio_max.append({'id': lista_id_max[i], 'preco': lista_max_10[i]})
    
    return lista_dicio_max

    
    

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_preco = []

    for i in range(len(dados)):
        f = float(dados[i]['preco'])
        dados[i].update({'preco':f})
        lista_preco.append(dados[i]['preco'])
    
    lista_preco.sort()    
    lista_min_10 = lista_preco[:10]
    
    lista_id_min = []

    for p in lista_min_10:
        for k in range(len(dados)):
            if p == dados[k]['preco']:
                lista_id_min.append(dados[k]['id'])

    lista_dicio_min = []

    for i in range(10):
        lista_dicio_min.append({'id': lista_id_min[i], 'preco': lista_min_10[i]})
    
    return lista_dicio_min

def menu(dados):
    '''
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''

def menu():
    print(60 * '*')
    print('* Sistema de Consultas de Produtos do Magalu! *')
    print(60 * '*')
    print('Escolha uma das opções abaixo:')
    print('1. Listar categorias')
    print('2. Listar produtos de uma categoria')
    print('3. Produto mais caro por categoria')
    print('4. Produto mais barato por categoria')
    print('5. Top 10 produtos mais caros')
    print('6. Top 10 produtos mais baratos')
    print('0. Sair')

    num = input('Opção: ')

    if num == '1':
        categorias = listar_categorias(d)
        print()
        print(categorias)
        print()
        menu()


    # 2. Listar produtos de uma categoria
    
    elif num == '2':
        categ = listar_categorias(d)
        categoria = input('Digite uma categoria para saber quais produtos ela contém.: ')
        if categoria in categ:
            print()
            print(listar_por_categoria(d, categoria))
            print()
        else:
            print()
            print(10*'*','Produto não encontrado.', 10*'*')
            print()
        menu()
    
#3. Produto mais caro por categoria
    
    elif num == '3':
        categ = listar_categorias(d)
        categoria = input('Digite uma categoria para saber qual produto é mais caro.: ')
        if categoria in categ:
            print()
            resultado = produto_mais_caro(d, categoria)
        
        dict_max = {'id':resultado[0], 'categria':categoria, 'Preço':resultado[1]}
        print(dict_max)
        print()
        menu()
    
    # 4. Produto mais barato por categoria
    
    elif num == '4':
        categ = listar_categorias(d)
        categoria = input('Digite uma categoria para saber qual produto é mais barato.: ')
        if categoria in categ:
            print()
            resultado = produto_mais_barato(d, categoria)
        
        dict_min = {'id':resultado[0], 'categria':categoria, 'Preço':resultado[1]}
        print(dict_min)
        print()
        menu()
    
    # 5. Top 10 produtos mais caros'    
    
    elif num == '5':
        max_10 = top_10_caros(d)
        print()
        print('lista dos 10 produtos mais caros.')
        print(max_10)
        menu()
    
    # 6. Top 10 produtos mais baratos
    
    elif num == '6':
        min_10 = top_10_baratos(d)
        print()
        print('lista dos 10 produtos mais baratos.')
        print(min_10)
        menu()
    
     # 0. Sair 
    elif num == '0':
        print()
        print('Você saiu do programa.')
        print()
       
    else:
        print()
        print('##### Opção inválida. Digite uma opção correta ou "0" para sair. #####')
        print()
        menu()
'''
    # 7. Print base de dados.
   
    elif num == '7':
        print(d)
    
    # 8. Valor mínimo de todos os produtos
    
    elif num == '8':
        preco_min = menor_valor_total(d)
        print(preco_min)
    
    # 9. Valor máximo de todos os produtos
    elif num == '9':
        preco_max = maior_valor_total(d)
        print(preco_max)
'''
 

# Programa Principal - não modificar!
d = obter_dados()

menu()



