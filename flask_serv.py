myapi = '2cba536a956bea45ab154761e21c770e66c92c80'
#print myapi
import json 
from watson_developer_cloud import VisualRecognitionV3
visual_recognition = VisualRecognitionV3('2016-05-20', api_key = myapi )
import os
from firebase import firebase
firebase = firebase.FirebaseApplication('https://ieee-arcshack.firebaseio.com/', None)
from flask import Flask
print 'imported'
app = Flask(__name__)
#app.debug = True
c = {}

def categorize(c):
    print 'in categoirze'
    mylen = min(len(c['images'][0]['classifiers'][0]['classes']), 3)
    #print mylen
    mystr = ''
    keywords = ['garbage', 'bin','dust','landfill','sewage','waste','can','dirty']
    for i in range(0,mylen):
         
        mystr = mystr +' ' + str(c['images'][0]['classifiers'][0]['classes'][i]['class'])
    #print mystr
    garbage_present = 0 
    if any(i in mystr for i in keywords):
        garbage_present = 1
    
    return garbage_present 


@app.route("/")
def hello():
    
    already_present = []   
    images = firebase.get('/Images', None)
       
    while( True ):
        
        for img in images:
            try:
                f = 0
                image_present = firebase.get('/image_ans', None)
                for  imgs in image_present : 
                    #print image_present[imgs]
                    
                    image_present[imgs] = json.loads(image_present[imgs])
                    
                    
                    #print img, image_present[imgs]['img_id']
                    if img == image_present[imgs]['img_id'] :
                        f = 1
                        break
                if f==1:
                    print 'found'
                    continue
                
                

                img_url =     images[img]['imageUrl']   
                res = (json.dumps(visual_recognition.classify(images_url = img_url), indent=2))
                c = json.loads(res)
                garbage = categorize(json.loads(res))
                latitude =       images[img]['latitude']
                longitude  =       images[img]['longitude']
                img_id = img

                #print 'ans is ', garbage
                data = {'img_id': img_id, 'latitude': latitude, 'longitude' : longitude,  'garbage': garbage}
                sent = json.dumps(data)
                result = firebase.post("/image_ans", sent)
                print 'inserted'
                
            except Exception as e: 
                print e
                break 
                #continue
        
        break
    
    return 'success'
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)