""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'router.us.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

# WiFi@OSU is unsecured, hence empty WIFI_PASS
# Register the MAC address here:
# https://mydevices.net.ohio-state.edu/guest/mydevices.php?url=https://mydevices.net.ohio-state.edu/%3f&_browser=1
print("WiFi MAC Address: ", end='')
print(ubinascii.hexlify(machine.unique_id(),'-').decode())

WIFI_SSID = 'WiFi@OSU'
WIFI_PASS = ''

# for US915
LORA_FREQUENCY = 903900000
LORA_GW_DR = "SF9BW125" # DR_1
LORA_NODE_DR = 1

# for EU868
'''
LORA_FREQUENCY = 868100000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5
'''
