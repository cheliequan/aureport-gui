# -*- coding: utf-8 -*-
#!/usr/bin/env python

from qt import *
from secreport import *
import sys
import locale
import settings
import gettext
from settings import *
from util import _

def installQTStuffTranslator(app):
    qtstuff_trans = QTranslator(app)
    qm_file = QString( "qtstuff_" ) + QTextCodec.locale()
    qtstuff_trans.load( qm_file, qtstuff_localedir)
    app.installTranslator(qtstuff_trans)
    return qtstuff_trans

if __name__=="__main__":
    locale.setlocale(locale.LC_ALL, '')
    gettext.bindtextdomain(settings.gettext_domain, settings.localedir)
    gettext.bind_textdomain_codeset(settings.gettext_domain, 'utf-8')
    gettext.textdomain(settings.gettext_domain)
    app = QApplication(sys.argv)
    installQTStuffTranslator(app)
    win=Secreport()
    app.installEventFilter(win)
    win.show()
    app.connect(app, SIGNAL("lastWindowClosed()"),
                app, SLOT("quit()"))
    app.exec_loop()


