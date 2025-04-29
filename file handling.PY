# with open ("TEXT.txt", 'w') as f:
#     f.write("\n I like video games")

#with open ("TEXT.txt", "r") as f:
 #   content = f.read()
  # print(content)


# with open ("data.csv", "r") as f:
#     c = f.read()
#     #print(c)


#     ## add new row to the csv file
# with open ("data.csv", "a") as obj:
#     obj.write("\nOla,50,delta")


#import numpy as np
# Load data from a csv file
#data = np.genfromtxt("data.csv", dtype=None, delimiter=",", usecols=2 )
#print(data)


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
print(f"\nthe median is: [median]")

std = np.std(array)
print(f"\nthe std is:[std]")

max = np.max(array)
print("f\nthe max is: [max]")

min = np.min(array)
print("f\nthe min is: [min]")

var= np.var(array)
print("f\nthe var is: [var]")












































































