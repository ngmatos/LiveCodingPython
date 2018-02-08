import paho.mqtt.publish as publish

class Publisher():
    
    def publishSingle(self, topic, message, hostname = "localhost"):
        publish.single(topic, message, 1, False, hostname)

    def publishMultiple(self, messages, hostname = "localhost"):
        publish.multiple(messages, hostname)