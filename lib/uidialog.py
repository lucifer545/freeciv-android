# Copyright (C) 2011 Michal Zielinski (michal@zielinscy.org.pl)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import osutil
import time

if osutil.is_desktop:
    import easygui
    
    def inputbox(text, default=''):
        return easygui.enterbox(text, default=default)
elif osutil.is_android:
    import pyjni
    
    def inputbox(text, default='', title=''):
        pyjni.make_input_dialog(title, text, default)
        
        while True:
            data = pyjni.get_dialog_retval()
            if data:
                n, rest = data.split(':', 1)
                print 'inputbox got:', rest
                if n == 'ok':
                    return rest
                else:
                    return None
            time.sleep(0.1)