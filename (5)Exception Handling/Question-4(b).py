#To use an assert statement without error message
def student(sub_marks):
    assert len(sub_marks)!=0
    return sum(sub_marks)/len(sub_marks)
student1 = []
print("Average marks = ",student(student1))

