from flask import Flask, request
from db_location import locationn
import datetime

app = Flask(__name__)

@app.route('/location',methods=[ 'GET'])
def location_api():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    timestamp = datetime.datetime.now()
    
    locationn(kecepatan=kecepatan,latitude=latitude,longitude=longitude,timestamp=timestamp)
    
    return{
        "kecepatan": kecepatan,
        "latitude": latitude,
        "longitude": longitude
    }

if __name__ == '__main__':
    app.run(debug=True)