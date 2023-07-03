import pandas as pd
file=("/home/onedata/Downloads/panadas/youtrack19/resource.xlsx")
new=pd.read_excel(file)
new1=new.drop(columns=["Estimation time"])
print(new)
new1["Spent time"]=new["Spent time"].div(60).round(0)
new["Spent time"]=new["Spent time"]%60
new1=new1.astype({"Spent time":int})
new1=new1.astype({"Spent time":str})
new=new.astype({"Spent time":str})
new=new.drop(columns=["Estimation time"])
new["Spent time"]=new1["Spent time"]+"h."+new["Spent time"]+"m"
new=new.rename(columns={"Item":"Resources"})
print(new)