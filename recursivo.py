def soma_recursiva (numero):
    if numero == 0 :
        return 0
    return numero -soma_recursiva(numero - 1)
print (soma_recursiva(5))

