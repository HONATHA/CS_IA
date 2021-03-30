import pandas as pd

# df = pd.read_html("http://www.espn.com/sports/tennis/rankings")

# df[0].to_csv('espn_ranking.csv')

df = pd.read_html("http://www.espn.com/tennis/player/_/id/296/novak-djokovic")

df[0].to_csv('djokovic.csv')

# df = pd.read_html("https://www.atptour.com/en/players/atp-head-2-head/novak-djokovic-vs-daniil-medvedev/D643/MM58")

# df[0].to_csv('head2head.csv')