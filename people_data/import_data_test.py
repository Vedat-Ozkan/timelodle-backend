import pandas as pd
from django.contrib.auth.models import User
from people_data.models import Person
import os
import math;

def run():
  # Read CSV file into a DataFrame
  csv_file_path = '../data/database.csv'
  df = pd.read_csv(csv_file_path, encoding='latin-1').head(1)
  a = Person.objects.all();
  a.delete();
  # Iterate through the DataFrame and create model instances
  for index, row in df.iterrows():
      # Create the Product instance
      print(int(row['birth']), row['death'], "hji")
      people = Person(
          name=row['name'].replace("_", " "),
          dob=int(row['birth']),
          dod=int(row['death']) if not math.isnan(row['death']) else 3025,
          gender=row['gender'],
          popularity=row['ranking_visib_5criteria'],
          occupation=row['level3_main_occ'],
          country=row['all_geography_groups']
      )
      #to save the current product
      people.save()

  print("CSV data has been loaded into the Django database.")