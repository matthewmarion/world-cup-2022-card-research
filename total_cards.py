from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt

# set the competition and season IDs
matches = sb.matches(competition_id=43, season_id=106)

# create an empty list to store results for each match
match_results = []

# iterate through each match
for index, match in matches.iterrows():
    # get all the events for the match
    events = sb.events(match_id=match['match_id'])
    # filter events to only include fouls with a card
    if 'foul_committed_card' in events.columns:
        filtered_events = events.loc[events['foul_committed_card'].notnull(), ['match_id', 'team', 'foul_committed_card']]
        print(filtered_events)
        # count the number of cards for each team
        card_counts = filtered_events['foul_committed_card'].groupby(filtered_events['team']).value_counts().unstack(fill_value=0)


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

# print the results
print(match_results)
