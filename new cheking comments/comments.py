import pandas as pd
file=("/home/onedata/Downloads/panadas/new cheking comments/report.xlsx")
read=pd.read_excel(file)
read=read.drop(read.columns[[0,1,2,4,6,7]],axis=1)
read=read.fillna("Not Commented")
read=read[read['Comment']=='Not Commented']
#read.to_excel("Null_comment_list.xlsx",index=False)
read=read.drop(read.iloc[-1].tolist())
print(read)   
    
    