import sublime
import sublime_plugin
from pathlib import Path



class FilesAndFolders:

	def getEverything(self, should_return = False):
		self.window = sublime.active_window()
		self.everything = self.window.extract_variables()
		if should_return:
			return self.everything

	def addParentFolder(self):
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


class AddFolderFromOpenFileCommand(sublime_plugin.WindowCommand):
	def run(self, group, index):
		folderContainer = FilesAndFolders()
		folderContainer.getEverything()
		folderContainer.addParentFolder()