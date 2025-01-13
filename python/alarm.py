'''
Description:
Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

employed | vacation 
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false

8kyu
12 m ago
'''
def set_alarm(emp, vac):
    if (emp==1 and vac==1):
        return False
    elif (emp==0 and vac==1):
        return False
    elif (emp==0 and vac==0):
        return False
    else:
        return True
a=1
b=0

set_alarm(a,a)
set_alarm(a,b)
set_alarm(b,a)
set_alarm(b,b)
