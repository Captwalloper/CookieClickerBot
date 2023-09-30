import time
import Keybind as KB
from CookieClicker import CookieClicker

CC = CookieClicker()
CC.Launch()
CC.Load()

def Main(canBuy: bool):
    CC.SpamClick(5)
    CC.PatrolGoldenCookie()
    if (canBuy):
        upgrades = CC.GetUpgrades()
        for u in upgrades:
            u.Buy()
        products = CC.GetProducts()
        print(products)
        products.reverse() # prefer latest building
        for p in products:
            p.Buy()

pause = False
def TogglePause():
    global pause
    pause = not pause
buyStuff = True
def ToggleUpgrades():
    global buyStuff
    buyStuff = not buyStuff
kill = False
def Kill():
    global kill
    kill = True
def Test():
    pass

KB.SetupKeybinds([
    KB.Keybind("q", Kill),
    KB.Keybind("m", TogglePause),
    KB.Keybind("u", ToggleUpgrades),
    KB.Keybind("t", Test),
], "h")

#Game Loop
while True:
    if (kill):
        CC.Close()
        break # exit game loop, end script
    elif (not pause):
        try:
            Main(buyStuff)
        except:
            pass
    else:
        time.sleep(0.01)
