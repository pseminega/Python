import pandas as pd

def load_data():
    data = pd.read_csv("hn_stories.csv")
    # Add columns
    data.columns = ['submission_time', 'upvotes', 'url', 'headline']
    # Print a few rows
    print(data.head())
    
if __name__ == "__main__":
    
    load_data()
    
    

    
