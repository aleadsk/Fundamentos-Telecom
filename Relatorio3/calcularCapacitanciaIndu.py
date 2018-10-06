import sys

##frequencia=1000

##reaCapa=((1/(2*3.141526*0.01*frequencia))*1000000)

#impedancia=(((reaCapa)**(2))+((33000)**(2)))**(0.5)

#corrente=5/(impedancia)

#tensaoCapa=(corrente*reaCapa)*(2**0.5)

#tensaoResis=(corrente*33000)*(2**0.5)

#print(reaCapa)
#print(impedancia)
#print(corrente)
#print(tensaoCapa)
#print(tensaoResis)


frequencia=100000

reaIndu=(2*3.1415*frequencia*(10/1000))

impedancia=(((reaIndu)**(2))+((4700)**(2)))**(0.5)

corrente=5/(impedancia)

tensaoIndu=(corrente*reaIndu)*(2**0.5)

tensaoResist=(corrente*4700)*(2**0.5)

print(reaIndu)
print(impedancia)
print(corrente)
print(tensaoIndu)
print(tensaoResist)