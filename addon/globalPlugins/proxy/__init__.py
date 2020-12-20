# Proxy support add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Copyright (C) 2020 Jose Manuel Delicado <jm.delicado@nvda.es>
import addonHandler
import globalPluginHandler
import config
import socket
import ssl
import urllib
import wx
from gui import guiHelper, NVDASettingsDialog
from gui.settingsDialogs import SettingsPanel
import os
from . import socks

addonHandler.initTranslation()
orig_socket = None
orig_env = None

config.conf.spec['proxy'] = {
	"http_host": "string(default='')",
	"http_port": "integer(default=8080)",
	"http_username": "string(default='')",
	"http_password": "string(default='')",
	"https_host": "string(default='')",
	"https_port": "integer(default=8080)",
	"https_username": "string(default='')",
	"https_password": "string(default='')",
	"ftp_host": "string(default='')",
	"ftp_port": "integer(default=8080)",
	"ftp_username": "string(default='')",
	"ftp_password": "string(default='')",
	"socks_host": "string(default='')",
	"socks_port": "integer(default=1080)",
	"socks_username": "string(default='')",
	"socks_password": "string(default='')",
	"socks_type": "integer(default=1)",
	"socks_dns": "boolean(default=True)",
}

proxyTypes = [
	# TRANSLATORS: socks4 proxy type
	_("SOCKS v4"),
	# TRANSLATORS: socks5 proxy type
	_("SOCKS v5"),
	# TRANSLATORS: http proxy type which redirects all traffic
	_("HTTP")
]


def applyConfig():
	if config.conf['proxy']['socks_host'] != '':
		for p in orig_env.keys():
			if p in os.environ.keys():
				del os.environ[p]
		socks.set_default_proxy(config.conf['proxy']['socks_type'], config.conf['proxy']['socks_host'], config.conf['proxy']['socks_port'], config.conf['proxy']['socks_dns'], config.conf['proxy']['socks_username'], config.conf['proxy']['socks_password'])
		socket.socket = socks.socksocket
		ssl.SSLContext.sslsocket_class = socks.sockSSLSocket
	else:
		socket.socket = orig_socket
		ssl.SSLContext.sslsocket_class = ssl.SSLSocket
		for k, v in orig_env.items():
			os.environ[k] = v
	for protocol in ['HTTP', 'HTTPS', 'FTP']:
		if config.conf['proxy'][protocol.lower() + "_host"] != '':
			proxy_url = config.conf['proxy'][protocol.lower() + "_host"] + ":" + str(config.conf['proxy'][protocol.lower() + "_port"])
			if config.conf['proxy'][protocol.lower() + "_username"] != '' and config.conf['proxy'][protocol.lower() + "_password"] != '':
				proxy_url = config.conf['proxy'][protocol.lower() + "_username"] + ":" + config.conf['proxy'][protocol.lower() + "_password"] + "@" + proxy_url
			proxy_url = "http://" + proxy_url
			os.environ[protocol + "_PROXY"] = proxy_url
		elif protocol + "_PROXY" in orig_env.keys() and config.conf['proxy']['socks_host'] == '':
			os.environ[protocol + "_PROXY"] = orig_env[protocol + "_PROXY"]
	urllib.request._opener = urllib.request.build_opener()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		global orig_socket, orig_env
		orig_socket = socket.socket
		orig_env = {}
		for p in ['HTTP_PROXY', 'HTTPS_PROXY', 'FTP_PROXY']:
			if p in os.environ.keys():
				orig_env[p] = os.environ[p]
		applyConfig()
		config.post_configProfileSwitch.register(self.onConfigChanged)
		config.post_configReset.register(self.onConfigChanged)
		NVDASettingsDialog.categoryClasses.append(ProxyPanel)

	def terminate(self):
		global orig_socket, orig_env
		socket.socket = orig_socket
		ssl.SSLContext.sslsocket_class = ssl.SSLSocket
		for k, v in orig_env.items():
			os.environ[k] = v
		orig_socket = None
		orig_env = None
		config.post_configProfileSwitch.unregister(self.onConfigChanged)
		config.post_configReset.unregister(self.onConfigChanged)
		NVDASettingsDialog.categoryClasses.remove(ProxyPanel)
		super(GlobalPlugin, self).terminate()

	def onConfigChanged(self, *args, **kwargs):
		applyConfig()


