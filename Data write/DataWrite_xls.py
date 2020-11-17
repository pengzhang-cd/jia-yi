import openpyxl 
wb=openpyxl.Workbook() 
sheet=wb.active
sheet.title='漫威宇宙'
sheet['A1'] = '漫威宇宙'
rows= [['美国队长','钢铁侠','蜘蛛侠'],['Captain America','Iron man','Spider man']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('Marvel.xlsx')