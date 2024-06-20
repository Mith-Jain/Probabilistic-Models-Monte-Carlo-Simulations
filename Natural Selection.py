import random 
from matplotlib import pyplot as plt
fast_creatures = []
slow_creatures = []
food = []
locality = []
locality_size = 500
fc_ini = 4
sc_ini = 80
food_ini = 200
hunger_tolerance = 20
food_loop_time = 10
food_loop_amount = 40
speed_ratio = 3

def creation():
    global locality
    global fast_creatures
    global slow_creatures
    global food
    locality = [0 for i in range(locality_size + 1)]
    fast_creatures = []
    slow_creatures = []
    food = []
    j = 0
    while(j <= food_ini):
        t = random.randint(0,locality_size)
        if locality[t] == 0:
            locality[t] = 'food'
            food.append(t)
            j += 1
    j = 0
    while(j <= fc_ini):
        t = random.randint(0,locality_size)
        if locality[t] == 0:
            fast_creatures.append([t,random.choice([-1,1]),0,0])
            j += 1
    j = 0
    while(j <= sc_ini):
        t = random.randint(0,locality_size)
        if locality[t] == 0:
            locality[t] = 'Slow Creatures'
            slow_creatures.append([t,random.choice([-1,1]),0,0])
            j += 1
    for i in slow_creatures:
        locality[i[0]] = 0
    for i in slow_creatures:
        locality[i[0]] = 0
fc = [0 for i in range(101)]
sc = [0 for i in range(101)]
fc[0] = fc_ini
sc[0] = sc_ini
for _ in range(10000):
    creation()
    t = 0
    while(t <= 100):
        for i in fast_creatures:
            if i[3] == hunger_tolerance:
                fast_creatures.remove(i)
            i[3] += 1
            if i[0] == 0:
                i[1] = 1
            elif i[0] == locality_size:
                i[1] = -1 
            i[0] += i[1]
            if locality[i[0]] == 'food':
                locality[i[0]] = 0
                food.remove(i[0])
                if i[2] == 0:
                    i[2] = 1
                    i[3] = 0
                else:
                    i[2] = 0
                    i[3] = 0
                    fast_creatures.insert(0,[i[0],random.choice([-1,1]),0,0])
            '''if i[2] == 2:
                i[2] = 0
                i[3] = 0
                fast_creatures.insert(0,(i[0],random.choice([-1,1],0)))'''
        for i in slow_creatures:
            if i[3] == hunger_tolerance:
                slow_creatures.remove(i)
            i[3] += 1
            if t % speed_ratio == 0:
                if i[0] == 0:
                    i[1] = 1
                elif i[0] == locality_size:
                    i[1] = -1 
                i[0] += i[1]
                if locality[i[0]] == 'food':
                    locality[i[0]] = 0
                    food.remove(i[0])
                    if i[2] == 0:
                        i[2] = 1
                        i[3] = 0
                    else:
                        i[2] = 0
                        i[3] = 0
                        slow_creatures.insert(0,[i[0],random.choice([-1,1]),0,0])
        fc[t] += len(fast_creatures)
        sc[t] += len(slow_creatures)
        t += 1
        if t % (food_loop_time) == 0:
            z = 0
            while(z <= food_loop_amount):
                r = random.randint(0,locality_size)
                if locality[r] == 0:
                    locality[r] = 'food'
                    food.append(r)
                    z += 1
        
        
for i in range(len(fc)):
    fc[i] /= 10000
for j in range(len(sc)):
    sc[j] /= 10000
x = [i for i in range(0,101)]
plt.plot(x,fc,x,sc)
plt.legend(['Fast creatures','Slow Creatures'])
plt.xlabel('Time in days')
plt.ylabel('Number of creatures')
plt.show()

        








