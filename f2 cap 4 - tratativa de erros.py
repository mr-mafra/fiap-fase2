#!/usr/bin/env python
# coding: utf-8

# # Execução de exceções:
# -- Execuções anomalas;
# 

# In[ ]:


#Estrutura básica:

try:
    print("Something here")
#Também é possível usar o except sem indicar um tipo de erro especifico para tratamento, mas pode atrapalhar na hora de identificar a causa raiz.
except ValueError:
    print("Value Error: Trata tipos de exceções que contenham falhas de valor.?")
    print("Alem deste valor, temos vários outros: Sendo eles: ...")
    #ValueError: Valor string é um tipo valido mas não é o tipo de valor esperado. Pode ocorrer também em funções
else:
    print("Só será executado se o código do try rodar sem erros")
finally:
    print("Sempre será executado independente de ter dado erro ou não")


# In[6]:


#Exemplos:
try:
    idade = int(input("Por favor, insira a idade do aluno: "))
except ValueError:
    print("Tenta de novo zeba!")
else:
    print(f"A idade do aluno é de {idade}")
finally:
    print("Valeu por tentar usar este programa!")


# In[7]:


#outro exemplo 2:
try:
    idade = int(input("Por favor, insira a idade do aluno: "))
    # Este é um exemplo de type error: Onde houve uma operação/ função com tipos inapropriados, gerando um erro.
    idade_a = input("Digite a idade do seu parça: ")
    idade_total = idade + idade_a
except ValueError:
    print("Tenta de novo zeba!")
else:
    print(f"Idade do aluno: {idade}")
    print(f"Idade do amigo do aluno: {idade_a}")
    print(f"Soma da idade dos colegas: {idade_total}")
finally:
    ("Foi bom rodar em vocÊ!")


# In[8]:


#Como tratar o exemplo 2:

#outro exemplo:
try:
    idade = int(input("Por favor, insira a idade do aluno: "))
    # Este é um exemplo de type error: Onde houve uma operação com tipos diferentes (Incompativeis), gerando um erro.
    idade_a = input("Digite a idade do seu parça: ")
    idade_total = idade + idade_a
except ValueError:
    print("Tenta de novo zeba!")
except TypeError:
    print(f"O programador esqueceu de tratar um valor! ")
else:
    print(f"Idade do aluno: {idade}")
    print(f"Idade do amigo do aluno: {idade_a}")
    print(f"Soma da idade dos colegas: {idade_total}")
finally:
    ("Foi bom rodar em vocÊ!")


# In[9]:


#exemplo 3: (erro genérico>)
try:
    idade = int(input("Por favor, insira a idade do aluno: "))
    # Este é um exemplo de type error: Onde houve uma operação com tipos diferentes (Incompativeis), gerando um erro.
    idade_a = input("Digite a idade do seu parça: ")
    #Erro forçado propositalmente para cair na última exceção:
    idade_total = 5/0
except ValueError:
    print("Tenta de novo zeba!")
except TypeError:
    print(f"O programador esqueceu de tratar um valor! ")
#Trata erros genéricos:
except Exception as error:
    print(f"Aqui está um erro inesperado forçado: {error}")
else:
    print(f"Idade do aluno: {idade}")
    print(f"Idade do amigo do aluno: {idade_a}")
    print(f"Soma da idade dos colegas: {idade_total}")
finally:
    ("Foi bom rodar em vocÊ!")


# In[18]:


#Construindo a minha própria classe de erro:
class IdadeMaximaExcedida (Exception):
    #Método especial que define um objeto string para minha classe
    def __str__(self):
        return "Idade invalida, a idade não pode ser maior que 125 anos"




#Exemplo 4: Criando erros personalizados:
try:
    idade = int(input("Por favor, insira a idade do aluno: "))
    if(idade < 0):
        #FOrçando a aplicação a apresentar um erro, com uma mensagem sobrescrita (artificialmente, substituindo apenas o texto apresentado)
        raise ValueError("Personalizando meu erro para idade abaixo de 0")
    elif idade > 125:
        raise IdadeMaximaExcedida
except ValueError as error:
    print(f"Tenta de novo zeba! deu erro: {error}")
#except Exception as error:
    #print(f"Erro {error}")
##Utilizando um except com a minha classe:
except IdadeMaximaExcedida as error:
    print(f"Você digitou uma idade invalida, erro: {error}")
else:
    print(f"A idade do aluno é de {idade} anos")


# In[ ]:


#Hands On:

try:
    vlTotal = float(input("Digite o valor total da compra: R$ "))
    qtdItens = int(input("Digite a quantidade total de itens: "))
    media = round(vlTotal/qtdItens)
except ValueError: 
    print("Entre com um número para realizar o cálculo")
except ZeroDivisionError:
    print("Não é possível dividir por zero, entre com pelomenos 1 item.")
except Exception as error:
    print(f"Erro identificado: {error}")
else:
    print(f"O valor médio dos itens é de R$ {media}")
finally:
    print("Obrigado por executar o programa!")


# In[22]:


#Criando minha classe personalizada por conta:

class ValorNegativo(Exception):
    def __str__(self):
        return "Número negativo invalido! O valor não pode ser negativo. (¬ ¬) Zeba!"

try:
    vlTotal = float(input("Digite o valor total da compra: R$ "))
    qtdItens = int(input("Digite a quantidade total de itens: "))
    media = round(vlTotal/qtdItens)
    if vlTotal < 0 or qtdItens < 0:
        raise ValorNegativo 
except ValueError: 
    print("Entre com um número para realizar o cálculo\n")
except ZeroDivisionError:
    print("Não é possível dividir por zero, entre com pelomenos 1 item.\n")
except Exception as error:
    print(f"Erro identificado: {error}")
else:
    print(f"O valor médio dos itens é de R$ {media}")
finally:
    print("Obrigado por executar o programa!")


# In[ ]:




