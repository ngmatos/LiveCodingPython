import paho.mqtt.client as mqtt

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
        
        print(log)
        print(filepath)
        print(code)

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
client.connect("192.168.11.10", 1883, 60)

client.loop_forever()