def longitud(cad):
    t = len(cad)
    return t

def fecha(d,m,a):
    la = longitud(a)
    aa = ""
    for i in range(la - 2, la):
        aa+= a[i]
    
    print(d,"/",m,"/",aa)

def main():
    d = input("dia ")
    m = input("mes ")
    a = input("ano ")
    fecha(d,m,a)


if __name__ == '__main__':
    main()

