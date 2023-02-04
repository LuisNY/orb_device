# below are all the variables that can be configured for testing purposes

BASE_URL = ' http://mock_server:8002'  # change this to whatever IP address the target server might be
IRISES_PATH = './irises/'

SIGNUP_URL = BASE_URL + '/signup'
REPORT_STATUS_URL = BASE_URL + '/status'

STATUS_REPORT_INTERVAL = 3  # secs
LIFE_EVENT_INTERVAL = 5  # secs

BATTERY_UPDATE_DELTA = -2  # %
CPU_TEMP_DELTA = 1  # Celsius
CPU_USAGE_DELTA = 2  # %
DISK_SPACE_DELTA = -2  # %

BATTERY_RESET_VALUE = 100  # %
CPU_TEMP_RESET_VALUE = 20  # Celsius
CPU_USAGE_RESET_VALUE = 0  # %
DISK_SPACE_RESET_VALUE = 100  # %
