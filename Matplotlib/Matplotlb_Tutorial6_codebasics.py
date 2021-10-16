from matplotlib import pyplot as plt
import numpy as np 

exp_vals = [1400,600,300,410,250]
exp_labels = ["Home Rent","Food","Phone/Internet Bill","Car","Other Utilities"]

# plt.pie(exp_vals,labels=exp_labels,radius=1.5,) # Radius = chart size
# plt.axis("equal")
# plt.show()

# # Show percentages in pie chart
# plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%f%%') # Radius = chart size
# plt.axis("equal")
# plt.show()

# # Format Percentage values
# plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.1f%%') # Radius = chart size
# plt.axis("equal")
# plt.show()

# # Exlode a specific Pie
# plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.1f%%',explode=[0,0,0.5,0,0]) # Radius = chart size
# plt.axis("equal")
# plt.show()

# Rotate Pie Chart based on First label
plt.pie(exp_vals,labels=exp_labels,radius=1.5,autopct='%0.1f%%',
		explode=[0,0,0.5,0,0],startangle=80) # Radius = chart size
plt.axis("equal")
plt.show()

plt.savefig("piechart.png",bbox_inches='tight',pad_inches=1)