# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2010 Leszek Lesner <leszek@zevenos.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import gtk

from compmanager.helpers import get_builder

import gettext
from gettext import gettext as _
gettext.textdomain('compmanager')

class AboutCompmanagerDialog(gtk.AboutDialog):
    __gtype_name__ = "AboutCompmanagerDialog"

    def __new__(cls):
        """Special static method that's automatically called by Python when 
        constructing a new instance of this class.
        
        Returns a fully instantiated AboutCompmanagerDialog object.
        """
        builder = get_builder('AboutCompmanagerDialog')
        new_object = builder.get_object("about_compmanager_dialog")
        new_object.finish_initializing(builder)
        return new_object

    def finish_initializing(self, builder):
        """Called while initializing this instance in __new__

        finish_initalizing should be called after parsing the ui definition
        and creating a AboutCompmanagerDialog object with it in order to
        finish initializing the start of the new AboutCompmanagerDialog
        instance.
        
        Put your initialization code in here and leave __init__ undefined.
        """
        # Get a reference to the builder and set up the signals.
        self.builder = builder
        self.builder.connect_signals(self)

        # Code for other initialization actions should be added here.


if __name__ == "__main__":
    dialog = AboutCompmanagerDialog()
    dialog.show()
    gtk.main()
