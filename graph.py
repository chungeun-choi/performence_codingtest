import pandas as pd
import os

FILE_FATH = input()
TEST_VLUE = os.open("/Users/cucuridas/Desktop/코딩테스트_성능지표/programmers_personality_type_test.csv")

def read_csv():
    df = pd.read_csv(TEST_VLUE)
    return df 

def preprocessing(df):
    df.fillna(0)
    df = df.replace(to_replace ='통과',value='',regex=True)
    return  

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.divide.html
# https://blockchainstudy.tistory.com/45
def devide_field(df):
    for column in df.columns.to_list():
        df[column]['performence'], df[column]['memory'] = df[column].apply(lambda x: x.split(', '))
    pass

if __name__ == "__main__":
    dataframe = read_csv()
    pre_df = preprocessing(dataframe)
    print(pre_df)