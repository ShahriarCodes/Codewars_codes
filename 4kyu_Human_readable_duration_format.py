seconds = 355

total_secs = seconds
time = 0

hours = total_secs // 3600
seconds_remainder = total_secs % 3600
minutes = seconds_remainder // 60
seconds_final = seconds_remainder % 60




# if seconds == 0:
#     time = 'now'
# elif seconds <=59:
#     time = '{} seconds'.format(seconds_final)
# elif minutes<=59:
#     time = ',{} seconds'.format(minutes,seconds_final)
