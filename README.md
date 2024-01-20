# teac-remote-control
This project aims to use the RS-232C to control the TEAC reference 700 series devices, including VRDS-701T and UD-701N.

This project includes 2 parts, web app and a server. The web app renders a remote control in web browser and send http requests to server. Server sends tcp packets to a ethernet com device. The com device connects to the TEAC devices via RS-232C directly.

You can also use the web app to control Roon.

# Special thanks
Special thanks to [Jerry Wossion](https://github.com/jerrywossion) who helped a lot about Vue.

# Devices connection
1. [USR-N540 ethernet com server](https://www.pusr.com/products/4-port-serial-to-ip-converters-usr-n540.html)

    Connect com port 1 to VRDS-701T via a DB9 **NON-CROSS** cable.

    Connect com port 2 to UD-701N via a DB9 **NON-CROSS** cable.

    Set com port 1 work mode to TCP server with port 23.

    Set com port 2 work mode to TCP server with port 26.

    Connect the ethernet port to your router/switch. Go to the admin page and setup the ip address of the com server. Assume it should be 172.16.68.188 in this project.

# Deployment

1. Install dependencies
    - Node.Js 21
    - npm
    - python3
    - pip
    - fastapi
    - uvicorn
    - RoonCommandLine // only if you want to control roon

2. Copy trc-*.service to /etc/systemd/system. Service files are under web and servcer folders.
    - systemctl daemon-reload
    - systemctl start trc-*.service
    - systemctl enable trc-*.service

# References
1. [USR-N540 ethernet com server (EN)](https://www.pusr.com/products/4-port-serial-to-ip-converters-usr-n540.html)
2. [USR-N540 ethernet com server user manual (EN)](https://www.pusr.com/support/download/User-Manual-USR-N580-N540-N520-N510-User-Manual.html)
3. [USR-N540 ethernet com server (CN)](https://www.usr.cn/Product/328.html)
4. [USR-N540 ethernet com server user manual (CN)](https://www.usr.cn/Download/1087.html)
5. [TEAC reference 700 series](https://teac.jp/int/category/reference_700)
6. [TEAC VRDS-701T](https://teac.jp/int/product/vrds-701t/top)
7. [TEAC UD-701N](https://teac.jp/int/product/ud-701n/top)
8. [TEAC RS-232C control specification](https://teac.jp/downloads/products/teac/rs232c/teac_rs232c_r1.1.pdf)
9. [Roon](https://roon.app/en/)
10. [Roon Command Line](https://github.com/doctorfree/RoonCommandLine)
