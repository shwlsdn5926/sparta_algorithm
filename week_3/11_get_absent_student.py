all_students = ["류진", "예지", "채령", "리아", "리나", "유나"]
present_students = ["리아", "류진", "채령", "유나"]


def get_absent_student(all_array, present_array):
    key_array = []
    student_dict ={}
    for k in all_array:
        student_dict[k] =True

    for k in present_array:
        del student_dict[k]

    for k, v in student_dict.items():
        if v is True:
            key_array.append(k)
    return key_array


print(get_absent_student(all_students, present_students))
