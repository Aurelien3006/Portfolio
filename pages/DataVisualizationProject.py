import streamlit as st

st.set_page_config(
    page_title='Data Visualization Project',
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
st.sidebar.page_link('./pages/Portfolio.py', label='Portfolio')

st.header('**Data Visualization Project : Regional Public Transportation System of Paris**', divider=True)

# imports :
from folium.plugins import MarkerCluster
import seaborn as sns
import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charging the files
stops_df = pd.read_csv('IDFM-gtfs/stops.txt')
trips_df = pd.read_csv('IDFM-gtfs/trips.txt')
routes_df = pd.read_csv('IDFM-gtfs/routes.txt')
stop_times_df = pd.read_csv('IDFM-gtfs/stop_times.txt')

st.markdown("""
    <p>
      The map below represents an interactive visualization of public transportation stops in the Paris region and its surroundings. 
      Each circle on the map indicates a cluster of stops located near each other. The number at the center of each circle corresponds 
      to the total number of stops in that area. 
      
      The larger the circle, the higher the number of stops, allowing for quick identification of high-density areas such as central Paris, around stations like Saint-Lazare and Gare du Nord, where multiple metro, RER, and 
      suburban train lines converge. 
      
      The color of the circles varies according to density, with areas having a greater number of stops 
      represented by darker colors. This visualization is useful for understanding the geographical distribution of public transport stops 
      in Paris and identifying key concentration points in the urban transport network.
    </p>
    """,unsafe_allow_html=True)

# Create a map centered on Paris :
map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Use MarkerCluster :
marker_cluster = MarkerCluster().add_to(map)

# Add a point for each stop :
for _, stop in stops_df.iterrows():
    folium.Marker(
        location=[stop['stop_lat'], stop['stop_lon']],
        popup=stop['stop_name']
    ).add_to(marker_cluster)

st_folium(map)




st.markdown("""
    <p>
      The bar chart below displays the <strong>top 10 transport lines with the highest number of trips</strong> in the region. 
      Each bar represents a specific transport line, with the height of the bar corresponding to the total number of trips on that line. 
      The transport lines include both <em>trains</em> and <em>metros</em>, as well as a <em>tramway</em>. 
      
      The lines are represented by their route names, such as "B", "3", "D", and "14", with each line color-coded to distinguish them from one another.
      To the right of the chart is a legend that indicates the type of transport for each route (train, metro, or tramway). 
      
      This visualization helps in quickly identifying which transport lines handle the most traffic in terms of trips, with lines like "B" and "3" 
      having the highest number of trips, followed by lines such as "D" and "14". The chart provides insights into the relative importance of 
      each line in the overall public transport network.
    </p>

    """,unsafe_allow_html=True)

# Join dataframes trips and routes
trips_routes_df = pd.merge(trips_df, routes_df, on='route_id')

# Dictionary :
route_type_map = {
    0: "Tramway",
    1: "Métro",
    2: "Train",
    3: "Bus",
    7: "Funiculaire"
}

trips_routes_df['route_type_desc'] = trips_routes_df['route_type'].map(route_type_map)
trips_count = trips_routes_df.groupby(['route_id', 'route_long_name', 'route_color', 'route_type_desc']).size().reset_index(name='trip_count')

top_routes = trips_count.nlargest(10, 'trip_count')

plt.figure(figsize=(10, 6))
bars = sns.barplot(x='route_long_name', y='trip_count', data=top_routes)

for bar, color in zip(bars.patches, top_routes['route_color']):
    bar.set_color(f"#{color}")  # Convertir en couleur hexadécimale

plt.title('Top 10 des lignes avec le plus de trajets', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Nombre de trajets sur la ligne')
plt.xlabel('Nom de la ligne')

# Add the legend for the type of route
legend_labels = [f"{name} ({route_type})" for name, route_type in zip(top_routes['route_long_name'], top_routes['route_type_desc'])]
plt.legend(legend_labels, title='Type de transport', bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(plt)




st.markdown("""
    <p>
      The pie chart below illustrates the <strong>proportion of trips made by the top 10 transport routes</strong> compared to all other routes. 
      The red section, which accounts for <strong>8.9%</strong> of the total trips, represents the trips made by the top 10 busiest routes. 
      These are likely the most heavily trafficked lines in the public transport network.
      
      The green section, which makes up the remaining <strong>91.1%</strong>, represents the trips made by all other routes.
      This visualization highlights the significant contribution of the top 10 routes, even though they represent a small percentage of the overall number of routes. 
      Despite this, the bulk of the trips are distributed among many other routes in the network.
    </p>

    """,unsafe_allow_html=True)

top_10_trips_sum = top_routes['trip_count'].sum()
total_trips_sum = trips_count['trip_count'].sum()
other_trips_sum = total_trips_sum - top_10_trips_sum

labels = ['Top 10 Routes', 'Autres Routes']
sizes = [top_10_trips_sum, other_trips_sum]
colors = ['#FF0000','#22CC00']

plt.figure(figsize=(2, 2))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=300,textprops={'fontsize': 5})
plt.title('Proportion des trajets du Top10 par rapport aux autres', fontsize=7)
plt.axis('equal')

st.pyplot(plt)





st.markdown("""
    <p>
      The stacked bar chart below shows the <strong>distribution of departure times by type of transport route</strong>. Each bar represents 
      a different hour of the day, from midnight (0) to 11 PM (23), with the height of the bar corresponding to the total number of departures during that hour. 
      The bars are color-coded based on the type of transport: <em>bus</em> (blue), <em>tramway</em> (yellow), <em>metro</em> (green), 
      <em>funicular</em> (red), and <em>train</em> (purple).
      
      As seen in the chart, buses make up the majority of the departures, particularly during peak hours in the morning (around 6-9 AM) 
      and in the evening (around 4-7 PM). The metro and trains also contribute significantly during these times, indicating their role 
      in handling commuter traffic. 
      
      The chart highlights the busiest times of the day for public transport, with the morning and evening 
      rush hours being the most prominent.
    </p>
    """,unsafe_allow_html=True)

# Join stop_times with trips to obtain le type de route
stop_times_trips_df = pd.merge(stop_times_df, trips_df, on='trip_id')
stop_times_trips_df = pd.merge(stop_times_trips_df, routes_df[['route_id', 'route_type']], on='route_id')

stop_times_trips_df['hour'] = pd.to_datetime(stop_times_trips_df['departure_time'], format='%H:%M:%S', errors='coerce').dt.hour

stop_times_trips_df['route_type_desc'] = stop_times_trips_df['route_type'].map(route_type_map)

# Create a graph with stacked bars
plt.figure(figsize=(12, 6))
sns.histplot(
    data=stop_times_trips_df.dropna(subset=['hour']),
    x='hour',
    hue='route_type_desc',
    multiple='stack',
    bins=24,
    palette='tab10',
    edgecolor='black'
)

plt.title('Distribution des heures de départ par type de route', fontsize=16)
plt.xlabel('Heure')
plt.ylabel('Nombre de départs')
plt.xticks(range(0, 24))

st.pyplot(plt)



st.markdown("""
    <p>
      The pie chart below shows the <strong>distribution of departures by type of transport</strong> in the public transport network. 
      The largest portion of the pie, making up <strong>80.3%</strong> of the total departures, represents the bus network, 
      which dominates the transportation system in terms of frequency of departures.
      
      Metros account for <strong>11.1%</strong> of the total, while trains make up <strong>5.4%</strong>. 
      Tramways and funiculars together account for a smaller proportion, with <strong>3.3%</strong> of departures.
      
      This chart highlights the significant role that buses play in the network, handling the majority of the departures, 
      followed by metros and trains, which provide additional capacity and coverage across different regions.
    </p>

    """,unsafe_allow_html=True)

# a Join
stop_times_trips_df = pd.merge(stop_times_df, trips_df, on='trip_id')
stop_times_trips_df = pd.merge(stop_times_trips_df, routes_df[['route_id', 'route_type']], on='route_id')

stop_times_trips_df['route_type_desc'] = stop_times_trips_df['route_type'].map(route_type_map)
stop_times_trips_df = stop_times_trips_df[stop_times_trips_df['route_type_desc'] != 'Funiculaire']

# Count the total number of departures by type of route
route_type_counts = stop_times_trips_df['route_type_desc'].value_counts()

labels = route_type_counts.index
sizes = route_type_counts.values
colors = sns.color_palette('tab10', len(labels))

plt.figure(figsize=(4, 4))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
plt.title('Répartition des départs par type de transport', fontsize=16)

st.pyplot(plt)




st.markdown("""
    <p>
      The map below displays the <strong>public transport network in the Paris metropolitan area</strong>, with routes of different lines represented as colored lines. 
      Each line corresponds to a specific transport route and is color-coded to distinguish it from other routes.
      
      The circular markers on the lines indicate the stops along each route.
      This visualization provides a comprehensive view of how different transport lines connect various parts of the city, with a high density of routes converging 
      in central Paris, especially in areas such as Châtelet, Saint-Lazare, and Gare du Nord, which serve as major transport hubs.
      
      The interactive map allows for a detailed examination of how the public transport network covers the city and connects the suburbs, providing insight 
      into the flow and accessibility of the transport system.
    </p>

    """,unsafe_allow_html=True)

metro_routes_df = routes_df[routes_df['route_type'] == 1]

# Join trips with stop_times and stops to select the underground's stops
metro_trips_df = pd.merge(trips_df, metro_routes_df[['route_id']], on='route_id')
metro_stops_df = pd.merge(stop_times_df, metro_trips_df[['trip_id', 'route_id']], on='trip_id')
metro_stops_coords = pd.merge(metro_stops_df, stops_df[['stop_id', 'stop_lat', 'stop_lon']], on='stop_id')

paris_map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

for _, route in metro_routes_df.iterrows():
    route_id = route['route_id']
    route_color = "#" + route['route_color']  # Couleur de la ligne en format hexadécimal

    # Filter each stop with its line
    line_stops = metro_stops_coords[metro_stops_coords['route_id'] == route_id]
    line_stops = line_stops.drop_duplicates(subset=['stop_id'])  # Eviter les doublons

    # list of tuples
    coordinates = list(zip(line_stops['stop_lat'], line_stops['stop_lon']))

    if len(coordinates) > 1:
        folium.PolyLine(locations=coordinates, color=route_color, weight=2.5).add_to(paris_map)

    for lat, lon in coordinates:
        folium.CircleMarker(location=[lat, lon], radius=3, color=route_color, fill=True).add_to(paris_map)

st_folium(paris_map)



st.markdown("""
    <p>
      The bar chart below shows the <strong>distribution of departures by hour of the day</strong> in the public transport network.
      
      Each bar represents the total number of departures occurring at a specific hour, starting from 5 AM and continuing until 11 PM (23). 
      The chart highlights a clear pattern of peak departure times, with the highest activity occurring during the morning rush hours, particularly 
      between 7 AM and 9 AM, and the evening rush hours between 4 PM and 7 PM. These periods represent the times when the majority of commuters 
      are using public transport, reflecting the daily work commute patterns.
      
      In contrast, early morning and late evening hours have significantly fewer departures, indicating reduced transport activity outside peak hours.
      This visualization helps in understanding the temporal distribution of transport activity and identifying key periods of high demand in the network.
    </p>

    """,unsafe_allow_html=True)

metro_routes = routes_df[routes_df['route_type'] == 1]['route_id']
metro_trips = trips_df[trips_df['route_id'].isin(metro_routes)]['trip_id']
metro_stop_times = stop_times_df[stop_times_df['trip_id'].isin(metro_trips)]
metro_stop_times['departure_time'] = pd.to_datetime(metro_stop_times['departure_time'], format='%H:%M:%S', errors='coerce')
metro_stop_times['hour'] = metro_stop_times['departure_time'].dt.hour
trips_per_hour = metro_stop_times.groupby('hour').size()

# Histogram of trips per hour
plt.figure(figsize=(10, 6))
trips_per_hour.plot(kind='bar', color='skyblue')
plt.title('Nombre de trajets de métro par heure')
plt.xlabel('Heure de la journée')
plt.ylabel('Nombre de trajets')
plt.xticks(rotation=0)
plt.grid(True)
plt.tight_layout()

st.bar_chart(trips_per_hour)



st.markdown("""
    <p>
      The area chart below shows the <strong>number of metro trips by hour for each metro line</strong> in the transport network.
      
      Each colored area represents a different metro line, with the size of the area corresponding to the number of trips for that line at each hour of the day.
      The chart clearly illustrates peak travel times, with two main spikes: one in the morning around 7-9 AM and another in the evening around 5-7 PM. 
      These peaks coincide with the typical commuter rush hours. The lines with the largest areas during these times represent the metro lines 
      with the highest number of trips, indicating their importance in handling commuter traffic.
      
      This visualization provides a detailed look at how metro traffic fluctuates throughout the day 
      and how different lines contribute to the overall volume of trips.
    </p>

    """,unsafe_allow_html=True)

metro_routes = routes_df[routes_df['route_type'] == 1][['route_id', 'route_short_name', 'route_color']]
metro_trips = trips_df[trips_df['route_id'].isin(metro_routes['route_id'])]
metro_stop_times = stop_times_df[stop_times_df['trip_id'].isin(metro_trips['trip_id'])]

metro_trips = metro_trips[['trip_id', 'route_id']]
metro_stop_times = metro_stop_times.merge(metro_trips, on='trip_id', how='left')
metro_stop_times = metro_stop_times.merge(metro_routes, on='route_id', how='left')
metro_stop_times['departure_time'] = pd.to_datetime(metro_stop_times['departure_time'], format='%H:%M:%S', errors='coerce')
metro_stop_times['hour'] = metro_stop_times['departure_time'].dt.hour
trips_per_hour_per_line = metro_stop_times.groupby(['hour', 'route_short_name']).size().unstack(fill_value=0)

metro_colors = metro_routes.set_index('route_short_name')['route_color'].fillna('808080')
metro_colors = metro_colors.apply(lambda x: f'#{x}' if not x.startswith('#') else x)

fig1, ax = plt.subplots(figsize=(12, 8))

trips_per_hour_per_line.plot(kind='area', stacked=True, ax=ax, color=[metro_colors.get(col, '#808080') for col in trips_per_hour_per_line.columns], alpha=0.8)

plt.title("Nombre de trajets de métro par heure pour chaque ligne", fontsize=16)
plt.xlabel("Heure de la journée", fontsize=12)
plt.ylabel("Nombre de trajets", fontsize=12)
plt.xticks(rotation=0)
plt.legend(title="Lignes de métro", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# Generation the stacked curves
fig2, ax = plt.subplots(figsize=(12, 8))
trips_per_hour_per_line.plot(kind='area', stacked=True, ax=ax, color=[metro_colors.get(col, '#808080') for col in trips_per_hour_per_line.columns], alpha=0.8)
plt.title("Nombre de trajets de métro par heure pour chaque ligne", fontsize=16)
plt.xlabel("Heure de la journée", fontsize=12)
plt.ylabel("Nombre de trajets", fontsize=12)
plt.xticks(rotation=0)
plt.legend(title="Lignes de métro", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

st.pyplot(fig2)