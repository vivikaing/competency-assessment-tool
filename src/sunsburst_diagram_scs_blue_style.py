import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('../data/data_scs_cu_all.csv')

# Sort the DataFrame based on the competency column using a custom key function
df_sorted = df.sort_values(by=['competency_cluster', 'competency_unit', 'competency'])

# Define a custom color scale (example: mapping specific values to specific colors)
custom_color_scale = [
    [0.0, "rgb(232,241,252)"],   # #E8F1FC
    [0.2, "rgb(207,225,248)"],   # #CFE1F8 Light blue
    [0.4, "rgb(180,209,245)"],  # #B4D1F5 (3.2)
    [0.6, "rgb(66,143,206)"],  # #9CC5F2 (1.6)
    [0.8, "rgb(32,99,168)"],  # #4FA7ED (2.4)
    [1.0, "rgb(5,48,97)"]  # #4FA7ED (2.4)
]

# Create the sunburst chart with the custom color scale
fig = px.sunburst(
    df_sorted,
    path=['competency_cluster', 'competency_unit', 'competency'],
    color='demonstrated',
    color_continuous_scale=custom_color_scale,
    hover_data={'competency_cluster_name': True,'competency_unit_name': True, 'competency_name': True, 'demonstrated':True}  # Add both fields
)

# Custom hover template
fig.update_traces(
    hovertemplate="<b>Competency cluster:  </b>%{customdata[0]}<br>" +
                  "<b>Competency unit:  </b>%{customdata[1]}<br>" +
                  "<b>Competency:  </b>%{customdata[2]}<br>" +
                  "<b>Demonstrated:  </b>%{customdata[3]}<br>"
)

# Show the chart
fig.show()