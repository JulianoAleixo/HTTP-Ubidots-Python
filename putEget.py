#Exemplo para enviar dados para o Ubidots - HTTP
#Fonte: Help Ubidots.com
import time
import requests 

TOKEN = " "  # Put your TOKEN here
DEVICE_LABEL = " "  # Put your device label here 
VARIABLE_LABEL_1 = " "  # Put your first variable label here
VARIABLE_LABEL_2 = " "

def post_request(payloadPOST):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payloadPOST)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def get_request(payloadGET):
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    url = url + "/" + VARIABLE_LABEL_2 + "/lv"
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.get(url=url, headers=headers, json=payloadGET)
        status = req.status_code
        attempts += 1
        time.sleep(1)
    
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False
    
    variable_1 = req.json()

    print("[INFO] request made properly, your device returned a data")
    print("[DATA] " + str(variable_1))
    return True


def main():
    status = input("Digite P para post e G para get. ")
    
    if status == "P":
        data = input("Digite um valor ")
        payload = {VARIABLE_LABEL_1: data}


        print("[INFO] Attemping to send data")
        post_request(payload)
        print("[INFO] finished")
        
    if status == "G":
        payload = {} 
        print("[INFO] Attemping to get data")
        get_request(payload)
        print("[INFO] finished")
        
    
if __name__ == '__main__':
    while (True):
        main()
        time.sleep(10)
