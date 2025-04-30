
import numpy as np
# with open ("loan.csv","r") as f:
#     data = f.read()
data = np.genfromtxt("loan.csv",delimiter=",", usecols=8,filling_values=0)
#    # print(data)


# create a 1D array
array= np.array(data)


#calculate the mean of the array
mean= np.mean(array)
print(f"the mean is: {mean}")


median= np.median(array)
print(f"the median is: {median}")

std = np.std(array)
print(f"the std is:{std}")

max = np.max(array)
print(f"the max is: {max}")

min = np.min(array)
print(f"the min is: {min}")

var= np.var(array)
print(f"the var is: {var}")












































































