# import pandas as pd
# import csv
# df = pd.read_csv("data.csv")
# print(df.groupby('Gender').mean())

# import plotly.graph_objects as go

# fig = go.Figure(go.Bar(
#     x = [20, 14, 23],
#     y = ['Apple', 'Oranges', 'Banana'],
#     orientation = 'h'))

# fig.show()

import pandas as pd
import csv
import plotly
import plotly_express as px
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
# print(df.groupby("level")["attempt"].mean())
mean = df.groupby(["student_id", "level"], as_index= False)["attempt"].mean()

fig = px.scatter(mean, x = "student_id" , y = "level", size = 'attempt', color = 'attempt')
plotly.offline.plot(fig)