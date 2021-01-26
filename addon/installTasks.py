# Proxy support add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2020 Jose Manuel Delicado <jm.delicado@nvda.es>

import config
import addonHandler


def onUninstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "proxy":
			return
	for k, v in list(config.conf._profileCache.items()):
		try:
			del config.conf._profileCache[k]['proxy']
		except:
			pass
	config.conf.save()
