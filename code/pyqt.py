import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QDialog, QVBoxLayout, QToolBar, QLabel, QSpacerItem, QSizePolicy
import pandas as pd
from PyQt5.QtGui import QColor
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import seting
class MyWindow(QMainWindow):



    def __init__(self): 
        super().__init__()


        # Create a QTableWidget to display the data
        self.table = QTableWidget()
        self.setCentralWidget(self.table)
        testbool = True
        # text = "PASSED: Perform next test"


        self.thresholds = {
            'diff_s': {'threshold': (2, -2), 'mean_threshold': (0.2, -0.2)},
            'diff_x': {'threshold': (0.2, -0.2), 'mean_threshold': (0.2, -0.2)},
            'diff_y': {'threshold': (0.2, -0.2), 'mean_threshold': (0.2, -0.2)},
            'diff_heading': {'threshold': (2, -2), 'mean_threshold': (0.2, -0.2)},
            'diff_speed': {'threshold': (1, -1), 'mean_threshold': (0.2, -0.2)}
        }

        # Load the data from the diff_df dataframe and round to 3 decimal places
        diff_df = pd.read_csv("summary.csv")
        data = diff_df.round(3)

        # Set the number of rows and columns in the table
        row_names = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
        # self.table.setRowCount(data.shape[0])
        self.table.setRowCount(len(row_names))
        self.table.setColumnCount(data.shape[1])

        # Set the font style and size for column names
        header_font = self.table.horizontalHeader().font()
        header_font.setBold(True)
        header_font.setPointSize(15)
        self.table.horizontalHeader().setFont(header_font)

        # Set the font style and size for row names
        row_font = self.table.verticalHeader().font()
        row_font.setBold(True)
        row_font.setPointSize(15)
        self.table.verticalHeader().setFont(row_font)




        # Populate the table with the data and row headings
        light_red = QColor(244, 76, 76)
        for i in range(data.shape[0]):
            item = QTableWidgetItem(str(data.index[i]))
            self.table.setVerticalHeaderItem(i, item)
            for j in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iloc[i, j]))

                if row_names[i] in ['mean', 'min', 'max'] and data.columns[j] in self.thresholds:
                    value = data.iloc[i, j]
                    threshold = self.thresholds[data.columns[j]]['threshold']
                    mean_threshold = self.thresholds[data.columns[j]]['mean_threshold']

                    if row_names[i] == 'mean':
                        if value > mean_threshold[0] or value < mean_threshold[1]:
                            item.setBackground(QColor(255, 128, 128))
                            testbool = False
                    elif row_names[i] in ['min', 'max']:
                        if value > threshold[0] or value < threshold[1]:
                            item.setBackground(QColor("magenta"))

                self.table.setItem(i, j, item)

        if testbool:
            self.test_result_label = QLabel("PASSED: Perform next test")
            self.test_result_label.setStyleSheet("color: green; font-weight: bold; font-size: 20px")
        else:
            self.test_result_label = QLabel("Failed Test, repeat")
            self.test_result_label.setStyleSheet("color: red; font-weight: bold; font-size: 20px")


        # Set the column headers
        self.table.setHorizontalHeaderLabels(data.columns)
        self.table.setVerticalHeaderLabels(row_names)


        # Create a Summary button
        self.summary_button = QPushButton('Log', self)
        self.summary_button.clicked.connect(self.show_summary)

        # Create a QToolBar for the result label
        result_toolbar = QToolBar()
        self.addToolBar(result_toolbar)



        self.toolbar2 = QToolBar()
        self.toolbar2.addWidget(self.test_result_label)



        # Create a QSpacerItem to add space between the button and label
        spacer = QSpacerItem(100, 50, QSizePolicy.Expanding, QSizePolicy.Preferred)

        # Create a QToolBar and add the button widget to it
        self.toolbar = QToolBar()

        self.toolbar.addSeparator()
        # self.toolbar.addWidget(self.test_result_label)
        self.toolbar.addSeparator()
        for key, value in self.thresholds.items():
            label = QLabel(f"{key}: {value['mean_threshold']}")
            label.setStyleSheet("color: gray; font-weight: bold; font-size: 12px")
            self.toolbar.addWidget(label)
            self.toolbar.addSeparator() 

        self.toolbar.addWidget(self.summary_button)

        # Add the toolbar to the main window
        self.addToolBar(self.toolbar2)
        self.addToolBarBreak()
        self.addToolBar(self.toolbar)

        self.toolbar.addSeparator()


    def show_summary(self):
        # Define the thresholds for each parameter
        thresholds = self.thresholds
        # Read the summary data from a CSV file
        data_df = pd.read_csv("diff_df.csv")
        # Create a QDialog to display the summary table
        dialog = QDialog()
        dialog.setWindowTitle('Log Data')
        layout = QVBoxLayout(dialog)

        toolbar = QToolBar()
        layout.addWidget(toolbar)

        for key, value in thresholds.items():
            threshold_val = value.get('threshold')
            label = QLabel(f"{key}: {threshold_val[0]}, {threshold_val[1]}")
            label.setStyleSheet("color: gray; font-weight: bold; font-size: 12px")
            toolbar.addWidget(label)
            toolbar.addSeparator()


        # Create a QTableWidget to display the summary data
        summary_table = QTableWidget()
        layout.addWidget(summary_table)

        # Set the number of rows and columns in the summary table
        summary_table.setRowCount(data_df.shape[0])
        summary_table.setColumnCount(data_df.shape[1])
        # Set the font style and size for column names
        header_font = summary_table.horizontalHeader().font()
        header_font.setBold(True)
        header_font.setPointSize(18)
        summary_table.horizontalHeader().setFont(header_font)



        # Populate the summary table with the data
        for i in range(data_df.shape[0]):
            row_values = data_df.iloc[i, :]
            for j in range(data_df.shape[1]):
                value = row_values[j]
                item = QTableWidgetItem("{:.3f}".format(value))

                if data_df.columns[j] != "Time":
                # Get the column name to retrieve the threshold
                    column_name = data_df.columns[j]
                    threshold = self.thresholds.get(column_name)

                    # Check if the value exceeds the threshold
                    if threshold is not None:
                        threshold_val = threshold.get('threshold')
                        if (
                            abs(value) > threshold_val[0]
                            or abs(value) < threshold_val[1]
                        ):
                            item.setBackground(QtGui.QColor("red"))  # Set the background color to red
                        else:
                            item.setBackground(QtGui.QColor("green"))  # Set the background color to green

                summary_table.setItem(i, j, item)

        # Set the column headers
        summary_table.setHorizontalHeaderLabels(data_df.columns)

        # Resize the summary table columns to fit the contents
        summary_table.resizeColumnsToContents()

        # Show the summary dialog
        dialog.exec_()


if __name__ == '__main__':
    seting.calculate_differences()
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())