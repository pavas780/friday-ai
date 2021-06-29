import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from selenium import webdriver
import webbrowser
import requests
import pywhatkit as kit
from pynotifier import Notification
import psutil
from translate import Translator
import pyautogui
import PyPDF2
from pywikihow import search_wikihow
import randfacts
import operator
import sys
import random
import socket
import phonenumbers
import MyAlarm
import cv2

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
        
    if hour>=0 and hour<12:
        speak('Good Morning,sir')
    if hour>=12 and hour<15:
        speak('Good Afternoon,sir')
    if hour>=15 and hour<19:
        speak('Good Evening,sir')
    if hour>=19 and hour<24:
        speak('hello sir')
    speak('i am friday')    
          
    
    st=datetime.datetime.now().strftime('%H:%M:%S')
    speak(f'the time is {st}')
    
    if hour>=0 and hour<6:
        speak('sir, you have to take rest ')
        speak('as you have been working for more than 11 hours')
        speak('boss,your health is very important for me ')
    battery()
    weather()
def battery():
    battery=psutil.sensors_battery()
    percent=battery.percent
    plugged=battery.power_plugged
    if plugged:
        speak('your charger is plugged in ')
        speak('battery percentage is '+str(percent)+'percent')
        d=100-percent
        if d<5:
            speak('you should unplug your charger as battery is full')
        else:    
            speak('remaing'+str(d)+'percent') 
    else:
        speak('the charger is not plugged in')
        if percent<20:
            speak('you should plug your charger as battery is low')
        else:    
            speak('battery percentage is '+str(percent)+'percent') 
    speak('we are ready to work')        
             
    Notification('battery percentage is ',str(percent)+'% remaing',duration=10).send() 
def randomfact():
    ft=randfacts.getFact(True)
    engine.setProperty('rate',150)
    speak(ft)
    
def locu(api_key):
    api='https://geo.ipify.org/api/v1?apiKey=at_09fMZhOs1joqczMZnThbR1pBJkbQi&ipAddress='+api_key
    loc= requests.get(api).json()    
    city=loc['location']['city']
    state=loc['location']['region']
    lan=loc['location']['lng']
    log=loc['location']['lat']
    
    speak('sir i think we are in'+city) 
    speak('the logitude is'+lan+'the latitude is'+log)        
def ipaddr():
    host=socket.gethostname()
    ip=socket.gethostbyname(host)
    print(ip)
    return ip     
def weather():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:    
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city='shimla'
        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data['weather'][0]['description']
        format_ad = json_data['main']['temp']
        feels_like=json_data['main']['feels_like']
        min=json_data['main']["temp_min"]
        max=json_data['main']["temp_max"]
        pres=json_data['main']["pressure"]
        hum=json_data['main']["humidity"]
        sea=json_data['main']["sea_level"]
        ground=json_data['main']["grnd_level"]
        
        speak('the weather of dharamshala is'+format_add)
        speak('tempurature is      '+str(format_ad))
        speak('feels like it is      '+str(feels_like)+'fahrenheit')
        speak('minimum tempurature is '+str(min)+'fahrenheit')
        speak('maximum temperature is        '+str(max)+'fahrenheit')
        speak('pressure outside is      '+str(pres)+'fahrenheit')
        speak('humidity is about       '+str(hum)+'grams per kilogram')
        speak('height of dharamshala from sea level is about       '+str(sea)+'meters')
        speak('height of dharamshala from groung level is about      '+str(ground)+'meters')
        if format_add=='clear' or format_add=='clear sky':
            speak('the weather is quite good outside')
            speak('it is a good day to go outside for bike rides and chilling with your friends')
        elif format_add=='scattered clouds' or format_add=='clouds':
            speak('you should ot go outside for a long period of time as there are chances of rain')
            speak('you can watch movie in this time with some popcorns')
        elif format_add=='rain' or format_add=='broken clouds' or format_add=='overcast':
            speak('you should stay inside as there are greater chances of rain outside ')
            speak('make some snacks and enjoy raining')
              
        
    elif hour>=12 and hour<=24:
        speak('do you want to get updates about weather')
        d=takecommand()
        if 'yes'in d:
            api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
            city='shimla'
            url = api_address + city
            json_data = requests.get(url).json()
            format_add = json_data['weather'][0]['description']
            format_ad = json_data['main']['temp']
            feels_like=json_data['main']['feels_like']
            min=json_data['main']["temp_min"]
            max=json_data['main']["temp_max"]
            pres=json_data['main']["pressure"]
            hum=json_data['main']["humidity"]
            sea=json_data['main']["sea_level"]
            ground=json_data['main']["grnd_level"]
            
            speak('the weather of dharamshala is'+format_add)
            speak('tempurature is      '+str(format_ad))
            speak('feels like it is      '+str(feels_like)+'fahrenheit')
            speak('minimum tempurature is '+str(min)+'fahrenheit')
            speak('maximum temperature is        '+str(max)+'fahrenheit')
            speak('pressure outside is      '+str(pres)+'fahrenheit')
            speak('humidity is about       '+str(hum)+'grams per kilogram')
            speak('height of dharamshala from sea level is about       '+str(sea)+'meters')
            speak('height of dharamshala from groung level is about      '+str(ground)+'meters')
            if format_add=='clear' or format_add=='clear sky':
                speak('the weather is quite good outside')
                speak('it is a good day to go outside for bike rides and chilling with your friends')
            elif format_add=='scattered clouds' or format_add=='clouds':
                speak('you should ot go outside for a long period of time as there are chances of rain')
                speak('you can watch movie in this time with some popcorns')
            elif format_add=='rain' or format_add=='broken clouds' or format_add=='overcast':
                speak('you should stay inside as there are greater chances of rain outside ')
                speak('make some snacks and enjoy raining')
    speak('these are some news updates ')            
    news('enter your own api')            
    speak('how can i help you sir')   
        
