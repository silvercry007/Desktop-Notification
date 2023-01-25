import time
from plyer import notification

if __name__ ==  "__main__":
    while True:
        notification.notify(
            title = "New Alert...!!",
            message = "Drink Water",
            timeout = 10
        )
        time.sleep(3600)