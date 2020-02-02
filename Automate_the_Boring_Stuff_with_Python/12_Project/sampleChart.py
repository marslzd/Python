# 图表
import openpyxl
import os 
os.chdir(os.path.join(os.getcwd(), '12_Project/'))

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

# Creat some data in column A
for i in range(1, 11):
    sheet['A' + str(i)] = i 

refObj = openpyxl.charts.Reference(sheet, (1, 1), (10, 1))

seriesObj = openpyxl.charts.Series(refObj, title='First series')

chartObj = openpyxl.charts.BarChart()
chartObj.append(seriesObj)
# Set the position (pixel)
chartObj.drawing.top = 50
chartObj.drawing.left = 100
chartObj.drawing.width = 300
chartObj.drawing.height = 200

sheet.add_chart(chartObj)
wb.save('sampleChart.xlsx')