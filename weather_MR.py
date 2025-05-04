'''Practical 5: Design and develop a distributed application to find the coolest/hottest year from the available
weather data. Use weather data from the Internet and process it using MapReduce. '''


from mrjob.job import MRJob
from mrjob.step import MRStep
import csv
from datetime import datetime

class CalculateMaxMinTemperature(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_find_max_min)
        ]

    def mapper(self, _, line):
        # Skip header
        if line.startswith('date'):
            return

        reader = csv.reader([line])
        for row in reader:
            try:
                date = row[0]
                tmx = float(row[2])
                tmn = float(row[3])
                yield "temperature_stats", (date, tmx, tmn)
            except (IndexError, ValueError):
                pass  # Skip lines with invalid data

    def reducer_find_max_min(self, key, values):
        max_date, max_temp = None, float('-inf')
        min_date, min_temp = None, float('inf')

        for date, tmx, tmn in values:
            if tmx > max_temp:
                max_temp = tmx
                max_date = date
            if tmn < min_temp:
                min_temp = tmn
                min_date = date

        yield "Max Temperature", (max_date, max_temp)
        yield "Min Temperature", (min_date, min_temp)


if __name__ == "__main__":
    CalculateMaxMinTemperature.run()

''' # CLI

cd desktop
pip install mrjob
python cool_hot_year.py weather.csv'''