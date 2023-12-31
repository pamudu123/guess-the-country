from PySide6.QtCore import Signal, QObject
import numpy as np


class WorkerSignals(QObject):
    timer_time_signal    = Signal(int)
    raw_image_signal     = Signal(np.ndarray)
    process_image_signal = Signal(np.ndarray)
    # pointing_coordinate_signal = Signal(tuple)
    pointing_coordinate_signal = Signal(np.ndarray, tuple)
    pause_signal = Signal()
    hint_signal = Signal()
    map_detected_signal = Signal()


    


