def caculate_homework(homework_arg):
    sum_of_homework = 0
    for x in homework_arg.values():
        sum_of_homework += x
    cau_avarage_homework = round(sum_of_homework/len(homework_arg),2)
    return cau_avarage_homework

