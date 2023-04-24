from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt

# set the competition and season IDs
events = sb.events(match_id=3857258)
print(events.columns)
for index, event in events.iterrows():

    if (type(event['foul_committed_card']) == str or event['bad_behaviour_card'] == 'Yellow Card'):
        print(event['foul_committed_card'])
        print(event['bad_behaviour_card'])
# create an empty list to store resulsts for each match
match_results = []
if 'foul_committed_card' in events.columns:
    filtered_events = events.loc[events['foul_committed_card'].notnull(), ['match_id', 'team', 'foul_committed_card']]
    print(filtered_events)
    # count the number of cards for each team
    card_counts = filtered_events['foul_committed_card'].groupby(filtered_events['team']).value_counts().unstack(fill_value=0)



