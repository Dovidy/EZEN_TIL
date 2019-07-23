def alarmBefore(hour:int, min:int):
    if min < 45:
        if hour == 0:
            return 23, min + 15
        else:
            return hour - 1, min + 15
    else:
        return hour, min - 45
