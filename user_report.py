import pandas as pd
from datetime import date
import os
path=os.path.dirname(__file__)
path=(f"{path}/user report")
df1=pd.read_excel(f"{path}/report.xlsx")
df2=pd.read_excel(f"{path}/billable.xlsx")
df3=pd.read_excel(f"{path}/non_billable.xlsx")
df4=pd.read_excel(f"{path}/total.xlsx")
mergeres=pd.merge(df1,df2,on=df1.columns[0],how='outer')
mergeres1=pd.merge(mergeres,df3,on=df1.columns[0],how='outer')
mergeres1.fillna(0, inplace=True)
mergeres1=mergeres1.drop(mergeres1.columns[[1,3,5]],axis=1)
mergeres1=mergeres1.rename(columns={"item":"Resources",'Spent time_x':"Spent Time",'Spent time_y':'Billable','Spent time':"Non Billable"})
print(mergeres1)
date_now=date.today()
mergeres1.to_excel(f"Resource_report.xlsx",index=False)



