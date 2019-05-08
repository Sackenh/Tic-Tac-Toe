#!/usr/bin/env.python3
__author__ = "Garrett Sacken"

from sys import path
import sys
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load
from os import path
from PyQt5.QtCore import pyqtSlot, QSettings, Qt, QTimer, QCoreApplication
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

class TicTacToe(QMainWindow):
    """A Game of Tic Tac Toe"""
    ticTacToe1 = ticTacToe2 = ticTacToe3 = ticTacToe4 = ticTacToe5 = ticTacToe6 = ticTacToe7 = ticTacToe8 = \
        ticTacToe9 = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.appSettings = QSettings()
        self.quitCounter = 0;

        uic.loadUi("ticTacToe.ui", self)

        buttonArray = []
        buttonArray.add(self.ticTacToe1, self.ticTacToe2, self.ticTacToe3, self.ticTacToe4, self.ticTacToe5,
                        self.ticTacToe6, self.ticTacToe7, self.ticTacToe8, self.ticTacToe9)

        self.ticTacToe1.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe2.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe3.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe4.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe5.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe6.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe7.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe8.clicked.connect(self.buttonClickedHandler)
        self.ticTacToe9.clicked.connect(self.buttonClickedHandler)

    def updateUI(self):
        self.ticTacToe1.setText("X")
        self.ticTacToe2.setText("X")
        self.ticTacToe3.setText("X")
        self.ticTacToe4.setText("X")
        self.ticTacToe5.setText("X")
        self.ticTacToe6.setText("X")
        self.ticTacToe7.setText("X")
        self.ticTacToe8.setText("X")
        self.ticTacToe9.setText("X")
        self.playerWinsLabel.setText(str("%i" % self.playerWins))
        self.computerWinsLabel.setText(str("%i" % self.computerWins))
        self.totalGamesLabel.setText(str("%i" % self.totalGames))

    def restartGame(self):
        if self.restartButton.clicked():
            self.logger.debug("Restarting game")
        self.ticTacToe1.setText("")
        self.ticTacToe2.setText("")
        self.ticTacToe3.setText("")
        self.ticTacToe4.setText("")
        self.ticTacToe5.setText("")
        self.ticTacToe6.setText("")
        self.ticTacToe7.setText("")
        self.ticTacToe8.setText("")
        self.ticTacToe9.setText("")
        self.playerWins = 0
        self.computerWins = 0
        self.totalGames = 0

    def buttonClickedHandler(self):
        self.results = ""
        if self.ticTacToe1.buttonClicked():
            self.ticTacToe1.setDisabled = True
            self.ticTacToe1.setText = "X"
        elif self.ticTacToe2.buttonClicked():
            self.tictactoe2.setDisabled = True
            self.ticTacToe2.setText = "X"
        elif self.ticTacToe3.buttonclicked():
            self.ticTacToe3.setDisabled = True
            self.ticTacToe3.setText = "X"
        elif self.ticTacToe4.buttonClicked():
            self.tictactoe4.setDisabled = True
            self.ticTacToe4.setText = "X"
        elif self.ticTacToe5.buttonClicked():
            self.ticTacToe5.setDisabled = True
            self.ticTacToe5.setText = "X"
        elif self.ticTacToe6.buttonClicked():
            self.ticTacToe6.setDisabled = True
            self.ticTacToe6.setText = "X"
        elif self.ticTacToe7.buttonClicked():
            self.ticTacToe7.setDisabled = True
            self.ticTacToe7.setText = "X"
        elif self.ticTacToe8.buttonClicked():
            self.ticTacToe8.setDisabled = True
            self.ticTacToe8.setText = "X"
        elif self.ticTacToe9.buttonClicked():
            self.ticTacToe9.setDisabled = True
            self.ticTacToe9.setText = "X"
        self.updateUI()

    def clearBoard(self):
        self.ticTacToe1.setText = ""
        self.ticTacToe1.setEnabled = True
        self.ticTacToe2.setText = ""
        self.ticTacToe2.setEnabled = True
        self.ticTacToe3.setText = ""
        self.ticTacToe3.setEnabled = True
        self.ticTacToe4.setText = ""
        self.ticTacToe4.setEnabled = True
        self.ticTacToe5.setText = ""
        self.ticTacToe5.setEnabled = True
        self.ticTacToe6.setText = ""
        self.ticTacToe6.setEnabled = True
        self.ticTacToe7.setText = ""
        self.ticTacToe7.setEnabled = True
        self.ticTacToe8.setText = ""
        self.ticTacToe8.setEnabled = True
        self.ticTacToe9.setText = ""
        self.ticTacToe9.setEnabled = True

    def checkWin(self):
        if self.ticTacToe1.text & self.ticTacToe2.text & self.ticTacToe3.text == "X" or "O":
            self.totalGames += 1
        elif self.ticTacToe4.text & self.ticTacToe5.text & self.ticTacToe6.text == "X" or "O":
            self.totalGames += 1
        elif self.ticTacToe7.text & self.ticTacToe8.text & self.ticTacToe9.text == "X" or "O":
            self.totalGames += 1
        elif self.tictacToe1.text & self.ticTacToe4.text & self.tictactoe7.text == "X" or "O":
            self.totalGames += 1
        elif self.ticTacToe2.text & self.ticTacToe5.text & self.tictactoe8.text == "X" or "O":
            self.totalGames += 1
        elif self.ticTacToe3.text & self.ticTacToe6.text & self.ticTacToe9.text == "X" or "O":
            self.totalGames += 1
        elif self.ticTacToe1.text & self.tictactoe5.text & self.ticTacToe9.text == "X" or "O":
            self.totalGames += 1
        elif self.tictactoe3.text & self.ticTacToe5.text & self.ticTacToe7.text == "X" or "O":
            self.totalGames += 1
        else:
            self.draws = 1



if __name__ == "__main__":
    QCoreApplication.setOrganizationName("Sacken Software")
    QCoreApplication.setOrganizationDomain("sackensoftware.com")
    QCoreApplication.setApplicationName("Tic Tac Toe")
    appSettings = QSettings()

call = TicTacToe()
call()



