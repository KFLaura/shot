
import numpy as np
import matplotlib as plt 
import math 



#create random shot
random_shot = 10

random_x = np.random.uniform(0,1.0, random_shot)
random_y = np.random.uniform(0,1.0, random_shot)




distance_test_list = []

a  = np.array((0,0))

for b in range (random_shot): 
    b = np.array(random_x[0], random_y[0])
    distance = np.linalg.norm(a - b)
    random_x = np.delete(np.array(random_x), 0)
    random_y= np.delete(np.array(random_y), 0)
    distance_test_list.insert(0, distance)


print(distance_test_list)
'''print(random_x)
print(random_y)'''

'''
red_out_of_circle = []
green_within_or_on_circle = []

for i in range(len(distance_test_list)):
    if distance_test_list[0] > 1.0:
        red_out_of_circle.insert(0, distance_test_list[0])
        distance_test_list.pop(0)
    else:
        green_within_or_on_circle.insert(0, distance_test_list[0])
        distance_test_list.pop(0)


print(distance_test_list)
print(red_out_of_circle)
print(green_within_or_on_circle)
'''

'''
#Versuch die Zufallsliste mithilfe eines Indexes zu durchlaufen 
distance_test_list = []

a  = np.array((0,0))

for index , value in enumerate(random_shot): 
    b = np.array(random_x[0], random_y[0])
    distance = np.linalg.norm(a - b)
    random_x = np.delete(np.array(random_x), 0)
    random_y= np.delete(np.array(random_y), 0)
    #distance_test_list.insert(0, distance)


print("index", index , "for value", value)
'''


'''
y_wert = []
for i in range(0, 101):
    x = i/100
    if i == 0.0:
        y = 1.0 
    else: 
        y = math.sqrt(1.0-x**2.0)

    y_wert.append(y)


x_wert = []
for i in range(0, 101):
    x = i/100
    x_wert.append(x)


test_distance_circleline = math.sqrt(x_wert[40]*x_wert[40]+y_wert[40]*y_wert[40])
'''


random_shot = 20  # datacards.consume.input.schieberegler_AnzahlTreffer()

random_x = np.random.uniform(0,1.0, random_shot)
random_y = np.random.uniform(0,1.0, random_shot)

for i in range(len(distance_test_list)-1):
    if distance_test_list[i] > 1.0:
        print()
    else:
        print(distance_test_list[i]) 
        