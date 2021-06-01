import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "PLEASE SIT STRAIGHT ",
            message= " DRINK WATER ONCE IN A HOUR ",
            app_icon = "E:\pycharm docs\imagedrawing\Iconsmind-Outline-Glass-Water.ico",
            timeout = 10
        )
        time.sleep(60*60)
