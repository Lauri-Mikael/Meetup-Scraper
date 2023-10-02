import pandas as pd

def toexcelandcsv(dataframe, city):
    df = pd.DataFrame(dataframe, columns = ['Title', 'Link', 'Day', 'Time', 'GroupName', 'Where', 'ImageName'])

    # Convert the dataframe to excel file
    df.to_excel(f'{city}.xlsx', index=False)
    df.to_csv(f'{city}.csv', index=False)

