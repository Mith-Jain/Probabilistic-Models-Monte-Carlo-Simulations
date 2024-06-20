import random 
import math
from matplotlib import pyplot as plt
n = int(input('Enter half of total number of creatures in the population'))
p = int(input('Enter the probablity of choosing the allene type A'))
l1 = ['Gene 1' for i in range(p)]
l2 = ['Gene 2' for i in range(2*n - p)] #This changes the probability distribution to include the bias of the allenes in the diploidy
l = l1 + l2 #Current population distribution
frequencylist = [0 for i in range(2*n + 1)] #To store the probabilites of p allenes of Gene 1 at the pth index
for j in range(1000000):
    newgen = [] #Next generation
    for i in range(2*n):
        newgen.append(random.choice(l))
    count = newgen.count('Gene 1')
    frequencylist[count] += 1 #Incrementing the relevant 
for i in range(2*n + 1):
    frequencylist[i] /= 1000000 #Divide by number of steps
print(frequencylist)
X = [i for i in range(2*n + 1)]
actual = [(math.factorial(2*n)/(math.factorial(i) * math.factorial(2*n - i) * math.pow(2*n, 2*n)) * math.pow(p,i) * math.pow(2*n - p,2*n - i)) for i in range(2*n + 1)]
#Actual formula for Wright model
plt.subplot(1,2,1)
plt.plot(X,frequencylist,'b-')
plt.xlabel('Number of creatures of Allene A in the next generation')
plt.ylabel('Probability found using Monte Carlo estimation')
plt.subplot(1,2,2)
plt.plot(X,actual,color = 'orange')
plt.xlabel('Number of creatures of Allene A in the next generation')
plt.ylabel('Probability using Wright model formula')
plt.show()

