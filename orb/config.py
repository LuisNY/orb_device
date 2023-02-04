# below are all the variables that can be configured for testing purposes

BASE_URL = 'http://0.0.0.0:8002'
IRISES_PATH = './irises/'

SIGNUP_URL = BASE_URL + '/signup'
REPORT_STATUS_URL = BASE_URL + '/status'

STATUS_REPORT_INTERVAL = 3  # secs
LIFE_EVENT_INTERVAL = 5  # secs

BATTERY_UPDATE_DELTA = -2  # secs
CPU_TEMP_DELTA = 1  # secs
CPU_USAGE_DELTA = 2  # secs
DISK_SPACE_DELTA = -2  # secs

BATTERY_RESET_VALUE = 100  # %
CPU_TEMP_RESET_VALUE = 20  # Celsius
CPU_USAGE_RESET_VALUE = 0  # %
DISK_SPACE_RESET_VALUE = 100  # %
