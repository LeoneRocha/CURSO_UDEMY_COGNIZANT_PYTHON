# Ask for the distance.
distancia = input('Quão longe você gostaria de viajar em milhas? ')
# Convert the distance to an integer.
distancia = int(distancia)
# Determine what mode of transport to use.
if distancia < 3:
    modo_de_transporte = 'pode ir andando'
elif distancia < 300:
    modo_de_transporte = 'pode ir dirigindo'
else:
    modo_de_transporte = 'melhor ir voando'
# Display the result.
print('Eu sugiro {} para voce ir ao destino.'.format(modo_de_transporte))