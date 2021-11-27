


moeda = [100,50,10,5,1]
sol = []
soma = 0
troco = 20

i = 0

while i < len(moeda) and soma !=troco:
    if soma + moeda[i] <= troco:
        sol.append(moeda[i])
        soma+=moeda[i]
    else:
        i+=1

print(sol)