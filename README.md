# winput  
## Record keyboard and mouse input on Windows  
**winput** is a small **extension** gives you the ability to **record** any **keyboard and mouse input**\.  
It does this by providing a **simple interface** to **user32\.dll**  
  
## Tiny documentation  
### About winput  
**winput must not be used to record the user's input without their consent\!**  
**winput** is supposed to be a **replacement** for the outdated extension [PyHook](https://pypi.org/project/pyHook/)\.  
  
### Using winput  
In order to use winput's functionality you have to  

    import winput
  
  
  
If you want to monitor mouse input, you have to give winput a function to call\.  

    winput.hook_mouse( callback_function )
  
The function will be supplied with a **MouseEvent** as it's only argument\.  

    class MouseEvent:
    	position		# [length-2-tuple] the screen coordinates at which the event occured
    	action		  # [int] which type of event occured - can be any of the mouse-wParams
    	time			# [int] time in ms since system startup
    	additional_data	# [int] additional information for specific mouse events (which X-Button, amount of mouse-wheel-movement)
    	type			# [string] = "MouseEvent"
  
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
    
  
  
  
If you want to monitor keyboard input you also have to give winput a function to call\.  

    winput.hook_keyboard( callback_function )
  
The function will be supplied with a **KeyboardEvent** as it's only argument\.  

    class KeyboardEvent:
    	action			# [int] which type of event occured - can be any of the keyboard-wParams
    	vkCode			# [int] virtual key code -- which key has been pressed
    	time			# [int] time in ms since system startup
    	type			# [string] = "KeyboardEvent"
  
The following keyboard\-wParams exist:  

    
    winput.WM_KEYDOWN               = 0x0100 # key pressed
    winput.WM_KEYUP                 = 0x0101 # key released
    
    winput.WM_SYSKEYDOWN            = 0x0104 # system-key pressed
    winput.WM_SYSKEYUP              = 0x0105 # system-key released
    
  
You can convert the virtual key codes to string using a predefined dict\.  

    winput.all_vk_codes[ vkCode ] -> string
  
  
  
winput requires to be running an infinite message\-loop when recording input\.  

    winput.wait_messages()
  
Be sure to stop the loop from within your callback functions to stop recording\.  

    winput.stop()
  
  
  
Finally you have to release the hook from mouse and keyboard event queues\.  

    winput.unhook_mouse()
    winput.unhook_keyboard()
  
  
### Example  

    
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
    
