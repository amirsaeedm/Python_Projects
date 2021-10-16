from matplotlib import pyplot as plt
import numpy as np 

company=['Google','Amazon','Microsoft','Facebook'] # Company name
revenue=[90,136,89,27] # Revenue
profit=[40,2,34,12] # profits

plt.bar(company,revenue,label="Revenue")
plt.bar(company,profit,label="Profits")
plt.xlabel('Company')
plt.ylabel('Revenue (bn)')
plt.title('US Tech Stocks')
plt.legend()
plt.show()

# to make a histogram
xpos = np.arange(len(company)) 

plt.xticks(xpos,company)
plt.bar(xpos-0.2,revenue,width=0.4,label="Revenue")
plt.bar(xpos+0.2,profit,width=0.4,label="Profits")
plt.xlabel('Company')
plt.ylabel('Revenue (bn)')
plt.title('US Tech Stocks')
plt.legend()
plt.show()

# horizontal bar chart
plt.barh(company,revenue,label="Revenue")
plt.barh(company,profit,label="Profits")
plt.xlabel('Revenue (bn)')
plt.ylabel('Company')
plt.title('US Tech Stocks')
plt.legend()
plt.show()