import numpy as np
import matplotlib.pyplot as plt 
from statistics import mean




# create random points 
random_shot = 400

random_x = np.random.uniform(-1.0,1.0, random_shot)
random_y = np.random.uniform(-1.0,1.0, random_shot)

# init empty containers
red_out_of_circle_x = []
red_out_of_circle_y = []

green_within_or_on_circle_x = []
green_within_or_on_circle_y = []



true_or_false = []

# compute

a  = np.array((0,0))

for i in range(random_shot): 
    b = np.array((random_x[i], random_y[i]))
    
    distance = np.linalg.norm(b)
    
    # fallunterscheidung
    if distance > 1.0:
        red_out_of_circle_x.insert(0, random_x[i])
        red_out_of_circle_y.insert(0, random_y[i])
        true_or_false.append(0)
   
    else: 
        green_within_or_on_circle_x.insert(0, random_x[i])
        green_within_or_on_circle_y.insert(0, random_y[i])
        true_or_false.append(1)
        


enumeration_number_true_or_false = [] 
zähler = 0

for i in range(len(true_or_false)): 
    zähler = zähler + 1 
    enumeration_number_true_or_false.append(zähler)
    

array_true_o_false = np.array(true_or_false)
array_true_o_false_length = len(true_or_false)
cumulative_total = np.cumsum(array_true_o_false)


array_enumeration_number_true_or_false = np.array(enumeration_number_true_or_false)


dividing = np.divide(cumulative_total, array_enumeration_number_true_or_false)



#calculating average of dividing 
def mean(dataset):
    return sum(dataset) / len(dataset)



x_value = []
for i in range(0, len(dividing)+1):
    x = i/1
    x_value.append(x)



mittelwert = []
for i in range(len(x_value)): 
    mittelwert.append(mean(dividing))




#set length of axis 
fig = plt.figure()
ax = fig.add_subplot()

plt.plot(array_enumeration_number_true_or_false, dividing, color = "black", linewidth = 1.5)
plt.plot(x_value, mittelwert, linestyle = "dotted", color = "blue", linewidth = .8)
#plt.fill_between(array_enumeration_number_true_or_false, dividing, alpha = 0.5)
plt.xlim(0, random_shot)
plt.ylim(0, 1.0)


rounded_mittwelwert = round(mean(dividing), 2)



#labeling at the bottom of the plot 
plt.xlabel("Anzahl Schüsse: " + str(random_shot) + "  Mittelwert: " + str(rounded_mittwelwert), family="serif", color="black", weight="normal", size=13, labelpad=10)


plt.savefig('sandbox.pdf')  

