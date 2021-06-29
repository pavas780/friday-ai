import datetime
import winsound
def alarm(time):
    altime=str(datetime.datetime.now().strptime(time, '%I:%M'))
    print(altime)
    altime=altime[11:-3]
    horel=altime[:2]
    horeal=int(horel)
    mireal=altime[3:5]
    mirel=int(mireal)
    print(f'alarm is set for {time}')
    while True:
        if horeal ==datetime.datetime.now().hour:
            if mirel==datetime.datetime.now().minute:
                print('alarm is running')
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif mirel <datetime.datetime.now().minute:
                break
if __name__=='__main__':
    alarm('45:00')            
                    