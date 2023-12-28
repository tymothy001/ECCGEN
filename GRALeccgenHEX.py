#pip install tqdm

from libnum import ecc
import sys
from tqdm import tqdm
if __name__ == "ELIPTIC CURVE ECC GENERATOR":
    main()

print("     --------------------------------------------------------------------------------      ")
print("                                                                                           ")
print("                                                                                           ")
print("                             ELIPTIC CURVE ECC GENERATOR                                   ")
print("                                                                                           ")
print("     --------------------------------------------------------------------------------      ")
print("                                                                                           ")
print("                                                                                           ")
print("                                                                                           ")
print("                                                                                           ")





f = open("output3.txt", "a")

def printPoints(name, a, b, p, G, scale):
    print(name, file=f)
    c = ecc.Curve(a, b, p, G)
    for n in tqdm(range(1, 600), desc=f"{name} calculation"):
        res = c.power(G, n)
        x, y = res
        print(n, "", "x:", hex(x)[2:], "y:", hex(y)[2:], file=f)
    res = c.power(G, scale)
    x, y = res
    print(scale, "", "x:", hex(x)[2:], "y:", hex(y)[2:], file=f)

scale = 2
if len(sys.argv) > 1:
    scale = int(sys.argv[1])

a = 0
b = 7
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240, 32670510020758816978083085130507043184471273380659243275938904335757337482424)
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
#parametry krzywej adresu 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa i innych
#G = (46833799212576611471711417854818141128240043280360231002189938627535641370294, 33454781559405909841731692443380420218121109572881027288991311028992835919199)


printPoints("\nsecp256k1", a, b, p, G, scale)
f.close()

