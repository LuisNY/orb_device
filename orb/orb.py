import uuid
import requests
import hashlib
import os
import random
import threading
import time
import logging
from config import SIGNUP_URL, REPORT_STATUS_URL, IRISES_PATH, STATUS_REPORT_INTERVAL, LIFE_EVENT_INTERVAL, \
    CPU_TEMP_DELTA, BATTERY_UPDATE_DELTA, DISK_SPACE_DELTA, CPU_USAGE_DELTA, BATTERY_RESET_VALUE, CPU_TEMP_RESET_VALUE, \
    CPU_USAGE_RESET_VALUE, DISK_SPACE_RESET_VALUE


class VirtualOrb:

    def __init__(self):

        # set default values on orb device
        self.id = uuid.uuid1()  # unique id of the orb
        self.battery = BATTERY_RESET_VALUE  # available battery in %
        self.cpu_usage = CPU_USAGE_RESET_VALUE  # usage in %
        self.cpu_temp = CPU_TEMP_RESET_VALUE  # degrees Celsius
        self.disk_space = DISK_SPACE_RESET_VALUE  # avail space on disk in %

    @staticmethod
    def validate_max(value, metric):
        if value >= 100:
            raise Exception(f"Invalid value of {value} for metric {metric}, needs reset...")

    @staticmethod
    def validate_min(value, metric):
        if value <= 0:
            raise Exception(f"Invalid value of {value} for metric {metric}, needs reset...")

    def update_battery(self, delta=0, reset=False):
        self.battery = BATTERY_RESET_VALUE if reset else self.battery + delta
        self.validate_min(self.battery, 'battery')

    def update_cpu_values(self, usage=0, temperature=0, reset=False):
        self.cpu_temp = CPU_TEMP_RESET_VALUE if reset else self.cpu_temp + temperature
        self.cpu_usage = CPU_USAGE_RESET_VALUE if reset else self.cpu_usage + usage
        self.validate_max(self.cpu_usage, 'cpu usage')

    def update_disk_space(self, delta=0, reset=False):
        self.disk_space = DISK_SPACE_RESET_VALUE if reset else self.disk_space + delta
        self.validate_min(self.disk_space, 'disk space')

    def simulate_orb_usage(self):
        self.update_battery(delta=BATTERY_UPDATE_DELTA)
        self.update_disk_space(delta=DISK_SPACE_DELTA)
        self.update_cpu_values(usage=CPU_USAGE_DELTA, temperature=CPU_TEMP_DELTA)

    def simulate_orb_full_recharge(self):
        self.update_battery(reset=True)

    def simulate_orb_device_reset(self):
        self.update_battery(reset=True)
        self.update_disk_space(reset=True)
        self.update_cpu_values(reset=True)

    def do_report_status(self):

        data = {
            'battery': self.battery,
            'cpu_usage': self.cpu_usage,
            'cpu_temp': self.cpu_temp,
            'disk_space': self.disk_space,
            'id': str(self.id)
        }

        response = requests.post(REPORT_STATUS_URL, json=data)
        logging.info(response.text)

        self.simulate_orb_usage()

    def do_signup(self):

        # pick iris image from a pool of images
        irises = [f for f in os.listdir(IRISES_PATH) if os.path.isfile(os.path.join(IRISES_PATH, f))]
        iris_to_upload = irises[random.randint(0, len(irises)-1)]

        # Read the image into memory
        with open(IRISES_PATH + iris_to_upload, "rb") as f:
            image_data = f.read()

        # create an id for the image
        image_id = hashlib.sha256(image_data).hexdigest()
        data = {'id': str(image_id)}
        files = {"image": ("example.jpg", image_data)}

        response = requests.post(SIGNUP_URL, data=data, files=files)
        logging.info(response.text)

        self.simulate_orb_usage()

    def status_report_thread(self):
        # constantly report status every STATUS_REPORT_INTERVAL secs
        # every time report is sent, simulate usage
        while True:
            try:
                time.sleep(STATUS_REPORT_INTERVAL)
                self.do_report_status()
            except Exception as e:
                logging.warning(e)
                self.simulate_orb_device_reset()

    def activity_thread(self):
        # simulate activities every LIFE_EVENT_INTERVAL secs
        # an activity can be:
        # - simulate signup + usage
        # - simulate orb recharging
        # - simulate orb full reset
        while True:
            try:
                time.sleep(LIFE_EVENT_INTERVAL)

                # the probabilities for the events below are arbitrary
                event = random.randint(1, 10)
                if 1 <= event <= 8:
                    self.do_signup()
                elif event == 9:
                    self.simulate_orb_full_recharge()
                else:
                    self.simulate_orb_device_reset()
            except Exception as e:
                logging.warning(e)
                self.simulate_orb_device_reset()

    def do_live(self):

        # thread to continuously report status to API
        status_thread = threading.Thread(target=self.status_report_thread)

        # thread to simulate orb activity (signups, usage, recharge)
        activity_thread = threading.Thread(target=self.activity_thread)

        status_thread.start()
        activity_thread.start()

        status_thread.join()
        activity_thread.join()
