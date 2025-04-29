import csv
from collections import defaultdict

def parse_data(file_path):
    yearly_data = defaultdict(list)
    
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            try:
                date = row[0]
                year = date.split("-")[2]
                tavg = float(row[1]) if row[1] else None
                if tavg is not None:
                    yearly_data[year].append(tavg)
            except:
                continue  # Skip malformed rows

    return yearly_data

def compute_averages(yearly_data):
    averages = {}
    for year, temps in yearly_data.items():
        if temps:
            avg = sum(temps) / len(temps)
            averages[year] = avg
    return averages

def find_extremes(averages):
    hottest_year = max(averages.items(), key=lambda x: x[1])
    coolest_year = min(averages.items(), key=lambda x: x[1])
    return hottest_year, coolest_year

if __name__ == '__main__':
    file_path = "DC/mumbai_weather.csv"  # Use raw string if needed: r"DC\mumbai_weather.csv"
    yearly_data = parse_data(file_path)
    averages = compute_averages(yearly_data)
    hottest, coolest = find_extremes(averages)
    
    print("Hottest Year:", hottest)
    print("Coolest Year:", coolest)
