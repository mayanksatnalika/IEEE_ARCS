import json 
import os
print 'imported'
from flask import Flask
import tweepy
consumer_key = "###"
consumer_secret = " "
access_token = " "
access_secret = " "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
auth.secure = True
auth.set_access_token(access_token, access_secret)
import smtplib
app = Flask(__name__)
#app.debug = True
c = {}

 

@app.route("/")
def hello():
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("abc@gmail.com", "def")
    server.sendmail("abc@gmail.com", "def@gmail.com", 'Garbage accumulating for past few days, no action being taken')
    server.quit()
    print 'email sent'
    res  = api.update_status(status = '@bmcindiaxyz garbage accumualating for days! #swacchbharat')
        
    
    return 'success'
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)