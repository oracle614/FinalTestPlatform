# @Time    : 2018/4/4 17:20
# @Author  : Eggsy

import xadmin
from testPlatform.Action import OpenReport, RunTest
from xadmin import views
from .models import TestCase


class TestCaseAdmin(object):
    list_display = ['case_id', 'case_name', 'steps', "test_file", 'class_name', 'test_method', 'test_report', 'test_result']
    search_fields = ['case_name', 'class_name', 'test_method', 'test_file', 'test_result', 'steps']
    list_filter = ['case_name', 'class_name', 'test_method', 'test_file', 'test_result', 'steps']
    actions = [OpenReport, RunTest]
    # filter_horizontal = ['steps']
    # style_fields = {'steps': 'm2m_transfer'}
    readonly_fields = ['test_report', 'test_result']
    list_editable = ['case_name', 'steps', "test_file", 'class_name', 'test_method']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "测试用例管理系统"
    site_footer = "Copyright 2018 Eggsy"
    menu_style = "accordion"


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(TestCase, TestCaseAdmin)
