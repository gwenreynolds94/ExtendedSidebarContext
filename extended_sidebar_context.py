import sublime
import sublime_plugin
from pathlib import Path



class FilesAndFolders:
		
	def getEverything(self, should_return = False):
		self.window = sublime.active_window()
		self.everything = self.window.extract_variables()
		if should_return:
			return self.everything

	def addParentFolder(self, file_to_get = None):
		self.window = sublime.active_window()
		self.getEverything()
		for k in self.everything:
			if k == "file":
				self.child = self.everything[k]
			if k == "file_path":
				self.parent = self.everything[k]
		if self.child and self.parent:
			config = {'follow_symlinks': True, 'path': self.parent}
			data = self.window.project_data()
			if not data:
				data = {'folders': [config]}
				self.window.set_project_data(data)
			else:
				data['folders'].append(config)
				self.window.set_project_data(data)



class ExtendedSidebarContextCommand(sublime_plugin.WindowCommand):
	def run(self, **args):
		return



class AddFolderFromOpenFileCommand(sublime_plugin.WindowCommand):
	def run(self, group, index):
		folderContainer = FilesAndFolders()
		folderContainer.getEverything()
		folderContainer.addParentFolder()


		
# class SyncSettingsCache(sublime_plugin.EventListener):
#	def on_init(self, views):
#		self.cache = InstanceCache()
#		
#	 def on_hover(self, View, Point, HoverZone):
#		 self.cache.updateOnHover(View, Point, HoverZone)
#		 out = self.cache.combine()
#		 print(self.cache.proj_file)
#		 print(self.cache.work_file)
#		 vList = sublime.active_window().extract_variables()
#		 xList = sublime.expand_variables("${file_path}", vList)
#		 print(sublime.active_window().folders())
#		
#	 def on_window_command(self, window, command_name, args):
#	 	return
		