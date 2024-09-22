import pandas as pd
import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

input_file = 'users.csv' 
df = pd.read_csv(input_file)

df = df[df['email'].apply(is_valid_email)]

df_cleaned = df.drop_duplicates(subset='name')

output_file = 'cleaned_users.csv'

df_cleaned.to_csv(output_file, index=False)

print("Cleaned data has been written to",output_file)
