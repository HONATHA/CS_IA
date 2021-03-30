import pandas as pd
#can do: <table><tr><td>

df = pd.read_html('https://en.wikipedia.org/wiki/Template:Current_ATP_Singles_Rankings')

df[0].to_csv('wiki_rank_table.csv')


