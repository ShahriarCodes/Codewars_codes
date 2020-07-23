seconds = 355

total_secs = seconds

hours = total_secs // 3600
seconds_remainder = total_secs % 3600
minutes = seconds_remainder // 60
seconds_final = seconds_remainder % 60




if hours < 10 and minutes >= 10 and seconds_final >= 10 :
    result = '0{}:{}:{}'.format(hours,minutes,seconds_final)
elif hours < 10 and minutes <10 and seconds_final >= 10 :
    result = '0{}:0{}:{}'.format(hours,minutes,seconds_final)
elif hours < 10 and minutes <10 and seconds_final < 10 :
    result = '0{}:0{}:0{}'.format(hours,minutes,seconds_final)
elif hours >= 10 and minutes <10 and seconds_final >= 10 :
    result = '{}:0{}:{}'.format(hours,minutes,seconds_final)
elif hours >= 10 and minutes <10 and seconds_final < 10 :
    result = '{}:0{}:0{}'.format(hours,minutes,seconds_final)
elif hours >= 10 and minutes >=10 and seconds_final < 10 :
    result = '{}:{}:0{}'.format(hours,minutes,seconds_final)
else:
    result = '{}:{}:{}'.format(hours,minutes,seconds_final)

print(result)



'-------others solution-----------------------------------'
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


    
