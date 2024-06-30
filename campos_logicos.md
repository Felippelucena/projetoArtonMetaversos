
# Diretrizes para o Preenchimento dos Campos Lógicos

Este documento fornece diretrizes sobre como preencher os campos lógicos para a criação de raças, classes, poderes, magias e regras em nosso sistema de gerenciamento de partidas de Tormenta 20.

## Estrutura Básica

1. Os campos lógicos são dicionários, salvos em JSON no banco de dados.
 
 O construtor lógico é organizado por etapas:

```json
{
  "etapa_1": {},
  "etapa_2": {}
}
```

2. Cada etapa possui N passos lógicos que respeitam uma estrutura regular.

## Passos Lógicos

### Estrutura

- `atributo`: Você chama o atributo que pretende acessar do personagem.
- `atributo_metodo(argumentos)`: Cada atributo possui uma lista de métodos com argumentos específicos.
- `atributo_metodo()*3`: Realizar o passo lógico 3 vezes.

**Exemplo de um passo lógico:**

Uma etapa com três passos lógicos: 
- Primeiro passo: o jogador escolhe um atributo para receber +2.
- Segundo passo: o jogador escolhe dois atributos, exceto força, para receber +1.
- Terceiro passo: o jogador não faz nenhuma escolha, o personagem recebe +1 em destreza.

```json
{
  "Etapa1": {
    "passos": [
      "atributos_add(2)",
      "atributos_add(1, '', ['del', 'for'])*2",
      "atributos_add(1, 'des')"
    ]
  }
}
```

### Lista de Passos Lógicos

#### Atributos

**Métodos**

- **add()**: Adicionar pontos de atributo.
  - Uso: `atributos_add(quantia, atributo, lista)`
  - Campos:
    - `quantia`: Valores entre -10 a 10.
    - `atributo`: O atributo que recebe a quantia. *Se deixar este campo vazio (''), o jogador escolhe*.
    - `lista`: Uma lista de escolhas, sendo o primeiro elemento da lista sua identificação: `add` (lista de opções disponíveis) ou `del` (lista de opções indisponíveis).
  - Exemplos:
    - `atributos_add(1)`: *O jogador escolhe um atributo para receber +1 entre todos existentes*.
    - `atributos_add(2, 'for')`: *O jogador não faz escolha, apenas recebe +2 em força*.
    - `atributos_add(1, '', ['del', 'car'])`: *O jogador escolhe um atributo para receber +1 entre todos existentes, exceto carisma*.

- **del()**: Remover pontos de atributo.
  - Uso: `atributos_del(quantia, atributo)`
  - Campos:
    - `quantia`: Valores entre -10 a 10.
    - `atributo`: O atributo que perderá a quantia. *Se deixar este campo vazio (''), o jogador escolhe*.
  - Exemplo:
    - `atributos_del(1)`: *O jogador escolhe um atributo para perder 1 ponto*.
    - `atributos_del(2, 'for')`: *O jogador não faz escolha, apenas perde 2 pontos em força*.

#### Perícias

**Métodos**

- **add()**: Adicionar pontos de perícia.
  - Uso: `pericias_add(quantia, pericia, treino, atrb, lista)`
  - Campos:
    - `quantia`: Valores entre -10 a 10.
    - `pericia`: A perícia que recebe a quantia. *Se deixar este campo vazio (''), o jogador escolhe*.
    - `treino` : Treinar Pericia, preencher com `treinar`
    - `atrb`: Alterar atributo chave, preencher com `atributo`
    - `lista`: Uma lista de escolhas, sendo o primeiro elemento da lista sua identificação: `add` (lista de opções disponíveis) ou `del` (lista de opções indisponíveis).
  - Exemplo:
    - `pericias_add(1)`: *O jogador escolhe uma perícia para receber +1 entre todas as disponíveis*.
    - `pericias_add('', 'sobrevivencia', 'treinar', '', '')`

- **del()**: Remover pontos de perícia.
  - Uso: `pericias_del(quantia, pericia)`
  - Campos:
    - `quantia`: Valores entre -10 a 10.
    - `pericia`: A perícia que perderá a quantia. *Se deixar este campo vazio (''), o jogador escolhe*.
  - Exemplo:
    - `pericias_del(2)`: *O jogador escolhe uma perícia para perder 2 pontos*.


#### Poder Geral

**Métodos**

- **add()**: Adicionar um poder geral.
  - Uso: `podergeral_add`
  - Exemplo:
    - `podergeral_add`: *Adicionar um poder geral*.

- **del()**: Remover um poder geral.
  - Uso: `podergeral_del`
  - Exemplo:
    - `podergeral_del`: *Remover um poder geral*.

#### Escolha

Para definir escolhas condicionais:

1. **Definir o número de escolhas**:
   - Uso: `escolha(opcao1, opcao2)`
   - Exemplo: `escolha(escolha 1, escolha 2)`

2. **Definir a ação para cada escolha**:
   - Uso: `escolha(opcao1[acao1], opcao2[acao2])`
   - Exemplo: `escolha(escolha 1[atributos_add(2)], escolha 2[pericias_treinar, pericias_atrb('for')])`

#### Condição

Para definir condições específicas:

1. **Definir a(s) condição(ões)**:
   - Uso: `condicao([variavel, operadorlogico, variavel])`
   - Exemplo: `condicao([localizacao, '==', 'subterraneo'])`

---

Espero que esta estrutura atualizada e melhorada torne o documento mais claro e fácil de entender. Se precisar de mais alguma coisa, estou à disposição!