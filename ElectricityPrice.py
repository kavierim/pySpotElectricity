# Python program get electricity SPOT prive via 


import requests
import json
import time


# function to get the electricity price
# return the price in snt/kWh
# return None if error

def get_electricity_price():
    # get data from API
    url = 'https://api.spot-hinta.fi/JustNow'
    response = requests.get(url)

    # check if the request is OK
    if response.status_code != 200:
        return None

    # parse the response
    data = response.json()

    # get 'PriceWithTax' value
    return data['PriceWithTax'] * 100

# Get electricity consumption from the Shelly 3EM
# return the consumption in c, 3 phases, [phase1, phase2, phase3]
# return None if error

def get_electricity_consumption():
    # TODO
    return None

# main function
def main():
    # get electricity price every second and print it to the console with time when it changes

    # get the first price
    price = get_electricity_price()
    print(time.strftime('%H:%M:%S'), 'Price: ', price)

    # loop forever
    while True:
        # get the new price
        new_price = get_electricity_price()

        # check if the price has changed
        if new_price != None :
            if new_price != price:
                # print the new price with time
                print(time.strftime('%H:%M:%S'), 'Price: ', new_price)

                # update the price
                price = new_price

        # wait 1 second
        time.sleep(10)



if __name__ == '__main__':
    main()
