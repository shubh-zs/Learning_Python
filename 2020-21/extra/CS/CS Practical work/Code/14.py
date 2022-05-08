def udf(a,b):
    print('Orignal Array(A) : ',a)
    print('Orignal Array(B) : ',b)
    print('After Selection Sort',"."*150)
    a.extend(b)
    c = len(a)
    for i in range(c):
        min_= i
        for j in range(i+1, c):
            if a[min_] > a[j]:
                min_ = j
                a[i], a[min_] = a[min_], a[i]
    print("Sorted list : ",a)



a = [3,2,1,6]
b = [8,7,5,9]
udf(a,b)