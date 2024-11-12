import array as arr 

array_num = arr.array('i',[1, 3, 5, 3, 7, 9, 3])
print(array_num)

print("The number of occurence of 3 : " , array_num.count(3))

array_num.reverse()
print("the reversed array is : " , array_num)