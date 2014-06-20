import sublime, sublime_plugin

class EditReplaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, start, end, result):
        line = self.view.line(sublime.Region(start, end));
        self.view.replace(edit, line, result);
