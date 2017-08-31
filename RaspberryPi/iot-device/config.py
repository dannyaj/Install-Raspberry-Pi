import ConfigParser

class Config(object):

    def __init__(self):
        cfg = ConfigParser.ConfigParser()    
        cfg.read("config.ini")
        self.cfg = cfg

    def get_auth_url(self):    
        return self.cfg.get('Auth', 'url')

    def get_auth_username(self):    
        return self.cfg.get('Auth', 'username')

    def get_auth_password(self):    
        return self.cfg.get('Auth', 'password')

    def get_report_url(self):    
        return self.cfg.get('Report', 'url')

    def get_register_url(self):    
        return self.cfg.get('Register', 'url')

    def get_interval(self):    
        return float(self.cfg.get('Device', 'interval'))



    