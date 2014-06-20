import sublime, sublime_plugin

import re

class VimReplaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.test(':s');
        # self.test(':12s');
        # self.test(':12,18s');
        # self.test(':^,10s');
        # self.test(':120,$s');
        # self.test(':%s');
        # end test
        self.view.window().show_input_panel('replace:', '', self.input_done, self.input_change, self.input_cancel);
        # print("gutianyu\n":);

    def test(self, input):
        print(">> " + input);
        regions = self.get_regions(input);
        for region in regions:
            print(self.view.substr(region));
        print("\n");

    def input_done(self, result):
        argArr = re.split('(?<!\\\\)/', result);
        print(argArr);
        argLen = len(argArr);
        if argLen < 3:
            return False;
        type = argArr[0];
        regions = self.get_regions(type);
        pattern = argArr[1];
        replace = argArr[2];
        isGlobal = False;
        if argLen >= 4 and len(argArr[3] and 'g') == 1:
            isGlobal = True;
        self.regions_replace(regions, pattern, replace, isGlobal);
        pass;

    def input_change(self, edit):
        # print("replace_change");
        pass;

    def input_cancel(self):
        # print("replace_cancel");
        pass;

    # 替换
    def regions_replace(self, regions, pattern, replace, isGlobal):
        count = 1;
        if isGlobal:
            count = 0;
        for region in regions:
            str = self.view.substr(region);
            arr = re.split('[\\n\\r]+', str);
            # print(arr);
            resultArr = [];
            for item in arr:
                # print(i);
                tmp = re.sub(pattern, replace, item, count);
                resultArr.append(tmp);
            result = "\n".join(resultArr);
            # result = re.sub(pattern, replace, str, count);
            self.view.run_command('edit_replace', {'start':region.a, 'end':region.b, 'result':result});
        pass;

    # 分析输入
    def get_regions(self, type):
        regions = [];
        if type == ':s':
            # 替换当前行
            for sel in self.view.sel():
                line = self.view.line(sel);
                regions.append(line);
        elif type == ':%s':
            # 替换所有行
            region = self.view.line(sublime.Region(0, self.view.size()));
            regions.append(region);
        elif re.match('^:(?P<num>\\d+)s$', type):
            # 替换从第一行（^）到第N行
            m = re.match('^:(?P<num>\\d+)s$', type);
            num = m.group('num');
            regions.append(self.get_line_by_num(num));
        elif re.match('^:(?P<num1>(?:\\d+|\\^)),(?P<num2>(?:\\d+|\\$))s$', type):
            # 替换从第X行到第Y行。当X=^,Y=$，和%功能类似
            m = re.match('^:(?P<num1>(?:\\d+|\\^)),(?P<num2>(?:\\d+|\\$))s$', type);
            begin = 0;
            end = 0;
            if m.group('num1') == '^':
                begin = 0;
            else:
                line = self.get_line_by_num(m.group('num1'));
                begin = line.a;
            if m.group('num2') == '$':
                end = self.view.size();
            else:
                line = self.get_line_by_num(m.group('num2'));
                end = line.b;
            regions.append(sublime.Region(begin, end));
        return regions;

    # 依据行号获得该行的内容
    def get_line_by_num(self, num):
        num = int(num) - 1;
        if num < 0:
            num = 0;
        point = self.view.text_point(num, 0);
        # print(point);
        line = self.view.line(sublime.Region(point));
        return line;
