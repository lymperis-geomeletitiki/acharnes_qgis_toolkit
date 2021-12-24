# -*- coding: utf-8 -*-
"""
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from qgis.PyQt import uic
from qgis.PyQt.QtCore import QVariant, Qt, QCoreApplication
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtGui import QStandardItemModel, QStandardItem, QIcon

from qgis.core import Qgis, QgsProject

import json

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Settings_Dialog.ui'))

settings_path = os.path.join(os.path.dirname(__file__), 'settings', 'settings.json')






def tr(string):
    return QCoreApplication.translate('Processing', string)

class SettingsDialog(QDialog, FORM_CLASS):
    """Settings Dialog module, lives in project root/Settings_Dialog.py"""


    def __init__(self, iface):
        """Initialize the data settings dialog window."""
        super(SettingsDialog, self).__init__(iface.mainWindow())
        self.setupUi(self)
        self.iface = iface

        
        

    def showEvent(self, event):
        """The dialog is being shown. We need to initialize it."""


        #connect the OK button
        self.accept_button.clicked.connect(self.accept)

        #read settings file
        with open(settings_path, 'r') as settings_file:
            settings = json.load(settings_file)

            # update the dialog fields
            self.geom_db_host.setText(settings['DB']['Geometry']['host'])
            self.geom_db_name.setText(settings['DB']['Geometry']['db'])
            self.geom_db_user.setText(settings['DB']['Geometry']['user'])
            self.geom_db_passw.setText(settings['DB']['Geometry']['passw'])
            self.attr_db_host.setText(settings['DB']['Attributes']['host'])
            self.attr_db_name.setText(settings['DB']['Attributes']['db'])
            self.attr_db_user.setText(settings['DB']['Attributes']['user'])
            self.attr_db_passw.setText(settings['DB']['Attributes']['passw'])
        settings_file.close()

        super(SettingsDialog, self).showEvent(event)
        

    def accept(self):
        """Called when the OK button has been pressed."""

        with open(settings_path, 'r+') as settings_file:
            settings = json.load(settings_file)

            # update the settings fields
            settings['DB']['Geometry']['host'] = self.geom_db_host.text()
            settings['DB']['Geometry']['db'] = self.geom_db_name.text()
            settings['DB']['Geometry']['user'] = self.geom_db_user.text()
            settings['DB']['Geometry']['passw'] = self.geom_db_passw.text()
            settings['DB']['Attributes']['host'] = self.attr_db_host.text()
            settings['DB']['Attributes']['db'] = self.attr_db_name.text()
            settings['DB']['Attributes']['user'] = self.attr_db_user.text()
            settings['DB']['Attributes']['passw'] = self.attr_db_passw.text()

            settings_file.seek(0)        # <--- should reset file position to the beginning.
            json.dump(settings, settings_file, indent=4)
            settings_file.truncate()

        settings_file.close()
        self.close()


       
    
    def openFolderDialog(self):
        None
  

