import pandas as pd
import plotly.express as px
df = pd.read_csv("Dataset/trafficMetaData.csv")
px.set_mapbox_access_token("pk.eyJ1IjoibmFtbnAiLCJhIjoiY2xhM244NWwxMHJwNDN0bXpyanI0dmM1bCJ9.Ta2hVHru-tlVyYzcE7jizA")
fig = px.scatter_mapbox(df, lat="POINT_1_LAT", lon="POINT_1_LNG", 
                        hover_data={"POINT_1_NAME","POINT_2_NAME"},
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
fig.show()