TAKE_IMAGE= 0x00
START_CAPTURE = 0x01
STOP_CAPTURE = 0x02
GET_CAMERA_SETTINGS = 0x03
GET_MOTOR_SETTINGS = 0x04
SET_CAMERA_SETTINGS = 0x05
SET_MOTOR_SETTINGS = 0x06
SAVE_SETTINGS = 0x07
MOTOR_ADVANCE=0x08
MOTOR_ADVANCE_ONE=0x09
MOTOR_STOP=0x0A
TERMINATE = 0x0B
GET_CAMERA_SETTING = 0x0C
START_PREVIEW = 0x0D
CALIBRATE_HDR = 0x0E
OPEN_CAMERA = 0x0F
CLOSE_CAMERA = 0x10
CALIBRATE_CAMERA = 0x11
MOTOR_ON = 0x12
MOTOR_OFF = 0x13
PAUSE_CAPTURE=0x14
MOTOR_ON_TRIGGER=0x15
WHITE_BALANCE=0x16
TAKE_BGR=0x17
SET_MOTOR_SETTING=0x18
CALIBRATE_MOTOR=0x19
MAX_FPS=0x1A
MAX_SPEED=0x1B
GET_MOTOR_SETTING=0x1C

commands = [
"TAKE_IMAGE",
"START_CAPTURE",
"STOP_CAPTURE",
"GET_CAMERA_SETTINGS",
"GET_MOTOR_SETTINGS",
"SET_CAMERA_SETTINGS",
"SET_MOTOR_SETTINGS",
"SAVE_SETTINGS",
"MOTOR_ADVANCE",
"MOTOR_ADVANCE_ONE",
"MOTOR_STOP",
"TERMINATE",
"GET_CAMERA_SETTING",
"START_PREVIEW",
"CALIBRATE_HDR",
"OPEN_CAMERA",
"CLOSE_CAMERA",
"CALIBRATE_CAMERA",
"MOTOR_ON",
"MOTOR_OFF",
"PAUSE_CAPTURE",
"MOTOR_ON_TRIGGER",
"WHITE_BALANCE",
"TAKE_BGR",
"SET_MOTOR_SETTING",
"CALIBRATE_MOTOR",
"MAX_FPS",
"MAX_SPEED",
"GET_MOTOR_SETTING"
]

CAPTURE_BASIC=0
CAPTURE_ON_TRIGGER=1
CAPTURE_ON_FRAME=2

MERGE_NONE=0
MERGE_MERTENS=1
MERGE_DEBEVEC=2

MOTOR_FORWARD=0
MOTOR_BACKWARD=1

LAMP_ON=1
LAMP_OFF=0

HEADER_IMAGE=0
HEADER_COUNT=1
HEADER_MESSAGE=2
HEADER_STOP=3
HEADER_HDR=4
HEADER_BGR=5
HEADER_ANALYZE=6
HEADER_CALIBRATE=7


V2_RESOLUTIONS=('1920x1080','3280x2464','3280x2464','1640x1232','1640x922','1280x720','1280x720')
V1_RESOLUTIONS=('1920x1080','2592x1944','2592x1944','1296x972','1296*730','640*480','640*480')
V3_RESOLUTIONS=('1920x1080','2028x1520','4056x3040','1012x760')

CALIBRATION_NONE=1
CALIBRATION_FLAT=2
CALIBRATION_TABLE=3
