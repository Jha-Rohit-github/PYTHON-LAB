"""1.Calculate the total revenue generated by two product categories in a store 

Input: category1_revenue = np.array([500, 600, 700, 550]) 

category2_revenue = np.array([450, 700, 800, 600]) 

Output: Total Revenue: [ 950 1300 1500 1150] """

import numpy as np

# Input arrays
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate total revenue
total_revenue = category1_revenue + category2_revenue

# Output
print("Total Revenue:", total_revenue)


#output: Total Revenue: [ 950 1300 1500 1150]
