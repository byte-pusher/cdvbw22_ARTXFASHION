

# basic stylesheet for whole application

stylesheet = ("""

 QMainWindow#main_window {
     background : black;
 }

 QPushButton {
     background-color: black;
     border : transparent;
 }

QPushButton#btn_shuffle_bottom, QPushButton#btn_shuffle_side {
    background-color : black
}

QPushButton#btn_arrow_left, QPushButton#btn_back {
    background : black;
}

QWidget#img_choice_side, QWidget#btn_area_side {
    background : transparent
}

QLabel#infotext {
    color : white;
    background-color : black;
    font-family : arial;
    font-size: 18px
}

QLabel#focus_view {
    background-color : transparent"
}



 """)
