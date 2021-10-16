from matplotlib import pyplot as plt

days=[1,2,3,4,5,6,7] # Days
max_temp=[50,51,52,48,47,49,46] # Temperature
min_t = [43,42,40,44,33,35,37]
avg_t = [45,48,48,46,48,42,41]

# plt.plot(days,max_temp)
# plt.plot(days,min_t)
# plt.plot(days,avg_t)
# plt.xlabel('Days')
# plt.ylabel('Temperature')
# plt.title("Day wise weather")
# plt.legend(['Max Temp','Min Temp','Avg Temp'],loc="upper right")
# plt.show()

#Another way to show legends
plt.plot(days,max_temp,label="Max Temp")
plt.plot(days,min_t,label="Min Temp")
plt.plot(days,avg_t,label="Avg Temp")
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title("Day wise weather")
plt.legend(loc="upper right",shadow=True, fontsize=5)  # without loc argument it fit is to best location
plt.grid()
plt.show()


