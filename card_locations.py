from statsbombpy import sb
import pandas as pd
from mplsoccer import Pitch
import matplotlib.pyplot as plt

pitch = Pitch(pitch_color='grass', line_color='white', stripe=True)
fig, ax = pitch.draw()

# set the competition and season IDs
matches = sb.matches(competition_id=43, season_id=106)
world_cup_total_events = []

for index, match in matches.iterrows():
    events = sb.events(match_id=match['match_id'])
    if 'foul_committed_card' in events.columns:
        filtered_events = events.loc[events['foul_committed_card'].notnull(), ['match_id', 'team', 'minute', 'location', 'foul_committed_card']]
        print(filtered_events)
        world_cup_total_events.append(filtered_events)

# concatenate all the filtered events dataframes into a single dataframe
world_cup_total_events = pd.concat(world_cup_total_events, ignore_index=True)

# plot each of the card locations on the pitch chart
for i, row in world_cup_total_events.iterrows():
    if row['foul_committed_card'] == 'Yellow Card':
        color = 'yellow'
    elif row['foul_committed_card'] == 'Red Card':
        color = 'red'
    else:
        color = 'white'
    ax.scatter(row['location'][0], row['location'][1], color=color, edgecolors='black')

plt.show()
