from flask import Flask, request
from device.device import Device


class Controller(object):
    device = ""

    @staticmethod
    def start():
        app.run(debug=False, host="0.0.0.0", port=3000)

    

app = Flask(__name__)

@app.route('/led', methods=['POST'])
def control_led():
    body = request.get_json(force=True)
    if body.get('power') == None:
        abort(400)

    try:
        Controller.device.addon.led.set(int(body.get('power')))
        return app.response_class(
            response="OK",
            status=200
        )
    except:
        return app.response_class(
            response="Failed",
            status=500
        )


if __name__ == "__main__":
    Controller.device = Device()
    Controller.start()

