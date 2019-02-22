# mf-lorawan-gateway
This repository contains the code for creating the LoRaWAN gateway necessary for the MicroFarm. Most of the code has been adapted from the following guide:
https://docs.pycom.io/tutorials/lora/lorawan-nano-gateway.

### Pycom LoPy 4
<img src="https://cdn.sparkfun.com//assets/parts/1/2/8/7/3/14674-Pycom_LoPy4_Development_Board-06.jpg" height="300" width="300" alt="Pycom LoPy 4">

We are currently using WiFi@OSU for Internet connectivity, which normally requires authentication through a captive portal. The captive portal can be bypassed by registering a MAC address here: https://mydevices.net.ohio-state.edu/guest/mydevices.php?_browser=1

For convenience, the MAC address of the Pycom device that runs this repo's code will be printed to the console at startup. Tip: any Pycom device's MAC address can be discovered by running the following Python code:

```
import machine
import ubinascii
ubinascii.hexlify(machine.unique_id(),'-').decode()
```

We recommend upgrading the device firmware after receiving any new Pycom board. Upgrading the firmware is accomplished by following the tutorial here: https://docs.pycom.io/gettingstarted/installation/firmwaretool.htm
