### ExtendedSidebarContext
##### Sidebar Context Menu plugin for Sublime Text
***


### **22 07 17 [12:38]**



* I've added a context menu option for the open files in the sidebar.
You can click on Add Parent Folder to add the directory of the currently
open file to the project, (or more accurately, the project data).

* If you haven't saved the window as a project yet, it won't have a *.sublime-project
or *.sublime-workspace file to write to, but the window can
still capture the data until you do save it.

* I'm not yet completely sure what the drawbacks of that is,
but I plan on adding the neccessary behaviour anyways. It just isn't as simple as
the rest of the script and it does what I need it to do for now.
