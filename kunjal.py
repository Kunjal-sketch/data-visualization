# -*- coding: utf-8 -*-
"""Kunjal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10rqrSfXQLSTqVZv4W_tDtYCCrzLvzTr8
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# %matplotlib inline

pokemon = pd.read_csv('/content/pokemon.csv')
print(pokemon.shape)
pokemon.head()

"""Bar Charts"""

sb.countplot(data = pokemon, x = 'generation_id');

base_color = sb.color_palette()[0]
sb.countplot(data = pokemon, x = 'generation_id', color = base_color)

base_color = sb.color_palette()[1]
gen_order = pokemon['generation_id'].value_counts().index
sb.countplot(data = pokemon, x = 'generation_id', color = base_color, 
              order = gen_order)

"""**Additional variables**"""

base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, x = 'type_1', color = base_color)

base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, x = 'type_1', color = base_color)
plt.xticks(rotation=90);

base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, y = 'type_1', color = base_color)

""" **count missing data**"""

pokemon.isna().sum()

na_counts = pokemon.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation=90);

"""**Pie Chart**"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# %matplotlib inline

df = pd.read_csv('/content/pokemon.csv')
print(df.shape)
df.head()

# code for the pie chart seen above
sorted_counts = df['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square');

"""**Additional Variation**"""

sorted_counts = df['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square');

"""**Histograms**"""

plt.hist(data = df, x = 'speed')

plt.hist(data = df, x = 'speed', bins = 20)

bins = np.arange(0, df['speed'].max()+1, 5)
plt.hist(data = df, x = 'speed', bins = bins)

plt.figure(figsize = [10, 5]) # larger figure size for subplots

# histogram on left, example of too-large bin size
plt.subplot(1, 2, 1) # 1 row, 2 cols, subplot 1
bin_edges = np.arange(0, df['speed'].max()+1, +5)
plt.hist(data = df, x = 'speed', bins = bin_edges);

# histogram on right, example of too-small bin size
plt.subplot(1, 2, 2) # 1 row, 2 cols, subplot 2
bin_edges = np.arange(0, df['speed'].max()++1, 1)
plt.hist(data = df, x = 'speed', bins = bin_edges);

"""**Alternative Approach**"""

sb.distplot(df['speed']);

sb.distplot(df['speed'], kde=False);

bin_edges = np.arange(0, df['speed'].max()+1, 5)
sb.distplot(df['speed'], bins = bin_edges, kde = False,
            hist_kws = {'alpha' : 1});