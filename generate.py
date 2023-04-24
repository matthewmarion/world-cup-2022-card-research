from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt

# Excluding match_results to shorten length of the file.
match_results = [
]

total_win_cards = 0
total_loss_cards = 0
card_win_loss = []
total_matches = 0
total_cards = 0
for match in match_results:
    total_matches = total_matches + 1
    if match['home_team'] in match['result'].split(' won ')[0]:
        win_cards = match['card_counts_home']
        card_win_loss.append((win_cards, 1))
        card_win_loss.append((match['card_counts_away'], 0))
        total_win_cards += win_cards

    elif match['away_team'] in match['result'].split(' won ')[0]:
        loss_cards = match['card_counts_home']
        card_win_loss.append((match['card_counts_home'], 0))
        card_win_loss.append((match['card_counts_away'], 1))
        total_loss_cards += loss_cards
    else:
        total_matches = total_matches - 1
        continue
    total_cards += match['card_counts_home'] + match['card_counts_away']

print(card_win_loss)
print(f'Total Cards: {total_cards}')
print(f'Total Win Cards: {total_win_cards}')
print(f'Total Loss Cards: {total_loss_cards}')
print(f'Total Matches: {total_matches}')
