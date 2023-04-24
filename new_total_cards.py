from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt

# set the competition and season IDs
matches = sb.matches(competition_id=43, season_id=106)

# create an empty list to store results for each match
match_results = []
bad = []

# iterate through each match
for index, match in matches.iterrows():
    # get all the events for the match
    events = sb.events(match_id=match['match_id'])
    # filter events to only include fouls with a card
    if 'foul_committed_card' in events.columns or 'bad_behaviour_card' in events.columns:
        # create a list of columns to include in filtered_events
        columns_to_include = ['match_id', 'team']
        if 'foul_committed_card' in events.columns:
            columns_to_include.append('foul_committed_card')
        if 'bad_behaviour_card' in events.columns:
            columns_to_include.append('bad_behaviour_card')
            bad.append(match['match_id'])

        filtered_events = events.loc[events[columns_to_include].notnull().all(axis=1), columns_to_include]

        # combine the two columns of cards
        if 'foul_committed_card' in filtered_events.columns and 'bad_behaviour_card' in filtered_events.columns:
            filtered_events['cards'] = filtered_events['foul_committed_card'].add(filtered_events['bad_behaviour_card'], fill_value=0)
        elif 'foul_committed_card' in filtered_events.columns:
            filtered_events['cards'] = filtered_events['foul_committed_card']
        else:
            filtered_events['cards'] = filtered_events['bad_behaviour_card']

        # count the number of cards for each team
        card_counts = filtered_events['cards'].groupby(filtered_events['team']).value_counts().unstack(fill_value=0)

        # get the match result
        home_team = match['home_team']
        away_team = match['away_team']
        home_goals = match['home_score']
        away_goals = match['away_score']
        if home_goals > away_goals:
            result = f"{home_team} won"
        elif home_goals < away_goals:
            result = f"{away_team} won"
        else:
            result = "draw"

        # calculate the number of cards for each team
        try:
            card_counts_home = card_counts.loc[home_team].sum().astype(int)
        except KeyError:
            card_counts_home = 0

        try:
            card_counts_away = card_counts.loc[away_team].sum().astype(int)
        except KeyError:
            card_counts_away = 0

        # append the match result and card counts to the list of results
        match_results.append({
            'match_id': match['match_id'],
            'home_team': home_team,
            'away_team': away_team,
            'home_goals': home_goals,
            'away_goals': away_goals,
            'result': result,
            'card_counts_home': card_counts_home,
            'card_counts_away': card_counts_away
        })
print(bad)
