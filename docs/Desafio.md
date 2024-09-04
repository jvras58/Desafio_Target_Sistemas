## Tarefa 1: Cálculo da Soma com Laço de Repetição

**Descrição:**
Observe o trecho de código abaixo e determine o valor final da variável `SOMA`.

```cpp
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { 
    K = K + 1; 
    SOMA = SOMA + K; 
}
Imprimir(SOMA);
```

**Checkpoints:**

1. Entenda o funcionamento do laço `Enquanto` (ou `while` em outras linguagens):
   - [x] O laço incrementa `K` e adiciona o valor de `K` a `SOMA` até que `K` seja igual a `INDICE`.
   
2. [x] Calcule o valor final de `SOMA` manualmente ou com uma ferramenta de simulação.

3. [x] Verifique o resultado e garanta que está correto. 

---

## Tarefa 2: Verificação de Número na Sequência de Fibonacci

**Descrição:**
Escreva um programa para verificar se um número informado pertence à sequência de Fibonacci.

**Checkpoints:**

1. **Implementação da Sequência de Fibonacci:**
   - [x] Crie uma função para gerar a sequência de Fibonacci até o número informado ou até que o número seja encontrado.

2. **Entrada do Usuário:**
   - [x] Implemente a entrada do número, seja através de input do usuário ou uma variável pré-definida.

3. **Verificação de Pertencimento:**
   - [x] Compare o número informado com os valores gerados na sequência de Fibonacci.

4. **Mensagem de Resultado:**
   - [x] Imprima uma mensagem indicando se o número pertence ou não à sequência de Fibonacci.

---

## Tarefa 3: Análise de Faturamento Diário

**Descrição:**
Crie um programa que analise um vetor com valores de faturamento diário e determine:
- O menor e o maior valor de faturamento.
- O número de dias em que o faturamento diário foi superior à média mensal.

**Checkpoints:**

1. **Importação dos Dados:**
   - [x] Leia o vetor de faturamento diário a partir de um arquivo JSON ou XML.

2. **Cálculo dos Valores:**
   - [x] Calcule o menor e o maior valor de faturamento.
   - [x] Calcule a média mensal considerando apenas os dias com faturamento.

3. **Contagem dos Dias Acima da Média:**
   - [x] Conte o número de dias em que o faturamento foi superior à média mensal.

4. **Resultado:**
   - [x] Imprima os resultados obtidos.

---

## Tarefa 4: Cálculo da Representação Percentual por Estado

**Descrição:**
Calcule o percentual de representação de cada estado no valor total mensal da distribuidora.

**Dados:**
- SP – R$67.836,43
- RJ – R$36.678,66
- MG – R$29.229,88
- ES – R$27.165,48
- Outros – R$19.849,53

**Checkpoints:**

1. **Cálculo do Valor Total:**
   - [ ] Some os valores de faturamento dos estados e o valor "Outros".

2. **Cálculo do Percentual:**
   - [ ] Calcule o percentual de cada estado em relação ao valor total.

3. **Resultado:**
   - [ ] Imprima o percentual de representação de cada estado.

---

## Tarefa 5: Inversão de String

**Descrição:**
Escreva um programa que inverta os caracteres de uma string.

**Checkpoints:**

1. **Entrada da String:**
   - [x] Implemente a entrada da string, seja através de input do usuário ou uma variável pré-definida.

2. **Inversão dos Caracteres:**
   - [x] Desenvolva um algoritmo para inverter a string sem usar funções prontas, como `reverse`.

3. **Resultado:**
   - [x] Imprima a string invertida.
