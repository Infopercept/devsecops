import requests
import time
import datetime
from io import StringIO
import configparser

try:
    config = configparser.RawConfigParser()
    config.readfp(open('bas-vm.properties'))
    bas_url = config.get("Config", "basUrl")
    bas_key = config.get("Config", "basToken")
    vm_url = config.get("Config", "vmUrl")
    vm_key = config.get("Config", "vmtoken")
    vm_product_id = config.get("Config", "vmProductId")
    sleep_time = config.get("Config","sleepTime")
except:
    print("[Error] bas-vm.properties file not found or parsing error")


today = datetime.date.today()
next_month = today.replace(day=1) + datetime.timedelta(days=32)
today_formatted = today.strftime("%Y-%m-%d")
next_month_formatted = next_month.strftime("%Y-%m-%d")

def list_operations(url, api_key):
    url = f"{url}/api/v2/operations"
    headers = {"Content-Type": "application/json","Accept":"application/json","KEY":api_key}

    try:
        response = requests.get(url, headers=headers, verify=False)
    except Exception as e:
        print(e)
        return False

    result = response.json()
    return result

def get_report(url, api_key, op_id):
    url = f"{url}/plugin/debrief/json"
    headers = {"Content-Type": "application/json","Accept":"application/json","KEY":api_key}
    try:
        response = requests.post(url, headers=headers, json={"operations":[op_id]},verify=False)
    except Exception as e:
        print(e)
        return False

    return response.json()

def list_to_html(data:list): #handler func, used in parsed_report
    data_list = [f"<li>{i}</li>" for i in data]
    data_String = "<ul>" + "".join(data_list) + "</ul>"    
    
    return data_String

def json_to_html(data): #handler func, used in parsed_report
    data_String = "<ul>"
    
    for key,val in data.items():
        key = f"<li><b>{key}</b>"
        val = f"<i>{val}</i></li>"
        data_String += f"{key}: {val}"   
    
    data_String += "</ul>"
    return data_String

def parse_report(data):
    filename = data.get("filename")
    
    if len(data.get("json_bytes")) == 0:
        print("No data found")
        return False

    data = data.get("json_bytes")[0]
    host_groups = list_to_html([i.get("host") for i in data.get("host_group")])
    name = data.get("name")
    facts = list_to_html(data.get("facts"))
    adversary = json_to_html(data.get("adversary"))

    data_String = f"<b>Host Groups: </b>{host_groups}<br><b>Name: </b>{name}<br><b>Facts:</b> {facts}<br><b>Adversary:</b> {adversary}"
    
    return data_String

def forward_to_vm(vm_api,product_id,data):
    filename = data.get("filename")
    data = parse_report(data)
    url = f"{vm_url}/api/v2/engagements/"
    headers = {
        "Content-Type":"application/json",
        "Accept":"application/json",
        "Authorization":f"Token {vm_api}"
    }

    body = {
        "name": f"{filename}",
        "description": f"{data}",
        "product": int(product_id),
        "target_start": today_formatted,
        "target_end": next_month_formatted,
    }
    try:
        response = requests.post(url,headers=headers,json=body)
    except Exception as e:
        print(e)
        return False

    return response

def import_scan(vm_api,engagement_id,data):
    filename = data.get("filename")
    data = parse_report(data)
    url = f"{vm_url}/api/v2/import-scan/"
    headers = {
        "Authorization":f"Token {vm_api}",
    }

    data = StringIO(f"'findings':[{data}]")

    body = {
        'engagement': int(engagement_id),
        "scan_type": "Generic Findings Import",
    }

    session = requests.Session()
    try:
        response = session.post(url,headers=headers,data=body,files={"file":data},verify=False)
    except Exception as e:
        print(e)
        return False

def driver():
    try:
        while True:
            print("Checking for new operations...")
            ops = list_operations(bas_url,bas_key)
            existing_ops = open("ops.txt").read().splitlines()
            #print("Checkin if operation data was sent or not...")
            for op in ops:
                if op.get("id") not in existing_ops:
                    print("New operation found....\n Parsing Data...")
                    data = get_report(bas_url,bas_key,op.get("id"))
                    if data != False:
                        forward_to_vm(vm_key, vm_product_id, data)
                        print("Operation forwarded to vm, adding to ops.txt")
                        f = open("ops.txt","a")
                        f.write(op["id"]+"\n")
                    else:
                        print("No data found")
                else:
                    print(f"No new operation found...going to sleep for {sleep_time} secs...")
            time.sleep(int(sleep_time))
    except KeyboardInterrupt:
        print("Exiting...")
        exit()

print(driver())
