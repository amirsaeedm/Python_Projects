from matplotlib import pyplot as plt

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

plt.plot(x,y, color='green', linewidth=5,linestyle='dotted')
plt.xlabel('day')
plt.ylabel('weather')
plt.title("Day wise weather")
plt.show()