from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from pyowm import OWM

import mysql_handler as mh


password = 'password321' #password for more secure connection

class requestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global password #import password
        print("POST triggered")

        if not self.headers['Authorization'] == password: # security check
            print("Wrong password")
            return

        #load info from content headern
        req = (self.rfile.read(int(self.headers['content-length']))).decode('utf-8')
        req = json.loads(req)

        location = 'Sjöbo,SE' #location of weather station
        owm = OWM('your api key here')   #api key for open weather api

        #init and get an wether observation
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(location)
        w = observation.weather

        time = req["metadata"]["time"]
        time = time.replace("T", " ")
        time = time.replace("Z", "")


        mh.input_data(req["dev_id"], req["payload_fields"]["pin_activ"], time,  w.temperature('celsius')['temp'],
                    w.wind()['speed'], w.humidity, w.clouds,
                    req["payload_fields"]["sensor_trigger"])


def main():
    PORT = 9321 #define port
    server_address = ('', PORT) #address is this computers ip adress
    server = HTTPServer(server_address, requestHandler) #start server
    print(f'server running on port {PORT}')
    server.serve_forever()#run it until closed

if __name__ == '__main__':
    main()
