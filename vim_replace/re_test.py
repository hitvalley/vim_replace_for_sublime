import sublime, sublime_plugin

import re

# 用于测试正则
class ReTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print(">> split: ");
        arr = re.split('(?<!\\\\)/', ':s/\/a\/var/\/usr/');
        print(arr);

        print(">> match num: ");
        mres1 = re.match('^:(?P<num>\\d+)s', ':12s')
        print(mres1.group("num"));

        print(">> match num1,num2: ");
        mres2 = re.match(':(?P<num1>\\d+),(?P<num2>\\d+)s', ':12,13s')
        print(mres2.group("num1"));
        print(mres2.group("num2"));


        print(">> match num1,num2: ");
        mres3 = re.match(':(?P<num1>(?:\\d+|\\^)),(?P<num2>(?:\\d+|\\$))s', ':^,13s')
        print(mres3.group("num1"));
        print(mres3.group("num2"));

        print(">> match num1,num2: ");
        mres4 = re.match('^:(?P<num1>(?:\\d+|\\^)),(?P<num2>(?:\\d+|\\$))s$', ':^,$s');
        print(mres4.group("num1"));
        print(mres4.group("num2"));
