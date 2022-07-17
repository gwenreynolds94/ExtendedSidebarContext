import sublime
import sublime_plugin

class InstanceCache:
	def __init__(self, logCom = False, logInput = False, nameSett = "Preferences.sublime-settings"):
		self.vw = None
		self.pt = None
		self.hz = None
		self.cc = None
		self.lastFound = sublime.active_window()
		self.justFound = sublime.active_window()
		self.proj_file = self.justFound.project_file_name() or None
		self.work_file = self.justFound.workspace_file_name() or None
	
	def combine(self):
		out = {"view": self.vw,
			"point": self.pt,
			"hoverzone": self.hz,
			"changecount": self.cc,
			"lastFound": self.lastFound,
			"justFound": self.justFound}
		return out
	
	def updateOnHover(self, view, point, hover):
		self.vw = view
		self.pt = point
		self.hz = hover
		self.cc = view.change_count()
		if self.justFound != sublime.active_window():
			self.lastFound = self.justFound
			self.justFound = sublime.active_window()
			self.proj_file = self.justFound.project_file_name() or None
			self.work_file = self.justFound.workspace_file_name() or None
			

class FilesAndFolders:
	def __init__(self, window):
		self.window = window or sublime.active_window()
		self.proj_file = window.project_file_name()
		self.work_file = window.workspace_file_name()


# window.extract_variables() -> possible combinations of...
# [Dict]
# "packages"
# "platform"
# "file"
# "file_path"
# "file_name"
# "file_base_name"
# "file_extension"
# "folder"
# "project"
# "project_path"
# "project_name"
# "project_base_name"
# "project_extension"
# fullList = sublime.active_window().extract_variables()
# lookUp = sublime.expand_variables("${file_path}", fullList) -> focused file's path
# window.find_open_file(file_name) -> view
# window.folders() -> 
		
		

class ExtendedSidebarContextCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		return
		
class SyncSettingsCache(sublime_plugin.EventListener):
	def on_init(self, views):
		self.cache = InstanceCache()
		
	def on_hover(self, View, Point, HoverZone):
		self.cache.updateOnHover(View, Point, HoverZone)
		# out = self.cache.combine()
		# print(self.cache.proj_file)
		# print(self.cache.work_file)
		# vList = sublime.active_window().extract_variables()
		# xList = sublime.expand_variables("${file_path}", vList)
		print(sublime.active_window().folders())
		
	# def on_window_command(self, window, command_name, args):
	# 	return
		