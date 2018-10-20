#Pg=EI-rI²
#Pu=VI
#n=Pu/Pg

r=[0.00000000001, 20, 40, 60, 80, 100, 200, 400, 600, 800, 100]
v=[0, 1.667, 2.857, 3.75, 4.444, 5, 6.667, 8, 8.571, 8.889, 9.091]
i=[0, 0.08333, 0.071426, 0.0625, 0.055556, 0.05, 0.0333333, 0.020, 0.014286, 0.01111, 0.009091]
V=10


calPu = [(a*b) for a, b in zip(v,i)]
    
print("Resultado Pu :")
print("\n", calPu)
print("--------")

for x in v:
    n=x/V
    print("Resultado n :")
    print(n)
    print("--------")

for y in r:
    puMax=(V*V)/(4*y)
    print("Resultado Potência Máxima :")
    print(puMax)
    print("--------")

#a = []
#for y in range(len(r)):
#    a.append(r[y]*(i[y]**2))
    # for x in i:
    #     res=i*i
    #     p1=V*i    
    # final=p1-(r*res)
    # print("Resultado ", y)
    # print(final)    
    # print("--------")

