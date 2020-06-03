hour = int(input("알람맞출 시 입력"))
minute = int(input("알람맞출 분 입력"))

if minute < 45:
    hour-=1
    minute = abs(minute - 45)
    print('{}시 {}분'.format(hour, minute))
else:
    minute = minute - 45
    print('{}시 {}분'.format(hour, minute))
