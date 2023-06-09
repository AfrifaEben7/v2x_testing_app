import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog
from PyQt5 import QtWidgets
import ctypes
from sys import platform
import time
import csv

# Get the current directory
current_dir = os.getcwd()

bool_check = False

if platform in ["linux", "linux2"]:
    se = ctypes.CDLL("../esmini/bin/libesminiLib.so")
    bool_check = True
elif platform == "darwin":
    se = ctypes.CDLL("../esmini/bin/libesminiLib.dylib")
elif platform == "win32":
    se = ctypes.CDLL("../esmini/bin/esminiLib.dll")
else:
    print(f"Unsupported platform: {platform}")
    quit()
    
# Define the structure for SEScenarioObjectState
class SEScenarioObjectState(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_int),
        ("model_id", ctypes.c_int),
        ("control", ctypes.c_int),
        ("timestamp", ctypes.c_float),
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
        ("z", ctypes.c_float),
        ("h", ctypes.c_float),
        ("p", ctypes.c_float),
        ("r", ctypes.c_float),
        ("roadId", ctypes.c_int),
        ("junctionId", ctypes.c_int),
        ("t", ctypes.c_float),
        ("laneId", ctypes.c_int),
        ("laneOffset", ctypes.c_float),
        ("s", ctypes.c_float),
        ("speed", ctypes.c_float),
        ("centerOffsetX", ctypes.c_float),
        ("centerOffsetY", ctypes.c_float),
        ("centerOffsetZ", ctypes.c_float),
        ("width", ctypes.c_float),
        ("length", ctypes.c_float),
        ("height", ctypes.c_float),
        ("objectType", ctypes.c_int),
        ("objectCategory", ctypes.c_int),
        ("wheelAngle", ctypes.c_float),
        ("wheelRot", ctypes.c_float),
    ]

# Define the relative paths from the current directory
esmini_folder_path = os.path.join(current_dir, "esmini")
scripts_folder_path = os.path.join(esmini_folder_path, "scripts")
replayer_path = os.path.join(esmini_folder_path, "bin/replayer")
resources_path = os.path.join(esmini_folder_path, "resources")
example_folder_path = os.path.join(esmini_folder_path, "EnvironmentSimulator/code-examples/hello_world")

# Create the main window as a QDialog
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        if bool_check:
            print("Running on Linux")
            uic.loadUi('gui.ui', self)
        else:
            uic.loadUi('xml_gui.ui', self)

        # Position the window in the top-right corner
        screen_geometry = QApplication.desktop().screenGeometry()
        window_geometry = self.geometry()
        self.setGeometry(screen_geometry.width() - window_geometry.width(), 0, window_geometry.width(), window_geometry.height())


        # Connect the "Load" button to the load_file function
        self.load_file.clicked.connect(self.load_file_function)
        self.stats.clicked.connect(self.stats_function)
        self.start.clicked.connect(self.start_function)
        self.replay.clicked.connect(self.replay_function)
        self.data.clicked.connect(self.data_function)

        # Get a reference to the LCD number and label widgets
        self.lcd_number = self.findChild(QtWidgets.QLCDNumber, 'time_target')
        self.lcd_number = self.findChild(QtWidgets.QLCDNumber, 't_speed_2')
        self.lcd_number = self.findChild(QtWidgets.QLCDNumber, 't_angle_2')
        self.lcd_number = self.findChild(QtWidgets.QLCDNumber, 'v_speed')
        self.lcd_number = self.findChild(QtWidgets.QLCDNumber, 'v_angle')

        # self.label1 = self.findChild(QtWidgets.QLabel, 't_speed')
        # self.label2 = self.findChild(QtWidgets.QLabel, 't_angle')
        # self.label3 = self.findChild(QtWidgets.QLabel, '')
        
        #changing background colors
        self.time_target.setStyleSheet("background-color: light-green;")
        self.t_speed_2.setStyleSheet("background-color: light-green;")
        self.t_angle_2.setStyleSheet("background-color: light-green;")
        self.v_speed.setStyleSheet("background-color: light-green;")
        self.v_angle.setStyleSheet("background-color: light-green;")
        
    def load_file_function(self):
        # Open a file dialog to choose a file to load
        
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '.', 'Text files (*.xosc)')
        if file_path:
            # Do something with the loaded file
            global path 
            path = file_path
            print('File loaded:', file_path)
                             
    def data_function(self):
        # Change to the current directory
        os.chdir(current_dir)
        command = "python pyqt.py"
        os.system(command)

    def stats_function(self):  # sourcery skip: inline-variable, last-if-guard

        os.chdir('../esmini')
        dat_path = self._extracted_from_replay_function_6()
        command = f"python ./scripts/plot_dat.py {dat_path} --param speed"
        comm = "chmod +x ./scripts/plot_dat.py"
        os.system(comm)
        os.system(command)      

    def replay_function(self):
        dat_path = self._extracted_from_replay_function_6()
        command = f'../esmini/bin/replayer --window 60 60 800 400 --res_path ./resources --file {dat_path}'

        os.system(command)


    def _extracted_from_replay_function_6(self):
        current_path = os.getcwd()
        scene = os.path.basename(path)
        name, ext = os.path.splitext(scene)
        new_filename = f"{name}.dat"       
        print(new_filename)

        return os.path.join(current_path, new_filename)
    def start_function(self):
        # Initialize the SE (Simulation Engine) with the selected file
        se.SE_Init(path.encode(), 0, 1, 0, 1)
        obj_state = SEScenarioObjectState()  # object that will be passed and filled in with object state info
        last_call_time = time.time()

        with open('mylog.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Time', 'ObjId', 's', 'x', 'y', 'heading', 'speed'])

            while not se.SE_GetQuitFlag():
                if time.time() - last_call_time >= 0.5:            
                        se.SE_GetObjectState(se.SE_GetId(j), ctypes.byref(obj_state))
                        self.time_target.display(obj_state.timestamp)
                        
                        if obj_state.id == 0:
                            self.v_speed.display(obj_state.speed)
                            self.v_angle.display(obj_state.wheelRot)

                        if obj_state.id == 1:
                            self.t_speed_2.display(obj_state.speed)
                            self.t_angle_2.display(obj_state.wheelRot)

                        data_row = [obj_state.timestamp, 
                                    obj_state.id,
                                    obj_state.s, 
                                    obj_state.x, 
                                    obj_state.y, 
                                    obj_state.h, 
                                    obj_state.speed * 3.6]
                        writer.writerow(data_row)
                        csvfile.flush()

                        last_call_time = time.time()
        
                print('Time {:.2f} ObjId s {:.2f} x {:.2f} y {:.2f} heading {:.2f} speed {:.2f} wheelAngle {:.2f} wheelRot {:.2f}'.format(
                            obj_state.timestamp, 
                            obj_state.id,
                            obj_state.s, 
                            obj_state.x, 
                            obj_state.y, 
                            obj_state.h, 
                            obj_state.speed * 3.6, 
                            obj_state.wheelAngle, 
                            obj_state.wheelRot))
                
                QApplication.processEvents()

                se.SE_Step()     
        # Call the data_function after the simulation is finished/quit           
        self.data_function()
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
    