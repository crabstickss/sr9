time_1 = input("Введите первый временной промежуток в формате HH:MM : ")
time_2 = input("Введите второй временной промежуток в формате HH:MM : ")

time_1 = time_1.split(":")
time_2 = time_2.split(":")
def time(time_1, time_2):

    if (int(time_1[1]) >= 60 or int(time_1[1]) < 0):
        return "Неправильный формат времени!"
        exit()
    if (int(time_2[1]) >= 60 or int(time_2[1]) <0):
        return "Неправильный формат времени!"
        exit()

    time_1_in_min = int(time_1[0])*60 + int(time_1[1])
    time_2_in_min = int(time_2[0])*60 + int(time_2[1])

    if time_1_in_min < time_2_in_min:
        a = str(time_2_in_min - time_1_in_min)
        return a
    else:
        a = str(time_1_in_min - time_2_in_min)
        return a
print( "Временной промежуток в минутах = " + str(time(time_1,time_2)))
