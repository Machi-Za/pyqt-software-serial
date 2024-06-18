import libs.IO
import time
from Main_Designer import Ui_Main
from PyQt5 import QtWidgets
from PyQt5.QtSerialPort import QSerialPortInfo

# Initialize the Port object from the IO module
Port = libs.IO.Ports()

class Main(QtWidgets.QMainWindow, Ui_Main):
    # to handle data received from the serial port
    def DataReceived(main,data):
        main.Txt_SRead.appendPlainText(data)
        main.Txt_SRead.verticalScrollBar().setValue(main.Txt_SRead.verticalScrollBar().maximum())

    # to send a message through the serial port
    def SerialPrintln(main,message):
        if Port.serial.is_open:
            Port.Write(message)
            main.Txt_SPrint.clear()
            time.sleep(1)
            Port.Write("")

    def __init__(main, parent=None):
        super(Main, main).__init__(parent)
        main.setupUi(main)


        main.port = None
        Port.ReadExisting.connect(main.DataReceived)

        # to update the list of available ports
        def ListPort():
            main.Cbx_Port.clear()
            ports = QSerialPortInfo.availablePorts()
            print(ports)
            if ports == []:
                main.Cbx_Port.addItem("None")
            else:
                for port in ports:
                    main.Cbx_Port.addItem(port.portName())
                
        # to update the list of baud rates
        def ListBaud():
            main.Cbx_Baud.addItems(Port.BaudRate)

        def Main_Load():
            ListPort()
            ListBaud()
            main.Cbx_Port.setCurrentIndex(0)
            main.Cbx_Baud.setCurrentText("9600")
        Main_Load()


        main.Btn_Connect.clicked.connect(lambda: Btn_Connect_Click())
        def Btn_Connect_Click():
            if main.Btn_Connect.text() == "Connect":
                PortName = main.Cbx_Port.currentText()
                if main.Cbx_Port.currentText() == "None":
                    QtWidgets.QMessageBox.warning(main,"Warning","No available COM port.")
                else:
                    Port.serial.port = PortName
                    Port.serial.baudrate = main.Cbx_Baud.currentText()
                    if Port.serial.port:
                        try:
                            Port.Open()
                            if Port.serial.is_open:
                                main.Btn_Connect.setText("Disconnect")
                        except Exception as ex:
                            QtWidgets.QMessageBox.warning(main,"Warning","No available COM port.")
                    else:
                        QtWidgets.QMessageBox.warning(main,"Warning","No available COM port.")
            else:
                Port.Close()
                main.Btn_Connect.setText("Connect")
        
        
        main.Btn_Send.clicked.connect(lambda: Btn_Send_Click())
        def Btn_Send_Click():
            message = main.Txt_SPrint.text()
            main.SerialPrintln(message)

        main.Btn_Delete.clicked.connect(lambda: Btn_Delete_Click())
        def Btn_Delete_Click():
            main.Txt_SRead.clear()