import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib import rc  
rc('font', family='AppleGothic') 			
plt.rcParams['axes.unicode_minus'] = False  

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
    
def divide_performence_and_memory(list_values):
    performence,memory = list_values.split(", ")
    
    return performence,memory

def color_set(peoples):
    color_dict = {}
    for i in peoples:
        color_dict.setdefault(i,random_color())
    return color_dict

def random_color():
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) 
    return color

if __name__ == "__main__":
    dataframe = read_csv()
    pre_df = preprocessing(dataframe)
    color_value = color_set(pre_df.columns.to_list())
    per_df = None
    mem_df = None

    for i in pre_df.columns.to_list():
        #Divide dataframe value by using string format
        result = list(map(divide_performence_and_memory,pre_df[i]))

        # i.performence value, i.memory value 
        perf = list(map(lambda x: float(x[0].strip()),result))
        mem = list(map(lambda x: float(x[1].strip()),result))

        perf_dict = {
            i: perf
        }

        mem_dict = {
            i: mem
        }


        if not isinstance(per_df,pd.DataFrame) :
            per_df = pd.DataFrame(perf_dict,index=[i for i in range(1,21)])
            mem_df = pd.DataFrame(mem_df)
        else:
            per_df = pd.concat([per_df,pd.DataFrame(perf_dict)],axis=1)
            mem_df = pd.concat([mem_df,pd.DataFrame(mem_dict)],axis=1)
        
        
    per_graph = per_df.plot.line(title='performence',color=color_value).get_figure()
    mem_graph = mem_df.plot.line(title='usage memory',color=color_value).get_figure()

    per_graph.savefig('per_graph.png')
    mem_graph.savefig('mem_graph.png')
    
        # new_dataframe[i]["memory"] = 


    

    