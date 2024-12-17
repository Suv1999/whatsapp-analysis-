
import pandas as pd


def preprocessor(df):
    # Renaming and splitting columns from the input DataFrame `df`
    y_ = df.columns
    df = df.rename(columns={y_[0]: 'chats'})
    df[['date_time', 'message']] = df['chats'].str.split(' - ', n=1, expand=True)
    df.drop('chats', axis=1, inplace=True)        
    
    # Convert `date_time` to datetime format
    df['date_time'] = pd.to_datetime(df['date_time'], format="%d/%m/%y, %I:%M %p", errors='coerce')
    
    # Splitting `message` column into `User` and `Message`
    df[["User", "Message"]] = df["message"].str.split(":", n=1, expand=True)
    df.drop('message', axis=1, inplace=True)
    
    # Extracting additional date and time features
    df["Year"] = df["date_time"].dt.year
    df["Month"] = df["date_time"].dt.month_name()
    df["Day"] = df["date_time"].dt.day
    df["Hour"] = df["date_time"].dt.hour
    df["Minute"] = df["date_time"].dt.minute
    
    # Dropping rows with any NaN values
    df.dropna(inplace=True)

    df = df.astype({col: 'int' for col in df.select_dtypes(include=['float']).columns})
    
    return df

