import numpy as np

#1.Generate 100 random numbers between 1 and 100

data = np.random.randint(1,101,100)
#here 100 is total numbers

print("Random Numbers\n", data)

#2.Calculate Statistics

mean_value = np.mean(data)
median_value = np.median(data)
std_value = np.std(data)
variance_value = np.var(data)

#Standard Deviation
#--------------------
# Measures:how far numbers are from the mean
# Small std → numbers are close
# Large std → numbers are very spread
#standard devaition is used for Real world interpretation 
#-------------------------

#Variance:Square of standard deviation,Shows mathematical spread of data
#Variance = (Std Dev)²
#variance is used for Mathematical Calculations




print("\n📊 STATISTICS RESULT")
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)
print("Variance:", variance_value)

