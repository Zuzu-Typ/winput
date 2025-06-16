# winput

winput provides a simple Python interface for capturing or sending keyboard and mouse input on Windows. It wraps functions from `user32.dll` so you can listen to events or automate input.

> **Warning**
> Do not record a user's input without their permission.

  
## About winput  
**winput must not be used to record the user's input without their consent\!**  
**winput** is supposed to **replace** the outdated extension [PyHook](https://pypi.org/project/pyHook/)\.  
  
## Installation

Install from PyPI:

    pip install winput

## Basic usage
  
To use winput in a script, you have to import the package `winput` using  

    import winput
  
or a wildcard import:  

    from winput import *
  
  

Here is a minimal example that prints every pressed key until Escape is hit:

```python
import winput


def on_key(event: winput.KeyboardEvent) -> int:
    print(event.vkCode)
    if event.vkCode == winput.VK_ESCAPE:
        return winput.WP_STOP

winput.hook_keyboard(on_key)
winput.wait_messages()
winput.unhook_keyboard()
```

See the [examples](examples/) directory for more scripts.

  
#### Capturing mouse input  
There are two ways you can get input from the mouse\.  
1\. You can get the current position of the mouse cursor using  

    get_mouse_pos() -> (x, y)
  
  
2\. You can hook onto the Windows message system to receive an Event every time   
the state of the mouse changes:  

    hook_mouse( callback_function )
  
The function will be supplied with a **MouseEvent** as it's only argument\.  

    class MouseEvent:
        position        # [length-2-tuple] the screen coordinates at which the event occured
        action          # [int] which type of event occured - can be any of the mouse-wParams (see below)
        time            # [int] time in ms since system startup
        additional_data # [int] information for specific mouse events (which X-Button, amount of mouse-wheel-movement)
        type            # [string] = "MouseEvent"
  
You **have to run a message loop** to use a hook\! \(see **\[Running a message loop\]** below\)  
  
Remember to unhook when you're done capturing by using:  

    unhook_mouse()
  
  
The following mouse\-wParams exist:  

    
    WM_MOUSEMOVE    = 0x0200 # the mouse has been moved
    
    WM_LBUTTONDOWN  = 0x0201 # left mouse button pressed
    WM_LBTTONUP     = 0x0202 # left mouse button released
    
    WM_RBUTTONDOWN  = 0x0204 # right mouse button pressed
    WM_RBUTTONUP    = 0x0205 # right mouse button released
    
    WM_MBUTTONDOWN  = 0x0207 # middle mouse button pressed
    WM_MBUTTONUP    = 0x0208 # middle mouse button released
    
    WM_MOUSEWHEEL   = 0x020A # mouse wheel moved
    WM_MOUSEHWHEEL  = 0x020E # mouse wheel moved (horizontal)
    
    WM_XBUTTONDOWN  = 0x020B # extra button pressed
    WM_XBUTTONUP    = 0x020C # extra button released
    
  
  
  
#### Capturing keyboard input  
If you want to monitor keyboard input you also have to hook onto the Windows message system\.  

    hook_keyboard( callback_function )
  
The function will be supplied with a **KeyboardEvent** as it's only argument\.  

    class KeyboardEvent:
        action  # [int] which type of event occured - can be any of the keyboard-wParams
        vkCode  # [int] virtual key code -- which key has been pressed
        time    # [int] time in ms since system startup
        type    # [string] = "KeyboardEvent"
  
You **have to run a message loop** to use a hook\! \(see *Running a message loop* below\)  
  
Again, remember to unhook when you're done capturing by using:  

    unhook_keyboard()
  
  
The following keyboard\-wParams exist:  

    
    WM_KEYDOWN      = 0x0100 # key pressed
    WM_KEYUP        = 0x0101 # key released
    
    WM_SYSKEYDOWN   = 0x0104 # system-key pressed
    WM_SYSKEYUP     = 0x0105 # system-key released
    
  

#### Return values for callback functions
The callback (hook) functions mentioned above are expected to return a **flag**.
The following flags exist:

Flag | Value | Meaning
-----|-------|--------
`WP_CONTINUE` | `0x00` | Continue normally
`WP_UNHOOK` | `0x01` | Remove this hook
`WP_STOP` | `0x02` | Stops the message loop
`WP_DONT_PASS_INPUT_ON` | `0x04` | Does not call any other hooks (i.e. input isn't passed on to other programs)

If the callback function returns `None`, `WP_CONTINUE` is assumed.  
  
**WARNING:** Using `WP_DONT_PASS_INPUT_ON` will also prevent the inputs to be passed on to Windows. If you do this for a mouse hook, the mouse will **not move** and you might loose control over your computer. Same goes for keyboard hooks. The keyboard events will **not be passed on** to the rest of your system. You may loose control over your computer.


#### Running a message loop  
If you're using a hook, you have to keep updating the Windows messages\.  
You can either do this by using   

    wait_messages()
  
to enter an infinite message loop, which you can stop by calling  

    stop()
  
  
Or you can have your own loop that repeatedly \(at least 100x per second\) calls  

    get_message()
  
  
  
#### Virtual Key Codes \(VK codes\)  
Virtual key codes or vk\_codes are numerical representations of given keys\.  
To get a list of all virtual key codes, take a look over [here](https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)\.  
All VK codes are members of the main `winput` module and the submodule `winput.vk_codes`\.  
If you want to import all the VK codes without performing a package\-wide wildcard import, you can use  

    from winput.vk_codes import *
  
  
You can also convert the virtual key codes to a literal representation using a predefined dict\.  

    vk_code_dict.get(vk_code, "VK_UNKNOWN") -> string
  
  
  
#### Sending mouse input  
To set the position of the mouse cursor, you can use  

    set_mouse_pos(x, y)
  
  
To make sure this also works with high DPI values, please use the DPI awareness functions below\.  
  
To move the mouse cursor by a given amount, you can use  

    move_mouse(dx, dy)
  
  
A mouse button can be pressed using  

    press_mouse_button(mouse_button)
  
and released using  

    release_mouse_button(mouse_button)
  
or pressed and released using  

    click_mouse_button(mouse_button)
  
  
The following mouse buttons exist:  

    
    LEFT_MOUSE_BUTTON   = LMB   = 1
    RIGHT_MOUSE_BUTTON  = RMB   = 2
    MIDDLE_MOUSE_BUTTON = MMB   = 4
    EXTRA_MOUSE_BUTTON1 = XMB1  = 8
    EXTRA_MOUSE_BUTTON2 = XMB2  = 16
  
  
The mousewheel can be moved using  
`move_mousewheel(amount[, horizontal = False])`  
  
#### Sending keyboard input  
To press a key, you can use  

    press_key(vk_code)
  
to release it, you can use  

    release_key(vk_code)
  
and to press and release it, you can use  

    click_key(vk_code)
  
  
  
#### DPI awareness  
To make the process running winput DPI aware, use the following function:  

    set_DPI_aware(per_monitor=True)
  
  
To get the DPI scaling factor for a given window handle \(HWND\), use  

    get_window_scaling_factor(hwnd)
  
  
### Example  
#### Capturing the mouse and keyboard  
```Python
import winput

def mouse_callback( event ):
    if event.action == winput.WM_LBUTTONDOWN:
        print("Left mouse button press at {}".format( event.position ))
    
def keyboard_callback( event ):
    if event.vkCode == winput.VK_ESCAPE: # quit on pressing escape
        return winput.WP_STOP
        # alternatively you could also call:
        # winput.stop()
        
print("Press escape to quit")
    
# hook input    
winput.hook_mouse( mouse_callback )
winput.hook_keyboard( keyboard_callback )

# enter message loop
winput.wait_messages()

# remove input hook
winput.unhook_mouse()
winput.unhook_keyboard()
``` 

#### Capturing keyboard without passthrough
```Python
import winput

def keyboard_callback(event : winput.KeyboardEvent) -> int:
  if event.key == winput.VK_ESCAPE:
    print("quitting")
    return winput.WP_UNHOOK | winput.WP_STOP
	
  print(winput.vk_code_dict.get(event.key, "VK_UNKNOWN"))
  
  return winput.WP_DONT_PASS_INPUT_ON
  
winput.hook_keyboard(keyboard_callback)
winput.wait_messages()
```

  
#### Sending input  

```Python
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
```
  
