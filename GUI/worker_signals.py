from PySide6.QtCore import Signal, QObject
import numpy as np


class WorkerSignals(QObject):
    live_image_signal = Signal(np.ndarray)
    pointing_coordinate_signal = Signal(np.ndarray, tuple)
    pause_signal = Signal()
    hint_signal = Signal()
    map_detected_signal = Signal()


    


