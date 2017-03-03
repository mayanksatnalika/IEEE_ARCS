myapi = '2cba536a956bea45ab154761e21c770e66c92c80'
print myapi
import json 
from watson_developer_cloud import VisualRecognitionV3
visual_recognition = VisualRecognitionV3('2016-05-20', api_key = myapi )
import os
from flask import Flask
print 'mported'
app = Flask(__name__)

c = {}

def categorize(c):
    print 'in categoirze'
    mylen = min(len(c['images'][0]['classifiers'][0]['classes']), 3)
    print mylen
    mystr = ''
    keywords = ['garbage', 'bin','dust','landfill','sewage','waste','can','dirty']
    for i in range(0,mylen):
        print c['images'][0]['classifiers'][0]['classes'][i]['class']
        mystr = mystr +' ' + str(c['images'][0]['classifiers'][0]['classes'][i]['class'])
    print mystr
    return mystr 

@app.route("/",methods=["POST"])
def hello():
    
    img = Image.open(request.files['file'])
    return 'Success!'
    
    
    
    
    img_file = open("image.jpg", "rb") 
    res = (json.dumps(visual_recognition.classify(images_file = img_file), indent=2))
    c = json.loads(res)
    categorize(json.loads(res))
    return "Hello world!"





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)