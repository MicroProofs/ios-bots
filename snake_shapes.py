from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


def square_loop(size, driver):
    # ---->
    actions = TouchAction(driver)
    actions.press(x=80, y=80)
    actions.wait(80)
    actions.move_to(x=180, y=80)
    actions.wait(170)
    actions.release()
    actions.perform()
    time.sleep(size)
    # |
    # |
    # |
    # v
    actions = TouchAction(driver)
    actions.press(x=80, y=80)
    actions.wait(80)
    actions.move_to(x=80, y=180)
    actions.wait(170)
    actions.release()
    actions.perform()
    time.sleep(size)

    # <------
    actions = TouchAction(driver)
    actions.press(x=180, y=80)
    actions.wait(80)
    actions.move_to(x=80, y=80)
    actions.wait(170)
    actions.release()
    actions.perform()
    time.sleep(size)

    # ^
    # |
    # |
    # |
    # |
    # |
    actions = TouchAction(driver)
    actions.press(x=80, y=180)
    actions.wait(80)
    actions.move_to(x=80, y=80)
    actions.wait(170)
    actions.release()
    actions.perform()
    time.sleep(size)


def hourglass_loop(size, driver):
    turn_time = size * 1000
    turn_double = size * 2000
    #      ^
    #     /
    #    /
    #   /
    #  /
    # /

    actions = TouchAction(driver)
    actions.press(x=80, y=80)
    actions.wait(40)
    actions.move_to(x=130, y=280)
    actions.wait(turn_double)
    actions.release()
    actions.perform()

    # |
    # |
    # |
    # v
    actions = TouchAction(driver)
    actions.press(x=80, y=80)
    actions.wait(40)
    actions.move_to(x=80, y=180)
    actions.wait(turn_time)
    actions.release()
    actions.perform()

    # \
    #  \
    #   \
    #    \
    #     v
    actions = TouchAction(driver)
    actions.press(x=130, y=280)
    actions.wait(40)
    actions.move_to(x=80, y=80)
    actions.wait(turn_double)
    actions.release()
    actions.perform()

    # ^
    # |
    # |
    # |
    # |
    # |
    actions = TouchAction(driver)
    actions.press(x=80, y=180)
    actions.wait(40)
    actions.move_to(x=80, y=80)
    actions.wait(turn_time)
    actions.release()
    actions.perform()


def veritcal_line_loop(size, driver):
    turn_time = size * 1000
    # |
    # |
    # |
    #  v
    actions = TouchAction(driver)
    actions.press(x=80, y=80)
    actions.wait(40)
    actions.move_to(x=120, y=180)
    actions.wait(turn_time)
    actions.release()
    actions.perform()

    # ^
    #  |
    #  |
    #  |
    #  |
    #  |
    actions = TouchAction(driver)
    actions.press(x=320, y=380)
    actions.wait(40)
    actions.move_to(x=280, y=280)
    actions.wait(turn_time)
    actions.release()
    actions.perform()