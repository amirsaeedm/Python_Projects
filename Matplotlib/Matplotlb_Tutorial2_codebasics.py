from matplotlib import pyplot as plt

x=[1,2,3,4,5,6,7] # Days
y=[50,51,52,48,47,49,46] # Temperature

# plt.plot(x,y, 'g+')
# plt.xlabel('day')
# plt.ylabel('weather')
# plt.title("Day wise weather")
# plt.show()

# plt.plot(x,y, '--r*')
# plt.xlabel('day')
# plt.ylabel('weather')
# plt.title("Day wise weather")
# plt.show()

# plt.plot(x,y, 'rD--')
# plt.xlabel('day')
# plt.ylabel('weather')
# plt.title("Day wise weather")
# plt.show()

# plt.plot(x,y, color='red',marker='D',linestyle='--',markersize=10) # or plt.plot(x,y, 'rD--')
# plt.xlabel('day')
# plt.ylabel('weather')
# plt.title("Day wise weather")
# plt.show()

plt.plot(x,y, color='red', alpha=0.25) # Alpha controls transparency of line
plt.xlabel('day')
plt.ylabel('weather')
plt.title("Day wise weather")
plt.show()