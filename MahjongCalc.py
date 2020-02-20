# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rafae\Desktop\MahjongCalc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import resources, constant, math


class Ui_MainWindow(object):
    # Maximum hand size, it increases after Kans
    max_hand_size = constant.MAX_STANDARD_HAND_SIZE

    # List of tiles in hand
    hand = []

    # Allows to know if the hand is open or closed which is used to determine yaku validity and calculate points
    hand_is_open = False

    # Total of han and fu, used to calculate points, a winning hand has always at least 20 fu
    total_han = 0
    total_fu = 20

    # Total of pon, chi, kan and closed kan
    total_pon = 0
    total_chi = 0
    total_kan = 0
    total_closed_kan = 0

    # List of open triplets and quads
    open_triplets_list = []
    open_quads_list = []
    closed_quads_list = []

    # Riichi Mahjong tiles list
    tiles_list = [
        "1 Man",
        "2 Man",
        "3 Man",
        "4 Man",
        "5 Man",
        "6 Man",
        "7 Man",
        "8 Man",
        "9 Man",
        "1 Pin",
        "2 Pin",
        "3 Pin",
        "4 Pin",
        "5 Pin",
        "6 Pin",
        "7 Pin",
        "8 Pin",
        "9 Pin",
        "1 So",
        "2 So",
        "3 So",
        "4 So",
        "5 So",
        "6 So",
        "7 So",
        "8 So",
        "9 So",
        "Ton",
        "Nan",
        "Xia",
        "Pei",
        "Hatsu",
        "Haku",
        "Chun"
    ]

    # This dictionary ties tiles to their respective image file path
    images_assignment_dictionary = {
        "1 Man": "image: url(:/tiles/1man.png);",
        "2 Man": "image: url(:/tiles/2man.png);",
        "3 Man": "image: url(:/tiles/3man.png);",
        "4 Man": "image: url(:/tiles/4man.png);",
        "5 Man": "image: url(:/tiles/5man.png);",
        "6 Man": "image: url(:/tiles/6man.png);",
        "7 Man": "image: url(:/tiles/7man.png);",
        "8 Man": "image: url(:/tiles/8man.png);",
        "9 Man": "image: url(:/tiles/9man.png);",
        "1 Pin": "image: url(:/tiles/1pin.png);",
        "2 Pin": "image: url(:/tiles/2pin.png);",
        "3 Pin": "image: url(:/tiles/3pin.png);",
        "4 Pin": "image: url(:/tiles/4pin.png);",
        "5 Pin": "image: url(:/tiles/5pin.png);",
        "6 Pin": "image: url(:/tiles/6pin.png);",
        "7 Pin": "image: url(:/tiles/7pin.png);",
        "8 Pin": "image: url(:/tiles/8pin.png);",
        "9 Pin": "image: url(:/tiles/9pin.png);",
        "1 So": "image: url(:/tiles/1so.png);",
        "2 So": "image: url(:/tiles/2so.png);",
        "3 So": "image: url(:/tiles/3so.png);",
        "4 So": "image: url(:/tiles/4so.png);",
        "5 So": "image: url(:/tiles/5so.png);",
        "6 So": "image: url(:/tiles/6so.png);",
        "7 So": "image: url(:/tiles/7so.png);",
        "8 So": "image: url(:/tiles/8so.png);",
        "9 So": "image: url(:/tiles/9so.png);",
        "Ton": "image: url(:/tiles/ton.png);",
        "Nan": "image: url(:/tiles/nan.png);",
        "Xia": "image: url(:/tiles/xia.png);",
        "Pei": "image: url(:/tiles/pei.png);",
        "Hatsu": "image: url(:/tiles/hatsu.png);",
        "Haku": "image: url(:/tiles/haku.png);",
        "Chun": "image: url(:/tiles/chun.png);",
        "Closed Kan": "image: url(:/tiles/hidden.png);",
        "1 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/1man_called.png);",
        "2 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/2man_called.png);",
        "3 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/3man_called.png);",
        "4 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/4man_called.png);",
        "5 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/5man_called.png);",
        "6 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/6man_called.png);",
        "7 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/7man_called.png);",
        "8 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/8man_called.png);",
        "9 Man"+constant.CALLED_TILE_STRING: "image: url(:/tiles/9man_called.png);",
        "1 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/1pin_called.png);",
        "2 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/2pin_called.png);",
        "3 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/3pin_called.png);",
        "4 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/4pin_called.png);",
        "5 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/5pin_called.png);",
        "6 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/6pin_called.png);",
        "7 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/7pin_called.png);",
        "8 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/8pin_called.png);",
        "9 Pin"+constant.CALLED_TILE_STRING: "image: url(:/tiles/9pin_called.png);",
        "1 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/1so_called.png);",
        "2 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/2so_called.png);",
        "3 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/3so_called.png);",
        "4 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/4so_called.png);",
        "5 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/5so_called.png);",
        "6 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/6so_called.png);",
        "7 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/7so_called.png);",
        "8 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/8so_called.png);",
        "9 So"+constant.CALLED_TILE_STRING: "image: url(:/tiles/9so_called.png);",
        "Ton"+constant.CALLED_TILE_STRING: "image: url(:/tiles/ton_called.png);",
        "Nan"+constant.CALLED_TILE_STRING: "image: url(:/tiles/nan_called.png);",
        "Xia"+constant.CALLED_TILE_STRING: "image: url(:/tiles/xia_called.png);",
        "Pei"+constant.CALLED_TILE_STRING: "image: url(:/tiles/pei_called.png);",
        "Hatsu"+constant.CALLED_TILE_STRING: "image: url(:/tiles/hatsu_called.png);",
        "Haku"+constant.CALLED_TILE_STRING: "image: url(:/tiles/haku_called.png);",
        "Chun"+constant.CALLED_TILE_STRING: "image: url(:/tiles/chun_called.png);",
        constant.BLANK_TILE: "image: url(:/tiles/blank.png);"
    }

    # Riichi Mahjong wind list
    wind_list = [
        "West",
        "South",
        "East",
        "North"
    ]

    # Riichi Mahjong dragon tiles list
    dragon_tiles_list = [
        "Hatsu",
        "Haku",
        "Chun"
    ]

    # Riichi Mahjong wind tiles list
    wind_tiles_list = [
        "Ton",
        "Nan",
        "Xia",
        "Pei"
    ]

    # Riichi Mahjong terminals tiles list
    terminal_tiles_list = [
        "1 Man",
        "9 Man",
        "1 Pin",
        "9 Pin",
        "1 So",
        "9 So"
    ]

    # Riichi Mahjong man tiles list
    man_tiles_list = [
        "1 Man",
        "2 Man",
        "3 Man",
        "4 Man",
        "5 Man",
        "6 Man",
        "7 Man",
        "8 Man",
        "9 Man"
    ]

    # Riichi Mahjong pin tiles list
    pin_tiles_list = [
        "1 Pin",
        "2 Pin",
        "3 Pin",
        "4 Pin",
        "5 Pin",
        "6 Pin",
        "7 Pin",
        "8 Pin",
        "9 Pin"
    ]

    # Riichi Mahjong so tiles list
    so_tiles_list = [
        "1 So",
        "2 So",
        "3 So",
        "4 So",
        "5 So",
        "6 So",
        "7 So",
        "8 So",
        "9 So"
    ]

    # Riichi Mahjong green tiles list
    green_tiles_list = [
        "2 So",
        "3 So",
        "4 So",
        "6 So",
        "8 So",
        "Hatsu"
    ]

    # Riichi Mahjong yaku list
    yaku_list = [
        "Chiitoitsu",
        "Pinfu",
        "Iipeiko",
        "Ryanpeiko",
        "Sanshoku",
        "Ittsuu",
        "San anko",
        "Toitoi",
        "San kantsu",
        "Sanshoku doko",
        "Tanyao",
        "Fanpai",
        "Chanta",
        "Junchan",
        "Honro",
        "Shosangen",
        "Honitsu",
        "Chinitsu",
        "Kokushi muso",
        "Su anko",
        "Daisangen",
        "Shosushii",
        "Daisushii",
        "Tsuiiso",
        "Chinroto",
        "Ryuiiso",
        "Su kantsu",
        "Churen poto",
        "Tsumo",
        "Riichi",
        "Double Riichi",
        "Ippatsu",
        "Haitei",
        "Hotei",
        "Rinshan",
        "Chankan"
    ]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_tileSelect = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tileSelect.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.comboBox_tileSelect.setMaxVisibleItems(34)
        self.comboBox_tileSelect.setObjectName("comboBox_tileSelect")
        self.tile_1 = QtWidgets.QLabel(self.centralwidget)
        self.tile_1.setGeometry(QtCore.QRect(10, 10, 55, 55))
        self.tile_1.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_1.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_1.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_1.setText("")
        self.tile_1.setObjectName("tile_1")
        self.tile_2 = QtWidgets.QLabel(self.centralwidget)
        self.tile_2.setGeometry(QtCore.QRect(65, 10, 55, 55))
        self.tile_2.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_2.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_2.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_2.setText("")
        self.tile_2.setObjectName("tile_2")
        self.tile_3 = QtWidgets.QLabel(self.centralwidget)
        self.tile_3.setGeometry(QtCore.QRect(120, 10, 55, 55))
        self.tile_3.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_3.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_3.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_3.setText("")
        self.tile_3.setObjectName("tile_3")
        self.tile_4 = QtWidgets.QLabel(self.centralwidget)
        self.tile_4.setGeometry(QtCore.QRect(175, 10, 55, 55))
        self.tile_4.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_4.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_4.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_4.setText("")
        self.tile_4.setObjectName("tile_4")
        self.tile_5 = QtWidgets.QLabel(self.centralwidget)
        self.tile_5.setGeometry(QtCore.QRect(230, 10, 55, 55))
        self.tile_5.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_5.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_5.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_5.setText("")
        self.tile_5.setObjectName("tile_5")
        self.tile_6 = QtWidgets.QLabel(self.centralwidget)
        self.tile_6.setGeometry(QtCore.QRect(285, 10, 55, 55))
        self.tile_6.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_6.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_6.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_6.setText("")
        self.tile_6.setObjectName("tile_6")
        self.tile_7 = QtWidgets.QLabel(self.centralwidget)
        self.tile_7.setGeometry(QtCore.QRect(340, 10, 55, 55))
        self.tile_7.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_7.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_7.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_7.setText("")
        self.tile_7.setObjectName("tile_7")
        self.tile_8 = QtWidgets.QLabel(self.centralwidget)
        self.tile_8.setGeometry(QtCore.QRect(395, 10, 55, 55))
        self.tile_8.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_8.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_8.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_8.setText("")
        self.tile_8.setObjectName("tile_8")
        self.tile_9 = QtWidgets.QLabel(self.centralwidget)
        self.tile_9.setGeometry(QtCore.QRect(450, 10, 55, 55))
        self.tile_9.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_9.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_9.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_9.setText("")
        self.tile_9.setObjectName("tile_9")
        self.tile_10 = QtWidgets.QLabel(self.centralwidget)
        self.tile_10.setGeometry(QtCore.QRect(505, 10, 55, 55))
        self.tile_10.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_10.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_10.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_10.setText("")
        self.tile_10.setObjectName("tile_10")
        self.tile_11 = QtWidgets.QLabel(self.centralwidget)
        self.tile_11.setGeometry(QtCore.QRect(560, 10, 55, 55))
        self.tile_11.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_11.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_11.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_11.setText("")
        self.tile_11.setObjectName("tile_11")
        self.tile_12 = QtWidgets.QLabel(self.centralwidget)
        self.tile_12.setGeometry(QtCore.QRect(615, 10, 55, 55))
        self.tile_12.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_12.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_12.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_12.setText("")
        self.tile_12.setObjectName("tile_12")
        self.tile_13 = QtWidgets.QLabel(self.centralwidget)
        self.tile_13.setGeometry(QtCore.QRect(670, 10, 55, 55))
        self.tile_13.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_13.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_13.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_13.setText("")
        self.tile_13.setObjectName("tile_13")
        self.tile_14 = QtWidgets.QLabel(self.centralwidget)
        self.tile_14.setGeometry(QtCore.QRect(725, 10, 55, 55))
        self.tile_14.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_14.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_14.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_14.setText("")
        self.tile_14.setObjectName("tile_14")
        self.tile_15 = QtWidgets.QLabel(self.centralwidget)
        self.tile_15.setGeometry(QtCore.QRect(780, 10, 55, 55))
        self.tile_15.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_15.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_15.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_15.setText("")
        self.tile_15.setObjectName("tile_15")
        self.tile_16 = QtWidgets.QLabel(self.centralwidget)
        self.tile_16.setGeometry(QtCore.QRect(835, 10, 55, 55))
        self.tile_16.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_16.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_16.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_16.setText("")
        self.tile_16.setObjectName("tile_16")
        self.tile_17 = QtWidgets.QLabel(self.centralwidget)
        self.tile_17.setGeometry(QtCore.QRect(890, 10, 55, 55))
        self.tile_17.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_17.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_17.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_17.setText("")
        self.tile_17.setObjectName("tile_17")
        self.tile_18 = QtWidgets.QLabel(self.centralwidget)
        self.tile_18.setGeometry(QtCore.QRect(945, 10, 55, 55))
        self.tile_18.setMinimumSize(QtCore.QSize(55, 55))
        self.tile_18.setMaximumSize(QtCore.QSize(55, 55))
        self.tile_18.setStyleSheet("image: url(:/tiles/blank.png);")
        self.tile_18.setText("")
        self.tile_18.setObjectName("tile_18")
        self.pushButton_addChi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addChi.setGeometry(QtCore.QRect(90, 100, 75, 23))
        self.pushButton_addChi.setObjectName("pushButton_addChi")
        self.pushButton_addPon = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addPon.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.pushButton_addPon.setObjectName("pushButton_addPon")
        self.pushButton_addKan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addKan.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.pushButton_addKan.setObjectName("pushButton_addKan")
        self.pushButton_addClosedKan = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addClosedKan.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.pushButton_addClosedKan.setObjectName("pushButton_addClosedKan")
        self.pushButton_addTile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addTile.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.pushButton_addTile.setObjectName("pushButton_addTile")
        self.label_addTiles = QtWidgets.QLabel(self.centralwidget)
        self.label_addTiles.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_addTiles.setObjectName("label_addTiles")
        self.radioButton_tsumo = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_tsumo.setEnabled(True)
        self.radioButton_tsumo.setGeometry(QtCore.QRect(10, 190, 82, 17))
        self.radioButton_tsumo.setChecked(True)
        self.radioButton_tsumo.setObjectName("radioButton_tsumo")
        self.label_setConditions = QtWidgets.QLabel(self.centralwidget)
        self.label_setConditions.setGeometry(QtCore.QRect(10, 170, 111, 16))
        self.label_setConditions.setObjectName("label_setConditions")
        self.radioButton_ron = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_ron.setGeometry(QtCore.QRect(100, 190, 82, 17))
        self.radioButton_ron.setObjectName("radioButton_ron")
        self.label_dora = QtWidgets.QLabel(self.centralwidget)
        self.label_dora.setGeometry(QtCore.QRect(10, 220, 47, 13))
        self.label_dora.setObjectName("label_dora")
        self.spinBox_dora = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_dora.setGeometry(QtCore.QRect(10, 240, 42, 22))
        self.spinBox_dora.setObjectName("spinBox_dora")
        self.label_honba = QtWidgets.QLabel(self.centralwidget)
        self.label_honba.setGeometry(QtCore.QRect(100, 220, 47, 13))
        self.label_honba.setObjectName("label_honba")
        self.spinBox_honba = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_honba.setGeometry(QtCore.QRect(100, 240, 42, 22))
        self.spinBox_honba.setObjectName("spinBox_honba")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(250, 130, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.label_prevalentWind = QtWidgets.QLabel(self.centralwidget)
        self.label_prevalentWind.setGeometry(QtCore.QRect(170, 170, 91, 16))
        self.label_prevalentWind.setObjectName("label_prevalentWind")
        self.comboBox_prevalentWind = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_prevalentWind.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.comboBox_prevalentWind.setCurrentText("")
        self.comboBox_prevalentWind.setObjectName("comboBox_prevalentWind")
        self.label_ownWind = QtWidgets.QLabel(self.centralwidget)
        self.label_ownWind.setGeometry(QtCore.QRect(170, 220, 71, 16))
        self.label_ownWind.setObjectName("label_ownWind")
        self.comboBox_ownWind = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ownWind.setGeometry(QtCore.QRect(170, 240, 75, 23))
        self.comboBox_ownWind.setObjectName("comboBox_ownWind")
        self.checkBox_riichi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_riichi.setGeometry(QtCore.QRect(10, 280, 70, 17))
        self.checkBox_riichi.setObjectName("checkBox_riichi")
        self.checkBox_doubleRiichi = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_doubleRiichi.setGeometry(QtCore.QRect(100, 280, 91, 17))
        self.checkBox_doubleRiichi.setObjectName("checkBox_doubleRiichi")
        self.checkBox_ippatsu = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ippatsu.setEnabled(False)
        self.checkBox_ippatsu.setGeometry(QtCore.QRect(200, 280, 70, 17))
        self.checkBox_ippatsu.setObjectName("checkBox_ippatsu")
        self.checkBox_haitei = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_haitei.setGeometry(QtCore.QRect(10, 310, 70, 17))
        self.checkBox_haitei.setObjectName("checkBox_haitei")
        self.checkBox_hotei = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_hotei.setEnabled(False)
        self.checkBox_hotei.setGeometry(QtCore.QRect(100, 310, 70, 17))
        self.checkBox_hotei.setObjectName("checkBox_hotei")
        self.checkBox_rinshan = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_rinshan.setEnabled(False)
        self.checkBox_rinshan.setGeometry(QtCore.QRect(200, 310, 70, 17))
        self.checkBox_rinshan.setObjectName("checkBox_rinshan")
        self.checkBox_chankan = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_chankan.setEnabled(False)
        self.checkBox_chankan.setGeometry(QtCore.QRect(10, 340, 70, 17))
        self.checkBox_chankan.setObjectName("checkBox_chankan")
        self.plainTextEdit_Result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_Result.setGeometry(QtCore.QRect(340, 100, 661, 261))
        self.plainTextEdit_Result.setPlainText("")
        self.plainTextEdit_Result.setObjectName("plainTextEdit_Result")
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 790, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_tileSelect.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Populates tiles combo boxes
        self.comboBox_tileSelect.addItems(self.tiles_list)
        self.comboBox_prevalentWind.addItems(self.wind_list)
        self.comboBox_ownWind.addItems(self.wind_list)

        # Clicked button events
        self.pushButton_addTile.clicked.connect(self.add_tile)
        self.pushButton_addPon.clicked.connect\
            (lambda:self.add_duplicates(constant.PON_SIZE, constant.CALLED_TILE, not constant.CLOSED_KAN))
        self.pushButton_addKan.clicked.connect\
            (lambda: self.add_duplicates(constant.KAN_SIZE, constant.CALLED_TILE, not constant.CLOSED_KAN))
        self.pushButton_addClosedKan.clicked.connect\
            (lambda: self.add_duplicates(constant.KAN_SIZE, not constant.CALLED_TILE, constant.CLOSED_KAN))
        self.pushButton_addChi.clicked.connect\
            (lambda: self.add_suite(constant.CHI_SIZE, constant.CALLED_TILE))
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_calculate.clicked.connect(self.calculate)

        # Radio buttons events
        self.radioButton_ron.clicked.connect(self.ron_selected)
        self.radioButton_tsumo.clicked.connect(self.tsumo_selected)

        # Check Boxes events
        self.checkBox_riichi.toggled.connect(self.riichi_toggled)
        self.checkBox_doubleRiichi.toggled.connect(self.double_riichi_toggled)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Riichi Mahjong Calculator"))
        self.pushButton_addChi.setText(_translate("MainWindow", "Chi"))
        self.pushButton_addPon.setText(_translate("MainWindow", "Pon"))
        self.pushButton_addKan.setText(_translate("MainWindow", "Kan"))
        self.pushButton_addClosedKan.setText(_translate("MainWindow", "Closed Kan"))
        self.pushButton_addTile.setText(_translate("MainWindow", "Add a tile"))
        self.label_addTiles.setText(_translate("MainWindow", "Add tiles to the hand"))
        self.radioButton_tsumo.setText(_translate("MainWindow", "Tsumo"))
        self.label_setConditions.setText(_translate("MainWindow", "Set the conditions"))
        self.radioButton_ron.setText(_translate("MainWindow", "Ron"))
        self.label_dora.setText(_translate("MainWindow", "Dora"))
        self.label_honba.setText(_translate("MainWindow", "Honba"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.label_prevalentWind.setText(_translate("MainWindow", "Prevalent wind"))
        self.label_ownWind.setText(_translate("MainWindow", "Own wind"))
        self.checkBox_riichi.setText(_translate("MainWindow", "Riichi"))
        self.checkBox_doubleRiichi.setText(_translate("MainWindow", "Double Riichi"))
        self.checkBox_ippatsu.setText(_translate("MainWindow", "Ippatsu"))
        self.checkBox_haitei.setText(_translate("MainWindow", "Haitei"))
        self.checkBox_hotei.setText(_translate("MainWindow", "Hotei"))
        self.checkBox_rinshan.setText(_translate("MainWindow", "Rinshan"))
        self.checkBox_chankan.setText(_translate("MainWindow", "Chankan"))
        self.pushButton_calculate.setText(_translate("MainWindow", "Calculate"))

    # Clears current hand and reinitializes UI
    def clear(self):
        # Set all global variables to default
        self.max_hand_size = constant.MAX_STANDARD_HAND_SIZE
        self.hand.clear()
        self.open_triplets_list.clear()
        self.open_quads_list.clear()
        self.closed_quads_list.clear()
        self.hand_is_open = False
        self.total_han = 0
        self.total_fu = 20
        self.total_pon = 0
        self.total_chi = 0
        self.total_kan = 0
        self.total_closed_kan = 0

        # Set UI to default
        self.tile_1.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_2.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_3.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_4.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_5.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_6.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_7.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_8.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_9.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_10.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_11.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_12.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_13.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_14.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_15.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_16.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_17.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.tile_18.setStyleSheet(self.images_assignment_dictionary[constant.BLANK_TILE])
        self.plainTextEdit_Result.clear()

        # Set Tsumo as default
        self.radioButton_tsumo.setChecked(True)
        self.tsumo_selected()

        # Set Combo boxes to default
        self.comboBox_tileSelect.clear()
        self.comboBox_tileSelect.addItems(self.tiles_list)
        self.comboBox_prevalentWind.clear()
        self.comboBox_prevalentWind.addItems(self.wind_list)
        self.comboBox_ownWind.clear()
        self.comboBox_ownWind.addItems(self.wind_list)

        # Set Spin Boxes to default
        self.spinBox_dora.setValue(0)
        self.spinBox_honba.setValue(0)

        # Set Check Boxes to default
        self.checkBox_chankan.setChecked(False)
        self.checkBox_hotei.setChecked(False)
        self.checkBox_haitei.setChecked(False)
        self.checkBox_doubleRiichi.setEnabled(True)
        self.checkBox_doubleRiichi.setChecked(False)
        self.checkBox_ippatsu.setChecked(False)
        self.checkBox_riichi.setEnabled(True)
        self.checkBox_riichi.setChecked(False)
        self.checkBox_rinshan.setChecked(False)

    # Prevents forbidden conditions when the hand is opened
    def opened_hand(self):
        self.hand_is_open = True
        self.checkBox_riichi.setEnabled(False)
        self.checkBox_riichi.setChecked(False)
        self.checkBox_doubleRiichi.setEnabled(False)
        self.checkBox_doubleRiichi.setChecked(False)

    # Prevents forbidden conditions and unlocks possible conditions when Ron is selected
    def ron_selected(self):
        self.checkBox_haitei.setEnabled(False)
        self.checkBox_haitei.setChecked(False)
        self.checkBox_rinshan.setEnabled(False)
        self.checkBox_rinshan.setChecked(False)
        self.checkBox_hotei.setEnabled(True)
        self.checkBox_chankan.setEnabled(True)

    # Prevents forbidden conditions and unlocks possible conditions when Tsumo is selected
    def tsumo_selected(self):
        self.checkBox_haitei.setEnabled(True)
        self.checkBox_hotei.setEnabled(False)
        self.checkBox_hotei.setChecked(False)
        self.checkBox_chankan.setEnabled(False)
        self.checkBox_chankan.setChecked(False)

        # Rinshan is allowed if there is a Kan in hand
        if self.total_kan + self.total_closed_kan > 0:
            self.checkBox_rinshan.setEnabled(True)
        else:
            self.checkBox_rinshan.setEnabled(False)

    # Prevents forbidden conditions and unlocks possible conditions when Riichi is selected
    def riichi_toggled(self):
        if self.checkBox_riichi.isChecked():
            self.checkBox_doubleRiichi.setEnabled(False)
            self.checkBox_doubleRiichi.setChecked(False)
            self.checkBox_ippatsu.setEnabled(True)
        elif not self.checkBox_riichi.isChecked() and not self.hand_is_open:
            self.checkBox_doubleRiichi.setEnabled(True)
            self.checkBox_ippatsu.setEnabled(False)
            self.checkBox_ippatsu.setChecked(False)
        else:
            self.checkBox_ippatsu.setEnabled(False)
            self.checkBox_ippatsu.setChecked(False)

    # Prevents forbidden conditions and unlocks possible conditions when Double Riichi is selected
    def double_riichi_toggled(self):
        if self.checkBox_doubleRiichi.isChecked():
            self.checkBox_riichi.setEnabled(False)
            self.checkBox_riichi.setChecked(False)
            self.checkBox_ippatsu.setEnabled(True)
        elif not self.checkBox_doubleRiichi.isChecked() and not self.hand_is_open:
            self.checkBox_riichi.setEnabled(True)
            self.checkBox_ippatsu.setEnabled(False)
            self.checkBox_ippatsu.setChecked(False)
        else:
            self.checkBox_ippatsu.setEnabled(False)
            self.checkBox_ippatsu.setChecked(False)

    # Adds in the UI a single tile to the hand
    def add_tile_ui(self, tile_name, position, called_tile, closed_kan):
        # Shows tile image at desired position
        if position == 1:
            if closed_kan:
                self.tile_1.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_1.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_1.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 2:
            if closed_kan:
                self.tile_2.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_2.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_2.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 3:
            if closed_kan:
                self.tile_3.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_3.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_3.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 4:
            if closed_kan:
                self.tile_4.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_4.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_4.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 5:
            if closed_kan:
                self.tile_5.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_5.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_5.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 6:
            if closed_kan:
                self.tile_6.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_6.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_6.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 7:
            if closed_kan:
                self.tile_7.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_7.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_7.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 8:
            if closed_kan:
                self.tile_8.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_8.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_8.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 9:
            if closed_kan:
                self.tile_9.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_9.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_9.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 10:
            if closed_kan:
                self.tile_10.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_10.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_10.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 11:
            if closed_kan:
                self.tile_11.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_11.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_11.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 12:
            if closed_kan:
                self.tile_12.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_12.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_12.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 13:
            if closed_kan:
                self.tile_13.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_13.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_13.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 14:
            if closed_kan:
                self.tile_14.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_14.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_14.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 15:
            if closed_kan:
                self.tile_15.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_15.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_15.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 16:
            if closed_kan:
                self.tile_16.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_16.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_16.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 17:
            if closed_kan:
                self.tile_17.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_17.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_17.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])
        elif position == 18:
            if closed_kan:
                self.tile_18.setStyleSheet(self.images_assignment_dictionary["Closed Kan"])
            elif called_tile:
                self.tile_18.setStyleSheet(
                    self.images_assignment_dictionary[tile_name + constant.CALLED_TILE_STRING])
            else:
                self.tile_18.setStyleSheet(
                    self.images_assignment_dictionary[tile_name])

    # Checks if it's possible to start a suite this a specific tile
    def suite_allowed(self, tile_name):
        # Conditions for the first tile
        # Only tiles from 1 to 7 are allowed to start a suite
        if self.duplicates_allowed(self.hand.count(str(self.comboBox_tileSelect.currentText())), 1):
            for i in range(1, 8):
                if tile_name[0] == str(i):
                    # Conditions for the second tile
                    next_tile_name = tile_name
                    next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if self.duplicates_allowed(self.hand.count(next_tile_name), 1):
                        # Conditions for the third tile
                        next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                        if self.duplicates_allowed(self.hand.count(next_tile_name), 1):
                            return True
                        else:
                            return False
                    else:
                        return False
        return False

    # Checks if an operation won't make the hand bigger than the maximum size allowed
    def hand_size_allowed(self, hand_size, operation_size):
        # If it's a Kan, operation size is -1 because the player will draw a tile
        if operation_size == constant.KAN_SIZE:
            operation_size - 1

        if hand_size <= self.max_hand_size - operation_size:
            self.plainTextEdit_Result.clear()
            return True
        else:
            self.plainTextEdit_Result.clear()
            self.plainTextEdit_Result.appendPlainText("Error:\nThis operation would make your hand bigger than the allowed hand size.")
            return False

    # Checks if an operation won't cause the hand to have more than the maximum duplicates allowed
    def duplicates_allowed(self, held_duplicates, operation_size):
        if held_duplicates <= constant.MAX_DUPLICATES - operation_size:
            self.plainTextEdit_Result.clear()
            return True
        else:
            self.plainTextEdit_Result.clear()
            self.plainTextEdit_Result.appendPlainText("Error:\nThis operation would make your hand hold more than 4 times the same tile.")
            return False

    # Checks if an operation is allowed
    def operation_allowed(self, operation_size):
         if self.hand_size_allowed(len(self.hand), operation_size)\
                 and self.duplicates_allowed(self.hand.count(str(self.comboBox_tileSelect.currentText())),
                                             operation_size):
            return True
         else:
            return False

    # Adds a single tile to the hand
    def add_tile(self):
        # The hand must not be full and a tile can't have more than a specified number of duplicates
        if self.operation_allowed(1):
            tile_name = str(self.comboBox_tileSelect.currentText())

            self.hand.append(tile_name)
            self.add_tile_ui(tile_name, len(self.hand), not constant.CALLED_TILE, not constant.CLOSED_KAN)

    # Adds duplicated tiles
    def add_duplicates(self, size, called_tile, closed_kan):
        # The hand must not be full and a tile can't have more than a specified number of duplicates
        if self.operation_allowed(size):
            tile_name = str(self.comboBox_tileSelect.currentText())

            # Updates actions count
            if size == constant.KAN_SIZE:
                # In Mahjong when the player has a Kan, he draws and extra tile and max hand size increases by one
                self.max_hand_size += 1
                if closed_kan:
                    self.total_closed_kan += 1
                    self.closed_quads_list.append(tile_name)
                else:
                    self.total_kan += 1
                    self.open_quads_list.append(tile_name)

                # Allow Rinshan condition for Kans when Tsumo condition is selected
                if self.radioButton_tsumo.isChecked():
                    self.checkBox_rinshan.setEnabled(True)
            elif size == constant.PON_SIZE:
                self.total_pon += 1
                self.open_triplets_list.append(tile_name)

            for i in range(size):
                self.hand.append(tile_name)

                if closed_kan:
                    # In a closed Kan, 2nd and 3rd tile must be hidden
                    if i == 1 or i == 2:
                        self.add_tile_ui(tile_name, len(self.hand), not constant.CALLED_TILE, constant.CLOSED_KAN)
                    else:
                        self.add_tile_ui(tile_name, len(self.hand), not constant.CALLED_TILE, not constant.CLOSED_KAN)
                elif called_tile:
                    # In a called tile, the first tile must be turned
                    if i == 0:
                        self.add_tile_ui(tile_name, len(self.hand), constant.CALLED_TILE, not constant.CLOSED_KAN)
                    else:
                        self.add_tile_ui(tile_name, len(self.hand), not constant.CALLED_TILE, not constant.CLOSED_KAN)

                    # When a tile is called, the hand becomes open
                    self.opened_hand()

                    # Removes riichi and doubleRiichi possiblity on UI
                    self.checkBox_riichi.setEnabled(False)
                    self.checkBox_doubleRiichi.setEnabled(False)

    # Adds suite tiles
    def add_suite(self, size, called_tile):
        tile_name = str(self.comboBox_tileSelect.currentText())

        if self.hand_size_allowed(len(self.hand), size) and self.suite_allowed(tile_name):

            # Adding duplicates to the hand reveals the hand to opponent
            self.hand_is_open = True

            # Adds the first tile of the suite
            self.hand.append(tile_name)
            self.add_tile_ui(tile_name, len(self.hand), constant.CALLED_TILE, not constant.CLOSED_KAN)

            # Since a tile is called, the hand becomes open
            self.opened_hand()

            # Removes riichi and doubleRiichi possiblity on UI
            self.checkBox_riichi.setEnabled(False)
            self.checkBox_doubleRiichi.setEnabled(False)

            # Size of the operation - 1 that corresponds to the first tile of the suite
            for i in range(size - 1):
                tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                self.hand.append(tile_name)
                self.add_tile_ui(tile_name, len(self.hand), not constant.CALLED_TILE, not constant.CLOSED_KAN)

    # Check if current hand is valid
    # It must be a four melds hand but there are two exceptions: chiitoitsu and kokushimuso
    def is_valid_hand(self):
        if len(self.hand) == self.max_hand_size and (self.four_melds_hand(self.hand) or self.chiitoitsu_yaku(self.hand)
                                                     or self.kokushimuso_yaku(self.hand)):
            return True
        else:
            return False

    # Returns the hand without the pairs and the total number of pairs that was in the hand
    def get_hand_pairs(self, hand):
        total_pairs = 0
        i = 0

        while i < len(hand):
            tile_name = hand[i]
            if hand.count(tile_name) == constant.PAIR_SIZE:
                for j in range(constant.PAIR_SIZE):
                    hand.remove(tile_name)
                total_pairs += 1
            else:
                # Increments i to test the next item on the list
                i += 1
        return hand, total_pairs

    # Returns the hand without the triplets and the total number of triplets that was in the hand
    def get_hand_triplets(self, hand):
        total_triplets = 0
        i = 0

        while i < len(hand):
            tile_name = hand[i]
            if hand.count(tile_name) == constant.TRIPLET_SIZE:
                for j in range(constant.TRIPLET_SIZE):
                    hand.remove(tile_name)
                total_triplets += 1
            else:
                # Increments i to test the next item on the list
                i += 1
        return hand, total_triplets

    # Returns the hand without the quads and the total number of quads that was in the hand
    def get_hand_quads(self, hand):
        total_quads = 0
        i = 0

        while i < len(hand):
            tile_name = hand[i]
            if hand.count(tile_name) == constant.QUAD_SIZE:
                for j in range(constant.QUAD_SIZE):
                    hand.remove(tile_name)
                total_quads += 1
            else:
                # Increments i to test the next item on the list
                i += 1
        return hand, total_quads

    # Returns the hand without the suites and the total number of suites that was in the hand
    def get_hand_suites(self, hand):
        total_suites = 0
        i = 0

        while i < len(hand):
            tile_name = hand[i]
            for j in range(1, 8):
                if tile_name[0] == str(j):
                    next_tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                    after_next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if hand.count(next_tile_name) > 0 and hand.count(after_next_tile_name) > 0:
                        hand.remove(tile_name)
                        hand.remove(next_tile_name)
                        hand.remove(after_next_tile_name)
                        total_suites += 1
                        # Since suite items were removed in the list, we need to retest the same position
                        i -= 1
            # Increments i to test the next item on the list
            i += 1
        return hand, total_suites

    # Returns total number of identical suites that was in the hand
    def identical_suites(self, hand):
        hand_copy = hand.copy()
        suite_starters = []
        total_identical_suites = 0
        i = 0
        k = 0

        # Collects all suite starters and store them in a list
        while i < len(hand_copy):
            tile_name = hand_copy[i]
            for j in range(1, 8):
                if tile_name[0] == str(j):
                    next_tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                    after_next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if hand_copy.count(next_tile_name) > 0 and hand_copy.count(after_next_tile_name) > 0:
                        suite_starters.append(tile_name)
                        hand_copy.remove(tile_name)
                        hand_copy.remove(next_tile_name)
                        hand_copy.remove(after_next_tile_name)
                        # Since suite items were removed in the list, we need to retest the same position
                        i -= 1
            # Increments i to test the next item on the list
            i += 1

        # Checks if how many suite starters that are identical
        while k < len(suite_starters):
            if suite_starters.count(suite_starters[k]) > 1:
                total_identical_suites += 1
                suite_starters.remove(suite_starters[k])
                suite_starters.remove(suite_starters[k])
            else:
                # Increments j to test the next item on the list
                k += 1
        return total_identical_suites

    # Returns total number of suites starting with the same number but of different type
    def same_number_suites(self, hand):
        hand_copy = hand.copy()
        suite_starters = []
        total_same_number_suites = 0
        i = 0

        # Collects all suite starters and store them in a list
        while i < len(hand_copy):
            tile_name = hand_copy[i]
            for j in range(1, 8):
                if tile_name[0] == str(j):
                    next_tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                    after_next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if hand_copy.count(next_tile_name) > 0 and hand_copy.count(after_next_tile_name) > 0:
                        suite_starters.append(tile_name)
                        hand_copy.remove(tile_name)
                        hand_copy.remove(next_tile_name)
                        hand_copy.remove(after_next_tile_name)
                        # Since suite items were removed in the list, we need to retest the same position
                        i -= 1
            # Increments i to test the next item on the list
            i += 1

        # Checks if how many times a different suite starts with same number
        for k in suite_starters:
            for m in suite_starters:
                if k[0] == m[0] and k[1:] != m[1:]:
                    total_same_number_suites += 1

        # Since we browser with two loops the same list, we need to divide by two
        return total_same_number_suites / 2

    # Returns true if hand holds a straight (all tiles of same type from 1 to 9)
    def straight_suites(self, hand):
        hand_copy = hand.copy()
        suite_starters = []
        i = 0
        k = 0

        # Collects all suite starters and store them in a list
        while i < len(hand_copy):
            tile_name = hand_copy[i]
            for j in range(1, 8):
                if tile_name[0] == str(j):
                    next_tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                    after_next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if hand_copy.count(next_tile_name) > 0 and hand_copy.count(after_next_tile_name) > 0:
                        suite_starters.append(tile_name)
                        hand_copy.remove(tile_name)
                        hand_copy.remove(next_tile_name)
                        hand_copy.remove(after_next_tile_name)
                        # Since suite items were removed in the list, we need to retest the same position
                        i -= 1
            # Increments i to test the next item on the list
            i += 1

        # Checks if there same straight suite members
        for k in suite_starters:
            first_suite_member = k[:0] + str(int(k[0]) + 3) + k[1:]
            second_suite_member = k[:0] + str(int(k[0]) + 6) + k[1:]

            if suite_starters.count(first_suite_member) > 0 and suite_starters.count(second_suite_member) > 0:
                return True

        return False

    # Returns true if hand has 3 triplets that have the same numbers
    def three_same_number_triplets(self, hand):
        hand_copy = hand.copy()
        triplets_list = []
        i = 0

        while i < len(hand_copy):
            tile_name = hand_copy[i]
            if hand_copy.count(tile_name) == constant.TRIPLET_SIZE:
                triplets_list.append(tile_name)
                for j in range(constant.TRIPLET_SIZE):
                    hand_copy.remove(tile_name)
            else:
                # Increments i to test the next item on the list
                i += 1

        # Only keeps the numbers for comparisons
        for k in range(len(triplets_list)):
            tile_name = triplets_list[k]
            tile_number = tile_name[0]
            triplets_list.pop(k)
            triplets_list.insert(k, tile_number)

        # Checks if there are at lest 3 members that share the same number
        for m in triplets_list:
            if triplets_list.count(m) >= 3:
                return True
        return False

    # Check if hand holds dragon tiles
    def dragon_tiles_hand(self, hand):
        for i in hand:
            if self.dragon_tiles_list.count(i) > 0:
                return True
        return False

    # Check if hand holds wind tiles
    def wind_tiles_hand(self, hand):
        for i in hand:
            if self.wind_tiles_list.count(i) > 0:
                return True
        return False

    # Check if hand holds terminal tiles
    def terminal_tiles_hand(self, hand):
        for i in hand:
            if self.terminal_tiles_list.count(i) > 0:
                return True
        return False

    # Returns own wind tile
    def get_wind_tile(self, wind):
        wind_tile = ""

        if wind == "West":
            wind_tile = "Ton"
        elif wind == "South":
            wind_tile = "Nan"
        elif wind == "East":
            wind_tile = "Xia"
        elif wind == "North":
            wind_tile = "Pei"

        return wind_tile

    # Check if hand is a valid found melds hand
    def four_melds_hand(self, hand):
        # Four melds hands are made of 1 pair and suites, quads and triplets
        hand_copy = hand.copy()
        hand_copy, total_suites = self.get_hand_suites(hand_copy)
        hand_copy, total_quads = self.get_hand_quads(hand_copy)
        hand_copy, total_triplets = self.get_hand_triplets(hand_copy)
        hand_copy, total_pairs = self.get_hand_pairs(hand_copy)

        if len(hand_copy) == 0 and total_pairs == 1 and (total_suites + total_quads + total_triplets) == 4:
            return True
        else:
            return False

    # Check if hand holds own or prevalent wind tiles
    def wind_hand(self, hand):
        if hand.count(self.get_wind_tile(self.comboBox_ownWind.currentText())) > 0\
                or hand.count(self.get_wind_tile(self.comboBox_prevalentWind.currentText())) > 0:
            return True
        return False

    # Checks if hand holds Chiitoitsu yaku, a hand with 7 pairs
    def chiitoitsu_yaku(self, hand):
        hand_copy = hand.copy()
        hand_copy, total_pairs = self.get_hand_pairs(hand_copy)

        if total_pairs == 7:
            return True
        else:
            return False

    # Checks Pinfu yaku validity, a closed four melds hand without fu points awarded
    def pinfu_yaku(self, hand):
        fu_points = 0
        fu_points += self.minko_anko_fu_points(hand)
        fu_points += self.minkan_ankan_fu_points(hand)
        fu_points += self.toitsu_fu_points(hand)
        fu_points += self.menzenkafu_fu_points(hand)

        if fu_points and self.four_melds_hand(hand) and not self.hand_is_open:
            return True
        else:
            return False

    # Checks Iipeiko yaku validity, a closed four melds hand with two identical suites
    def iipeiko_yaku(self, hand):
        hand_copy = hand.copy()

        if self.identical_suites(hand) == 1 and self.four_melds_hand(hand) and not self.hand_is_open:
            return True
        else:
            return False

    # Checks Ryanpeiko yaku validity, a closed hand with 2x two identical suites
    def ryanpeiko_yaku(self, hand):
        if self.identical_suites(hand) == 2 and self.four_melds_hand(hand) and not self.hand_is_open:
            return True
        else:
            return False

    # Checks Sanshoku yaku validity, a hand with 3 different suites starting with same number
    def sanshoku_yaku(self, hand):
        if self.same_number_suites(hand) == 3 and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Ittsuu validity, a hand with 3 suites of same type covering nombers from 1 to 9
    def ittsuu_yaku(self, hand):
        if self.straight_suites(hand) and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks San Anko yaku validity, a hand with at least 3 self drawn triplets/quads
    def sananko_yaku(self, hand):
        hand_copy = hand.copy()
        hand_copy, total_suites = self.get_hand_suites(hand_copy)
        hand_copy, total_quads = self.get_hand_quads(hand_copy)
        hand_copy, total_triplets = self.get_hand_triplets(hand_copy)

        if total_triplets + total_quads >= 3 and self.total_pon + self.total_kan <= 1 and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Toitoi yaku validity, a hand with ony triplets/quads (and a pair).
    # If all four triplets/quads are closed, the hand becomes Sananko instead
    def toitoi_yaku(self, hand):
        hand_copy = hand.copy()
        hand_copy, total_suites = self.get_hand_suites(hand_copy)

        if total_suites == 0 and self.total_pon + self.total_kan != 0 and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Sankantsu validity, a hand with 3 quads
    def sankantsu_yaku(self, hand):
        hand_copy = hand.copy()
        hand_copy, total_suites = self.get_hand_suites(hand_copy)
        hand_copy, total_quads = self.get_hand_quads(hand_copy)

        if total_quads == 3 and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Sukantsu validity, a hand with 4 quads
    def sukantsu_yaku(self, hand):
        hand_copy = hand.copy()
        hand_copy, total_suites = self.get_hand_suites(hand_copy)
        hand_copy, total_quads = self.get_hand_quads(hand_copy)

        if total_quads == 4 and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Sanshoku Doko yaku validity, a hand with 3 triplets of same number.
    def sanshokudoko_yaku(self, hand):
        if self.three_same_number_triplets(hand) and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Tanyao yaku validity, a closed hand without terminals and honors.
    def tanyao_yaku(self, hand):
        if not self.terminal_tiles_hand(hand) and not self.wind_tiles_hand(hand) and not self.dragon_tiles_hand(hand)\
                and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Returns how many Fanpai yaku are in hand (triplets/quads made of honors).
    def fanpai_yaku(self, hand):
        fanpai_total = 0

        if self.four_melds_hand(hand):
            valid_honors = []

            valid_honors.extend(self.dragon_tiles_list)
            valid_honors.append(self.get_wind_tile(self.comboBox_ownWind.currentText()))
            valid_honors.append(self.get_wind_tile(self.comboBox_prevalentWind.currentText()))

            for i in valid_honors:
                if hand.count(i) >= 3:
                    fanpai_total += 1
        return fanpai_total

    # Checks Chanta validity, a hand with at least one suite, all suites should be 1-2-3 or 7-8-9
    # Triplets/Quads/Pairs must be terminals or honors.
    def chanta_yaku(self, hand):
        hand_copy = hand.copy()
        suite_starters = []
        i = 0

        # Collects all suite starters and store them in a list
        while i < len(hand_copy):
            tile_name = hand_copy[i]
            for j in range(1, 8):
                if tile_name[0] == str(j):
                    next_tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                    after_next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if hand_copy.count(next_tile_name) > 0 and hand_copy.count(after_next_tile_name) > 0:
                        suite_starters.append(tile_name)
                        hand_copy.remove(tile_name)
                        hand_copy.remove(next_tile_name)
                        hand_copy.remove(after_next_tile_name)
                        # Since suite items were removed in the list, we need to retest the same position
                        i -= 1
            # Increments i to test the next item on the list
            i += 1

        # Checks first condition which is at least one suite
        if len(suite_starters) >= 1:
            # Checks that all suites starts with allowed starters
            for k in suite_starters:
                if not k[0] == "1" and not k[0] == "7":
                    return False
        else:
            return False

        # If the hand met all conditions until here, we need to check that all other tiles are honors or terminals
        valid_tiles = []
        valid_tiles.extend(self.dragon_tiles_list)
        valid_tiles.extend(self.wind_tiles_list)
        valid_tiles.extend(self.terminal_tiles_list)

        for m in hand_copy:
            valid = False
            for n in valid_tiles:
                if m == n:
                    valid = True
            if not valid:
                return False

        # If the hand met all conditions until here, we just need to check that the hand is a valid four melds hand
        if self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Junchan validity, a hand with at least one suite, all suites should be 1-2-3 or 7-8-9
    # Triplets/Quads/Pairs must be terminals.
    def junchan_yaku(self, hand):
        hand_copy = hand.copy()
        suite_starters = []
        i = 0

        # Collects all suite starters and store them in a list
        while i < len(hand_copy):
            tile_name = hand_copy[i]
            for j in range(1, 8):
                if tile_name[0] == str(j):
                    next_tile_name = tile_name[:0] + str(int(tile_name[0]) + 1) + tile_name[1:]
                    after_next_tile_name = next_tile_name[:0] + str(int(next_tile_name[0]) + 1) + next_tile_name[1:]

                    if hand_copy.count(next_tile_name) > 0 and hand_copy.count(after_next_tile_name) > 0:
                        suite_starters.append(tile_name)
                        hand_copy.remove(tile_name)
                        hand_copy.remove(next_tile_name)
                        hand_copy.remove(after_next_tile_name)
                        # Since suite items were removed in the list, we need to retest the same position
                        i -= 1
            # Increments i to test the next item on the list
            i += 1

        # Checks first condition which is at least one suite
        if len(suite_starters) >= 1:
            # Checks that all suites starts with allowed starters
            for k in suite_starters:
                if not k[0] == "1" and not k[0] == "7":
                    return False
        else:
            return False

        # If the hand met all conditions until here, we need to check that all other tiles are honors or terminals
        valid_tiles = []
        valid_tiles.extend(self.terminal_tiles_list)

        for m in hand_copy:
            valid = False
            for n in valid_tiles:
                if m == n:
                    valid = True
            if not valid:
                return False

        # If the hand met all conditions until here, we just need to check that the hand is a valid four melds hand
        if self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Honro yaku validity, a hand with only terminals and honors.
    def honro_yaku(self, hand):
        valid_tiles = []
        valid_tiles.extend(self.dragon_tiles_list)
        valid_tiles.extend(self.wind_tiles_list)
        valid_tiles.extend(self.terminal_tiles_list)

        for m in hand:
            valid = False
            for n in valid_tiles:
                if m == n:
                    valid = True
            if not valid:
                return False

        return True

    # Checks Shosangen yaku validity, a hand with two triplets/quads of dragons and a pair of the other.
    def shosangen_yaku(self, hand):
        # Collects the pairs and store them in a copy
        hand_copy = hand.copy()
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_quads(hand_copy)[0]
        hand_copy = self.get_hand_triplets(hand_copy)[0]

        valid_tiles = []
        valid_tiles.extend(self.dragon_tiles_list)

        # Checks if the pairs are made of dragon tiles
        for i in hand_copy:
            valid = False
            for j in valid_tiles:
                if i == j:
                    valid = True
            if not valid:
                return False
            
        # Collects the triplets and quads and store them in a copy
        hand_copy = hand.copy()
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_pairs(hand_copy)[0]
        total_dragon_tiles = 0

        # Checks if there are two triplets/quads made of dragon tiles
        for m in hand_copy:
            for n in valid_tiles:
                if m == n:
                    total_dragon_tiles += 1

        # It the total of dragon tiles outnumbers the tiles needed for a single KAN, that means that there are
        # at least two dragon triplets (that needs 6 tiles)
        if self.four_melds_hand(hand) and total_dragon_tiles > constant.KAN_SIZE:
            return True
        else:
            return False

    # Checks Hon'itsu yaku validity, a hand with tiles of same type or honor tiles
    def honitsu_yaku(self, hand):
        if self.four_melds_hand(hand):
            valid = True

            # Checks if all tiles are man or honor tiles
            valid_tiles = []
            valid_tiles.extend(self.dragon_tiles_list)
            valid_tiles.extend(self.wind_tiles_list)
            valid_tiles.extend(self.man_tiles_list)

            for i in hand:
                if valid_tiles.count(i) == 0:
                    valid = False

            if not valid:
                valid = True

                # Checks if all tiles are pin or honor tiles
                valid_tiles.clear()
                valid_tiles.extend(self.dragon_tiles_list)
                valid_tiles.extend(self.wind_tiles_list)
                valid_tiles.extend(self.pin_tiles_list)

                for i in hand:
                    if valid_tiles.count(i) == 0:
                        valid = False

                if not valid:
                    valid = True

                    # Checks if all tiles are so or honor tiles
                    valid_tiles.clear()
                    valid_tiles.extend(self.dragon_tiles_list)
                    valid_tiles.extend(self.wind_tiles_list)
                    valid_tiles.extend(self.so_tiles_list)

                    for i in hand:
                        if valid_tiles.count(i) == 0:
                            valid = False
                    if not valid:
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return False

    # Checks Chin'itsu yaku validity, a hand with numbered tiles of same type only
    def chinitsu_yaku(self, hand):
        if self.four_melds_hand(hand):
            valid = True

            # Checks if all tiles are man
            valid_tiles = []
            valid_tiles.extend(self.man_tiles_list)

            for i in hand:
                if valid_tiles.count(i) == 0:
                    valid = False

            if not valid:
                valid = True

                # Checks if all tiles are pin tiles
                valid_tiles.clear()
                valid_tiles.extend(self.pin_tiles_list)

                for i in hand:
                    if valid_tiles.count(i) == 0:
                        valid = False

                if not valid:
                    valid = True

                    # Checks if all tiles are so tiles
                    valid_tiles.clear()
                    valid_tiles.extend(self.so_tiles_list)

                    for i in hand:
                        if valid_tiles.count(i) == 0:
                            valid = False
                    if not valid:
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return False

    # Checks Kokushi Muso yaku validity, a hand with all terminals and honors and just a pair
    def kokushimuso_yaku(self, hand):
        # Checks if all tiles are man or honor tiles
        valid_tiles = []
        valid_tiles.extend(self.dragon_tiles_list)
        valid_tiles.extend(self.wind_tiles_list)
        valid_tiles.extend(self.terminal_tiles_list)

        for i in hand:
            valid = False
            for j in valid_tiles:
                if i == j:
                    valid = True
            if not valid:
                return False

        hand_copy = hand.copy()

        hand_copy, total_suites = self.get_hand_suites(hand_copy)
        hand_copy, total_quads = self.get_hand_quads(hand_copy)
        hand_copy, total_triplets = self.get_hand_triplets(hand_copy)
        hand_copy, total_pairs = self.get_hand_pairs(hand_copy)

        if total_pairs == 1 and total_quads == 0 and total_triplets == 0:
            return True
        else:
            return False

    # Checks Suu Anko yaku validity, a hand with 4 self drawn triplets/quads
    def suanko_yaku(self, hand):
        hand_copy = hand.copy()
        hand_copy, total_suites = self.get_hand_suites(hand_copy)
        hand_copy, total_quads = self.get_hand_quads(hand_copy)
        hand_copy, total_triplets = self.get_hand_triplets(hand_copy)

        if total_triplets + total_quads == 4 and self.total_pon + self.total_kan == 0 and self.four_melds_hand(hand):
            return True
        else:
            return False

    # Checks Daisangen yaku validity, a hand with three triplets/quads of dragons
    def daisangen_yaku(self, hand):
        valid_tiles = []
        valid_tiles.extend(self.dragon_tiles_list)
        total_dragon_tiles = 0

        # Collects the triplets and quads and store them in a copy
        hand_copy = hand.copy()
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_pairs(hand_copy)[0]

        # Checks if there are three triplets/quads made of dragon tiles
        for m in hand_copy:
            for n in valid_tiles:
                if m == n:
                    total_dragon_tiles += 1

        # It the total of dragon tiles outnumbers the tiles needed for two KANs, that means that there are
        # at least three dragon triplets (that needs 9 tiles)
        if self.four_melds_hand(hand) and total_dragon_tiles > 2 * constant.KAN_SIZE:
            return True
        else:
            return False

    # Checks Shosushii yaku validity, a hand with three triplets/quads of winds and a pair of the other.
    def shosushii_yaku(self, hand):
        # Collects the pairs and store them in a copy
        hand_copy = hand.copy()
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_quads(hand_copy)[0]
        hand_copy = self.get_hand_triplets(hand_copy)[0]

        valid_tiles = []
        valid_tiles.extend(self.wind_tiles_list)

        # Checks if the pairs are made of wind tiles
        for i in hand_copy:
            valid = False
            for j in valid_tiles:
                if i == j:
                    valid = True
            if not valid:
                return False

        # Collects the triplets and quads and store them in a copy
        hand_copy = hand.copy()
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_pairs(hand_copy)[0]
        total_wind_tiles = 0

        # Checks if there are three triplets/quads made of wind tiles
        for m in hand_copy:
            for n in valid_tiles:
                if m == n:
                    total_wind_tiles += 1

        # It the total of dragon tiles outnumbers the tiles needed for two KANs, that means that there are
        # at least three wind triplets (that needs 9 tiles)
        if self.four_melds_hand(hand) and total_wind_tiles > 2 * constant.KAN_SIZE:
            return True
        else:
            return False

    # Checks Daisushii yaku validity, a hand with four triplets/quads of winds
    def daisushii_yaku(self, hand):
        # Collects the triplets and quads and store them in a copy
        hand_copy = hand.copy()
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_pairs(hand_copy)[0]
        total_wind_tiles = 0

        valid_tiles = []
        valid_tiles.extend(self.wind_tiles_list)

        # Counts the different types of wind tiles
        for m in valid_tiles:
            if hand_copy.count(m) > 0:
                total_wind_tiles += 1

        # True if all kind of winds are present and the hand has four melds
        if self.four_melds_hand(hand) and total_wind_tiles == len(self.wind_tiles_list):
            return True
        else:
            return False

    # Checks Tsuiiso yaku validity, a hand with honors only
    def tsuiiso_yaku(self, hand):
        valid_tiles = []
        valid_tiles.extend(self.dragon_tiles_list)
        valid_tiles.extend(self.wind_tiles_list)

        for i in hand:
            if valid_tiles.count(i) == 0:
                return False
        return True

    # Checks Chinroto yaku validity, a hand with terminals only
    def chinroto_yaku(self, hand):
        valid_tiles = []
        valid_tiles.extend(self.terminal_tiles_list)

        for i in hand:
            if valid_tiles.count(i) == 0:
                return False
        return True

    # Checks Ryuiiso yaku validity, a hand with terminals only
    def ryuiiso_yaku(self, hand):
        valid_tiles = []
        valid_tiles.extend(self.green_tiles_list)

        for i in hand:
            if valid_tiles.count(i) == 0:
                return False
        return True

    # Checks Churen Poto yaku validity, a hand with 1-1-1-2-3-4-5-6-7-8-9-9-9 of one tile type,
    # plus any other tile of same type
    def churenpoto_yaku(self, hand):
        # Checks all tiles are numbered tiles and of one type)
        valid = True

        # Checks if all tiles are man
        valid_tiles = []
        valid_tiles.extend(self.man_tiles_list)

        for i in hand:
            if valid_tiles.count(i) == 0:
                valid = False

        if not valid:
            valid = True

            # Checks if all tiles are pin tiles
            valid_tiles.clear()
            valid_tiles.extend(self.pin_tiles_list)

            for i in hand:
                if valid_tiles.count(i) == 0:
                    valid = False

            if not valid:
                valid = True

                # Checks if all tiles are so tiles
                valid_tiles.clear()
                valid_tiles.extend(self.so_tiles_list)

                for i in hand:
                    if valid_tiles.count(i) == 0:
                        valid = False
                if not valid:
                    valid = False
            else:
                valid = True
        else:
            valid = True

        if valid:
            # Extraction of all tiles numbers and put them in a list
            tile_numbers = []
            for i in hand:
                tile_numbers.append(i[0])

            # Checks churen poto number conditions
            if tile_numbers.count("1") >= 3\
                    and tile_numbers.count("2") >= 1\
                    and tile_numbers.count("3") >= 1\
                    and tile_numbers.count("4") >= 1\
                    and tile_numbers.count("5") >= 1\
                    and tile_numbers.count("6") >= 1\
                    and tile_numbers.count("7") >= 1\
                    and tile_numbers.count("8") >= 1\
                    and tile_numbers.count("9") >= 3:
                return True
        else:
            return False

    # Returns if the player is the dealer
    def is_dealer(self):
        # In Riichi Mahjong, the player with west wind is always the dealer
        if self.comboBox_ownWind.currentText() == "West":
            return True
        else:
            return False

    # Fu points obtained trough triplets
    def minko_anko_fu_points(self, hand):
        hand_copy = hand.copy()
        fu_points = 0

        # List of tiles that give extra fu points
        bonus_point_tiles = []
        bonus_point_tiles.extend(self.terminal_tiles_list)
        bonus_point_tiles.extend(self.wind_tiles_list)
        bonus_point_tiles.extend(self.dragon_tiles_list)

        # Isolates triplets to calculate fu points based on triplets
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_pairs(hand_copy)[0]
        hand_copy = self.get_hand_quads(hand_copy)[0]

        # Separates open and closed triplets
        closed_triplets_list = []
        i = 0
        while i < len(hand_copy):
            if not self.open_triplets_list.count(hand_copy[i]) > 0 and closed_triplets_list.count(hand_copy[i]) == 0:
                closed_triplets_list.append(hand_copy[i])
            i += 1

        # Open triplets are worth 2 fu and closed are worth 4 fu
        fu_points += len(self.open_triplets_list) * 2 + len(closed_triplets_list) * 4

        # Bonus points for specific tiles, 2 for open triplets and 4 for closed triplets
        for j in bonus_point_tiles:
            if self.open_triplets_list.count(j) > 0:
                fu_points += 2
            elif closed_triplets_list.count(j) > 0:
                fu_points += 4

        return fu_points

    # Fu points obtained trough quads
    def minkan_ankan_fu_points(self, hand):
        fu_points = 0

        # List of tiles that give extra fu points
        bonus_point_tiles = []
        bonus_point_tiles.extend(self.terminal_tiles_list)
        bonus_point_tiles.extend(self.wind_tiles_list)
        bonus_point_tiles.extend(self.dragon_tiles_list)

        # Open triplets are worth 8 fu and closed are worth 16 fu
        fu_points += len(self.open_quads_list) * 8 + len(self.closed_quads_list) * 16

        # Bonus points for specific tiles, 2 for open triplets and 4 for closed triplets
        for j in bonus_point_tiles:
            if self.open_quads_list.count(j) > 0:
                fu_points += 8
            elif self.closed_quads_list.count(j) > 0:
                fu_points += 16

        return fu_points

    # Fu points obtained trough pairs
    def toitsu_fu_points(self, hand):
        hand_copy = hand.copy()
        fu_points = 0

        # List of tiles that give extra fu points
        bonus_point_tiles = [self.get_wind_tile(self.comboBox_ownWind.currentText()),
                             self.get_wind_tile(self.comboBox_prevalentWind.currentText())]
        bonus_point_tiles.extend(self.dragon_tiles_list)

        # Isolates quads to calculate fu points based on quads
        hand_copy = self.get_hand_suites(hand_copy)[0]
        hand_copy = self.get_hand_quads(hand_copy)[0]
        hand_copy = self.get_hand_triplets(hand_copy)[0]

        # Fu points for pairs with bonus point tiles
        for j in bonus_point_tiles:
            if hand_copy.count(j) > 0:
                fu_points += 2

        return fu_points

    # Checks if it's won by Ron
    def ron(self):
        if self.radioButton_ron.isChecked():
            return True
        else:
            return False

    # Checks if it's won by Tsumo
    def tsumo(self):
        if self.radioButton_tsumo.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Riichi
    def riichi(self):
        if self.checkBox_riichi.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Double Riichi
    def double_riichi(self):
        if self.checkBox_doubleRiichi.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Ippatsu
    def ippatsu(self):
        if self.checkBox_ippatsu.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Haitei
    def haitei(self):
        if self.checkBox_haitei.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Hotei
    def hotei(self):
        if self.checkBox_hotei.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Rinshan
    def rinshan(self):
        if self.checkBox_rinshan.isChecked():
            return True
        else:
            return False

    # Checks if it's won with Chankan
    def chankan(self):
        if self.checkBox_chankan.isChecked():
            return True
        else:
            return False

    # Return the total of dora
    def get_dora_total(self):
        return self.spinBox_dora.value()

    # Fu points obtained by winning through a claimed tile
    def menzenkafu_fu_points(self, hand):
        # Menzen Kafu points are worth 10
        if self.ron():
            return 10
        else:
            return 0

    # Fu points obtained by dawing winning tile
    def tsumo_fu_points(self, hand):
        # Tsumo if worth 2 fu
        if self.tsumo():
            return 2
        else:
            return 0

    # Han points calculation
    def han_points(self):
        # If the hand contains hands worth Yakuman (13 han), other small yakus and dora aren't taken in consideration
        # That's why Yakuman yaku must be checked first
        # Since Yakuman represents the limit of han, combination of Yakuman yaku is not counted
        if self.kokushimuso_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Kokushi muso\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.suanko_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Su anko\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.daisangen_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Daisangen\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.shosushii_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Shosushii\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.daisushii_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Daisushii\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.tsuiiso_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Tsuiiso\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.chinroto_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Chinroto\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.ryuiiso_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Ryuiiso\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.churenpoto_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Churen poto\n")
            return constant.YAKUMAN_HAN_POINTS

        if self.sukantsu_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Su kantsu\n")
            return constant.YAKUMAN_HAN_POINTS

        # Special conditions points
        if self.riichi():
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Riichi\n")

        if self.double_riichi():
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("Double Riichi\n")

        if self.tsumo() and not self.hand_is_open:
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Tsumo\n")

        if self.ippatsu():
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Ippatsu\n")

        if self.haitei():
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Haitei\n")

        if self.hotei():
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Hotei\n")

        # Must have at least one closed of open kan
        if self.rinshan() and self.total_kan + self.total_closed_kan > 0:
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Rinshan\n")

        # Must have at least one closed of open kan and one suite
        if self.chankan() and self.total_kan + self.total_closed_kan > 0 and self.get_hand_suites(self.hand)[1] > 0:
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Chankan\n")

        # Yaku points
        # Ryanpeiko has more value than chiitoitsu and takes precedence
        if self.chiitoitsu_yaku(self.hand) and not self.ryanpeiko_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("Chiitoitsu\n")

        if self.pinfu_yaku(self.hand):
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Pinfu")

        # Chiitoitsu and Ryanpeiko have more value than Iipeiko and take precedence
        # This yaku is incompatible with Honro
        if self.iipeiko_yaku(self.hand) and not self.chiitoitsu_yaku(self.hand) and not self.ryanpeiko_yaku(self.hand)\
                and not self.honro_yaku(self.hand):
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Ippeiko")

        if self.ryanpeiko_yaku(self.hand):
            self.total_han += 3
            self.plainTextEdit_Result.appendPlainText("Ryanpeiko")

        if self.sanshoku_yaku(self.hand):
            if self.hand_is_open:
                self.total_han += 1
                self.plainTextEdit_Result.appendPlainText("Sanshoku")
            else:
                self.total_han += 2
                self.plainTextEdit_Result.appendPlainText("Sanshoku")

        if self.ittsuu_yaku(self.hand):
            if self.hand_is_open:
                self.total_han += 1
                self.plainTextEdit_Result.appendPlainText("Ittsuu")
            else:
                self.total_han += 2
                self.plainTextEdit_Result.appendPlainText("Ittsuu")

        if self.toitoi_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("Toitoi")

        if self.sananko_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("San anko")

        if self.sanshokudoko_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("Sanshoku doko")

        if self.tanyao_yaku(self.hand):
            self.total_han += 1
            self.plainTextEdit_Result.appendPlainText("Tanyao")

        if self.sankantsu_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("San kantsu")

        # Each Fanpai is worth 1 han
        if self.fanpai_yaku(self.hand) > 0:
            total_fanpai = self.fanpai_yaku(self.hand)
            self.total_han += total_fanpai
            self.plainTextEdit_Result.appendPlainText(str(total_fanpai)+"x "+"Fanpai")

        # Junchan and Honro take precedence if conditions are met
        if self.chanta_yaku(self.hand) and not self.junchan_yaku(self.hand) and not self.honro_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Chanta")
            if self.hand_is_open:
                self.total_han += 1
            else:
                self.total_han += 2

        # Chinitsu and Honro take precedence if conditions are met
        if self.junchan_yaku(self.hand) and not self.chinitsu_yaku(self.hand) and not self.honro_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Junchan")
            if self.hand_is_open:
                self.total_han += 2
            else:
                self.total_han += 3

        if self.honro_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("Honro")

        if self.shosangen_yaku(self.hand):
            self.total_han += 2
            self.plainTextEdit_Result.appendPlainText("Shosangen")

        # Chinitsu take precedence if conditions are met
        if self.honitsu_yaku(self.hand) and not self.chinitsu_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Honitsu")
            if self.hand_is_open:
                self.total_han += 2
            else:
                self.total_han += 3

        if self.chinitsu_yaku(self.hand):
            self.plainTextEdit_Result.appendPlainText("Chinitsu")
            if self.hand_is_open:
                self.total_han += 5
            else:
                self.total_han += 6

        # Each dora is worth 1 extra han
        self.total_han += self.get_dora_total()

        if self.total_han >= constant.YAKUMAN_HAN_POINTS:
            return constant.YAKUMAN_HAN_POINTS
        else:
            return self.total_han

    # Fu points calculation
    def fu_points(self, hand):
        # Checks chiitoitsu special scoring rule
        if self.chiitoitsu_yaku(self.hand) and not self.ryanpeiko_yaku(self.hand):
            self.total_fu = 25
        else:
            self.total_fu += self.minko_anko_fu_points(hand)
            self.total_fu += self.minkan_ankan_fu_points(hand)
            self.total_fu += self.toitsu_fu_points(hand)
            self.total_fu += self.menzenkafu_fu_points(hand)
            if not self.pinfu_yaku(hand):
                self.total_fu += self.tsumo_fu_points(hand)
            # Fu points must but round up to highest 10s
            self.total_fu = math.ceil(self.total_fu/10)*10

    # Checks if points are Mangan worth
    def is_mangan(self, points):
        if self.is_dealer() and points >= constant.MANGAN_POINTS * 1.5:
            return True
        elif not self.is_dealer() and points >= constant.MANGAN_POINTS:
            return True
        else:
            return False

    # Calculates the total score of the hand based on possible yakus
    def calculate(self):
        # Mangan is a unit used to calculate the score when it's above 2000 points
        mangan = False

        if self.is_valid_hand():
            self.plainTextEdit_Result.clear()
            self.plainTextEdit_Result.appendPlainText("Your hand holds:")
            self.total_han = self.han_points()

            if self.total_han == 0:
                self.plainTextEdit_Result.appendPlainText("No yaku.")

            self.fu_points(self.hand)
            self.plainTextEdit_Result.appendPlainText("\n" + str(self.total_han) + " han " + str(self.total_fu) + " fu")

            points = self.total_fu * (2 ** (2 + self.total_han))

            if self.is_dealer():
                points *= 6
            else:
                points *= 4

            points = math.ceil(points / 100) * 100

            if self.is_mangan(points):
                if 2 < self.total_han < 6:
                    if self.is_dealer():
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: "
                                                                  + str(constant.MANGAN_POINTS * 1.5))
                    else:
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: " + str(constant.MANGAN_POINTS))
                    self.plainTextEdit_Result.appendPlainText("MANGAN!")
                elif 5 < self.total_han < 8:
                    if self.is_dealer():
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: "
                                                                  + str(constant.MANGAN_POINTS * 1.5 * 1.5))
                    else:
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: "
                                                                  + str(constant.MANGAN_POINTS * 1.5))
                    self.plainTextEdit_Result.appendPlainText("HANEMAN!!")
                elif 7 < self.total_han < 11:
                    if self.is_dealer():
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: "
                                                                  + str(constant.MANGAN_POINTS * 2 * 1.5))
                    else:
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: " + str(constant.MANGAN_POINTS * 2))
                    self.plainTextEdit_Result.appendPlainText("BAIMAN!!!")
                elif 10 < self.total_han < 13:
                    if self.is_dealer():
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: "
                                                                  + str(constant.MANGAN_POINTS * 3 * 1.5))
                    else:
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: " + str(constant.MANGAN_POINTS * 3))
                    self.plainTextEdit_Result.appendPlainText("SANBAIMAN!!!!")
                elif self.total_han >= constant.YAKUMAN_HAN_POINTS:
                    if self.is_dealer():
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: "
                                                                  + str(constant.MANGAN_POINTS * 4 * 1.5))
                    else:
                        self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: " + str(constant.MANGAN_POINTS * 4))
                    self.plainTextEdit_Result.appendPlainText("YAKUMAN!!!!!")
            else:
                self.plainTextEdit_Result.appendPlainText("\nTOTAL POINTS: " + str(points))
        else:
            self.plainTextEdit_Result.clear()
            self.plainTextEdit_Result.appendPlainText("Your hand is not valid. A Riichi Mahjong hands must hold a four melds hand, chiitoitsu or kokushimuso.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
