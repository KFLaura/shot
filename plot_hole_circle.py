import numpy as np
import matplotlib.pyplot as plt 
import math



# create random points
random_shot = 30
random_x = np.random.uniform(-1.0,1.0, random_shot)
random_y = np.random.uniform(-1.0,1.0, random_shot)

# init empty containers
red_out_of_circle_x = []
red_out_of_circle_y = []

green_within_or_on_circle_x = []
green_within_or_on_circle_y = []

# compute
a  = np.array((0,0))

for i in range(random_shot): 
    b = np.array((random_x[i], random_y[i]))
    
    distance = np.linalg.norm(b)
    

    # fallunterscheidung
    if distance > 1.0:
        red_out_of_circle_x.insert(0, random_x[i])
        red_out_of_circle_y.insert(0, random_y[i])
       
    else: 
        green_within_or_on_circle_x.insert(0, random_x[i])
        green_within_or_on_circle_y.insert(0, random_y[i])
        
    

#y-value of circleline 
y_value_1 = []

for i in range(-100, 101):
    x = i/100
    if i == 0.0:
        y = 1.0 
    else: 
        y = math.sqrt(1.0-x**2.0)

    y_value_1.append(y)


y_value_2 = []
for i in range(-100, 101):
    x = i/100
    if i == 0.0:
        y = -1.0
    else: 
        y = -math.sqrt(1.0-x**2.0)
    y_value_2.append(y)



#x-value of circleline
x_value_1 = []
for i in range(-100, 101):
    x = i/100
    x_value_1.append(x)


x_value_2 = []
for i in range(-100, 101):
    x = i/100
    x_value_2.append(x)



#set length of axis to 1 & set the diagram to be square 
fig = plt.figure()
ax = fig.add_subplot()

plt.plot(x, y)
plt.xlim(-1.0, 1.0)
plt.ylim(-1.0, 1.0)


ax.set_aspect("equal", adjustable="box")


#create scatter
plt.scatter(red_out_of_circle_x, red_out_of_circle_y, c = 'red', s = 8)
plt.scatter(green_within_or_on_circle_x, green_within_or_on_circle_y, c = 'green', s = 8)


#create circleline  
plt.plot(x_value_1, y_value_1, color = 'green',  linewidth = 4)

plt.plot(x_value_2, y_value_2, color = 'green',  linewidth = 4)


#create area filling 
filling_x_1 = x_value_1
filling_y_1 = y_value_1

filling_inside = plt.fill_between(filling_x_1, filling_y_1, color = 'green', alpha = 0.15)
filling_ouside = plt.fill_between(x_value_1, y_value_1, np.max(1), color = 'red', alpha = 0.15)

filling_x_2 = x_value_2
filling_y_2 = y_value_2

filling_inside = plt.fill_between(filling_x_2, filling_y_2, color = 'green', alpha = 0.15)
filling_ouside = plt.fill_between(x_value_2, y_value_2, np.max(-1), color = 'red', alpha = 0.15)

# create label of the total number off shots 
plt.title("Anzahl Schüsse insg.: " + str(random_shot), family="serif", color="black", weight="normal", size=14)



#compute probability of hits in percent rounded to second decimal place
percent_hits = (len(green_within_or_on_circle_x)*100)/random_shot
percent_hits_rounded = round(percent_hits, 2)


#compute probability of loost shots in percent roundet to second decimal place 
percent_lost = (len(red_out_of_circle_x)*100)/random_shot
percent_lost_rounded = round(percent_lost, 2)




#labeling at the bottom of the plot 
plt.xlabel("Anzahl Treffer: " + str(len(green_within_or_on_circle_x)) + "  (" + str(percent_hits_rounded) +  "%" " ) " + "     Anzahl Nieten: " + str(len(red_out_of_circle_x)) + "  (" + str(percent_lost_rounded) +  "%" " ) ", family="serif", color="black", weight="normal", size=11, labelpad=10)


#Show the plot
plt.show()


#create pdf file that is showing the plot
plt.savefig('line_plot_hole.pdf')   



