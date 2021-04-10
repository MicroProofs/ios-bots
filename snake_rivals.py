# iOS environment
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from multiprocessing import Process, Queue
from snake_shapes import square_loop, hourglass_loop, veritcal_line_loop


def run_loop(qu: Queue):
    desired_caps = dict(
        platformName="iOS",
        platformVersion="14.4",
        automationName="xcuitest",
        deviceName="iPhone 11 Pro Max",
        udid="",
        bundleId="com.supersolid.snake",
    )

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    size = 0
    while True:
        if (not size == 0) and qu.empty():
            hourglass_loop(size, driver)
        elif (not size == 0) and (not qu.empty()):
            message = qu.get()
            size = message
        elif qu.empty():
            driver.device_time
            time.sleep(5)
        else:
            message = qu.get()
            size = message


if __name__ == "__main__":

    g = 0
    started = False
    q = Queue()
    t = Process(target=run_loop, args=(q,))
    t.start()
    while True:
        if (not g == 0) and (not started):
            started = True
        elif (not g == 0) and started:
            g = int(input("Exit bot? "))
            q.put(g)
        else:
            g = int(input("Enter bot size: "))
            q.put(g)
            started = False
