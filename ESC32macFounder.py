import network
import ubinascii

# Initialize the station interface
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Print the ESP32's own MAC address
my_mac = ubinascii.hexlify(sta_if.config('mac')).decode('utf-8')
print("My ESP32 MAC Address:", my_mac)

# Scan for available Wi-Fi networks
print("\nScanning for Wi-Fi networks...")
networks = sta_if.scan()  # Each result is a tuple: (ssid, bssid, channel, RSSI, security, hidden)

# Loop through and display SSID and MAC (BSSID) of each network
for net in networks:
    ssid = net[0].decode('utf-8')
    # Convert the bssid (a bytes object) to a human-readable hex string
    bssid = ubinascii.hexlify(net[1]).decode('utf-8')
    print("SSID: {}, BSSID: {}".format(ssid, bssid))