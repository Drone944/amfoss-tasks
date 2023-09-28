import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import requests
from os import listdir

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        self.w = None        
        self.setFixedSize(850, 500)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        
        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)


        self.enter_button = QPushButton("Search", self)
        self.enter_button.setGeometry(50, 300, 160, 43)
        self.enter_button.setCheckable(True)
        self.enter_button.clicked.connect(self.enter_button_clicked)

        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.setCheckable(True)
        capture_button.clicked.connect(self.tocapture)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.todisplay)

        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
            """)
        self.Backgroundimg = QPixmap("../assets/landing.jpg")
        self.Backgroundimg_P = QPalette()
        self.Backgroundimg_P.setBrush(QPalette.Window,self.Backgroundimg)
        self.setPalette(self.Backgroundimg_P)
        setScaledContents = True
        
        self.Name = QLabel(self)
        self.Name.setGeometry(500, 295, 600, 70)
        self.Abilities = QLabel(self)
        self.Abilities.setGeometry(500, 310, 600, 70)
        self.Abilities1 = QLabel(self)
        self.Abilities1.setGeometry(560, 310, 600, 70)
        self.Type = QLabel(self)
        self.Type.setGeometry(500, 325, 600, 70)
        self.Stats = QLabel(self)
        self.Stats.setGeometry(500, 340, 600, 70)
        self.Stat0 = QLabel(self)
        self.Stat0.setGeometry(500, 355, 600, 70)
        self.Stat1 = QLabel(self)
        self.Stat1.setGeometry(500, 370, 600, 70)
        self.Stat2 = QLabel(self)
        self.Stat2.setGeometry(500, 385, 600, 70)
        self.Stat3 = QLabel(self)
        self.Stat3.setGeometry(500, 400, 600, 70)
        self.Stat4 = QLabel(self)
        self.Stat4.setGeometry(500, 415, 600, 70)
        self.Stat5 = QLabel(self)
        self.Stat5.setGeometry(500, 430, 600, 70)
        self.Err = QLabel(self)
        self.Err.setGeometry(500, 250, 600, 70)
        self.pokeimg = QLabel(self)
        self.captext = QLabel(self)

    def enter_button_clicked(self):
        self.Backgroundimg = QPixmap("../assets/pBG.jpg")
        self.Backgroundimg_P = QPalette()
        self.Backgroundimg_P.setBrush(QPalette.Window,self.Backgroundimg)
        self.setPalette(self.Backgroundimg_P)
        setScaledContents = True
        self.Name.clear()
        self.Abilities.clear()
        self.Abilities1.clear()
        self.Type.clear()
        self.Stats.clear()
        self.Stat0.clear()
        self.Stat1.clear()
        self.Stat2.clear()
        self.Stat3.clear()
        self.Stat4.clear()
        self.Stat5.clear()
        self.Err.clear()
        self.pokeimg.clear()
        self.captext.clear()

        try:
            z = self.textbox.text().lower()
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{z}")
            data = response.json()
            self.Name .setText("Name : "+data['forms'][0]['name'].capitalize())
            self.Name.show()
            self.Abilities.setText("Abilities : ")
            self.Abilities.show()

            s = ""
            for i in data['abilities']:
                s = s+", "+[i][0]['ability']['name'].capitalize()
                
            self.Abilities1.setText(s)
            self.Abilities1.show()
            self.Type.setText("Type : "+data['types'][0]['type']['name'].capitalize())
            self.Type.show()
            self.Stats.setText("Stats : ")
            self.Stats.show()
            self.Stat0.setText("\t"+data['stats'][0]['stat']['name']+":"+str(data['stats'][0]['base_stat']))
            self.Stat0.show()
            self.Stat1.setText("\t"+data['stats'][1]['stat']['name']+":"+str(data['stats'][1]['base_stat']))
            self.Stat1.show()
            self.Stat2.setText("\t"+data['stats'][2]['stat']['name']+":"+str(data['stats'][2]['base_stat']))
            self.Stat2.show()
            self.Stat3.setText("\t"+data['stats'][3]['stat']['name']+":"+str(data['stats'][3]['base_stat']))
            self.Stat3.show()
            self.Stat4.setText("\t"+data['stats'][4]['stat']['name']+":"+str(data['stats'][4]['base_stat']))
            self.Stat4.show()
            self.Stat5.setText("\t"+data['stats'][5]['stat']['name']+":"+str(data['stats'][5]['base_stat']))
            self.Stat5.show()

            pimg1 = requests.get(data['sprites']['other']['official-artwork']['front_default'])
            with open ("wasd.png","wb") as g:
                g.write(pimg1.content)

            self.pix1 = QPixmap("wasd.png")
            self.pokeimg.setPixmap(self.pix1)
            self.pokeimg.setScaledContents(True)
            self.pokeimg.setGeometry(450, 10, 300, 300)
            self.pokeimg.show()
        except:
            self.Err.setText("THIS POKEMON DOESN'T EXIST !!!")
            self.Err.show()

    def tocapture(self):
        z = self.textbox.text()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{z}")
        data = response.json()
        pimg = requests.get(data['sprites']['other']['official-artwork']['front_default'])
        with open("captured/"+data['forms'][0]['name'].capitalize()+".png","wb") as fi:
            fi.write(pimg.content)
            fi.close()
        self.captext.setText("GOTCHA!!!")
        self.captext.setGeometry(500, 275, 600, 70)
        self.captext.setStyleSheet('''
            font: bold 24px;
            ''')

    def todisplay(self):

        l1=[]
        dlg = QDialog(self)
        dlg.setFixedSize(500,500)
        dlg.setWindowTitle("Your Pokemon")
        next_button = QPushButton("Next", dlg)
        next_button.setGeometry(250, 400, 250, 100)
        next_button.setCheckable(True)
        previous_button = QPushButton("Previous", dlg)
        previous_button.setGeometry(0, 400, 250, 100)
        previous_button.setCheckable(True)


        img_dir = "captured"
        for images in os.listdir(img_dir):
            if(images.endswith(".png")):
                l1.append("captured/"+images)
        print(l1)

        cimg1 = QLabel(dlg)
        dlg.img1 = QPixmap(l1[0])
        cimg1.setPixmap(dlg.img1) 
        cimg1.setScaledContents(True)
        cimg1.setGeometry(100, 40, 300, 300)
        cimg1.show()
        global x
        x = 0


        def tonext():
            global x
            x+=1
            try:
                dlg.img1 = QPixmap(l1[x])
                cimg1.setPixmap(dlg.img1) 
                cimg1.setScaledContents(True)
                cimg1.setGeometry(100, 40, 300, 300)
                cimg1.show()
            except:
                x = 0
                dlg.img1 = QPixmap(l1[x])
                cimg1.setPixmap(dlg.img1) 
                cimg1.setScaledContents(True)
                cimg1.setGeometry(100, 40, 300, 300)
                cimg1.show()


        def toprevious():
            global x
            x-=1
            try:
                dlg.img1 = QPixmap(l1[x])
                cimg1.setPixmap(dlg.img1) 
                cimg1.setScaledContents(True)
                cimg1.setGeometry(100, 40, 300, 300)
                cimg1.show()
            except:
                x = 0
                dlg.img1 = QPixmap(l1[x])
                cimg1.setPixmap(dlg.img1) 
                cimg1.setScaledContents(True)
                cimg1.setGeometry(100, 40, 300, 300)
                cimg1.show()


        next_button.clicked.connect(tonext)
        previous_button.clicked.connect(toprevious)
        dlg.exec()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())