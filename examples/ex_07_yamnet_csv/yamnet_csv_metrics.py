"""
An example of metrics that can be extracted out of the YAMNet CSV downloaded from a RedVox report
Start from RedVox Report https://redvox.io/#/reports/6598

WARNING: This example may not function if you change any lines except line 15.
WARNING: This example may not function if you do not use the file you are instructed to download.
"""
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict
import pprint

# Input path to CSV downloaded from report
input_file: str = "/CHANGE/ME/DATA_2022/REDVOX_EXAMPLES/yamnet.csv"

if __name__ == "__main__":
    print(__doc__)

    # Load CSV
    df = pd.read_csv(input_file)
    print(f'Available columns: {df.columns.values}')

    # Get ID of stations
    stations = df["Station ID"].unique()

    for station in stations:
        # Get rows with station ID specific information
        df_station = df.loc[df['Station ID'] == station]
        dict_counts = df_station["class_0"].value_counts().to_dict()

        # Some preparation to extract metrics
        # Get index of max and min yamnet scores
        idx_max_score = df_station["score_0"].idxmax()
        idx_min_score = df_station["score_0"].idxmin()
        # Get names of most and least frequent class names
        most_frequent_class = df_station["class_0"].mode()[0]
        least_frequent_class = min(dict_counts, key=dict_counts.get)

        # Calculate average yamnet score per classification name
        dict_avg_scores: Dict = {}
        for idx, class_name in enumerate(dict_counts.keys()):

            df_class_name = df_station.loc[df_station['class_0'] == class_name]
            dict_avg_scores[f"{class_name}"] = "{0:.3f}".format(df_class_name['score_0'].mean())

        # Showcase some metrics
        print(f'\nStation ID: {station}'
              f'\nNumber of classification names found: {len(dict_counts.keys())}'
              f'\nClassification names found: {list(dict_counts.keys())}'
              
              f'\nMost common classification name: "{most_frequent_class}"'
              f'\nNumber of times "{most_frequent_class}" appears: '
              f'{dict_counts.get(most_frequent_class)}'

              f'\nLeast common classification name: "{least_frequent_class}"'
              f'\nNumber of times "{least_frequent_class}" appears: '
              f'{dict_counts.get(least_frequent_class)}'
              
              
              f'\nHighest YAMNet Score: "{df_station["class_0"][idx_max_score]}" with score '
              f'{"{0:.3f}".format(df_station["score_0"][idx_max_score])} '
              f'at {datetime.fromtimestamp(df_station["Window Start"][idx_max_score]/1e6)} (UTC)'
              f'\nLowest YAMNet Score: "{df_station["class_0"][idx_min_score]}" with score '
              f'{"{0:.3f}".format(df_station["score_0"][idx_min_score])} '
              f'at {datetime.fromtimestamp(df_station["Window Start"][idx_min_score]/1e6)} (UTC)'
              f'\nAverage YAMNet Score per classification name: ')
        pprint.pprint(dict_avg_scores)

        # Start pie chart figure
        labels = [f"{key} ({str(dict_counts.get(key))})" for key in dict_counts.keys()]
        sizes = dict_counts.values()

        fig, ax = plt.subplots()
        plt.suptitle(f"Station {station} - Total YAMNet annotations: {sum(dict_counts.values())}")
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

