from tabula.io import read_pdf
import pandas as pd
import os
from GoogleMap import GetGeoCode
new_column_names = [
    "Case Number",
    "Location",
    "DateReported",
    "Time",
    "DateOccurred",
    "TimeOccurred",
    "Type",
    "Dispo",
    "Arrestee",
    "DOB"
]
last_column_names = [
    "DateReported",
    "Time",
    "Location",
    "lat",
    "lng"
]
folder = "./crime"
def convert_pdf_to_csv(input_path, output_path):
    try:
        print(input_path)
        # Read the PDF file and convert it to CSV
        lst = read_pdf(input_path, pages='all')
        print(lst)
        if df.columns[0] == 'Case Number':
            df = df.rename(columns=dict(zip(df.columns, new_column_names)))
            #df.to_csv(output_path, index=False, header=True)
            return df
        # Assign the modified DataFrame with updaed column names
        df = df[1:].rename(columns=dict(zip(df.columns, new_column_names)))
        # Reset the index if desired
        df = df.reset_index(drop=True)
        # Save the DataFrame to CSV
        # df.to_csv(output_path, index=False, header=True)
        return df
        # for index, row in df.iterrows():
        #df.to_csv(output_path, index=False, header=True)
        
    except Exception as e:
        print("An error occurred during the conversion:", str(e))

def ConvertAll():
    files = os.listdir(folder)
    # Convert the PDF to CSV
    # Get the structure from the first file
    df_all = pd.DataFrame(columns=new_column_names)
    i = 0
    for file in files:
        # drop if it is online data
        if file.split(' ')[0] == "online": # or file == "040923cl.pdf"
            continue
        # Set the input PDF file path
        pdf_file = folder +'/'+ file
        # Set the output CSV file path
        csv_file = file.split()[0]+'.csv'
        df = convert_pdf_to_csv(pdf_file, csv_file)
        df_all = pd.concat([df_all, df], ignore_index=True)
        df_all = df_all.reset_index(drop=True)
        
    
    df_all = df_all.reset_index(drop=True)
    df_all.to_csv('crime_data.csv', index=False, header=True)
    print(df_all)

def AddGeoColumn():
    csv_file_path = './crime_data.csv'
    df = pd.read_csv(csv_file_path)
    # add new column Geocode at the end

    df['lat'] = df['Location']
    df['lng'] = df['Location']
    for index, row in df.iterrows():
        # change address to geocode
        address = row['Location']
        geocode = GetGeoCode(address)
        print(geocode)
        df.at[index, 'lat'] = geocode['lat']
        df.at[index, 'lng'] = geocode['lng']

    df.to_csv('crime_data_geo.csv', index=False, header=True)
    print(df)

def Preprocess():
    csv_file_path = './crime_data_geo.csv'
    df = pd.read_csv(csv_file_path)
    # add new column Geocode at the end
    for index, row in df.iterrows():
        time = row['Time']
        df.at[index, 'Time'] = time[:-3]
    # delete useless column
    columns = df.columns.tolist()
    for col in columns:
        if col not in last_column_names:
            df = df.drop(col, axis=1)
        
    df = df.reindex(columns=last_column_names)
    df.to_csv('crime_data_preprocess.csv', index=False, header=True)
    print(df)

def GetCrime(input):
    df = pd.read_csv('crime_data_preprocess.csv')
    df_return = pd.DataFrame(columns=last_column_names)
    for index, row in df.iterrows():
        datereported = row['DateReported']
        if datereported == input:
            df_return = df_return._append(row, ignore_index=True)
    # Convert DataFrame to JSON
    json_data = df_return.to_json(orient='records')
    
    # Save JSON data to a file
    with open('CrimeDate.json', 'w') as file:
        file.write(json_data)       


if __name__ == "__main__":
    # AddGeoColumn()
    # Preprocess()
    # # Read the CSV file into a DataFrame
    # df = pd.read_csv('crime_data_preprocess.csv')
    
    # # Convert DataFrame to JSON
    # json_data = df.to_json(orient='records')
    
    # # Save JSON data to a file
    # with open('output.json', 'w') as file:
    #     file.write(json_data)
    GetCrime('4/25/2023')
    