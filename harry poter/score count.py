file1 = open(r'D:\Personal\python practice\harry poter\scores.txt','r',encoding='utf-8')
file_lines = file1.readlines()  
file1.close()
print(file_lines)

final_scores = []

for i in file_lines:
    data = i.split()
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = data[0] + str(sum)+'\n'
    print(result)
    final_scores.append(result)

print(final_scores)

winner = open(r'D:\Personal\python practice\harry poter\winner.txt','w',encoding='utf-8') 
winner.writelines(final_scores)
winner.close()

file2 = open(r'D:\Personal\python practice\harry poter\winner.txt','r',encoding='utf-8') 
file2_lines = file2.readlines()
file2.close()
# print(file2_lines)

dict_score = {}
list_score = []
winnernew = []

for i in file2_lines:
    name = i[:-4]
    score = i[-4:-1]
    dict_score[score] = name
    list_score.append(score)

print(list_score)
print(dict_score)

list_score.sort(reverse=True)
print(list_score)

for i in list_score:
    result = dict_score[i] + str(i) + '\n'
    winnernew.append(result)

print(winnernew)

file3 = open(r'D:\Personal\python practice\harry poter\winnernew.txt','w',encoding='utf-8') 
file3_lines = file3.writelines(winnernew)
file3.close()