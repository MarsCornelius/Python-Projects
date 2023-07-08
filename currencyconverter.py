############################################################################
#                                                                          #
#                          Created By: Kibwe Gooding                       #
#                             Date: July 2nd 2023                          #
#                              A Simple Converter                          #
############################################################################

import requests


def get_exchange_rates():
    access_key = "92ea84f8cc54b829a17149d49e762d1a"
    base_currency = "CAD"

    url = f"http://data.fixer.io/api/latest?access_key={access_key}# &base={base_currency}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        curr_rates = data["rates"]
        return curr_rates
    else:
        print("API Error", "Failed to fetch exchange rates")
        return None


rates = get_exchange_rates()


def curr_converter():
    print("$$$$$FOREIGN CURRENCY CONVERT$$$$$$")
    print("Base Currency: EUR")
    curr_input = float(input("How much would you like to convert?: "))

    for currency, rate in rates.items():
        match currency:
            case 'CAD':
                conversion = f"{round(curr_input * rate, 2)}"
                print("Currency: CAD  ""Rate: " + str(rate) + " " + "Converted rate: " + str(conversion))

            case 'GBP':
                conversion = f"{round(curr_input * rate, 2)}"
                print("Currency: GBP  ""Rate: " + str(rate) + " " + "Converted rate: " + str(conversion))

            case 'KRW':
                conversion = f"{round(curr_input * rate, 2)}"
                print("Currency: KRW  ""Rate: " + str(rate) + " " + "Converted rate: " + str(conversion))

            case 'TTD':
                conversion = f"{round(curr_input * rate, 2)}"
                print("Currency: TTD  ""Rate: " + str(rate) + " " + "Converted rate: " + str(conversion))

            case 'USD':
                conversion = f"{round(curr_input * rate, 2)}"
                print("Currency: USD  ""Rate: " + str(rate) + " " + "Converted rate: " + str(conversion))


def metric_converter():
    print("*****METRIC CONVERTER*****")

    print("1. kg to lbs |2. ounces to grams |3. km to miles")
    category = int(input("What are you converting: "))
    if 0 < category < 3:
        amount = float(input("What is the value for conversion: "))

        match category:
            case 1:
                c_value = f"{round(amount * 2.20462, 2)}"
                print("The weight in lbs is " + c_value)

            case 2:
                c_value = f"{round(amount * 28.3495, 2)}"
                print("The weight in grams is " + c_value)

            case 3:
                c_value = f"{round(amount * 0.621371, 2)}"
                print("The distance in miles is " + c_value)
    else:
        print("Invalid entry. Goodbye.")
        exit()


print("1. Currency Converter 2. Metric Converter")
prompt = int(input("Good day. Which converter would you like to use? "))

if 0 < prompt < 3:
    match prompt:
        case 1:
            curr_converter()
        case 2:
            metric_converter()
else:
    print("Invalid entry. Goodbye.")
    exit()
