import pandas as pd
from django.contrib.auth.models import User
from people_data.models import Person
import os
import math;

def run():
  # Read CSV file into a DataFrame
  csv_file_path = '../data/database.csv'
  df = pd.read_csv(csv_file_path, encoding='utf-8').head(4000)
  # Iterate through the DataFrame and create model instances
  count = 1
  for index, row in df.iterrows():
      # Create the Product instance
      hasBirth = row['birth']
      hadDeath = row['death']
      people = Person(
          name=row['name'].replace("_", " "),
          dob=int(row['birth']) if not math.isnan(row['birth']) else 3025,
          dod=int(row['death']) if not math.isnan(row['death']) else 3025,
          gender=row['gender'],
          popularity=count,
          occupation=row['level3_main_occ'],
          country=row['all_geography_groups']
      )
      #to save the current product
      count += 1
      people.save()

  print("CSV data has been loaded into the Django database.")