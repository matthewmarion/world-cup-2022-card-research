import pandas as pd
import numpy as np
import statsmodels.api as sm

match_results = [
  {
    "match_id": 3857257,
    "home_team": "Australia",
    "away_team": "Denmark",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Australia won",
    "card_counts_home": 2,
    "card_counts_away": 1
  },
  {
    "match_id": 3857258,
    "home_team": "Brazil",
    "away_team": "Serbia",
    "home_goals": 2,
    "away_goals": 0,
    "result": "Brazil won",
    "card_counts_home": 0,
    "card_counts_away": 3
  },
  {
    "match_id": 3857288,
    "home_team": "Tunisia",
    "away_team": "Australia",
    "home_goals": 0,
    "away_goals": 1,
    "result": "Australia won",
    "card_counts_home": 3,
    "card_counts_away": 0
  },
  {
    "match_id": 3857267,
    "home_team": "Ecuador",
    "away_team": "Senegal",
    "home_goals": 1,
    "away_goals": 2,
    "result": "Senegal won",
    "card_counts_home": 0,
    "card_counts_away": 1
  },
  {
    "match_id": 3869321,
    "home_team": "Netherlands",
    "away_team": "Argentina",
    "home_goals": 2,
    "away_goals": 2,
    "result": "draw",
    "card_counts_home": 7,
    "card_counts_away": 8
  },
  {
    "match_id": 3857287,
    "home_team": "Uruguay",
    "away_team": "South Korea",
    "home_goals": 0,
    "away_goals": 0,
    "result": "draw",
    "card_counts_home": 1,
    "card_counts_away": 1
  },
  {
    "match_id": 3869486,
    "home_team": "Morocco",
    "away_team": "Portugal",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Morocco won",
    "card_counts_home": 3,
    "card_counts_away": 1
  },
  {
    "match_id": 3869685,
    "home_team": "Argentina",
    "away_team": "France",
    "home_goals": 3,
    "away_goals": 3,
    "result": "draw",
    "card_counts_home": 5,
    "card_counts_away": 3
  },
  {
    "match_id": 3857260,
    "home_team": "Saudi Arabia",
    "away_team": "Mexico",
    "home_goals": 1,
    "away_goals": 2,
    "result": "Mexico won",
    "card_counts_home": 6,
    "card_counts_away": 1
  },
  {
    "match_id": 3857264,
    "home_team": "Poland",
    "away_team": "Argentina",
    "home_goals": 0,
    "away_goals": 2,
    "result": "Argentina won",
    "card_counts_home": 1,
    "card_counts_away": 1
  },
  {
    "match_id": 3857266,
    "home_team": "France",
    "away_team": "Denmark",
    "home_goals": 2,
    "away_goals": 1,
    "result": "France won",
    "card_counts_home": 1,
    "card_counts_away": 2
  },
  {
    "match_id": 3857289,
    "home_team": "Argentina",
    "away_team": "Mexico",
    "home_goals": 2,
    "away_goals": 0,
    "result": "Argentina won",
    "card_counts_home": 1,
    "card_counts_away": 4
  },
  {
    "match_id": 3857269,
    "home_team": "Brazil",
    "away_team": "Switzerland",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Brazil won",
    "card_counts_home": 1,
    "card_counts_away": 1
  },
  {
    "match_id": 3857294,
    "home_team": "Netherlands",
    "away_team": "Qatar",
    "home_goals": 2,
    "away_goals": 0,
    "result": "Netherlands won",
    "card_counts_home": 1,
    "card_counts_away": 0
  },
  {
    "match_id": 3869254,
    "home_team": "Portugal",
    "away_team": "Switzerland",
    "home_goals": 6,
    "away_goals": 1,
    "result": "Portugal won",
    "card_counts_home": 0,
    "card_counts_away": 2
  },
  {
    "match_id": 3869118,
    "home_team": "England",
    "away_team": "Senegal",
    "home_goals": 3,
    "away_goals": 0,
    "result": "England won",
    "card_counts_home": 0,
    "card_counts_away": 1
  },
  {
    "match_id": 3869519,
    "home_team": "Argentina",
    "away_team": "Croatia",
    "home_goals": 3,
    "away_goals": 0,
    "result": "Argentina won",
    "card_counts_home": 2,
    "card_counts_away": 2
  },
  {
    "match_id": 3869354,
    "home_team": "England",
    "away_team": "France",
    "home_goals": 1,
    "away_goals": 2,
    "result": "France won",
    "card_counts_home": 1,
    "card_counts_away": 3
  },
  {
    "match_id": 3869552,
    "home_team": "France",
    "away_team": "Morocco",
    "home_goals": 2,
    "away_goals": 0,
    "result": "France won",
    "card_counts_home": 0,
    "card_counts_away": 1
  },
  {
    "match_id": 3869420,
    "home_team": "Croatia",
    "away_team": "Brazil",
    "home_goals": 1,
    "away_goals": 1,
    "result": "draw",
    "card_counts_home": 2,
    "card_counts_away": 3
  },
  {
    "match_id": 3869220,
    "home_team": "Morocco",
    "away_team": "Spain",
    "home_goals": 0,
    "away_goals": 0,
    "result": "draw",
    "card_counts_home": 1,
    "card_counts_away": 1
  },
  {
    "match_id": 3869219,
    "home_team": "Japan",
    "away_team": "Croatia",
    "home_goals": 1,
    "away_goals": 1,
    "result": "draw",
    "card_counts_home": 0,
    "card_counts_away": 2
  },
  {
    "match_id": 3869253,
    "home_team": "Brazil",
    "away_team": "South Korea",
    "home_goals": 4,
    "away_goals": 1,
    "result": "Brazil won",
    "card_counts_home": 0,
    "card_counts_away": 1
  },
  {
    "match_id": 3869151,
    "home_team": "Argentina",
    "away_team": "Australia",
    "home_goals": 2,
    "away_goals": 1,
    "result": "Argentina won",
    "card_counts_home": 0,
    "card_counts_away": 2
  },
  {
    "match_id": 3869152,
    "home_team": "France",
    "away_team": "Poland",
    "home_goals": 3,
    "away_goals": 1,
    "result": "France won",
    "card_counts_home": 1,
    "card_counts_away": 2
  },
  {
    "match_id": 3869117,
    "home_team": "Netherlands",
    "away_team": "United States",
    "home_goals": 3,
    "away_goals": 1,
    "result": "Netherlands won",
    "card_counts_home": 2,
    "card_counts_away": 0
  },
  {
    "match_id": 3857256,
    "home_team": "Serbia",
    "away_team": "Switzerland",
    "home_goals": 2,
    "away_goals": 3,
    "result": "Switzerland won",
    "card_counts_home": 7,
    "card_counts_away": 4
  },
  {
    "match_id": 3857270,
    "home_team": "Portugal",
    "away_team": "Uruguay",
    "home_goals": 2,
    "away_goals": 0,
    "result": "Portugal won",
    "card_counts_home": 3,
    "card_counts_away": 2
  },
  {
    "match_id": 3857263,
    "home_team": "Spain",
    "away_team": "Germany",
    "home_goals": 1,
    "away_goals": 1,
    "result": "draw",
    "card_counts_home": 1,
    "card_counts_away": 3
  },
  {
    "match_id": 3857259,
    "home_team": "Cameroon",
    "away_team": "Serbia",
    "home_goals": 3,
    "away_goals": 3,
    "result": "draw",
    "card_counts_home": 2,
    "card_counts_away": 2
  },
  {
    "match_id": 3857295,
    "home_team": "Japan",
    "away_team": "Costa Rica",
    "home_goals": 0,
    "away_goals": 1,
    "result": "Costa Rica won",
    "card_counts_home": 3,
    "card_counts_away": 3
  },
  {
    "match_id": 3857283,
    "home_team": "Belgium",
    "away_team": "Morocco",
    "home_goals": 0,
    "away_goals": 2,
    "result": "Morocco won",
    "card_counts_home": 1,
    "card_counts_away": 1
  },
  {
    "match_id": 3857282,
    "home_team": "United States",
    "away_team": "Wales",
    "home_goals": 1,
    "away_goals": 1,
    "result": "draw",
    "card_counts_home": 4,
    "card_counts_away": 2
  },
  {
    "match_id": 3857286,
    "home_team": "Qatar",
    "away_team": "Ecuador",
    "home_goals": 0,
    "away_goals": 2,
    "result": "Ecuador won",
    "card_counts_home": 4,
    "card_counts_away": 2
  },
  {
    "match_id": 3857301,
    "home_team": "Qatar",
    "away_team": "Senegal",
    "home_goals": 1,
    "away_goals": 3,
    "result": "Senegal won",
    "card_counts_home": 3,
    "card_counts_away": 3
  },
  {
    "match_id": 3857300,
    "home_team": "Argentina",
    "away_team": "Saudi Arabia",
    "home_goals": 1,
    "away_goals": 2,
    "result": "Saudi Arabia won",
    "card_counts_home": 0,
    "card_counts_away": 6
  },
  {
    "match_id": 3857299,
    "home_team": "South Korea",
    "away_team": "Ghana",
    "home_goals": 2,
    "away_goals": 3,
    "result": "Ghana won",
    "card_counts_home": 2,
    "card_counts_away": 2
  },
  {
    "match_id": 3857298,
    "home_team": "Portugal",
    "away_team": "Ghana",
    "home_goals": 3,
    "away_goals": 2,
    "result": "Portugal won",
    "card_counts_home": 2,
    "card_counts_away": 4
  },
  {
    "match_id": 3857297,
    "home_team": "Poland",
    "away_team": "Saudi Arabia",
    "home_goals": 2,
    "away_goals": 0,
    "result": "Poland won",
    "card_counts_home": 3,
    "card_counts_away": 2
  },
  {
    "match_id": 3857296,
    "home_team": "Croatia",
    "away_team": "Belgium",
    "home_goals": 0,
    "away_goals": 0,
    "result": "draw",
    "card_counts_home": 0,
    "card_counts_away": 1
  },
  {
    "match_id": 3857293,
    "home_team": "Ghana",
    "away_team": "Uruguay",
    "home_goals": 0,
    "away_goals": 2,
    "result": "Uruguay won",
    "card_counts_home": 2,
    "card_counts_away": 5
  },
  {
    "match_id": 3857292,
    "home_team": "Costa Rica",
    "away_team": "Germany",
    "home_goals": 2,
    "away_goals": 4,
    "result": "Germany won",
    "card_counts_home": 1,
    "card_counts_away": 0
  },
  {
    "match_id": 3857291,
    "home_team": "Spain",
    "away_team": "Costa Rica",
    "home_goals": 7,
    "away_goals": 0,
    "result": "Spain won",
    "card_counts_home": 0,
    "card_counts_away": 2
  },
  {
    "match_id": 3857290,
    "home_team": "Switzerland",
    "away_team": "Cameroon",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Switzerland won",
    "card_counts_home": 2,
    "card_counts_away": 1
  },
  {
    "match_id": 3857285,
    "home_team": "Senegal",
    "away_team": "Netherlands",
    "home_goals": 0,
    "away_goals": 2,
    "result": "Netherlands won",
    "card_counts_home": 2,
    "card_counts_away": 1
  },
  {
    "match_id": 3857281,
    "home_team": "Croatia",
    "away_team": "Canada",
    "home_goals": 4,
    "away_goals": 1,
    "result": "Croatia won",
    "card_counts_home": 2,
    "card_counts_away": 2
  },
  {
    "match_id": 3857280,
    "home_team": "Cameroon",
    "away_team": "Brazil",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Cameroon won",
    "card_counts_home": 4,
    "card_counts_away": 2
  },
  {
    "match_id": 3857279,
    "home_team": "France",
    "away_team": "Australia",
    "home_goals": 4,
    "away_goals": 1,
    "result": "France won",
    "card_counts_home": 0,
    "card_counts_away": 3
  },
  {
    "match_id": 3857278,
    "home_team": "Iran",
    "away_team": "United States",
    "home_goals": 0,
    "away_goals": 1,
    "result": "United States won",
    "card_counts_home": 3,
    "card_counts_away": 1
  },
  {
    "match_id": 3857277,
    "home_team": "Morocco",
    "away_team": "Croatia",
    "home_goals": 0,
    "away_goals": 0,
    "result": "draw",
    "card_counts_home": 1,
    "card_counts_away": 0
  },
  {
    "match_id": 3857276,
    "home_team": "Canada",
    "away_team": "Morocco",
    "home_goals": 1,
    "away_goals": 2,
    "result": "Morocco won",
    "card_counts_home": 4,
    "card_counts_away": 0
  },
  {
    "match_id": 3857275,
    "home_team": "Tunisia",
    "away_team": "France",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Tunisia won",
    "card_counts_home": 1,
    "card_counts_away": 0
  },
  {
    "match_id": 3857274,
    "home_team": "Netherlands",
    "away_team": "Ecuador",
    "home_goals": 1,
    "away_goals": 1,
    "result": "draw",
    "card_counts_home": 0,
    "card_counts_away": 1
  },
  {
    "match_id": 3857273,
    "home_team": "Wales",
    "away_team": "Iran",
    "home_goals": 0,
    "away_goals": 2,
    "result": "Iran won",
    "card_counts_home": 2,
    "card_counts_away": 2
  },
  {
    "match_id": 3857271,
    "home_team": "England",
    "away_team": "Iran",
    "home_goals": 6,
    "away_goals": 2,
    "result": "England won",
    "card_counts_home": 0,
    "card_counts_away": 2
  },
  {
    "match_id": 3857268,
    "home_team": "Belgium",
    "away_team": "Canada",
    "home_goals": 1,
    "away_goals": 0,
    "result": "Belgium won",
    "card_counts_home": 3,
    "card_counts_away": 2
  },
  {
    "match_id": 3857265,
    "home_team": "Mexico",
    "away_team": "Poland",
    "home_goals": 0,
    "away_goals": 0,
    "result": "draw",
    "card_counts_home": 2,
    "card_counts_away": 1
  },
  {
    "match_id": 3857262,
    "home_team": "South Korea",
    "away_team": "Portugal",
    "home_goals": 2,
    "away_goals": 1,
    "result": "South Korea won",
    "card_counts_home": 2,
    "card_counts_away": 0
  },
  {
    "match_id": 3857261,
    "home_team": "Wales",
    "away_team": "England",
    "home_goals": 0,
    "away_goals": 3,
    "result": "England won",
    "card_counts_home": 2,
    "card_counts_away": 0
  },
  {
    "match_id": 3857255,
    "home_team": "Japan",
    "away_team": "Spain",
    "home_goals": 2,
    "away_goals": 1,
    "result": "Japan won",
    "card_counts_home": 3,
    "card_counts_away": 0
  },
  {
    "match_id": 3857254,
    "home_team": "Denmark",
    "away_team": "Tunisia",
    "home_goals": 0,
    "away_goals": 0,
    "result": "draw",
    "card_counts_home": 2,
    "card_counts_away": 1
  }
]
# create a DataFrame from the match_results dictionary
match_df = pd.DataFrame(match_results)

# create a new column 'home_win' that indicates whether the home team won
match_df['home_win'] = match_df.apply(lambda x: x['home_team'] in x['result'], axis=1)

# create a new column 'away_win' that indicates whether the away team won
match_df['away_win'] = match_df.apply(lambda x: x['away_team'] in x['result'], axis=1)

# create a new column 'draw' that indicates whether the match was a draw
match_df['draw'] = match_df['result'].str.contains('draw')

# create a new DataFrame with only the columns we want to use for the regression
regression_df = match_df[['card_counts_home', 'card_counts_away', 'home_win', 'away_win']]

# fit a logistic regression model to the data
X = regression_df[['card_counts_home', 'card_counts_away']]
y = regression_df['home_win']
logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())
