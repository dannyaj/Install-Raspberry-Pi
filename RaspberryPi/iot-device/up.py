from flask import Flask, request, flash, abort
import json, threading, time

from device.device import Device
from auth_token import AuthToken
from register import Register
from reporter import Reporter
from controller import *
from config import Config

config = Config()
AUTH_URL = config.get_auth_url()
AUTH_USERNAME = config.get_auth_username()
AUTH_PASSWORD = config.get_auth_password()
REPORT_URL = config.get_report_url()
REGISTER_URL = config.get_register_url()
INTERVAL = config.get_interval()

device = Device()
Controller.device = device
auth_token = AuthToken(AUTH_URL, AUTH_USERNAME, AUTH_PASSWORD)

def report(interval):
    print "[Info - Reporter] Thread Start"
    reporter = Reporter(REPORT_URL, device)
    while True:
        try:
            resp = reporter.report(auth_token.get_token())
            print resp
        except Exception as exception:
            print exception
            pass
        time.sleep(interval)

if __name__ == '__main__':
    register = Register(REGISTER_URL, device)
    while True:
        token = auth_token.get_token()
        if register.register(token) == True:
            print "[Info - Register] Register Success"
            print "[Info - Main] Sleep %s Seconds" %INTERVAL
            threading.Thread(target = report, args = {INTERVAL}, name = "reporter-thread").start()
            Controller.start()
            exit()
        else:
            print "Sleep 10 Seconds"
            time.sleep(INTERVAL)