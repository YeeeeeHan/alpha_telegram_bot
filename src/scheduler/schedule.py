import threading
import time

import schedule

from pendle import price_alert


# Create a separate thread for the schedule loop
def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_schedule():
    # Start the schedule checker
    schedule_thread = threading.Thread(target=schedule_checker)
    schedule_thread.start()

    # Schedule the message
    price_alert()
    schedule.every().minute.do(price_alert)
