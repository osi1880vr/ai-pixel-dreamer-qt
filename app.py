import sys
from PyQt6 import QtWidgets, uic


from MainWindow import Ui_MainWindow

from widgets.sizer_count import Ui_txt2img
from widgets.twod_flip import TwoD_Flip
from widgets.threed_motion import ThreeD_Motion
from widgets.animation import Animation
from widgets.depth_warping import DepthWarping
from widgets.init_image import InitImage
from widgets.mask import Mask

from widgets.output import Output
from widgets.sampler import Sampler
from widgets.upscale import Upscale
from widgets.uploader import Uploader



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class OtherWindow(QtWidgets.QWidget, Ui_txt2img):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowTwoD_Flip(QtWidgets.QWidget, TwoD_Flip):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowTwoD_Flip, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowThreeD_Motion(QtWidgets.QWidget, ThreeD_Motion):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowThreeD_Motion, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowAnimation(QtWidgets.QWidget, Animation):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowAnimation, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowDepthWarping(QtWidgets.QWidget, DepthWarping):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowDepthWarping, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowInitImage(QtWidgets.QWidget, InitImage):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowInitImage, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowMask(QtWidgets.QWidget, Mask):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowMask, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowOutput(QtWidgets.QWidget, Output):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowOutput, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowSampler(QtWidgets.QWidget, Sampler):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowSampler, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowUpscale(QtWidgets.QWidget, Upscale):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowUpscale, self).__init__(*args, **kwargs)
        self.setupUi(self)

class OtherWindowUploader(QtWidgets.QWidget, Uploader):
    def __init__(self, *args, obj=None, **kwargs):
        super(OtherWindowUploader, self).__init__(*args, **kwargs)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.stackedWidget.setCurrentIndex(window.comboBox_5.currentIndex())
window.comboBox_5.currentIndexChanged.connect(
    lambda: window.stackedWidget.setCurrentIndex(window.comboBox_5.currentIndex()))

first = OtherWindow()
flip = OtherWindowTwoD_Flip()
motion = OtherWindowThreeD_Motion()
animation = OtherWindowAnimation()
depth_warping = OtherWindowDepthWarping()
init_image = OtherWindowInitImage()
mask = OtherWindowMask()
output = OtherWindowOutput()
sampler = OtherWindowSampler()
upscale = OtherWindowUpscale()
uploader = OtherWindowUploader()



window.show()

first.show()
flip.show()
motion.show()
animation.show()
depth_warping.show()
init_image.show()
mask.show()
output.show()
sampler.show()
upscale.show()
uploader.show()


app.exec()
