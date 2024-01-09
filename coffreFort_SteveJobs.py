'''Coffre fort
Trouver le code à 4 chiffres du coffre-fort
'''
def code_bon(m,c,d,u):
    rep = m%2==0 and m+c==15 and d==c-m and m==u*d
    return rep

def decomposer(nb):
    u=nb%10
    d=int(nb/10)%10
    c=int(nb/100)%10
    m=int(nb/1000)%10
    return(m,c,d,u)

