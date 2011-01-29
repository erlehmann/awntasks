# -*- coding: utf-8 -*-
# Copyright (c) 2011    Nils Dagsson Moskopp <nils@dieweltistgarnichtso.net>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import dbus

class pluginAwnTasks:
    def __init__(self):
        bus = dbus.SessionBus()
        obj = bus.get_object('com.google.code.Awn', '/com/google/code/Awn')
        self.awn = dbus.Interface(obj, 'com.google.code.Awn')

    def _update_(self):
        tasksNumber = str(len(self.plugin_api.get_all_tasks()))
        self.awn.SetInfoByName('gtg', tasksNumber)

    def activate(self, plugin_api):
        self.plugin_api = plugin_api

        self.requester = self.plugin_api.get_requester()
        self.requester.connect("task-added", self.onTaskAdded)
        self.requester.connect("task-deleted", self.onTaskDeleted)
        self.requester.connect("task-modified", self.onTaskModified)

        self._update_()

    def deactivate(self, plugin_api):
        self.awn.SetInfoByName('gtg', '')

    def onTaskOpened(self, plugin_api):
        pass

    def onTaskAdded(self, requester, tid):
        self._update_()

    def onTaskDeleted(self, requester, tid):
        self._update_()

    def onTaskModified(self, requester, tid):
        self._update_()
