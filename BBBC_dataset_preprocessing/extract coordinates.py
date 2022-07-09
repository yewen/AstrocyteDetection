import glob
import pandas as pd

files = glob.glob('the/place/you/save/the/csv/labels/*.csv')

for filenames in files:
    df=pd.read_csv(filenames, header=None, names=['Cell', 'A','B','C','xmin', 'ymin', 'xmax', 'ymax','D','E','F','G','H','I','J'])
    df=df.drop(['A','B','C','D','E','F','G','H','I','J'],axis=1)
    df.to_csv(filenames,index=False) 
