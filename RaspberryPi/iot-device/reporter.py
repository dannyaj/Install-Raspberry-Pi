import requests, time, json

class Reporter(object):
    def __init__(self, url, device):
        self.url = url
        self.device = device

    def __enter__(self):
        pass

    def get_reporter_body(self):
        try:
            ip = self.device.network.get_ip_address('wlan0')
        except:
            ip = self.device.network.get_ip_address('eth0')
        msg_obj = {
            'id': self.device.cpu.get_sn(),
            'ip': ip,
            'cpu_temp': self.device.cpu.get_temps(),
            'cpu_usage': self.device.cpu.get_usage(),
            'memory_usage': self.device.memory.get_usage(),
            'disk_usage': self.device.disk.get_usage(),
            'traffic': self.device.network.get_traffic(),
            'temp': self.device.addon.get_thermal(),
            'led': self.device.addon.led.get(),
            'timestamp': int(time.time())
        }
        body = json.dumps(msg_obj)  
        return body

    def report(self, token):
        body = self.get_reporter_body()
        print "[Info - Reporter] report - %s" %body
        response = requests.post(
            self.url, 
            headers={
                "Auth-Token":token,
                "Content-Type":"application/json"
                }, 
            data=body)
        return response.text

    def __exit__(self,  type, value, traceback):
        pass

if __name__ == "__main__":
    pass