class ProxyPanel(SettingsPanel):
	# TRANSLATORS: title for the Proxy settings category in NVDA settings dialog
	title = _("Proxy")
	# TRANSLATORS: description for the proxy settings panel
	panelDescription = _("The following options allows you to configure a proxy server so NVDA can connect to the Internet")

	def makeSettings(self, sizer):
		helper = guiHelper.BoxSizerHelper(self, sizer=sizer)
		helper.addItem(wx.StaticText(self, label=self.panelDescription))
		# TRANSLATORS: label for a group of proxy settings in the proxy settings panel
		socks_group = guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("All traffic")), wx.HORIZONTAL))
		helper.addItem(socks_group)
		# TRANSLATORS: label for a combo box which contains SOCKS proxy types
		self.socks_type = socks_group.addLabeledControl(_("SOCKS proxy type"), wx.Choice, choices=proxyTypes)
		self.socks_type.SetSelection(config.conf['proxy']['socks_type'] - 1)
		# TRANSLATORS: proxy host for socks connections
		self.socks_host = socks_group.addLabeledControl(_("Host: "), wx.TextCtrl, value=config.conf['proxy']['socks_host'])
		# TRANSLATORS: proxy port for socks connections
		self.socks_port = socks_group.addLabeledControl(_("Port: "), wx.SpinCtrl, min=1, max=65535, value=str(config.conf['proxy']['socks_port']))
		# TRANSLATORS: option to redirect dns traffic through a SOCKSv5 proxy
		self.socks_dns = socks_group.addItem(wx.CheckBox(self, wx.ID_ANY, label=_("Use proxy for DNS requests if possible")))
		self.socks_dns.SetValue(config.conf['proxy']['socks_dns'])
		# TRANSLATORS: proxy username for socks connections
		self.socks_username = socks_group.addLabeledControl(_("Username: "), wx.TextCtrl, value=config.conf['proxy']['socks_username'])
		# TRANSLATORS: proxy password for socks connections
		self.socks_password = socks_group.addLabeledControl(_("Password: "), wx.TextCtrl, value=config.conf['proxy']['socks_password'])
		# TRANSLATORS: label for a group of proxy settings in the proxy settings panel
		http_group = guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("HTTP traffic")), wx.HORIZONTAL))
		helper.addItem(http_group)
		# TRANSLATORS: proxy host for http connections
		self.http_host = http_group.addLabeledControl(_("Host: "), wx.TextCtrl, value=config.conf['proxy']['http_host'])
		# TRANSLATORS: proxy port for http connections
		self.http_port = http_group.addLabeledControl(_("Port: "), wx.SpinCtrl, min=1, max=65535, value=str(config.conf['proxy']['http_port']))
		# TRANSLATORS: proxy username for http connections
		self.http_username = http_group.addLabeledControl(_("Username: "), wx.TextCtrl, value=config.conf['proxy']['http_username'])
		# TRANSLATORS: proxy password for http connections
		self.http_password = http_group.addLabeledControl(_("Password: "), wx.TextCtrl, value=config.conf['proxy']['http_password'])
		# TRANSLATORS: label for a group of proxy settings in the proxy settings panel
		https_group = guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("HTTPS traffic")), wx.HORIZONTAL))
		helper.addItem(https_group)
		# TRANSLATORS: proxy host for https connections
		self.https_host = https_group.addLabeledControl(_("Host: "), wx.TextCtrl, value=config.conf['proxy']['https_host'])
		# TRANSLATORS: proxy port for https connections
		self.https_port = https_group.addLabeledControl(_("Port: "), wx.SpinCtrl, min=1, max=65535, value=str(config.conf['proxy']['https_port']))
		# TRANSLATORS: proxy username for https connections
		self.https_username = https_group.addLabeledControl(_("Username: "), wx.TextCtrl, value=config.conf['proxy']['https_username'])
		# TRANSLATORS: proxy password for https connections
		self.https_password = https_group.addLabeledControl(_("Password: "), wx.TextCtrl, value=config.conf['proxy']['https_password'])
		# TRANSLATORS: label for a group of proxy settings in the proxy settings panel
		ftp_group = guiHelper.BoxSizerHelper(self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=_("FTP traffic")), wx.HORIZONTAL))
		helper.addItem(ftp_group)
		# TRANSLATORS: proxy host for ftp connections
		self.ftp_host = ftp_group.addLabeledControl(_("Host: "), wx.TextCtrl, value=config.conf['proxy']['ftp_host'])
		# TRANSLATORS: proxy port for ftp connections
		self.ftp_port = ftp_group.addLabeledControl(_("Port: "), wx.SpinCtrl, min=1, max=65535, value=str(config.conf['proxy']['ftp_port']))
		# TRANSLATORS: proxy username for ftp connections
		self.ftp_username = ftp_group.addLabeledControl(_("Username: "), wx.TextCtrl, value=config.conf['proxy']['ftp_username'])
		# TRANSLATORS: proxy password for ftp connections
		self.ftp_password = ftp_group.addLabeledControl(_("Password: "), wx.TextCtrl, value=config.conf['proxy']['ftp_password'])

	def onSave(self):
		config.conf['proxy']['http_host'] = self.http_host.GetValue()
		config.conf['proxy']['http_port'] = self.http_port.GetValue()
		config.conf['proxy']['http_username'] = self.http_username.GetValue()
		config.conf['proxy']['http_password'] = self.http_password.GetValue()
		config.conf['proxy']['https_host'] = self.https_host.GetValue()
		config.conf['proxy']['https_port'] = self.https_port.GetValue()
		config.conf['proxy']['https_username'] = self.https_username.GetValue()
		config.conf['proxy']['https_password'] = self.https_password.GetValue()
		config.conf['proxy']['ftp_host'] = self.ftp_host.GetValue()
		config.conf['proxy']['ftp_port'] = self.ftp_port.GetValue()
		config.conf['proxy']['ftp_username'] = self.ftp_username.GetValue()
		config.conf['proxy']['ftp_password'] = self.ftp_password.GetValue()
		config.conf['proxy']['socks_host'] = self.socks_host.GetValue()
		config.conf['proxy']['socks_port'] = self.socks_port.GetValue()
		config.conf['proxy']['socks_username'] = self.socks_username.GetValue()
		config.conf['proxy']['socks_password'] = self.socks_password.GetValue()
		config.conf['proxy']['socks_type'] = self.socks_type.Selection + 1
		config.conf['proxy']['socks_dns'] = self.socks_dns.GetValue()
		applyConfig()
