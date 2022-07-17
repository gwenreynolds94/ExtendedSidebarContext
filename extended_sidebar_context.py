import sublime
import sublime_plugin
from pathlib import Path


DEFAULT_PROJECT_FILE_TEXT = """{
	"folders":
	[
		{
			"path": "."
		}
	]
}"""



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
	def __init__(self, window = None):
		self.window = window if window else sublime.active_window()
		self.proj_file = self.window.project_file_name()
		self.work_file = self.window.workspace_file_name()
		self.parent = None
		self.everything = None
		self.all_file_paths = None
		self.project_added = None
		
	def updateChanges(self, window = None):
		self.window = window if window else sublime.active_window()
		self.proj_file = self.window.project_file_name()
		self.work_file = self.window.workspace_file_name()
		
	def getParentFolder(self, should_return = False):
		if not self.everything:
			self.getEverything()
		self.parent = sublime.expand_variables("${file_path}", self.everything)
		if should_return:
			return self.parent
		
	def getEverything(self, should_return = False, window = None):
		if not self.window and not window:
			self.window = sublime.active_window()
		self.everything = self.window.extract_variables()
		if should_return:
			return self.everything
			
	def printEverything(self, only_keys = False, only_values = False):
		if not self.everything:
			self.getEverything()
		print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
		for k in self.everything:
			print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
			print(k)
			print(self.everything[k])
		print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
		
	def getAllFilePaths(self, should_return = False, window = None):
		if not self.everything or not self.window:
			self.getEverything()
		self.all_file_paths = sublime.expand_variables("${file_path}", self.everything)
		if should_return:
			return self.all_file_paths

	def addParentFolder(self, file_name = False):
		if not self.parent or not self.window:
			self.getParentFolder()
			self.window = sublime.active_window()
		if project_added:
			sublime.status_message("Cannot add folder if project settings already intialized")
			return None
		else:
			self.open_folders = self.window.folders()
		
		
		

# window.extract_variables() -> possible combinations of...
# 
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
# 
# fullList = sublime.active_window().extract_variables()
# lookUp = sublime.expand_variables("${file_path}", fullList) -> focused file's path
# window.find_open_file(file_name) -> view
# window.folders() -> 
		

class ExtendedSidebarContextCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		return
		

class AddFolderFromOpenFileCommand(sublime_plugin.WindowCommand):
	def run(self, group, index):
		f_and_f = FilesAndFolders()
		p_dir = f_and_f.getParentFolder(True)
		a_f_f = f_and_f.getEverything(True)
		f_and_f.printEverything()


		
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
		# print(sublime.active_window().folders())
		
	# def on_window_command(self, window, command_name, args):
	# 	return
		