
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.inf)

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson sampling ( Ni_n = number of rewards for n )
import random
N = 10000
d = 10
ads_selected = []
Ni_1 = [0] * d 
Ni_0 = [0] * d 
total_reward = 0
for n in range(0,N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(Ni_1[i] + 1 , Ni_0[i] + 1)
        if(random_beta > max_random): 
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if (reward == 1):
        Ni_1[ad] = Ni_1[ad] + 1
    else:
        Ni_0[ad] = Ni_0[ad] + 1   
    total_reward = total_reward + reward 
   
# Visualizing the results
plt.hist(ads_selected)
plt.title('Histogram of ads')
plt.xlabel('Ads')
plt.ylabel('Number of times the ads were selected')
plt.show()    
    