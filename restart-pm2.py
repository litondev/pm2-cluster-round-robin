import os
import time

while True:
    os.system("npm run pm2-cluster-stop")
    os.system("npm run pm2-cluster-start")
    time.sleep(3)