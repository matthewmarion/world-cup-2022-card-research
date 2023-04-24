from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt

# Excluding match_results to shorten length of the file.
match_results = [
]

# create empty lists to store the x and y values for each point
# create a list of winning and losing points
winning_points = []
losing_points = []
match_num = 0
for result in match_results:
    # get the match number
    match_num = match_num + 1

    # get the card counts for each team
    home_cards = result['card_counts_home']
    away_cards = result['card_counts_away']

    # determine the color of the point based on the result
    if result['home_team'] in result['result'].split(' won ')[0]:
        winning_points.append((match_num, home_cards))
        losing_points.append((match_num, away_cards))
    else:
        winning_points.append((match_num, away_cards))
        losing_points.append((match_num, home_cards))


print(winning_points)
print(losing_points)

# plot the winning and losing points
fig, ax = plt.subplots()
ax.scatter(*zip(*winning_points), color='g')
ax.scatter(*zip(*losing_points), color='r')

# plot the lines connecting the winning and losing points
winning_x, winning_y = zip(*winning_points)
losing_x, losing_y = zip(*losing_points)
ax.plot(winning_x, winning_y, color='g', label='Winning Team')
ax.plot(losing_x, losing_y, color='r', label='Losing Team')

# set the x-axis and y-axis labels
ax.set_xlabel('Match')
ax.set_ylabel('Number of Cards')

x_tick_positions = range(1, len(match_results) + 1)
x_tick_labels = [f'{i}' for i in x_tick_positions]
ax.set_xticks(x_tick_positions)
ax.set_xticklabels(x_tick_labels)

ax.set_ylim(0, 10)
ax.legend()

# show the plot
plt.show()



