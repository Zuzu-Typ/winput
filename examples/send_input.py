import winput

import time

# open the RUN menu (WIN + R)
winput.press_key(winput.VK_LWIN)
winput.click_key(winput.VK_R)
winput.release_key(winput.VK_LWIN)

time.sleep(0.5)

# enter "notepad.exe"
winput.click_key(winput.VK_N)
winput.click_key(winput.VK_O)
winput.click_key(winput.VK_T)
winput.click_key(winput.VK_E)
winput.click_key(winput.VK_P)
winput.click_key(winput.VK_A)
winput.click_key(winput.VK_D)
winput.click_key(winput.VK_OEM_PERIOD)
winput.click_key(winput.VK_E)
winput.click_key(winput.VK_X)
winput.click_key(winput.VK_E)
winput.click_key(winput.VK_RETURN)

time.sleep(1)

# enter "hello world"
winput.click_key(winput.VK_H)
winput.click_key(winput.VK_E)
winput.click_key(winput.VK_L)
winput.click_key(winput.VK_L)
winput.click_key(winput.VK_O)
winput.click_key(winput.VK_SPACE)
winput.click_key(winput.VK_W)
winput.click_key(winput.VK_O)
winput.click_key(winput.VK_R)
winput.click_key(winput.VK_L)
winput.click_key(winput.VK_D)
