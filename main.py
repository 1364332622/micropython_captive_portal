import gc
import network
import usocket
import uasyncio

html = """
<!DOCTYPE html><html><head><meta charset=utf-8 name=viewport content="width=device-width,height=device-height,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no"></head><div style=width:100%;text-align:center><h1>Welcome,my dear</h1><hr><h2>Welcome,my dear</h2><hr><p style="word-break:normal;word-wrap:break-word;border:1px solid #969696;"><br>Welcome,my dear<br><br><a href="Welcome, my dear"target="_blank"rel="noopener noreferrer">Welcome,my dear</a><br><br>Welcome,my dear<br><br><a href="Welcome, my dear"target="_blank"rel="noopener noreferrer">Welcome,my dear</a><br><br></p><h2>Welcome,my dear</h2><hr><h2>Welcome,my dear</h2><h2>Welcome,my dear<br>Welcome,my dear</h2></div></html>

"""


class DNSQuery:
    def __init__(self, data):
        try:
            self.data = data
            self.domain = ''
            tipo = (data[2] >> 3) & 15
            if tipo == 0:
                ini = 12
                lon = data[ini]
                while lon != 0:
                    self.domain += data[ini + 1:ini + lon + 1].decode('utf-8') + '.'
                    ini += lon + 1
                    lon = data[ini]
        except Exception:
            gc.collect()

    def response(self, ip):
        try:
            if self.domain:
                packet = self.data[:2] + b'\x81\x80'
                packet += self.data[4:6] + self.data[4:6] + b'\x00\x00\x00\x00'
                packet += self.data[12:]
                packet += b'\xC0\x0C'
                packet += b'\x00\x01\x00\x01\x00\x00\x00\x3C\x00\x04'
                packet += bytes(map(int, ip.split('.')))
            return packet
        except Exception:
            gc.collect()


def Create_Wifi():
    try:
        wifi_ssid = " 🌈SVIP_WIFI"
        wifi.config(essid=wifi_ssid, authmode=network.AUTH_OPEN)
        # wifi.config(essid=wifi_ssid, authmode=network.AUTH_WPA_WPA2_PSK, password="12345678")

        global ap_ip
        ap_ip = wifi.ifconfig()[0]
        gc.collect()
    except Exception:
        gc.collect()


class AP_Program:
    async def start(self):
        try:
            gc.collect()
            Loop = uasyncio.get_event_loop()
            Server = uasyncio.start_server(self.Http_Connection, ap_ip, 80)
            Loop.create_task(Server)
            Loop.create_task(self.Dns_Server())
            Loop.run_forever()
            gc.collect()
        except Exception:
            gc.collect()

    async def Http_Connection(self, reader, writer):
        try:
            Data = await reader.readline()
            Request_line = Data.decode()
            while True:
                gc.collect()
                line = await reader.readline()
                if line == b'\r\n':
                    break
            if len(Request_line) > 0:
                htmlstr = "HTTP/1.0 200 OK\r\n\r\n" + html
                await writer.awrite(htmlstr)
            await writer.aclose()
            gc.collect()
        except Exception:
            gc.collect()

    async def Dns_Server(self):
        try:
            udps = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
            udps.setblocking(False)
            udps.bind((ap_ip, 53))
            while True:
                gc.collect()
                try:
                    gc.collect()
                    if IS_V3:
                        yield uasyncio.core._io_queue.queue_read(udps)
                    else:
                        yield uasyncio.IORead(udps)
                    data, addr = udps.recvfrom(256)
                    DNS = DNSQuery(data)
                    udps.sendto(DNS.response(ap_ip), addr)
                except Exception:
                    break
            udps.close()
            gc.collect()
        except Exception:
            gc.collect()


while True:
    try:
        gc.enable()
        gc.collect()
        IS_V3 = hasattr(uasyncio, "__version__") and uasyncio.__version__ >= (3,)
        sta_if = network.WLAN(network.STA_IF)
        wifi = network.WLAN(network.AP_IF)
        sta_if.active(True)
        wifi.active(True)
        Create_Wifi()
        AP_Pro = AP_Program()
        if IS_V3:
            uasyncio.run(AP_Pro.start())
        else:
            Loop = uasyncio.get_event_loop()
            Loop.run_until_complete(AP_Pro.start())
    except Exception:
        gc.collect()
