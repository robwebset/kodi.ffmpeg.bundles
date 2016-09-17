# -*- coding: utf-8 -*-
import os
import stat
import traceback
import xbmc
import xbmcaddon


ADDON = xbmcaddon.Addon(id='script.module.ffmpeg')


#########################
# Main
#########################
if __name__ == '__main__':
    # Check that the ffmpeg executable has executable permissions set
    try:
        # Get the location of the executable file
        modulePath = ADDON.getAddonInfo('path')
        execPath = os.path.join(modulePath, 'exec')
        ffmpegExec = os.path.join(execPath, 'ffmpeg')

        # Now make sure it is executable
        st = os.stat(ffmpegExec)
        # Only set execute permission if not already set
        if not (st.st_mode & stat.S_IEXEC):
            os.chmod(ffmpegExec, st.st_mode | stat.S_IEXEC)
    except:
        xbmc.log("Failed to set ffmpeg permissions: %s" % traceback.format_exc(), xbmc.LOGDEBUG)
