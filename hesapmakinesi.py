import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton,QLineEdit
from math import sqrt

num = 0.0
newNum = 0.0
sumAll = 0.0
operator = ""

action = False
counter = 0

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Hesap Makinesi QT5'
        self.left = 400
        self.top = 160
        self.width = 275
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Design Part

        # 1. textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(30, 30)
        self.textbox.resize(195, 30)

        # 1. letter
        #7. button
        seven = QPushButton('7', self)
        seven.move(30, 75)
        seven.resize(35, 30)
        seven.clicked.connect(self.Nums)
        #8. button
        eight = QPushButton('8', self)
        eight.move(70, 75)
        eight.resize(35, 30)
        eight.clicked.connect(self.Nums)
        #9. button
        nine = QPushButton('9', self)
        nine.move(110, 75)
        nine.resize(35, 30)
        nine.clicked.connect(self.Nums)
        # reset button
        reset = QPushButton('C', self)
        reset.move(150, 75)
        reset.resize(35, 30)
        reset.clicked.connect(self.C)
        #Back button
        back = QPushButton('DEL', self)
        back.move(190, 75)
        back.resize(35, 30)
        back.clicked.connect(self.Back)

        #2. letter

        # 4 button
        four = QPushButton('4', self)
        four.move(30, 110)
        four.resize(35, 30)
        four.clicked.connect(self.Nums)
        # 5 button
        five = QPushButton('5', self)
        five.move(70, 110)
        five.resize(35, 30)
        five.clicked.connect(self.Nums)
        # 6 button
        six = QPushButton('6', self)
        six.move(110, 110)
        six.resize(35, 30)
        six.clicked.connect(self.Nums)
        # * buton
        mult = QPushButton('*', self)
        mult.move(150, 110)
        mult.resize(35, 30)
        mult.clicked.connect(self.Operator)
        # Squared buton
        sqared = QPushButton('x²', self)
        sqared.move(190, 110)
        sqared.resize(35, 30)
        sqared.clicked.connect(self.Squared)

        #3. line
        # 1 button
        one = QPushButton('1', self)
        one.move(30, 145)
        one.resize(35, 30)
        one.clicked.connect(self.Nums)
        # 2 button
        two = QPushButton('2', self)
        two.move(70, 145)
        two.resize(35, 30)
        two.clicked.connect(self.Nums)
        # 3 button
        three = QPushButton('3', self)
        three.move(110, 145)
        three.resize(35, 30)
        three.clicked.connect(self.Nums)
        # / button
        diveded = QPushButton('/', self)
        diveded.move(150, 145)
        diveded.resize(35, 30)
        diveded.clicked.connect(self.Operator)
        # Sqrt button
        sqrt= QPushButton('√', self)
        sqrt.move(190, 145)
        sqrt.resize(35, 30)
        sqrt.clicked.connect(self.Sqrt)

        #4. line
        # 0 button
        zero = QPushButton('0', self)
        zero.move(30, 180)
        zero.resize(35, 30)
        zero.clicked.connect(self.Nums)
        # . button
        point = QPushButton('.', self)
        point.move(70, 180)
        point.resize(35, 30)
        point.clicked.connect(self.Point)

        # + buttton
        plus = QPushButton('+', self)
        plus.move(110, 180)
        plus.resize(35, 30)
        plus.clicked.connect(self.Operator)
        # - buton
        minus = QPushButton('-', self)
        minus.move(150, 180)
        minus.resize(35, 30)
        minus.clicked.connect(self.Operator)
        # = button
        equal = QPushButton('=', self)
        equal.move(190, 180)
        equal.resize(35,30)
        equal.clicked.connect(self.Equal)

        self.show()

        # Real Work
        # All action here

    def Nums(self):
        global num
        global newNum
        global action

        sender = self.sender()
        newNum = int(sender.text())
        setNum = str(newNum)
        if action == False:
            self.textbox.setText(self.textbox.text() + setNum)

        else:
            self.textbox.setText(setNum)
            action = False

    def Point(self):
        global opVar

        if "." not in self.textbox.text():
            self.textbox.setText(self.textbox.text() + ".")


    def Operator(self):
        global num
        global opVar
        global operator
        global sumIt

        counter += 1

        if counter> 1:
            self.Equal()

        num = self.textbox.text()

        sender = self.sender()

        operator = sender.text()

        action = True

    def Equal(self):
        global num
        global newNum
        global sumAll
        global operator
        global opVar

        newNum = self.textbox.text()

        if operator == "+":
            sumAll = float(num) + float(newNum)

        elif operator == "-":
            sumAll = float(num) - float(newNum)

        elif operator == "/":
            sumAll = float(num) / float(newNum)

        elif operator == "*":
            sumAll = float(num) * float(newNum)

        self.textbox.setText(str(sumAll))
        opVar = True

    def C(self):
        global newNum
        global sumAll
        global operator
        global num

        #Herşeyi sıfırla
        self.textbox.clear()
        num = 0.0
        newNum = 0.0
        sumAll = 0.0
        operator = ""

    def Back(self):
        self.textbox.backspace()

    def Squared(self):
        global num

        num = float(self.textbox.text())
        n = num**2
        num = n

        self.textbox.setText(str(num))
    def Sqrt(self):
        global num

        num = float(self.textbox.text())
        n = sqrt(num)
        num = n

        self.textbox.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())