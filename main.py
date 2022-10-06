#from qt.main_ui import TwoD_Flip
from qt.main_window import Ui_MainWindow
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PIL import Image

import sys, traceback, time

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6.QtGui import QIcon, QPixmap

from diffusers import StableDiffusionPipeline

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done







class GenerateWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        #self.ui = TwoD_Flip()
        self.mw = qtw.QMainWindow()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        #self.show()

        self.ui.pushButton.clicked.connect(self.oh_no)
        #self.ui.pushButton.clicked.connect(self.generate)

    def generate(self, progress_callback):

        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token="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")
        pipe = pipe.to("cuda")
        def dummy_checker(images, **kwargs): return images, False
        pipe.safety_checker = dummy_checker

        prompt = "Astronaut riding a horse"

        # First-time "warmup" pass (see explanation above)
        _ = pipe(prompt, num_inference_steps=1)
        try:
            # Results match those from the CPU device after the warmup pass.
            image = pipe(prompt, num_inference_steps=4)['sample'][0]
            image.save("image.png")
        except Exception as e:
            print(e)

    def get_pic(self):
        pixmap = QPixmap("image.png")
        self.ui.label.setPixmap(pixmap)

    def oh_no(self):
        # Pass the function to execute
        worker = Worker(self.generate) # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.get_pic)

        # Execute
        self.threadpool.start(worker)




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    widget = GenerateWindow()
    widget.show()
    sys.exit(app.exec())
