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


def get_images_coordinates(image_path):
    # Load the target image
    target_image = cv2.imread(image_path)

    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Search for the target image in the screenshot
    result = cv2.matchTemplate(screenshot_image, target_image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(
        result >= 0.8
    )  # Find all locations with a match value above the threshold

    # If there are no matches, return None
    if len(locations[0]) == 0:
        return None

    # Get the coordinates of the matched image below the first occurrence
    image_width, image_height = target_image.shape[1], target_image.shape[0]
    x = locations[1][0]  # x-coordinate of the first occurrence
    y = locations[0][0] + image_height  # y-coordinate below the first occurrence

    return (x, y)


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
    i = 0
    while coordinates == None:
        i += 1
        print("looking for {}", target_image_path)
        coordinates = get_image_coordinates(target_image_path)
        time.sleep(1)
        if i >= 10:
            break
    if coordinates:
        click_on_image(target_image_path)
        time.sleep(1)


def click_image_below_another(image_path, reference_image_path):
    reference_coordinates = get_images_coordinates(reference_image_path)
    if reference_coordinates:
        reference_x, reference_y = reference_coordinates

        target_coordinates = get_images_coordinates(image_path)
        if target_coordinates:
            target_x, target_y = target_coordinates

            # Calculate the coordinates below the reference image
            target_y_below_reference = reference_y + (target_y - reference_y)

            # Perform a mouse click at the calculated coordinates
            pyautogui.click(target_x, target_y_below_reference)


def playGame(list):
    # bulletinboard
    if "Bulletin Board" in list:
        click_if_there("pics/outpost.png")
        click_if_there("pics/bulletinboard.png")
        click_if_there("pics/dispatchall.png")
        click_if_there("pics/dispatch.png")
        time.sleep(1)
        click_if_there("pics/homebulletinboard.png")
        click_if_there("pics/home.png")

    # daily login shop
    if "Daily Login Shop" in list:
        click_if_there("pics/cashshop.png")
        click_if_there("pics/dailyloginsymbol.png")
        click_if_there("pics/dailytext.png")
        click_if_there("pics/dailyfreepackage.png")
        click_if_there("pics/cashshopclaimrewards.png")
        click_if_there("pics/home.png")

    # Send friend points
    if "Send Friend Points" in list:
        click_if_there("pics/friends.png")
        click_if_there("pics/friendssendandreceive.png")
        click_if_there("pics/confirm.png")
        click_if_there("pics/x.png")

    # Claim Outpost defense
    if "Claim Outpost Defense" in list:
        click_if_there("pics/outpostdefense.png")
        # Wipeout
        click_if_there("pics/wipeout.png")
        time.sleep(2)
        if is_image_on_screen("pics/gemswipeout.png"):
            click_if_there("pics/exitwipeout.png")
        else:
            click_if_there("pics/wipeoutbutton.png")
            click_if_there("pics/afterwipeout.png")
            click_if_there("pics/leavewipeout.png")
        click_if_there("pics/outpostdefenseclaim.png")
        click_if_there("pics/outpostdefenseclaim3.png")
        time.sleep(3)

    # General Shop
    if "General Shop" in list:
        click_if_there("pics/shop.png")
        click_if_there("pics/100sale.png")
        click_if_there("pics/buy.png")
        click_if_there("pics/outpostdefenseclaim2.png")
        click_if_there("pics/refresh.png")
        if is_image_on_screen("pics/zerogems.png"):
            click_if_there("pics/confirm.png")
            click_if_there("pics/100sale.png")
            click_if_there("pics/buy.png")
            click_if_there("pics/outpostdefenseclaim2.png")
        else:
            click_if_there("pics/leaveshop.png")
        if "Arena Shop" not in list:
            click_if_there("pics/home.png")

    # Arenashop from General Shop
    if "Arena Shop" in list:
        if "General Shop" not in list:
            click_if_there("pics/shop.png")
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
    ark = False
    if (
        "Claim Special Rewards" in list
        or "Simulation Room" in list
        or "Tribe Tower" in list
        or "Arena" in list
    ):
        time.sleep(3)
        click_if_there("pics/ark.png")
        ark = True

    # Get special rewards
    if "Claim Special Rewards" in list:
        click_if_there("pics/specialreward.png")
        click_if_there("pics/claimarena.png")

    # Try having it do simulation room
    if "Simulation Room" in list:
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
            elif is_image_on_screen("pics/missionfailed.png"):
                exit()
            # Has a chance to get stuck
            elif is_image_on_screen("pics/samebuff.png"):
                click_image_below_another(
                    "pics/simulationroomchainlevels.png", "pics/activebufflist.png"
                )
                click_if_there("pics/confirm.png")
            time.sleep(4)

    # Arena
    if "Arena" in list:
        rookiearena = True
        specialarena = True
        click_if_there("pics/arena.png")
        click_if_there("pics/fivefreeattempts.png")
        while rookiearena:
            if is_image_on_screen("pics/free.png"):
                click_if_there("pics/free.png")
                click_if_there("pics/startbattle.png")
                time.sleep(10)
            elif is_image_on_screen("pics/arenatap.png"):
                click_if_there("pics/arenatap.png")
                time.sleep(3)
            elif is_image_on_screen("pics/arenanomorebattles.png"):
                click_if_there("pics/back.png")
                rookiearena = False
                time.sleep(3)
            time.sleep(2)
        click_if_there("pics/twofreeattempts.png")
        while specialarena:
            if is_image_on_screen("pics/free.png"):
                click_if_there("pics/free.png")
                click_if_there("pics/startbattle.png")
                time.sleep(10)
            elif is_image_on_screen("pics/arenatap.png"):
                click_if_there("pics/arenatap.png")
                time.sleep(3)
            elif is_image_on_screen("pics/arenanomorebattles.png"):
                click_if_there("pics/back.png")
                specialarena = False
                time.sleep(3)
            time.sleep(2)
        click_if_there("pics/back.png")
        time.sleep(2)
        click_if_there("pics/back.png")
        time.sleep(2)

    # Tribe Tower
    if "Tribe Tower" in list:
        tribe_tower = True
        time.sleep(4)
        click_if_there("pics/tribetower.png")
        time.sleep(2)
        while tribe_tower:
            if is_image_on_screen("pics/tribetowerattempts.png"):
                click_if_there("pics/tribetowerattempts.png")
            elif is_image_on_screen("pics/clicktribetower.png"):
                click_if_there("pics/clicktribetower.png")
                click_if_there("pics/tribetowerstart.png")
            elif is_image_on_screen("pics/nextstagetribetower.png"):
                click_if_there("pics/nextstagetribetower.png")
            # Currently leaves if any tribe tower levels fail
            elif is_image_on_screen("pics/missionfailed.png"):
                click_if_there("pics/backafteroperationfailed.png")
                time.sleep(4)
                click_if_there("pics/back.png")
                time.sleep(2)
                click_if_there("pics/back.png")
                tribe_tower = False
            elif is_image_on_screen("pics/tribetowernomore.png"):
                click_if_there("pics/back.png")
                time.sleep(2)
                click_if_there("pics/back.png")
                tribe_tower = False
            time.sleep(3)

    # Go back if in ark
    if ark:
        time.sleep(1)
        click_if_there("pics/home.png")

    exit()


if __name__ == "__main__":
    playGame()
