import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('../data/data_scs_cu_nuar.csv')

# Sort the DataFrame based on the competency column using a custom key function
df_sorted = df.sort_values(by=['competency_cluster', 'competency_unit', 'competency'])

# Create the sunburst chart with the custom color scale
fig = px.sunburst(
    df_sorted,
    path=['competency_cluster', 'competency_unit', 'competency'],
    color='demonstrated',
    color_continuous_scale='Purp',
    hover_data={'competency_cluster_name': True,'competency_unit_name': True, 'competency_name': True, 'demonstrated':True}  # Add both fields
)

# Custom hover template
fig.update_traces(
    hovertemplate="<b>Competency cluster: </b>%{customdata[0]}<br>" +
                  "<b>Competency unit: </b>%{customdata[1]}<br>" +
                  "<b>Competency: </b>%{customdata[2]}<br>" +
                  "<b>Demonstrated: </b>%{customdata[3]}<br>"
)

# Show the chart
fig.show()