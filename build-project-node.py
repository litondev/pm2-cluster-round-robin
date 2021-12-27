import os
import time

while True:
    # try edit server.js it will be downtime and handle by nginx :)
    os.system("sudo docker-compose up -d --build project-node")
    time.sleep(5)
    