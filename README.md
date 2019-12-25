## Ubuntu Panel Indicator  


This library can be used to print the output of any script in the ubuntu unity panel.  

>Example: Network Speed Indicator 
```
from panel_indicator.indicator import PanelIndicator
import subprocess

class MyIndicator(PanelIndicator):
    """ abstract function(set_new_value) returns a string """
    """ update_interval in seconds """
    def __init__(self, update_interval):
        self.current_val = 0
        PanelIndicator.__init__(self, update_interval)
    
    def set_new_value(self):
        out, err = self.bash_script_runner("/home/ketankr9/bin/netusage.sh")
        
        old_val = self.current_val
        self.current_val = int(out.strip().decode('utf-8'))
        
        # convert bytes to megabytes
        val = (self.current_val*1.0 - old_val)/10**3
        val /= self.update_interval

        if val/10**3 >= 1.0:
            # convert megabytes to gigabytes
            val /= 10**3
            val = round(val, 1)
            val = str(val) + " MB"
        else:
            val = round(val, 1)
            val = str(val) + " KB"

        return val

MyIndicator(1.5)
```  
>Skeleton:
```
from panel_indicator.indicator import PanelIndicator

class MyIndicator(PanelIndicator):
    def __init__(self, update_interval):
        PanelIndicator.__init__(self, update_interval)
    
    # runs after every 1 seconds
    def set_new_value(self):
        return "yayy"

MyIndicator(1)
```
