from PyQt5 import QtWidgets, uic
app = QtWidgets.QApplication([])
dlg = uic.loadUi("project.ui")

class rotor:
    def __init__(self,pattern,rem,pos):
        self.rem = rem
        self.pos=pos
        self.pattern=pattern

r1 = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",26,0)
r2 = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE",26,0)
r3 = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO",26,0)
r=[r1,r2,r3]

class decipher:
    def __init__(self,str1,str2,res):
        self.str1=""
        self.str2=""
        self.res=""

    def reset(self):
        dlg.lineEdit_1.setText("")
        dlg.lineEdit_2.setText("")
        dlg.dial_1.setValue(0)
        dlg.dial_2.setValue(0)
        dlg.dial_3.setValue(0)
        r1.pos=r2.pos=r3.pos=0
        r1.rem=r2.rem=r3.rem=26
        self.str1=""
        self.str2=""
        self.res=""

        
    def encode(self,str):
        str=dlg.lineEdit_1.text()
        self.str2=str
        if self.str1 in str:
            temp=str.replace(self.str1,"")
            str=temp    
        self.str1=self.str2
        for j in range(0,len(str)):
            if str[j]== ' ':
                self.res+=' '
                continue
            r1.pos=(r1.pos+1)%26
            r1.rem=r1.rem-1
            dlg.dial_1.setValue(r1.pos)
            if r1.rem==0 :
                r2.rem=r2.rem-1
                r2.pos=(r2.pos+1)%26
                dlg.dial_2.setValue(r2.pos)
                r1.rem=26
            if r2.rem==0 :
                r3.rem=r3.rem-1
                r3.pos=(r3.pos+1)%26
                dlg.dial_3.setValue(r3.pos)
                r2.rem=26
            x=str[j]
            k=1
            for i in range(0,3):
                for k in range (0,26):
                    if r[i].pattern[(k+r[i].pos)%26]==x:
                        x=chr(ord('A')+k)
                        break
            k=25-k
            x=r[2].pattern[(k+r[2].pos)%26]
            for i in range(1,-1,-1):
                x=r[i].pattern[(ord(x)-ord('A')+r[i].pos)%26]
            self.res+=x
        dlg.lineEdit_2.setText(self.res)
        
d = decipher("","","")

class slide():
    ch1='A'
    ch2='A'
    ch3='A'
    def chng1(self):
        self.ch1=chr(dlg.dial_1.value()+ord('A'))
        dlg.pos1.setText(self.ch1)
        r1.pos=dlg.dial_1.value()

    def chng2(self):
        self.ch2=chr(dlg.dial_2.value()+ord('A'))
        dlg.pos2.setText(self.ch2)
        r2.pos=dlg.dial_2.value()
        
    def chng3(self):
        self.ch3=chr(dlg.dial_3.value()+ord('A'))
        dlg.pos3.setText(self.ch3)
        r3.pos=dlg.dial_3.value()

s=slide()

dlg.pushButton.clicked.connect(d.reset)
dlg.lineEdit_1.textChanged.connect(d.encode)
dlg.dial_1.valueChanged.connect(s.chng1)
dlg.dial_2.valueChanged.connect(s.chng2)
dlg.dial_3.valueChanged.connect(s.chng3)
    
dlg.show()
app.exec()