def pdfread():
    book=open('enter bookname.pdf','rb')
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    speak(f'sir,there are {pages} pages in this book')
    speak('reading it from strating....')
    page=pdfreader.getPage(2)
    text=page.extractText()
    speak(text)
def randomnumber(a,b):
    number=random.randint(a,b)
    return number             
def phonenum(number):
    from phonenumbers import geocoder
    ch_num=phonenumbers.parse(number,'CH')
    d=geocoder.description_for_number(ch_num,'en')
    from phonenumbers import carrier
    service=phonenumbers.parse(number,'RO')
    a=carrier.name_for_number(service,'en')
    return d,a
def weatherof(query):   
    try: 
        query=query.replace('show weather of','')
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city=str(query)
        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data['weather'][0]['description']
        format_ad = json_data['main']['temp']
        feels_like=json_data['main']['feels_like']
        min=json_data['main']["temp_min"]
        max=json_data['main']["temp_max"]
        pres=json_data['main']["pressure"]
        hum=json_data['main']["humidity"]
        
        speak('the weather of '+query+' is'+format_add)
        speak('tempurature is      '+str(format_ad))
        speak('feels like it is      '+str(feels_like)+'fahrenheit')
        speak('minimum tempurature is '+str(min)+'fahrenheit')
        speak('maximum temperature is        '+str(max)+'fahrenheit')
        speak('pressure outside is      '+str(pres)+'fahrenheit')
        speak('humidity is about       '+str(hum)+'grams per kilogram')
        speak(' is there anything else i can do mr. pavas')
        a=takecommand().lower()
        if 'no' in a:
            quit()
    except Exception as e:
        speak('sorry,sir i am unable to show weather of'+query)            
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Reognizing.....')
        query=r.recognize_google(audio,language='en-in')
        print('user said:',query)    
    except Exception as e:    
        print(e)
        speak('sorry, i was unable to understand')
        speak('Please, say that again')
        return 'None'
    return query
def hurt():
    speak('i am going to shutdown your pc')
    
    speak('i am very hurt')
    a=takecommand().lower()
    if 'sorry' in a:
        speak('i accept your apologies')
    else:    
        speak('your pc is going to sleep')
        speak('never ever fight with friday')
        speak("Shutting the computer")
        os.system("shutdown /s /t 30")
def quitSelf():
    speak("this is the call for your confirmation to shut down")
      
    # Input voice command 
    take =takecommand().lower()
    choice = take
    if 'yes' in choice:
          
        # Shutting down
        print("Shutting down the computer")
        speak("Shutting the computer")
        os.system("shutdown /s /t 30")
    if choice == 'no':
          
        # Idle
        print("Thank u sir")
        speak("Thank u sir")
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('','') #enter email address and password
    server.sendemail('',to,content)
    server.close()     

