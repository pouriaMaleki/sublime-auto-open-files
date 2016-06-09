import sublime, sublime_plugin, os, re

class OpenStylWithLsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      jobView = self.view
      # sublime.message_dialog("adadd")
      if re.search(r'\.ls$', jobView.file_name()) is not None:
        stylFile = re.sub(r'\.ls$', '.styl', jobView.file_name())
        if os.path.exists(stylFile):
          activeGroup = sublime.active_window().active_group()
          if activeGroup == 1:
            # sublime.message_dialog("is 0")
            sublime.active_window().set_view_index(jobView, 0, 0)
          sublime.active_window().focus_group(1)
          sublime.active_window().open_file(stylFile)
      
      if re.search(r'\.styl$', jobView.file_name()) is not None:
        lsFile = re.sub(r'\.styl$', '.ls', jobView.file_name())
        if os.path.exists(lsFile):
          activeGroup = sublime.active_window().active_group()
          if activeGroup == 0:
            sublime.active_window().set_view_index(jobView, 1, 0)
            
          sublime.active_window().focus_group(0)
          sublime.active_window().open_file(lsFile)

class OpenStylWithLs(sublime_plugin.EventListener):
  def on_load(self, view):
    if view == sublime.active_window().transient_view_in_group(sublime.active_window().active_group()):
      return
    
    if view.settings().get('open_styl_with_ls') == 1:
      if view.settings().get('open_styl_with_ls_only_if_2_groups') == 1:
        if sublime.active_window().num_groups() != 2:
          return

      view.run_command('open_styl_with_ls')

      
      # fileName = os.path.basename(view.file_name())
      # dirName = os.path.dirname(view.file_name())
      # sublime.message_dialog()

      