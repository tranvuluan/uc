import socket
from zeroconf import ServiceInfo, Zeroconf

def register_service():
    desc = {'version': '1.0.0'}
    info = ServiceInfo(
        "_http._tcp.local.",
        "MyService._http._tcp.local.",
        addresses=[socket.inet_aton("192.168.1.100")],
        port=8080,
        properties=desc,
        server="my-device.local."
    )
    
    zeroconf = Zeroconf()
    zeroconf.register_service(info)
    try:
        input("Press enter to exit...\n\n")
    finally:
        zeroconf.unregister_service(info)
        zeroconf.close()

register_service()
