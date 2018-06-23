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
