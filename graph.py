import pandas as pd
import csv

#FILE_FATH = input()
TEST_VLUE = "/Users/cucuridas/Desktop/performence_codingtest/programmers_personality_type_test.csv"
PREPROCESSING_OBJECTS = ["통과","\(","\)","ms","MB"]

def read_csv():
    df = pd.read_csv(TEST_VLUE,index_col=0)
    return df 

def preprocessing(df):
    df.fillna(0)

    for pre in PREPROCESSING_OBJECTS:
        df = df.replace(to_replace =pre,value='',regex=True)
    return  df

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.divide.html
# https://blockchainstudy.tistory.com/45
def create_new_dataframe(df,value):
    people = df.columns.tolist()
    multi_columns = []
    columns = []
    index = df.index.tolist()

    for i in people:
        columns.extend([i,i])

    for i in range(0,len(people)):
        multi_columns.extend(["performence","memory"])
    
    new_dataframe = pd.DataFrame(data=value,index = index, columns= [columns,multi_columns])
    
    return new_dataframe
    
def divide_performence_and_memory(list_values):
    performence,memory = list_values.split(", ")
    
    return performence,memory




if __name__ == "__main__":
    dataframe = read_csv()
    pre_df = preprocessing(dataframe)
    index_list = pre_df.index.to_list()
    value_list = []
    df = None

    for i in pre_df.columns.to_list():
        #Divide dataframe value by using string format
        result = list(map(divide_performence_and_memory,pre_df[i]))

        # i.performence value, i.memory value 
        perf = list(map(lambda x: float(x[0].strip()),result))
        mem = list(map(lambda x: float(x[1].strip()),result))

        value_dict = {
            (i,'performence'):perf,
            (i,'memory'):mem
        }

        if not isinstance(df,pd.DataFrame) :
            df = pd.DataFrame(data=value_dict,columns=([[i,i],['performence','memory']]))
        else:
            df = pd.concat([df,pd.DataFrame(data=value_dict,columns=([[i,i],['performence','memory']]))],axis=1)
        
    
        # new_dataframe[i]["memory"] = 


    

    