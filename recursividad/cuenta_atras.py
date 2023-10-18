def cuenta_atras(n):
    if n<0:
        print ("fin")
    else:
        print(n)
        n=n-1
        cuenta_atras(n)

cuenta_atras(5)