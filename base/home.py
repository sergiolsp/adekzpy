'''
Created on 27/08/2013

@author: Sergio
'''

import PyQt4
from PyQt4 import QtCore, QtGui, QtSvg
import webbrowser

app = QtGui.QApplication([])

i = QtGui.QSystemTrayIcon()

m = QtGui.QMenu()

def quitCB():
 QtGui.QApplication.quit()
 
def aboutToShowCB():
 print 'Fechou!'

def openUrl():
 print 'abrindo Pekz...'
 url="http://master.adekz.com:8888/web/adekzpekz"
 webbrowser.open(url)
 
def teste():
 print 'teste!'

 
m.addAction('Pekz', openUrl)
m.addAction('Quit', quitCB)

QtCore.QObject.connect(m, QtCore.SIGNAL('aboutToShow()'), aboutToShowCB)
i.setContextMenu(m)


svg = QtSvg.QSvgRenderer('anvil.svg')
if not svg.isValid():
 raise RuntimeError('bad SVG')

pm = QtGui.QPixmap(16, 16)
painter = QtGui.QPainter(pm)
svg.render(painter)
icon = QtGui.QIcon(pm)
i.setIcon(icon)
i.show()

app.exec_()

del painter, pm, svg # avoid the paint device getting
del i, icon          # deleted before the painter
del app