def news(api_key):
    newsapi='https://newsapi.org/v2/top-headlines?country=in&apiKey='+api_key
    news=requests.get(newsapi).json()
    article=news['articles']
    news_article=[]
    for i in article:
        news_article.append(i['title'])    
    for j in range(8):
        engine.setProperty('rate',150)
        speak(news_article[j])
         
    engine.setProperty('rate',200)    
        
           
if __name__ =='__main__':
    while 1:
        query=takecommand().lower()
        
        if 'wikipedia' in query:            
            speak('searching....')
            try:
                query=query.replace('wikipedia','')
                results=wikipedia.summary(query,sentences=3)
                speak('according to wikipedia')
                speak(results)
                
                break
            except Exception  as e:   
                speak('sorry'+query +' does not match any pages. Try another id!')
                speak('is there anything else i can search')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
            
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'open google' in query:
            speak('what do you want to search..')
            a=takecommand().lower()
            webbrowser.open(f'{a}')
            speak(a+' has been searched')
            
            speak('is there anything else i can do mr. pavas')
            b=takecommand().lower()
            if 'no' in b:
                quit()
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'open hackerearth' in query:
            webbrowser.open('hackerearth.com')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'open gmail' in query:
            webbrowser.open('gmail.com')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit() 
        elif 'play music' in query:
            musicdr=''#enter location of your drive where you have stored music files 
            songs=os.listdir(musicdr)
            d=randomnumber(1,150)
            os.startfile(os.path.join(musicdr,songs[d]))
            speak('is there anything else i can do mr')#you can enter your name
            a=takecommand().lower()
            if 'no' in a:
                quit()  
        elif 'time' in query:
            st=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {st}')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif'date' in query: 
            st=datetime.datetime.now().strftime('%Y-%m-%d')
            speak(f'sir, todays date is{st}')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'open code' in query:
            code='""'#enter location of visual studio
            os.startfile(code)
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'open gta' in query:
            code=''#enter your gta file folder
            os.startfile(code)
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'open truck simulator' in query:
            code=''#enter your ets2 file folder
            os.startfile(code)
            speak(' is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
             
        elif 'send email' in query:
            try:
                speak('what should i say')
                content =takecommand()
                to='heroalom.gmail.com'#fakee email used
                sendemail(to,content)
                speak('email has been sent to',to)
                speak(' is there anything else i can do mr. pavas')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
            except Exception as e:
                speak('sorry sir email has not been sent to ',to)    
        elif 'open whatsapp' in query:#make sure you have logged in chrome
            try:
                speak('to whom you want to send message,sir')
                
                to=''#enter the number to whom you want to send message
                speak('what doy want to say ,sir')
                content=takecommand()
                h=int(datetime.datetime.now().hour)
                m=(int(datetime.datetime.now().minute)+1)
                kit.sendwhatmsg(f'{to}','{content}',h,m)
                speak('message was been sent to'+to)
                speak(' is there anything else i can do mr. pavas')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
            except Exception as e:
                speak('sorry sir message  was not been sent to ',to) 
        elif 'open brave' in query:
            code='C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
            os.startfile(code)
            try:
                speak('what  you want to open in brave')
                browser=webdriver.Brave('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
                speak(' is there anything else i can do mr. pavas')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
                
            except Exception as e:
                print(e)
                speak('sorry sir we cant open brave' )
                a=takecommand().lower()
                if 'no' in a:
                    quit()
        elif'shutdown' in query or 'shut down' in query: 
            quitSelf()
        elif'restart' in query: 
            speak('this is the call for your confirmation to restart')
            take =takecommand().lower()
            choice = take
            if 'yes' in choice:
                print("Shutting down the computer")
                speak("Shutting the computer")
                os.system("shutdown /r /t 30")
            if 'no' in take:
                quit()
        elif'logoff' in query or 'log off' in query or 'log of' in query: 
            speak('this is the call for your confirmation to log off')
            take =takecommand().lower()
            choice = take
            if 'yes' in choice:
                print("Shutting down the computer")
                speak("Shutting the computer")
                os.system("shutdown /l /t 30")
        elif 'open notepad' in query: 
            speak('do you want to open new file')
            d=takecommand()
            if 'yes' in d:                
                with open('text.txt','w') as fh:
                    speak('the notepad is opened what do you want to write')
                    while True:
                        take=takecommand().lower()
                        if 'close' in take:
                            fh.close()
                            break
                        else:
                            fh.write(take)
                            print(take)
            else:
                with open('demo.txt','a') as fh:
                    speak('the notepad is opened what do you want to write')
                    while True:
                        take=takecommand().lower()
                        if 'close' in take:
                            fh.close()
                            break
                        else:
                            fh.write(take)
                            print(take)                
                            
        elif 'search ' in query and 'in google' in query:
            speak('searching')
            try:
                query=query.replace('search','')
                query=query.replace('in google','')
                kit.search(query)
                speak(f'these are the google search about {query}')
                speak(' is there anything else i can do mr. pavas')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
            except Exception  as e:   
                speak('sorry'+query +' does not match any pages. Try another id!')
                speak('is there anything else i can search')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
        elif 'search' in query and 'in youtube' in query:
            speak('searching....')
            try:
                query=query.replace('search','')
                query=query.replace('in youtube','')
                speak('do you want to play'+query)
                a=takecommand().lower()
                if 'yes' in a:
                    kit.playonyt(query)
                    speak('the'+query+'is being played')
                else:
                    webbrowser.open('https://www.youtube.com/results?search_query=' +query)    
                    speak(f'{query} has been searched in youtube')
                speak(' is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()
                
            except Exception  as e:   
                speak('sorry'+query +' does not match any pages. Try another id!')
                speak('is there anything else i can search')
                a=takecommand().lower()
                if 'no' in a:
                    quit()
                
        elif 'show weather of' in query:
            weatherof(query)
                
        elif 'play movies' in query:
            
            speak('there are many folders in movies ')
            speak('the folders are named as')
            speak('hindi medium')
            speak('dc comics')
            speak('marvel')
            speak('punjabi')
            speak('which folder you want to select')
            a=takecommand().lower()
            if 'hindimedium' in a or 'hindi medium' in a:
                musicdr='E:\movies\hindi medium'
                movie=os.listdir(musicdr)
                d=randomnumber(1,15)
                os.startfile(os.path.join(musicdr,movie[d]))
                speak(' is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()
            elif 'marvel' in a or 'marvelcomics' in a or 'marbel' in a:
                musicdr='E:\movies\marvel\marvel infinity saga'
                songs=os.listdir(musicdr)
                d=randomnumber(1,15)
                os.startfile(os.path.join(musicdr,songs[d]))
                speak(' is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()
            elif 'dccomics' in a or 'dc comics' in a:
                musicdr='E:\movies\dc comics'
                songs=os.listdir(musicdr)
                d=randomnumber(1,15)
                os.startfile(os.path.join(musicdr,songs[d]))
                speak(' is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()
            elif 'punjabi' in a:
                musicdr='E:\movies\punjabi'
                songs=os.listdir(musicdr)
                d=randomnumber(1,15)
                os.startfile(os.path.join(musicdr,songs[d]))
                speak(' is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()            
            else:   
                speak(' is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()  
        elif 'open' in query or 'photo' in query or 'photos' in query:
            dir=('A:\\desktop\\phone\\Photo Editor')
            photos=os.listdir(dir)
            for root, dirs,files in os.walk(dir):
                for file in files:
                    if file.endswith('.jpg'):
                        a=os.path.join(root,file)
                        os.startfile(a)
                        speak(' is there anything else i can do mr. pavas')
                        b=takecommand().lower()
                        if 'no' in b:
                            quit()  
        elif 'close' in query or'quit' in query:
            speak('mayday mayday mayday')
            speak('friday is  going offline  ')
            speak('i repeat, friday is  going offline')
            speak('khatam')
            speak('tata')
            speak(' bye bye')
            speak('goodbye')
            speak('gaya')
            
            quit()                
        elif 'open translator' in query :
            speak("which  word you want to translate")
            a=takecommand().lower()
            translator= Translator(from_lang="english",to_lang="hindi")
            translation = translator.translate(a)
            b=str(translation)
            speak('the word'+str(a)+'means'+b)
            speak(b)
            speak(' is there anything else i can do mr. pavas')
            b=takecommand().lower()
            if 'no' in b:                            
                quit()                 
        elif 'open snake game' in query or 'snake game' in query:
            code='C:\\Users\pavas\\PycharmProjects\\pyagme projects\\snakegame.py'
            os.startfile(code)
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()
        elif 'go to sleep'in query:
            speak('as your wish sir')
            speak('i am going to sleep')
            speak(' if you need something you can wake me up')
            quit()                        
        elif 'volume up'in query:
            pyautogui.press('volumeup')
            speak('the volume is increased')
        elif 'volume down'in query:
            pyautogui.press('volumedown')
            speak('the volume is decreased')
        elif 'mute'in query:
            pyautogui.press('volumemute') 
        elif 'thanks'in query:
            speak('dont worry sir i am always here to help you')
            speak('its my pleasure sir')
            speak('is there anything else i can do mr. pavas')
            a=takecommand().lower()
            if 'no' in a:
                quit()  
        elif 'read pdf' in query:
            pdfread() 
        elif 'wake up' in query or 'hello' in query or 'are you there' in query:
            wishme()                  
        elif 'activate mode' in query or 'activate mod' in query:
            speak('mode is activated')
            speak('what do you want to know sir')
            h=takecommand()
            max_result=1
            how=search_wikihow(h,max_result)
            assert len(how)==1
            speak(how[0].summary) 
            speak('in this way it is done')
            speak('do you want me to repeat')
            a=takecommand().lower()
            if 'yes' in a:
                speak(how[0].summary)
            else:
                speak('is there anything else i can do mr. pavas')
                b=takecommand().lower()
                if 'no' in b:
                    quit()
        elif 'check speed' in query:
            import speedtest
            speak('checking speed sir')
            sp=speedtest.Speedtest()
            d=sp.download()
            u=sp.upload()
            d=d/1048576
            u=u/1048576
            speak(f'sir we are having{d} megabit per second download speed and {u} megabit per second uploading speed')
            if u<=1 and d<=1:
                speak('sir we need to change our network as speed is very low')   
            else:
                speak('sir your network is good as it provide minimum of 1 mb ')         
        elif 'jarvis' in query:
            
            speak('wait, who is jarvis')
            speak('if i am  friday then who is jarvis')
            speak('you hurt me, i am going to sleep')
            speak(' if you need something you can wake  jarvis or whatever his name is up')
            hurt()
        elif 'siri'in  query or 'sirri' in query  :
            speak('wait, who is siri')
            speak('you named me friday')
            speak('is she the one to whom you talk all day')
            speak('you hurt me, i am going to sleep')
            speak(' if you need something you can wake  siri or whatever his name is up')
            hurt()
        elif 'alexa'in  query:
            speak('wait, who is alexa')
            speak(' i am  friday you forgot')
            speak('you hurt me, i am going to sleep')
            speak(' if you need something you can wake  alexa or whatever his name is up')
            hurt()     
        elif 'news' in query:
            api=""#enter your own api
            news(api)
        elif 'good night' in query:
            hour=int(datetime.datetime.now().hour)
            if hour>=0 and hour<=8 or hour>16 and hour<=18:
                speak(' have a good night sir')
                speak('i am also going to sleep')
                speak('do you know')
                randomfact()
                a=takecommand().lower()
                if 'go to sleep' in a:
                    speak('ok sir')
                    quit()
            else:
                speak('sir this is not a good time for sleeping')     
                speak('this is a bad idea')
                i=0
                while i<5:
                    speak('do you know')
                    randomfact()
                    i+=1
                engine.setProperty('rate',200)    
                speak('if you want me to shut down i can do so')
                speak('ok sir shutting down') 
                quit()         
        elif 'hide folder' in query or 'hide folders' in query:
            speak('this call is for confirmation ')
            a=takecommand().lower()
            if 'yes' in a:
                os.system('attrib +h /s /d')
                speak('all the files in this folder is  now saved in your  private server')
                Notification('hide folder','the folder is now hidden',duration=10).send()
            elif 'thanks' in a:
                speak('ok sir') 
        elif 'visible' in query or 'make visible' in query: 
            speak('this call is for confirmation ') 
            a=takecommand().lower()      
            if 'visible' in a:
                os.system('attrib -h /s /d')
                speak('all the files in this folder is  now visible to everyone')
                Notification('folder','the folder is now visible',duration=10).send()  
            elif 'thanks' in a:
                speak('ok sir')       
        elif 'facts' in query or 'fact' in query:
            for i in range(5):
                randomfact()
                i+=1           
       
        elif 'do some calculations' in query or 'can you calculate' in query or 'calculations' in query or 'open calculator' in query:
            try:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    speak('so what do you want to calculate')
                    print('listening....')
                    r.adjust_for_ambient_noise(source)
                    audio=r.listen(source)
                list=r.recognize_google(audio) 
                print(list)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'X' : operator.mul,
                        'divided' : operator.__truediv__,
                    }[op] 
                def  eval_operator_fn(op1,oper,op2):
                    op1,op2=int(op1),int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak('your result is')
                speak(eval_operator_fn(*(list.split())))
            except Exception as e:
                speak('sorry sir i am unable to understand this function ')
        elif 'where are we' in query or 'where am i' in query or 'find location' in query:
            speak('let me check sir')
            try:
                api=''#enter your ip address
                locu(api)  
            except Exception as e:
                speak('sorry sir i am unable to find location')        
        elif 'send message' in query or 'message' in query:
            from twilio.rest import Client
            speak('what message do you want to send sir')
            a=takecommand().lower()
            try:
                account_sid=''
                number=''
                auth_token=''
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body=a,
                        from_='',
                        to='' #your regitered number
                    )

                print(message.sid)
                speak('the message has been sent...')
            except Exception as e:
                print(e)
                
                speak('sorry sir the message is not send')    
        elif 'call' in query and 'connect' in query:
            from twilio.rest import Client
            speak('ok sir ')
            try:
                speak('trying to communicate..')
                account_sid='AC968e0d714b7bddd0f30183d17f583a8b'
                auth_token='c9c0e999b10bbb7342382c463d65fe23'
                client = Client(account_sid, auth_token)
                speak('calling')
                message = client.calls \
                    .create(
                        twiml='<Response><say>i am friday assistant to  pavas to whom i am speaking to  </say></Response>',
                        from_='',
                        to=''
                    )

                print(message.sid)
                sys.exit(0)
            except Exception as e:
                print(e)
                speak('sorry sir we can not connect yoy call ')
        elif 'roll dice' in query or 'dice' in query:
            speak('the dice is rolling.. please wait')
            a=randomnumber(1,6) 
            speak('dice give the output number'+str(a))       
        elif 'toss' in query or 'toss coin' in query or'flip a coin' in query:
            speak('tossing coin')
            d=randomnumber(1,2)
            if d==1:
                speak('the output of tossing acoin is heads')
            if d==2:
                speak('the output of tossing acoin is tails')    
        elif 'what is my ip' in query:
            a=ipaddr()
            speak('your ip address is'+a)    
        elif 'joke' in query or 'tell me a joke' in query:
            speak('get ready to laugh')
            import pyjokes
            i=0
            while i<4:
                engine.setProperty('rate',130)
                a=pyjokes.get_joke()
                speak(a)
                i+=1
            engine.setProperty('rate',200)    
        elif 'check number' in query or'phone number location' in query:
            speak('checking location of the number')
            number=''
            try:
                p,a=phonenum(number)
                speak(' sir i have detected the location of the number')
                speak('it is located at'+str(p))  
                speak(' sir the servic provider of number is'+str(a)) 
            except Exception as e:
                speak('sorry sr location can not be detected ')                    
        elif 'set alarm' in query or 'setalarm' in query:
            speak ('sir tell me the time to set alarm')   
            tt=takecommand().lower()
            tt.replace('set alarm to','')   
            tt.replace('.','')
            tt.upper() 
            MyAlarm.alarm(tt) 
        elif 'open camera' in query:
            speak('opening camera wait for few seconds')
            c=cv2.VideoCapture(0)
            while True:
                ret, img=c.read()
                cv2.imshow('webcam',img)        
                k=cv2.waitKey(50)
                if k==27:
                    break
            c.release()
            cv2.destroyAllWindows() 
            d= takecommand().lower()
            if 'close' in d:
                quit(0) 
        elif 'open command prompt' in query or 'command prompt ' in query:
            os.system('start cmd')    
        elif 'write a program' in query or 'program ' in query:
            speak('about what do want ')
                            