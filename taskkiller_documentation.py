# Importieren der benötigten Module
import sys  # Das Modul sys wird importiert, um auf Systemfunktionen zugreifen zu können
from qtpy import QtWidgets, QtGui  # Die Module QtWidgets und QtGui aus dem qtpy-Paket werden importiert
import os  # Das Modul os wird importiert, um Betriebssystemfunktionen auszuführen

# Initialisierung der Qt-Anwendung
app = QtWidgets.QApplication(sys.argv)  # Eine Qt-Anwendung wird erstellt und dem Objekt "app" zugewiesen

# Erstellen des Hauptfensters
window = QtWidgets.QMainWindow()  # Ein QMainWindow-Objekt namens "window" wird erstellt
window.setGeometry(900, 450, 235, 240)  # Die Position und Größe des Fensters werden festgelegt
window.setWindowTitle("Taskkiller")  # Der Fenstertitel wird festgelegt
icon = QtGui.QIcon()  # Ein QIcon-Objekt namens "icon" wird erstellt
icon.addPixmap(QtGui.QPixmap("python.ico"))  # Ein Icon-Bild wird dem QIcon-Objekt hinzugefügt
window.setWindowIcon(icon)  # Das Icon wird dem Hauptfenster zugewiesen

# Button 1 - Outlook
button_outlook = QtWidgets.QPushButton(window)  # Ein QPushButton-Objekt namens "button_outlook" wird erstellt und dem Hauptfenster zugewiesen
button_outlook.setText("Outlook")  # Der Text auf dem Button wird festgelegt
button_outlook.setGeometry(60, 20, 110, 30)  # Die Position und Größe des Buttons werden festgelegt

# Die Funktion program_outlook wird definiert, die beim Klicken auf den Button ausgeführt wird
def program_outlook():
    os.system("taskkill /im outlook.exe /f")  # Das Betriebssystem wird aufgerufen, um den Prozess "outlook.exe" zu beenden
button_outlook.clicked.connect(program_outlook)  # Die Funktion program_outlook wird mit dem Button-Klickereignis verbunden
button_outlook.show()  # Der Button wird angezeigt

# Button 2 - SAP
button_sap = QtWidgets.QPushButton(window)  # Ein QPushButton-Objekt namens "button_sap" wird erstellt und dem Hauptfenster zugewiesen
button_sap.setText("SAP")  # Der Text auf dem Button wird festgelegt
button_sap.setGeometry(60, 50, 110, 30)  # Die Position und Größe des Buttons werden festgelegt

# Die Funktion program_sap wird definiert, die beim Klicken auf den Button ausgeführt wird
def program_sap():
    os.system("taskkill /im saplgpad.exe /f")  # Das Betriebssystem wird aufgerufen, um den Prozess "saplgpad.exe" zu beenden
button_sap.clicked.connect(program_sap)  # Die Funktion program_sap wird mit dem Button-Klickereignis verbunden
button_sap.show()  # Der Button wird angezeigt

# Button 3 - Brave-Browser
button_brave = QtWidgets.QPushButton(window)  # Ein QPushButton-Objekt namens "button_brave" wird erstellt und dem Hauptfenster zugewiesen
button_brave.setText("Brave")  # Der Text auf dem Button wird festgelegt
button_brave.setGeometry(60, 80, 110, 30)  # Die Position und Größe des Buttons werden festgelegt
# Die Funktion program_brave wird definiert, die beim Klicken auf den Button ausgeführt wird
def program_brave():
    os.system("taskkill /im brave.exe /f")  # Das Betriebssystem wird aufgerufen, um den Prozess "brave.exe" zu beenden
button_brave.clicked.connect(program_brave)  # Die Funktion program_brave wird mit dem Button-Klickereignis verbunden
button_brave.show()  # Der Button wird angezeigt

# Button 4 - OneNote
button_killall = QtWidgets.QPushButton(window)  # Ein QPushButton-Objekt namens "button_killall" wird erstellt und dem Hauptfenster zugewiesen
button_killall.setText("OneNote")  # Der Text auf dem Button wird festgelegt
button_killall.setGeometry(60, 110, 110, 30)  # Die Position und Größe des Buttons werden festgelegt

# Die Funktion program_onenote wird definiert, die beim Klicken auf den Button ausgeführt wird
def program_onenote():
    os.system("taskkill /im onenote.exe /f")  # Das Betriebssystem wird aufgerufen, um den Prozess "onenote.exe" zu beenden
button_killall.clicked.connect(program_onenote)  # Die Funktion program_onenote wird mit dem Button-Klickereignis verbunden
button_killall.show()  # Der Button wird angezeigt

# Button 5 - Kill all
button_killall = QtWidgets.QPushButton(window)  # Ein QPushButton-Objekt namens "button_killall" wird erstellt und dem Hauptfenster zugewiesen
button_killall.setText("Feierabend!")  # Der Text auf dem Button wird festgelegt
button_killall.setGeometry(60, 155, 110, 30)  # Die Position und Größe des Buttons werden festgelegt

# Die Funktion program_killall wird definiert, die beim Klicken auf den Button ausgeführt wird
def program_killall():
    program_outlook()  # Die Funktion program_outlook wird aufgerufen
    program_sap()  # Die Funktion program_sap wird aufgerufen
    program_brave()  # Die Funktion program_brave wird aufgerufen
    program_onenote()  # Die Funktion program_onenote wird aufgerufen
    os.system("shutdown /s /t 10")  # Das Betriebssystem wird aufgerufen, um den Computer herunterzufahren
    program_quit()  # Die Funktion program_quit wird aufgerufen

button_killall.clicked.connect(program_killall)  # Die Funktion program_killall wird mit dem Button-Klickereignis verbunden
button_killall.show()  # Der Button wird angezeigt

# Button 6 - Quit
button_quit = QtWidgets.QPushButton(window)  # Ein QPushButton-Objekt namens "button_quit" wird erstellt und dem Hauptfenster zugewiesen
button_quit.setText("Fenster schließen")  # Der Text auf dem Button wird festgelegt
button_quit.setGeometry(60, 200, 110, 30)  # Die Position und Größe des Buttons werden festgelegt

# Die Funktion program_quit wird definiert, die beim Klicken auf den Button ausgeführt wird
def program_quit():
    sys.exit(app.exec())  # Das Programm wird beendet

button_quit.clicked.connect(program_quit)  # Die Funktion program_quit wird mit dem Button-Klickereignis verbunden
window.show()  # Das Hauptfenster wird angezeigt
sys.exit(app.exec())  # Das Programm wird beendet

sys.exit(app.exec())  # Die Qt-Anwendung wird gestartet und die Hauptschleife wird ausgeführt

