
from time import sleep
from flask import Flask,request, render_template
from flask.json import jsonify
import RPi.GPIO as GPIO
import netifaces


app = Flask(__name__)

def get_ip_address(interface_name):
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        if interface == interface_name:
            addresses = netifaces.ifaddresses(interface)
            ip_info = addresses.get(netifaces.AF_INET)
            if ip_info:
                ip_address = ip_info[0]['addr']
                return ip_address
    return None

# Specify the interface name you want the IP address for
    





class PostData:
    def __init__(self,onoff):
        self.onoff = onoff

@app.route("/")
def hello_world():
    return render_template('index.html',baseUrlFromFlask="http://172.16.8.60",portFromFlask=port_number)

@app.route("/on2")
def turnon():
    GPIO.output(5,GPIO.LOW)
    respData = { 'msg':'The Led has been turned on by Flask'}
    return jsonify(respData)

@app.route("/off2")
def turnoff():
    GPIO.output(5,GPIO.HIGH)
    respData = { 'msg':'The Led has been turned off by Flask'}
    return jsonify(respData)

@app.route("/on1")
def turnon2():
    GPIO.output(6,GPIO.HIGH)
    respData = { 'msg':'The Machine has been turned on by Flask'}
    return jsonify(respData)

@app.route("/off1")
def turnoff2():
    GPIO.output(6,GPIO.LOW)
    respData = { 'msg':'The Machine has been turned on by Flask'}
    return jsonify(respData)

@app.route("/toggle", methods=['POST'])
def handle_toggle():
    data = request.json
    myPostData = PostData(data['onoff'])
    if (myPostData.onoff == 1):
        GPIO.output(5,GPIO.HIGH)
        respData = { 'msg':'The Machine has been turned on by Flask'}
        return jsonify(respData)
    else:
        GPIO.output(5,GPIO.LOW)
        respData = { 'msg':'The Machine has been turned off by Flask'}
        return jsonify(respData)


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(6,GPIO.OUT)
    GPIO.output(5,GPIO.LOW)
    sleep(5)
    GPIO.output(5,GPIO.HIGH)
    GPIO.output(6,GPIO.LOW)
    


    interface_name = "wlan0"  # Replace with the desired interface name
    port_number = "5000"
    # Call the function to get the IP address
    
    current_ip = get_ip_address(interface_name)
    print("Current IP address: ",current_ip)
    
    
    app.run(host='0.0.0.0',port=port_number)
