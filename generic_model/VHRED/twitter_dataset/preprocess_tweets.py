import pandas as pd
import numpy as np
import math


list_floats = list(np.linspace(0,300,301))
list_ints = [int(i) for i in list_floats]
df = pd.read_csv('tweets_test_final.csv', skip_blank_lines=True, names=list_ints, dtype=str)
df.fillna('', inplace=True)

print(df.shape)


for i in range(df.shape[0]):
    print("Preprocessing Context: " + str(i) + " of " + str(df.shape[0]))
    for j in range(df.shape[1]):
        if df.loc[i, j] != "":
            df.loc[i, j] = " ".join(filter(lambda x:x[0] != '@', df.loc[i,j].split()))
            df.loc[i, j] = '</s>' + df.loc[i, j] + '</s>'

f = open('preprocessed_twitter_data.txt', 'w')
print("Opened file!")
for i in range(df.shape[0]):
    j=0
    context = ''
    while(df.loc[i, j] != ""):
        context = context + df.loc[i, j]
        j=j+1
    context = context + '\n'
    print("Writing Context: " + str(i) + " of " + str(df.shape[0]) + " to file!")
    f.write(context)


f.close()