# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, # incidents)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

bin_inci = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28]


plt.figure(figsize=(4,7)) # change the size of the plot/figure


plt.hist(
    dataset.incidents, # input data; array or array of sequence or dataframe
    bins = bin_inci, # no. of bins/values of x-axis ; default 10;
    label = ('Incidents'), # legend values initiation to be shown in legend()
    alpha = 0.55, # transparency
    color = 'blue',
        )

plt.yscale("symlog")
plt.yticks(ticks = [0,1,10,50,100,1000,1500,2000,2500])
plt.gca().yaxis.set_major_formatter(mpl.ticker.LogFormatter())

plt.title("Frequency Distribution (Incidents)")
plt.xlabel("Incidents")
plt.ylabel("Frequency")

plt.legend() # show the initiated values from label

plt.show()
