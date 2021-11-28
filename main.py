import gc
import socket
import network
from machine import Pin, PWM
from time import sleep_ms

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('jbuist_ext', '1055leonard')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


def listen_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    return s

def pct_to_duty(pct):
    pct /= 100
    min = 120
    max = 30
    duty = int((max-min)*pct + min)
    return duty

def claw_check():
    claw_servo.duty(pct_to_duty(0))
    led.on()
    sleep_ms(2000)
    led.off()
    sleep_ms(500)
    claw_servo.duty(pct_to_duty(100))
    led.on()
    sleep_ms(2000)
    led.off()
    claw_servo.duty(0)


print('Calling do_connect()')
do_connect()
led = Pin(2, Pin.OUT)

# Establish the claw
claw_servo = PWM(Pin(13), freq=50)
# Open it up.
claw_check()

print('Calling listen_server()')
s = listen_server(80)
last_pct = -1
while True:
    if gc.mem_free() < 102000:
        gc.collect()
    print('Waiting for connection')
    conn, addr = s.accept()
    print('Got it')
    req = conn.recv(1024)
    print('req: ', req)
    if req.startswith(b'GET /'):
        print('Got a GET request')
        qs = req.split(b' ')[1].decode('utf8')
        print(qs)
        if qs.startswith('/setpos/'):
            _, in_pct = qs.split('/setpos/')
            conn.send(b'HTTP/1.1 204\n\n')
            print('in_pct: ', in_pct)

            if in_pct == last_pct:
                continue

            last_pct = in_pct
            duty = pct_to_duty(int(in_pct))
            print('duty: ', duty)
            claw_servo.duty(duty)
            led.on()
            sleep_ms(2000)
            led.off()
            claw_servo.duty(0)
        else:
            conn.send(b'HTTP/1.1 404')
        conn.close()
    else:
        print('Got a strange request')
        conn.send(b'HTTP/1.1 400 Bad Request\n\n')
        conn.close()
