import pandas as pds
import xlsxwriter
file=("/home/tamilan/Documents/xl_writter/Project_Allocation_Info.xlsx")
data=pds.read_excel(file)
#print(data.sort_values("Project"))
Adata=data["Project Manager"]
length=len(Adata)
a=Adata.tolist()
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet=workbook.add_worksheet()
for i in range(0,length):
    worksheet.write(i,1,a[i])
workbook.close()