if __name__ == '__main__':
    students = list()

    for _ in range(int(input())):
        students.append([input(), float(input())])

    students.sort(key=lambda x: x[1])

    lowest = students[0]
    students.pop(0)

    while True:
        if lowest[1] == students[0][1]:
            students.pop(0)
        else:
            break

    lowests = [students[0]]
    for name, score in students[1:len(students)]:
        if score == lowest[0][1]:
            lowests.append([name, score])

    lowests.sort(key=lambda x: x[0])
    for name, score in lowest:
        print(name)
