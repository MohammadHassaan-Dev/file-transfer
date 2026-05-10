def grade(marks):
    if marks>90:
        return "A+"
    if marks>=80 and marks<=89:
        return "A"

    if marks>=70 and marks<=79:
        return "B"

    if marks>=60 and marks<=69:
        return "C"

    if marks<=60:
        return "Fail"


marks_list = [95, 82, 77, 61, 55]
lenght = len(marks_list)

i = 1
for num in marks_list:
    print(f"Student {i}: {grade(num)}")
    i+=1
    
    