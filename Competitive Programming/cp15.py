import re

def gridSearch(G, P):

    l = len(P)
    m = len(P[0])
    for x,y in enumerate(G):
        for i in ((m.start(0)) for m in re.finditer("(?=%s)"%P[0], y)):
            for a in range(1,l):
                if G[a+x][i:i+m]!=P[a]:
                    break
            else:
                return "YES"
      
    return "NO"
                

G = ['400453592126560',
'114213133098692',
'474386082879648',
'522356951189169',
'887109450487496',
'252802633388782',
'502771484966748',
'075975207693780',
'511799789562806',
'404007454272504',
'549043809916080',
'962410809534811',
'445893523733475',
'768705303214174',
'650629270887160']
P = ['99', '99']
print(gridSearch(G, P))