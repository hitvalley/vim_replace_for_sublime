import sublime, sublime_plugin

class ViewTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        str = self.view.substr(sublime.Region(0, self.view.size()));
        print(str);

        self.get_line_info(8);
        self.get_line_info(100);
        for i in range(3, 5):
            print(i);

    def get_line_info(self, line):
        size = self.view.size();
        print("size : " + str(size));
        point = self.view.text_point(line, 0);
        print("point : " + str(point));
        line = self.view.line(sublime.Region(point));
        lineStr = self.view.substr(line);
        print(lineStr);
