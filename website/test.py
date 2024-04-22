'''import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Value': [10, 15, 20, 18, 25],
    'Component': ['P', 'P', 'P', 'P', 'P']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for component 'P'
df_p = df[df['Component'] == 'P']

# Sort data by date
df_p = df_p.sort_values(by='Date')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df_p['Date'], df_p['Value'], marker='o', linestyle='-')
plt.title('Component P - Value Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)

# Format date on x-axis
date_form = DateFormatter("%Y-%m-%d")  # Customize the date format as per your preference
plt.gca().xaxis.set_major_formatter(date_form)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()








def upload_to_db(db_file, tbl_name, col_str, file, dataframe):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    print('Opened database successfully')

    # Construct the SQL INSERT query
   

    insert_query = f"INSERT INTO user_components (id,user_id,component,value,date) VALUES (?,?,?,?,?)"



    # Read data from CSV file and execute the INSERT query
    with open(file, 'r') as my_file:
        next(my_file)  # Skip header rowss
        df = pd.read_csv(my_file, delimiter=';')

# Conversion des données en tuples
        data = [row for _, row in df.iterrows()]
        cursor.executemany(insert_query,data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print('Data uploaded successfully')'''