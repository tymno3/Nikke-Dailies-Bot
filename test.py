from pyautogui import *
import pyautogui
import cv2
import time
import keyboard
import random
import numpy as np
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def get_image_coordinates(image_path):
    # Load the target image
    target_image = cv2.imread(image_path)

    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Search for the target image in the screenshot
    result = cv2.matchTemplate(screenshot_image, target_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Define a threshold value for matching
    threshold = 0.8

    # If the maximum value exceeds the threshold, return the coordinates
    if max_val >= threshold:
        # Get the coordinates of the matched image
        image_width, image_height = target_image.shape[1], target_image.shape[0]
        top_left = max_loc
        bottom_right = (top_left[0] + image_width, top_left[1] + image_height)

        # Calculate the center point of the matched image
        center_x = top_left[0] + image_width // 2
        center_y = top_left[1] + image_height // 2

        return (center_x, center_y)

    return None


def is_image_on_screen(image_path):
    coordinates = get_image_coordinates(image_path)
    return coordinates is not None


def click_on_image(image_path):
    coordinates = get_image_coordinates(image_path)
    if coordinates:
        # Perform a mouse click at the center of the matched image
        click(coordinates[0], coordinates[1])


def click_if_there(target_image_path):
    coordinates = get_image_coordinates(target_image_path)
    while coordinates == None:
        print("looking for {}", target_image_path)
        coordinates = get_image_coordinates(target_image_path)
        time.sleep(1)
    if coordinates:
        click_on_image(target_image_path)
        time.sleep(1)


if __name__ == "__main__":
    # bulletinboard
    click_if_there("pics/outpost.png")
    click_if_there("pics/bulletinboard.png")
    click_if_there("pics/dispatchall.png")
    click_if_there("pics/dispatch.png")
    time.sleep(1)
    click_if_there("pics/homebulletinboard.png")
    click_if_there("pics/home.png")

    # daily login shop
    click_if_there("pics/cashshop.png")
    click_if_there("pics/dailyloginsymbol.png")
    click_if_there("pics/dailytext.png")
    click_if_there("pics/dailyfreepackage.png")
    click_if_there("pics/cashshopclaimrewards.png")
    time.sleep(1)
    click_if_there("pics/home.png")

    # Send friend points
    click_if_there("pics/friends.png")
    click_if_there("pics/friendssendandreceive.png")
    click_if_there("pics/confirm.png")
    click_if_there("pics/x.png")

    # Claim Outpost defense
    click_if_there("pics/outpostdefense.png")
    click_if_there("pics/outpostdefenseclaim.png")
    click_if_there("pics/outpostdefenseclaim3.png")

    # Shop
    click_if_there("pics/shop.png")

    # General Shop
    click_if_there("pics/100sale.png")
    click_if_there("pics/buy.png")
    click_if_there("pics/outpostdefenseclaim2.png")
    click_if_there("pics/refresh.png")
    click_if_there("pics/confirm.png")

    click_if_there("pics/100sale.png")
    click_if_there("pics/buy.png")
    click_if_there("pics/outpostdefenseclaim2.png")

    # Arenashop from General Shop
    click_if_there("pics/arena shop.png")
    click_if_there("pics/codeManualArenaShop.png")
    click_if_there("pics/buy.png")
    click_if_there("pics/outpostdefenseclaim2.png")
    click_if_there("pics/codeManualArenaShop.png")
    click_if_there("pics/buy.png")
    click_if_there("pics/outpostdefenseclaim2.png")
    click_if_there("pics/codeManualArenaShop.png")
    click_if_there("pics/buy.png")
    click_if_there("pics/outpostdefenseclaim2.png")

    click_if_there("pics/home.png")

    # Go to ark
    click_if_there("pics/ark.png")

    # Get special rewards
    click_if_there("pics/specialreward.png")
    click_if_there("pics/claimarena.png")

    # Try having it do simulation room
    click_if_there("pics/simulationroom.png")
    click_if_there("pics/beginsimulation.png")
    click_if_there("pics/simulationroom5.png")
    click_if_there("pics/simulationroomc.png")
    click_if_there("pics/beginsimulationbutton.png")
    simulation_mode = True
    while simulation_mode:
        if is_image_on_screen("pics/simulationselect.png"):
            if is_image_on_screen("pics/simulationroomnormal.png"):
                print("Looking for normal then quick select")
                click_if_there("pics/simulationroomnormal.png")
                click_if_there("pics/quickbutton.png")
                time.sleep(1)
            elif is_image_on_screen("pics/simulationroomhard.png"):
                print("looking for hard")
                click_if_there("pics/simulationroomhard.png")
                click_if_there("pics/simulationroomstartbattle.png")
                time.sleep(30)
            elif is_image_on_screen("pics/simulationroomicu.png"):
                print("Looking for icu")
                click_if_there("pics/simulationroomicu.png")
                click_if_there("pics/simulationroomicurecover.png")
                click_if_there("pics/recoverconfirm.png")
                click_if_there("pics/confirm.png")
        elif is_image_on_screen("pics/simulationselectbuffs.png"):
            print("looking for chain levels")
            click_if_there("pics/simulationroomchainlevels.png")
            click_if_there("pics/confirm.png")
        elif is_image_on_screen("pics/simulationroomtapthespacetoclear.png"):
            print("looking for space to clear")
            click_if_there("pics/simulationroomtapthespacetoclear.png")
            time.sleep(2)
        elif is_image_on_screen("pics/simulationsavesimulation.png"):
            print("looking to end simulation")
            click_if_there("pics/simulationsavesimulation.png")
            click_if_there("pics/confirm.png")
            click_if_there("pics/simulationroomchainlevels.png")
            click_if_there("pics/confirm.png")
            click_if_there("pics/back.png")
            simulation_mode = False
        time.sleep(1)
