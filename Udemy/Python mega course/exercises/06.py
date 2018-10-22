import datetime
import glob2

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","a") as file:
    for filename in glob2.glob("file*"):
        with open(filename, "r") as f:
            file.write(f.read())
