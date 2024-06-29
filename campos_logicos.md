Diretrizes para o preenchimento dos campos lógicos:


As escolhas organizadas por etapas identificadas com [].
exemplo: [etapa1][etapa2]

metodos:
metodos são os passos que cada etapa vai seguir.

1. No final de um metodo é possivel passar uma lista [] de opções possiveis.
    O primeiro elemento da lista informa se a lista é de 'escolha' ou 'exceto'.

    Exemplo de uso 1: [pericias_add_2[escolha,acrobacia,sobrevivencia,guerra,atletismo]] #O jogador pode escolher entre as 4 pericias para receber mais 2 em uma.

    Exemplo de uso 2: [atributos_add_1[exceto,car]*3] #O jogador coloca +1 em 3 atributos diferentes exeto carisma.

2. No final de um metodo é possivel multiplicar seu efeito utilizando o simbolo de multiplicador mais a quantidade '*2'.
    Exemplo de uso: [atributos_add_1*3] #Adicionar +1 em 3 atributos diferentes.

3. Lista de metodos:

    atributos:
        - add --> uso: atributos_add_* (ex: atributos_add_2)
        - del --> uso: atributos_del_* (ex: atributos_del_1)

    pericias:
        - add --> pericias_add_* (ex: pericias_add_1)
        - del --> pericias_del_* (ex: pericias_del_2)
        - treinar --> pericias_treinar
        - atrb --> pericias_atrb_* (ex: pericias_atrb_for)

    podergeral:
        - add --> podergeral_add (ex: podergeral_add)
        - del --> podergeral_del (ex: podergeral_del)

    escolha:

        Primeiro, definir o numero de escolhas:
        - () --> uso: escolha(escolha 1,escolha 2)

        Segundo, para cada escolha definir um ação:
        - [] --> uso: escolha(escolha 1[atributos_add_2],escolha 2[pericias_treinar,pericias_atrb_for])
    
    condicao():
        Primeiro, definiar a(s) condição(ões):
        - [variavel,operadorlogico,variavel] --> uso: condicao([localizacao,==,subterraneo])



