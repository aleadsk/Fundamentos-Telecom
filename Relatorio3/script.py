from math import pi, sqrt

Vrms = 10
freqs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
C = 10 * (10**(-9))
L = 10 * (10**(-3))
R = 1000

print("f\tVc\tVl\tVr\tI\tZ")

for freq in freqs:
    Xc = 1 / (2*pi*freq*1000*C)
    Xl = (2*pi*freq*1000*L)
    X = Xl - Xc

    Z = sqrt(R**2 + X**2)
    I = Vrms / Z

    Vc = (I * Xc)
    Vl = (I * Xl)
    Vr = (I * R)

    print("{};{};{};{};{};{}".format(freq, round(Vc,3), round(Vl,3), round(Vr,3), round(I*1000,3), round(Z,3)))
