# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Year, Quarter, Month, Day, Victims Injured)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

bin_kill = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,100,150]


plt.figure(figsize=(4,7)) # change the size of the plot/figure


plt.hist(
    dataset.injured_victims, # input data; array or array of sequence or dataframe
    bins = bin_kill, # no. of bins/values of x-axis ; default 10;
    label = ('Injured'), # legend values initiation to be shown in legend()
    alpha = 0.55, # transparency
    color = 'green',
        )

plt.yscale("symlog")
plt.yticks(ticks = [0,1,10,50,100,1000,1500,2000])
plt.gca().yaxis.set_major_formatter(mpl.ticker.LogFormatter())

plt.title("Frequency Distribution (People Injured)")
plt.xlabel("People Injured")
plt.ylabel("Frequency")

plt.legend() # show the initiated values from label

plt.show()
