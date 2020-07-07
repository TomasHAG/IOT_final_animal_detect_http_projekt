from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import json

from twilio.rest import Client


# the following line needs your Twilio Account SID and Auth Token


# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number



password = 'password123' #password for more secure connection

class requestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Post triggered")

        if not self.headers['Authorization'] == password: # security check
            print("Wrong password")
            return

        req = (self.rfile.read(int(self.headers['content-length']))).decode('utf-8')
        req = json.loads(req)
        #print(req)
        if int(req["payload_fields"]["sensor_trigger"]) == 1:
            client = Client("ACfce62142ff5d83bf280a7eac274f45d8", "a4e4271930345f4db976d1485f38cdab")
            client.messages.create(to="+46704911238",
                        from_="+16193500841",
                        body=f'Animal in at device { req["dev_id"] } was triggered.')

def main():
    PORT = 9123 #define port
    server_address = ('', PORT) #address is this computers ip adress
    server = HTTPServer(server_address, requestHandler) #start server
    print(f'server running on port {PORT}')
    server.serve_forever()#run it until closed

if __name__ == '__main__':
    main()