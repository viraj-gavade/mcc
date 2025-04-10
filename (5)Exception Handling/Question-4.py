#To use an assert statement with error message
def student(sub_marks):
    assert len(sub_marks)!=0,"No value found" #message(optional)
    return sum(sub_marks)/len(sub_marks)
student1 = [10,20,30]
print("Average marks = ",student(student1))

student2 = []
print("Average marks = ",student(student2))
