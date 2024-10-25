import matplotlib.pyplot as plt
from obspy import read_events, UTCDateTime
from collections import Counter

# Load the catalog (assuming it's in QuakeML format)
catalog = read_events('bohol_2013_earthquake.xml')

# Extract event dates and group by day
event_dates = [event.origins[0].time.date for event in catalog]
daily_counts = Counter(event_dates)

# Prepare data for plotting
dates = sorted(daily_counts.keys())
counts = [daily_counts[date] for date in dates]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(dates, counts, marker='o', linestyle='-')

# Add titles and labels
plt.title('Bohol 2013 Earthquake - Daily Aftershock Activity (ObsPy)')
plt.xlabel('Date')
plt.ylabel('Number of Earthquakes')
plt.grid(True)
plt.xticks(rotation=45)

# Highlight the mainshock
mainshock_date = UTCDateTime('2013-10-15').date
plt.axvline(mainshock_date, color='red', linestyle='--', label='Mainshock')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
