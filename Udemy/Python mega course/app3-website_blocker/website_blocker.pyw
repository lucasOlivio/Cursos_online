import time
from datetime import datetime as dt

host_path_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect  = "127.0.0.1"
website_list  = ["www.facebook.com","facebook.com", "www.hotmail.com"]

while True:
    with open(host_path_temp, 'r+') as file:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
            print("Trabaiaaa vagabuundo")
        else:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print("Trankiiilo")
    time.sleep(5)
