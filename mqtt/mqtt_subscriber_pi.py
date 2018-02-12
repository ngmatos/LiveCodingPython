import paho.mqtt.client as mqtt
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with code " + str(rc))

    client.subscribe("test")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8', 'ignore')

    if starts_with_date:
        filepath_code = get_filepath_code(payload)
        log = filepath_code[0].strip()
        filepath = filepath_code[1].strip()
        code = filepath_code[2].strip()
        
        if code.startswith('<!SOF!>') and code.endswith('<!EOF!>'):
            code = code.replace('<!SOF!>', '').replace('<!EOF!>', '').strip()

            f = open(filepath, 'w')
            f.write(code)
            f.close()

            print('Saved file')
            print('Executing file')
            
            path = os.getcwd() + delete_char_at(filepath, 0)
            print(path)
            run(path)
        
        #print(log)
        #print(filepath)
        #print(code)

def run(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())

def delete_char_at(string, n):
    begin = string[:n]
    end = string[n+1:]
    return begin + end

def starts_with_date(msg):
    import re
    regex = re.compile('\d\d\d\d')
    if re.match(regex, msg):
        return True
    return False

def get_filepath_code(msg):
    filepath = str(msg).split('->')
    return filepath

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.11.11", 1883, 60)

client.loop_forever()