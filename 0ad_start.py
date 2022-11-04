import subprocess

# 22-1104_1946-56 N.: ensure that you're in alpha26 with pidgin before connecting 0ad
p2 = subprocess.Popen("pidgin", shell=True)

p2 = subprocess.Popen("screenkey", shell=True) # something usefull for teaching

from pathlib import Path
home = str(Path.home())
c = home + "/git/0a26/binaries/system/pyrogenesis"

# dont wait till the proccess is edndet . 
from subprocess import Popen
p = Popen([c, '-writableRoot']) # something long running
# ... do other stuff while subprocess is running
# p.terminate()

time.sleep(.3)  # .2 works is maybe sometimes to fast
c = "pyrogenesis.pyrogenesis"
window.activate(c, False, True)
window.resize_move(c, xOrigin=1908, yOrigin=-27, width=1925, height=1089, matchClass=True)



if True:
    from plyer import notification
    notification.notify(
        title = "started ? :)",
        message = "hi from 0ad_start",
        timeout= 2,
        toast=False)
