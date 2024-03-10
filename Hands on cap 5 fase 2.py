#!/usr/bin/env python
# coding: utf-8

# In[12]:


def calculaPizza(tamanho = 'm',sabores = 1):
    if tamanho.lower() in ('p','pequeno','pequena'):
        preco = 20
    elif tamanho.lower() in ('m','medio','médio'):
        preco = 30
    else:
        preco = 40
    preco += (sabores-1)*5
    return preco


# In[19]:


print(calculaPizza('p',1))
print(calculaPizza('médio',1))
print(calculaPizza('médio',2))
print(calculaPizza('Grande',3))


# In[23]:


verificar_atmosfera = lambda planeta: "Ufa, pode respirar a vontade" if planeta != "Hoth" else "Cuidado! Não ouse retirar a vestimenta"
print(list(map(verificar_atmosfera, ["Tatooine", "Hoth", "Endor", "Alderaan", "Naboo"])))


# In[ ]:




