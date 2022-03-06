import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

office_episodes = pd.read_csv('office_episodes.csv')
office_episodes.head()

colors = []
for lab, row in office_episodes.iterrows():
    if row['scaled_ratings'] < 0.25:
        colors.append('red')
    elif row['scaled_ratings'] < 0.50:
        colors.append('orange')
    elif row['scaled_ratings'] < 0.75:
        colors.append('lightgreen')
    else:
        colors.append('darkgreen')
print(colors)

sizes = []
for lab, row in office_episodes.iterrows():
    if row['has_guests'] == False:
        sizes.append(25)
    else:
        sizes.append(250)

office_episodes['colors'] = colors
office_episodes['sizes'] = sizes

non_guest_df = office_episodes[office_episodes['has_guests'] == False]
guest_df = office_episodes[office_episodes['has_guests'] == True]

fig = plt.figure ()
plt.scatter(x=non_guest_df['episode_number'], y=non_guest_df['viewership_mil'],c=non_guest_df.colors,s=25)
plt.scatter(x=guest_df['episode_number'], y=guest_df['viewership_mil'], c=guest_df['colors'], s=250,marker='*')
plt.title('Popularity, Quality, and Guest Appearances on the Office')
plt.xlabel('Episode Number')
plt.ylabel('Viewership (Millions)')
plt.show()

office_episodes[office_episodes['viewership_mil'] > 20]['guest_stars']

top_star = 'Cloris Leachman'


