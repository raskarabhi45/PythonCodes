import pywhatkit as kit
import schedule  #ModuleNotFoundError: No module named 'schedule'
import time
import datetime


def Message():
    schedule.every(5).minutes.do(fun)  

    while(True): #unconditional infinite true
        schedule.run_pending()
        #same like lahan mulana zopvlyavr aaila tichi kame krta yetat   
        # time.sleep(1)  #for thir
 


kit.sendwhatmsg("+919763582314","Good Afternoon",13,25)