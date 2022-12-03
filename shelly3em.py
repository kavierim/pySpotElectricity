# this program reads power consumption from a Shelly 3EM

import requests
import json
import time
import datetime

# Shelly 3EM IP address
shelly3em_ip = "192.168.1.120"

# Shelly 3EM API URL
shelly3em_url = "http://" + shelly3em_ip + "/status"

# Electricity price in Euro per kWh
electricity_price = 0.25

# Total consumption for 1,2,3 phases
total_consumption = [0, 0, 0]

# hide cursor
print("\033[?25l", end="")

#unlimited loop
while True:
    # Shelly 3EM API request
    shelly3em_request = requests.get(shelly3em_url)

    # Shelly 3EM API response
    shelly3em_response = shelly3em_request.json()

    # Shelly 3EM power consumption from channel 1,2,3
    shelly3em_power1 = shelly3em_response["emeters"][0]["power"]
    shelly3em_power2 = shelly3em_response["emeters"][1]["power"]
    shelly3em_power3 = shelly3em_response["emeters"][2]["power"]
    total_power = shelly3em_power1 + shelly3em_power2 + shelly3em_power3
    # round total to 2 decimals
    total_power = round(total_power, 2)

    # Shelly 3EM total consumption from channel 1,2,3 in kWh
    total_consumption[0] += shelly3em_power1 / 3600000
    total_consumption[1] += shelly3em_power2 / 3600000
    total_consumption[2] += shelly3em_power3 / 3600000

    
    # Print power consumption
    # clear line
    print("\033[2K", end="")
    print("Power consumption channel 1: " + str(shelly3em_power1) + " W" + " Total: " + str(round(total_consumption[0], 4)) + " kWh" + " Cost: " + str(round(total_consumption[0] * electricity_price, 4)) + " Euro")
    print("\033[2K", end="")
    print("Power consumption channel 2: " + str(shelly3em_power2) + " W" + " Total: " + str(round(total_consumption[1], 4)) + " kWh" + " Cost: " + str(round(total_consumption[1] * electricity_price, 4)) + " Euro")
    print("\033[2K", end="")
    print("Power consumption channel 3: " + str(shelly3em_power3) + " W" + " Total: " + str(round(total_consumption[2], 4)) + " kWh" + " Cost: " + str(round(total_consumption[2] * electricity_price, 4)) + " Euro")

    # Print total power consumption
    print("\033[2K", end="")
    print("Total power consumption: " + str(total_power ) + " W" + " Total: " + str(round(total_consumption[0] + total_consumption[1] + total_consumption[2], 4)) + " kWh" + " Cost: " + str(round((total_consumption[0] + total_consumption[1] + total_consumption[2]) * electricity_price, 4)) + " Euro")

    # jump 5 lines up
    print("\033[4A", end="")

    # braek if CTRL+C
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        # print 3 lines down
        print("\033[E\033[E\033[E")
        # show cursor
        print("\033[?25h", end="")
        break

    # wait 1 second
    time.sleep(1)




