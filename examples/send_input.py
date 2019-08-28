import winput
from winput.vk_codes import *

import time

def slow_click(vk_code): # delay each keypress by 1/10 of a second
    time.sleep(0.1)
    winput.click_key(vk_code)

# open the RUN menu (WIN + R)
winput.press_key(VK_LWIN)
winput.click_key(VK_R)
winput.release_key(VK_LWIN)

time.sleep(0.5)

# enter "notepad.exe"
slow_click(VK_N)
slow_click(VK_O)
slow_click(VK_T)
slow_click(VK_E)
slow_click(VK_P)
slow_click(VK_A)
slow_click(VK_D)
slow_click(VK_OEM_PERIOD)
slow_click(VK_E)
slow_click(VK_X)
slow_click(VK_E)
slow_click(VK_RETURN)

time.sleep(1)

# enter "hello world"
slow_click(VK_H)
slow_click(VK_E)
slow_click(VK_L)
slow_click(VK_L)
slow_click(VK_O)
slow_click(VK_SPACE)
slow_click(VK_W)
slow_click(VK_O)
slow_click(VK_R)
slow_click(VK_L)
slow_click(VK_D)
