from matplotlib import pyplot as plt
import numpy as np 

blood_sugar_men = [113,85,90,150,149,88,93,115,135,80,77,82,129]
blood_sugar_women = [67,98,89,120,133,150,84,69,89,79,120,112,100]

plt.hist(blood_sugar_men) # by default hist will create 10 bins
plt.show()

plt.hist(blood_sugar_men,bins=3,rwidth=0.95) #rwidth = relative width
plt.show()

#Customer Bins size (80--100,  100--125, above 125 and less than 150)
plt.hist(blood_sugar_men,bins=[80,100,125,150],rwidth=0.95,color='green') 
plt.show()

# Display sugar levels of Men and Women
plt.hist([blood_sugar_men,blood_sugar_women],bins=[80,100,125,150],rwidth=0.95,
	color=['green','orange'],label=['men','women']) 
plt.legend()
plt.xlabel('Sugar Range')
plt.ylabel('Frequency')
plt.title("Blood Sugar Analysis")
plt.show()

# Display sugar levels of Men and Women horizontally
plt.hist([blood_sugar_men,blood_sugar_women],bins=[80,100,125,150],rwidth=0.95,
	color=['green','orange'],label=['men','women'],orientation='horizontal') 
plt.legend()
plt.xlabel('Frequency')
plt.ylabel('Sugar Range')
plt.title("Blood Sugar Analysis")
plt.show()