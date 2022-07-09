import glob
import pandas as pd

annotations = glob.glob('...csv/labels/location/*.csv')

for file in annotations:
     df=pd.read_csv(file)
     width=990
     df["width"]=width
     height=708
     df["height"]=height   
     filename=file.split('/')[-1].split('.')[0] + '.png'
     df["filename"] =filename
     classs='cell'
     df['class']=classs  
     names=["filename","width","height","class","xmin","ymin","xmax","ymax"]
     df = df.reindex(columns=names)
     df.to_csv(file,index=False)
