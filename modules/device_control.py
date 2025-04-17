import paho.mqtt.client as mqtt
import asyncio

class DeviceControl:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect("broker.hivemq.com", 1883, 60)

    async def control_device(self, device_id, action):
        self.client.publish(f"jarvis/devices/{device_id}", action)
        return f"Команда отправлена: {action} для устройства {device_id}."