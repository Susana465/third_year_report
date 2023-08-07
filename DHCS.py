# Data Hazards Case Study (DHCS)


#| label: fig-polar
#| fig-cap: "A line plot on a polar axis"
'''
import numpy as np
import matplotlib.pyplot as plt
# The dataset:
data = {'Reinforces existing biases':2, 'High environmental impact':3,
        'Lacks community involvement':2, 'Danger of misuse':3, 'Difficult to understand':5,
        'May cause direct harm':2}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (17, 5))
 
# Creating the bar plot
plt.bar(courses, values, color ='tab:red',
        width = 0.4)
 
plt.xlabel("Data Hazard Labels")
plt.ylabel("No. of times label was chosen as relevant for my PhD project")
plt.title("Data Hazards labels that may apply to my PhD")
plt.show()
'''

https://stackoverflow.com/questions/44246650/add-image-annotations-to-bar-plots

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox

def get_flag(name):
    path = "data/flags/Flags/flags/flags/24/{}.png".format(name.title())
    im = plt.imread(path)
    return im

def offset_image(coord, name, ax):
    img = get_flag(name)
    im = OffsetImage(img, zoom=0.72)
    im.image.axes = ax

    ab = AnnotationBbox(im, (coord, 0),  xybox=(0., -16.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)
    

countries = ["Norway", "Spain", "Germany", "Canada", "China"]
valuesA = [20, 15, 30, 5, 26]
 

fig, ax = plt.subplots()

ax.bar(range(len(countries)), valuesA, width=0.5,align="center")
ax.set_xticks(range(len(countries)))
ax.set_xticklabels(countries)
ax.tick_params(axis='x', which='major', pad=26)

for i, c in enumerate(countries):
    offset_image(i, c, ax)

plt.show()