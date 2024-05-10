limiteInferior = int(input('Digite o limite inferior: '))
limiteSuperior = int(input('Digite o limite superior: '))
incremento = int(input('Digite o incremento: '))

limiteInferiorPadrao = limiteInferior
print(limiteInferiorPadrao)

while limiteSuperior > limiteInferior:
    limiteInferior += incremento
    
    if limiteSuperior < limiteInferior:
        break

    print(limiteInferior)

    

    
