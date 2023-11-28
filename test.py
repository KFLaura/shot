
import numpy as np
import matplotlib.pyplot as plt 
import math



# create random points
random_shot = 555
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
        
    


#set length of axis to 1 & set the diagram to be square 
fig = plt.figure()
ax = fig.add_subplot()

plt.xlim(-1.0, 1.0)
plt.ylim(-1.0, 1.0)



#create scatter
plt.scatter(red_out_of_circle_x, red_out_of_circle_y, c = 'red', s = 14)
plt.scatter(green_within_or_on_circle_x, green_within_or_on_circle_y, c = 'green', s = 14)



'''
#create circle
draw_circle = plt.Circle((0.0, 0.0), 1.0, fill = False, color = "green", linewidth = 4.25)
ax.add_artist(draw_circle)

'''


#make diagramm take shape of a box
ax.set_aspect("equal", adjustable="box")








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
plt.savefig('line_plot_test.pdf')  



