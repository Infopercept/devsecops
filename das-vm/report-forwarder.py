import time
import configparser
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import requests
import datetime

#### variables ####
patterns = ["archini.json","zap.xml","nuclei.json"]
ignore_patterns = None   
ignore_directories = True
case_sensitive = True
my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

try:
    config = configparser.RawConfigParser()
    config.readfp(open('das-VM.properties'))
    vm_url = config.get("Config", "vmUrl")
    vm_token = config.get("Config", "vmtoken")
    vm_product_id = config.get("Config", "vmProductId")
    ssl_verify = config.get("Config", "sslVerify")
    path = rf'{config.get("Config", "reportDir")}'
except:
    print("[Error] das-VM.properties file not found or parsing error")

today = datetime.date.today()
next_month = today.replace(day=1) + datetime.timedelta(days=32)
today_formatted = today.strftime("%Y-%m-%d")
next_month_formatted = next_month.strftime("%Y-%m-%d")
##########

def add_engagement_vm(product, engagement_name):
    engagement_name_updated = engagement_name +  "-" + str(datetime.datetime.now())
    #print(engagement_name_updated)

    url = vm_url + "/api/v2/engagements/"
    headers = {"Content-Type": "application/json","Authorization": f"Token {vm_token}"}
    payload = {"name":engagement_name_updated,"product": product, "target_start": str(today_formatted),"target_end":str(next_month_formatted)} 

    try:
        response = requests.post(url, headers=headers, json=payload,verify=ssl_verify)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    if response.status_code == 201:
        return {"status": "success", "message": "Engagement created successfully","engagement_id": response.json()["id"]}
    else:
        return {"status": "error", "message": "Engagement creation failed", "status_code": response.status_code,"response": response.text}

def import_scan_vm(engagement_id, scan_type, file_path):
    url = vm_url + "/api/v2/import-scan/"
    headers = {"Authorization": f"Token {vm_token}"}
    payload = {"scan_type": scan_type,"engagement": int(engagement_id)}

    r = requests.post(url, headers=headers, data=payload, files={"file":(file_path, open(file_path, 'rb'))})
    print(r.status_code)

##VMDR API call##

def on_created(event):
    print(f"{event.src_path} has been created!")
    if "archini.json" in event.src_path:
        engagement = add_engagement_vm(vm_product_id, "Arachni")
        if engagement["status"] == "success":
            print("Engagement added successfully in VMDR")
            report = import_scan_vm(engagement["engagement_id"], "Arachni Scan", event.src_path)
            print("Reports forwarded to VM")
        else:
            print("Engagement adding failed in VMDR")
    elif "zap.xml" in event.src_path:
        engagement = add_engagement_vm(vm_product_id, "Zap")
        if engagement["status"] == "success":
            print("Engagement added successfully in VMDR")
            report = import_scan_vm(engagement["engagement_id"], "ZAP Scan", event.src_path)
            print("Reports forwarded to VM")
        else:
            print(engagement)
            print("Engagement adding failed in VMDR")
    elif "nuclei.json" in event.src_path:
        engagement = add_engagement_vm(vm_product_id, "Nuclei Scan")
        if engagement["status"] == "success":
            print("Engagement added successfully in VMDR")
            report = import_scan_vm(engagement["engagement_id"], "Nuclei Scan", event.src_path)
            print("Reports forwarded to VM")
        else:
            print(engagement)
            print("Engagement adding failed in VMDR")

####### WatchDog #######
my_event_handler.on_created = on_created

go_recursively = False
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
print("Monitoring..")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...")
    my_observer.stop()
    my_observer.join()
