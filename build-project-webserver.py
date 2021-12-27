import os
import time

while True:
    # nginx will reload config every 1 second and is smoothly :)
    os.system("sudo docker-compose exec -u root webserver nginx -s reload")
    time.sleep(1)