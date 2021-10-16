import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 


# Plot two lines in one chart wiuth legends
# x = [1,2,3]
# y = [1,4,9]
# z = [10,8,3]
# plt.plot(x,y)
# plt.plot(x,z)
# plt.title("Test Plot")
# plt.xlabel("x")
# plt.ylabel("y and z")
# plt.legend(["This is y","This is z"])
# plt.show()

# sample_data = pd.read_csv("D:/Python_Projects/Charts in PyQt5/sample_data.csv")
countries = pd.read_csv("D:/Python_Projects/Charts in PyQt5/countries.csv")

us = countries[countries.country == "United States"]
china = countries[countries.country == "China"]
pakistan = countries[countries.country == "Pakistan"]
india = countries[countries.country == "India"]

plt.plot(us.year, us.population)
plt.plot(china.year, china.population)
plt.plot(pakistan.year, pakistan.population)
plt.plot(india.year, india.population)
plt.title("Year wise Population")
plt.xlabel("Year")
plt.ylabel("Population growth (first year = 100)")
plt.legend(["USA", "China","Pakistan","India"])
plt.show()

plt.plot(us.year, us.population / us.population.iloc[0]*100)
plt.plot(china.year, china.population / china.population.iloc[0]*100)
plt.plot(pakistan.year, pakistan.population / pakistan.population.iloc[0]*100)
plt.plot(india.year, india.population / india.population.iloc[0]*100)
plt.title("Year wise Population")
plt.xlabel("Year")
plt.ylabel("Population growth (first year = 100)")
plt.legend(["USA", "China","Pakistan","India"])
plt.show()