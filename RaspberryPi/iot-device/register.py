import requests, time, json

class Register(object):
    def __init__(self, url, device):
        self.url = url
        self.device = device
        print url
    def __enter__(self):
        pass

    def get_register_body(self):
        id = self.device.cpu.get_sn()
        try:
            ip = self.device.network.get_ip_address('wlan0')
        except:
            ip = self.device.network.get_ip_address('eth0')
        msg_obj = {
            'cmd': 'register',
            'state': 'new',
            'id': id,
            'name': 'Room Device', 
            'ip': ip,
            'sensor_type': 'Thermal', 
            'additional': 'LED',
            'cpu_model': self.device.cpu.get_model(),
            'memory_size': self.device.memory.get_size(),
            'disk_size': self.device.disk.get_size(),
            'timestamp': int(time.time())
        }  
        body = json.dumps(msg_obj)  
        return body

    def register(self, token):
        body = self.get_register_body()
        response = requests.post(
            self.url, 
            headers={
                "Auth-Token":token, 
                "Content-Type":"application/json"
            }, 
            data=body
        )
        return response.status_code == 201

    def __exit__(self,  type, value, traceback):
        pass

if __name__ == "__main__":
    pass