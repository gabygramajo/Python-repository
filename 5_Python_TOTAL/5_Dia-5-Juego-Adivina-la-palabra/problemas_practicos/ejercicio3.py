def se_repite_cero(*args):
    for i in range(0, len(args)-1):
        if args[i] == args[i+1]:
            return True
    return False

print(se_repite_cero(5,6,1,0,0,9,3,5)) #>>> True
print(se_repite_cero(6,0,5,1,0,3,0,1)) #>>> False
print(se_repite_cero(6,0,5,1,0,3,0,0,1)) #>>> True
print(se_repite_cero(6,0,5,1,0,3,3,0,0)) #>>> True
print(se_repite_cero(0,0,5,1,0,3,0,1)) #>>> True