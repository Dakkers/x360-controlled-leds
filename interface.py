import serial, time
import XboxController

ser = serial.Serial('/dev/ttyACM0', 9600)

# def myCallBack(controlId, value):
#     print "Control id = {}, Value = {}".format(controlId, str(value).zfill(2))

# xboxCont = XboxController.XboxController(controllerCallBack = myCallBack)
xboxCont = XboxController.XboxController()

def callbackTemplate(buttonID):

    # a god awful name, sorry not sorry
    def returnCallback(value):
        ser.write(str(buttonID))
        ser.write(str(value))
        # print buttonID, value

    return returnCallback

aCallback = callbackTemplate(6)
bCallback = callbackTemplate(7)
xCallback = callbackTemplate(8)
yCallback = callbackTemplate(9)


xboxCont.setupControlCallback(xboxCont.XboxControls.A, aCallback)
xboxCont.setupControlCallback(xboxCont.XboxControls.B, bCallback)
xboxCont.setupControlCallback(xboxCont.XboxControls.X, xCallback)
xboxCont.setupControlCallback(xboxCont.XboxControls.Y, yCallback)

xboxCont.start()

time.sleep(15)

xboxCont.stop()