# winput  
## Capture and send keyboard and mouse input on Windows  
**winput** is a small **extension** gives you the ability to **capture** and **send** any **keyboard and mouse input**\.  
It does this by providing a **simple interface** to **user32\.dll**  
  
## Tiny documentation  
### About winput  
**winput must not be used to record the user's input without their consent\!**  
**winput** is supposed to **replace** the outdated extension [PyHook](https://pypi.org/project/pyHook/)\.  
  
### Using winput  
To install winput you can use the PyPI:  

    pip install winput
  
To use winput in a script, you have to import the package 
    winput
 using  

    import winput
  
  
  
#### Capturing mouse input  
There are two ways you can get input from the mouse\.  
1\. You can get the current position of the mouse cursor using  

    get_mouse_pos() -> (x, y)
  
  
2\. You can hook onto the Windows message system to receive an Event every time   
the state of the mouse changes:  

    winput.hook_mouse( callback_function )
  
The function will be supplied with a **MouseEvent** as it's only argument\.  

    class MouseEvent:
    	position		# [length-2-tuple] the screen coordinates at which the event occured
    	action		  	# [int] which type of event occured - can be any of the mouse-wParams
    	time			# [int] time in ms since system startup
    	additional_data	# [int] additional information for specific mouse events (which X-Button, amount of mouse-wheel-movement)
    	type			# [string] = "MouseEvent"
  
You **have to run a message loop** to use a hook\! \(see below\)  
  
Remember to unhook when you're done capturing by using:  

    unhook_mouse()
  
  
The following mouse\-wParams exist:  

    
    winput.WM_MOUSEMOVE      = 0x0200 # the mouse has been moved
    
    winput.WM_LBUTTONDOWN    = 0x0201 # left mouse button pressed
    winput.WM_LBTTONUP       = 0x0202 # left mouse button released
    
    winput.WM_RBUTTONDOWN    = 0x0204 # right mouse button pressed
    winput.WM_RBUTTONUP      = 0x0205 # right mouse button released
    
    winput.WM_MBUTTONDOWN    = 0x0207 # middle mouse button pressed
    winput.WM_MBUTTONUP      = 0x0208 # middle mouse button released
    
    winput.WM_MOUSEWHEEL     = 0x020A # mouse wheel moved
    winput.WM_MOUSEHWHEEL    = 0x020E # mouse wheel moved (horizontal)
    
    winput.WM_XBUTTONDOWN    = 0x020B # extra button pressed
    winput.WM_XBUTTONUP      = 0x020C # extra button released
    
  
  
  
#### Capturing keyboard input  
If you want to monitor keyboard input you also have to hook onto the Windows message system\.  

    winput.hook_keyboard( callback_function )
  
The function will be supplied with a **KeyboardEvent** as it's only argument\.  

    class KeyboardEvent:
    	action			# [int] which type of event occured - can be any of the keyboard-wParams
    	vkCode			# [int] virtual key code -- which key has been pressed
    	time			# [int] time in ms since system startup
    	type			# [string] = "KeyboardEvent"
  
You **have to run a message loop** to use a hook\! \(see below\)  
  
Again, remember to unhook when you're done capturing by using:  

    unhook_keyboard()
  
  
The following keyboard\-wParams exist:  

    
    winput.WM_KEYDOWN               = 0x0100 # key pressed
    winput.WM_KEYUP                 = 0x0101 # key released
    
    winput.WM_SYSKEYDOWN            = 0x0104 # system-key pressed
    winput.WM_SYSKEYUP              = 0x0105 # system-key released
    
  
You can convert the virtual key codes to string using a predefined dict\.  

    winput.all_vk_codes[ vkCode ] -> string
  
  
  
#### Running a message loop  
If you're using a hook, you have to keep updating the Windows messages\.  
You can either do this by using   

    winput.wait_messages()
  
to enter an infinite message loop, which you can stop by calling  

    winput.stop()
  
  
Or you can have your own loop that repeatedly calls  

    get_message()
  
  
  
#### Sending mouse input  
To set the position of the mouse cursor, you can use  

    set_mouse_pos(x, y)
  
  
To move the mouse cursor by a given amount, you can use  

    move_mouse(dx, dy)
  
  
A mouse button can be pressed using  

    press_mouse_button(mouse_button)
  
and released using  

    release_mouse_button(mouse_button)
  
or pressed and released using  

    click_mouse_button(mouse_button)
  
  
The following mouse buttons exist:  

    
    winput.LEFT_MOUSE_BUTTON 	= winput.LMB 	= 1
    winput.RIGHT_MOUSE_BUTTON 	= winput.RMB 	= 2
    winput.MIDDLE_MOUSE_BUTTON 	= winput.MMB 	= 4
    winput.EXTRA_MOUSE_BUTTON1 	= winput.XMB1 	= 8
    winput.EXTRA_MOUSE_BUTTON2 	= winput.XMB2 	= 16
  
  
The mousewheel can be moved using  

    move_mousewheel(amount, [horizontal = False])
  
  
#### Sending keyboard input  
To press a key, you can use  

    press_key(vk_code)
  
to release it, you can use  

    release_key(ck_code)
  
and to press and release it, you can use  

    click_key(vk_code)
  
  
\[vk_code\] is a numerical representation of a given key\.  
To get a list of all virtual key codes, take a look over [here](https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)\.  
  
  
### Example  
#### Capturing the mouse and keyboard  

    
    import winput
    
    def mouse_callback( event ):
    	if event.action == winput.WM_LBUTTONDOWN:
    		print("Left mouse button press at {}".format( event.position ))
    	
    def keyboard_callback( event ):
    	if event.vkCode == winput.VK_ESCAPE: # quit on pressing escape
    		winput.stop()
    		
    print("Press escape to quit")
    	
    # hook input	
    winput.hook_mouse( mouse_callback )
    winput.hook_keyboard( keyboard_callback )
    
    # enter message loop
    winput.wait_messages()
    
    # remove input hook
    winput.unhook_mouse()
    winput.unhook_keyboard()
    
  
#### Sending input  

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
  
