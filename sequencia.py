def sequencia(lista,itens_restantes):
    if len(itens_restantes) == 0:
        return len(lista)
    else:
        itens_restantes_ = itens_restantes[:]
        del(itens_restantes_[0])
        if len(lista) > 0:
            print(lista)
            if lista[len(lista) - 1] < itens_restantes[0]:
                return max(sequencia(lista.append(itens_restantes[0]),itens_restantes_) + 1,sequencia(lista, itens_restantes_))
            else:
                return sequencia(lista, itens_restantes_)

print(sequencia([],[1,2,7,8,3]))

