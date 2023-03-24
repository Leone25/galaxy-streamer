import network
import time
from microWebSrv import MicroWebSrv

from cosmic import CosmicUnicorn
from picographics import PicoGraphics, DISPLAY_COSMIC_UNICORN as DISPLAY

cu = CosmicUnicorn()
graphics = PicoGraphics(DISPLAY)

cu.update(graphics)

ssid = 'ssid'
password = 'pwd'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

def _acceptWebSocketCallback(webSocket, httpClient) :
    print("WS ACCEPT")
    webSocket.RecvBinaryCallback = _recvBinaryCallback
    webSocket.ClosedCallback = _closedCallback

def _recvBinaryCallback(webSocket, data) :
    memoryview(graphics)[:] = data
    cu.update(graphics)

def _closedCallback(webSocket) :
    print("WS CLOSED")

mws = MicroWebSrv(webPath="www/")
mws.WebSocketThreaded       = False
mws.MaxWebSocketRecvLen     = 4096
mws.AcceptWebSocketCallback = _acceptWebSocketCallback
mws.Start(threaded=False)

