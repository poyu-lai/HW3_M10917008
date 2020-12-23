import csv
from sklearn import tree
import numpy as np
'''
Abalone dataset
Number of Instances: 4177


	Name		Data Type	Meas.	Description
	----		---------	-----	-----------
0.	Sex		nominal			M, F, and I (infant)
1.	Length		continuous	mm	Longest shell measurement
2.	Diameter	continuous	mm	perpendicular to length
3.	Height		continuous	mm	with meat in shell
4.	Whole weight	continuous	grams	whole abalone
5.	Shucked weight	continuous	grams	weight of meat
6.	Viscera weight	continuous	grams	gut weight (after bleeding)
7.	Shell weight	continuous	grams	after being dried
8.	Rings		integer			+1.5 gives the age in years

8.Ring is our class object(1~29)
'''

#string label to num
Sex = ['M','F','I']

prepare_abalone_datas=[]
with open('abalone.data', 'r') as csvfile:
    rows = csv.reader(csvfile)

    for row_data in rows:
        addlist = [Sex.index(row_data[0])]
        for i in range(7):
            addlist.append(float(row_data[i+1]))
        addlist.append(int(row_data[8]))

        prepare_abalone_datas.append(addlist)

print(prepare_abalone_datas)
print(len(prepare_abalone_datas))

with open('abalone_prepare.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for prepare_row_data in prepare_abalone_datas:
        writer.writerow(prepare_row_data)


