from time import sleep
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from pxconfig import *
from pxframe.pxos_handle import *
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def reload():
    """
    :return:None
    """
    if poco("com.puxin.accountant:id/refreshlayout"):
        poco("com.puxin.accountant:id/refreshlayout").swipe([0, 0.5])
    elif poco("android.widget.FrameLayout"):
        poco("android.widget.FrameLayout").swipe([0, 0.5])
    elif poco("com.puxin.accountant:id/recyclerview"):
        poco("com.puxin.accountant:id/recyclerview").swipe([0, 0.5])
    else:
        print("不存在可刷新的基元素")
    sleep(3)

#选择照片
def addimg():
    """
    :return:None
    """
    poco("com.puxin.accountant:id/iv_img").click()
    poco(text="相册").click()
    poco("com.puxin.accountant:id/iv_thumb").click()
    poco("com.puxin.accountant:id/btn_ok").click()

def startapp():
    connect_device('Android://127.0.0.1:5037/{}'.format(sn))
    # stop_app(apk)
    wake()
    start_app(gwapk)
    try:
        poco(text="我的").wait_for_appearance(20)
    except:
        pass

def stopapp():
    stop_app(gwapk)
    wake()
    time.sleep(2)
    # time.sleep(10)

def startjf():
    connect_device('Android://127.0.0.1:5037/{}'.format(sn))
    # stop_app(apk)
    wake()
    start_app(jfapk)
    try:
        poco(text="我的").wait_for_appearance(20)
    except:
        pass

def stopjf():
    stop_app(jfapk)
    wake()
    time.sleep(2)

# 财富顾问app登录
def gwlogin():
    # time.sleep(10)
    # 重新登录
    if poco("com.puxin.accountant:id/single_bottom_tv"):
        poco("com.puxin.accountant:id/single_bottom_tv").click()
        poco("com.puxin.accountant:id/et_mobile").set_text(gwphone)
        if pmode=='sc':
            poco("com.puxin.accountant:id/bt_sms").click()
            gwcode = inputcode('请输入{}手机收到的顾问验证码'.format(gwname))
            poco("com.puxin.accountant:id/et_sms").set_text(gwcode)
        else:
            poco("com.puxin.accountant:id/et_sms").set_text("0000")
        poco("com.puxin.accountant:id/et_puxinpassword").set_text(gwpwd)
        poco("com.puxin.accountant:id/bt_login").click()
    # 首次登录
    elif poco("com.puxin.accountant:id/bt_login"):
        poco("com.puxin.accountant:id/et_mobile").set_text(gwphone)
        if pmode == 'sc':
            poco("com.puxin.accountant:id/bt_sms").click()
            gwcode = inputcode('请输入{}手机收到的顾问验证码'.format(gwname))
            poco("com.puxin.accountant:id/et_sms").set_text(gwcode)
        else:
            poco("com.puxin.accountant:id/et_sms").set_text("0000")
        poco("com.puxin.accountant:id/et_puxinpassword").set_text(gwpwd)
        poco("com.puxin.accountant:id/bt_login").click()
        try:
            poco("com.puxin.accountant:id/btn_dialog_simple_enter").click()
        except:
            pass
    # 已登录
    elif poco(text="我的").exists():
        poco(text="我的").click()
        time.sleep(5)
        if not poco("com.puxin.accountant:id/tv_name").get_text()==gwname:
            poco("com.puxin.accountant:id/iv_settimg").click()
            poco("com.puxin.accountant:id/tv_exit").click()
            poco("com.puxin.accountant:id/btn_dialog_simple_enter").click()
            poco("com.puxin.accountant:id/et_mobile").set_text(gwphone)
            if pmode=='sc':
                poco("com.puxin.accountant:id/bt_sms").click()
                gwcode = inputcode('请输入{}手机收到的顾问验证码'.format(gwname))
                poco("com.puxin.accountant:id/et_sms").set_text(gwcode)
            else:
                poco("com.puxin.accountant:id/et_sms").set_text("0000")
            poco("com.puxin.accountant:id/et_puxinpassword").set_text(gwpwd)
            poco("com.puxin.accountant:id/bt_login").click()
        else:
            pass

# 普信金服app登录
def jflogin():
    if not poco(text="我的").exists():
        for i in range(3):
            poco("android.widget.ImageView").swipe([-1, 0])
            poco("android.widget.ImageView").click()
    else:
        pass
    poco(text="我的").click()
    if poco("com.puxin.asset:id/iv_logo"):
        poco("com.puxin.asset:id/et_mobile").set_text(jfphone)
        if pmode=='sc':
            poco("com.puxin.asset:id/bt_sms").click()
            jfcode = inputcode('请输入{}手机收到金服验证码'.format(jfname))
            poco("com.puxin.asset:id/et_sms").set_text(jfcode)
        else:
            poco("com.puxin.asset:id/et_sms").set_text('0000')
        poco("com.puxin.asset:id/cx_service").click()
        poco("com.puxin.asset:id/bt_login").click()
        if poco("com.puxin.asset:id/btn_dialog_simple_enter"):
            poco("com.puxin.asset:id/btn_dialog_simple_enter").click()
        elif poco("com.puxin.asset:id/iv_back"):
            poco("com.puxin.asset:id/iv_back").click()
            raise ("网络异常，或登录功能有误，请在前端验证")
        else:
            # 待增加切换客户登录信息，请参考gwlogin()
            pass
    else:
        pass

def exit_login():
    poco(text='我的').click()
    time.sleep(2)
    poco('com.puxin.accountant:id/iv_settimg').click()
    time.sleep(2)
    poco('com.puxin.accountant:id/tv_exit').click()
    time.sleep(2)
    poco('com.puxin.accountant:id/btn_dialog_simple_enter').click()

def assert_element_exists(element, str):
    flag = 0
    if poco(element):
        print('%s成功' % str)
    else:
        flag = 1
        print('%s失败' % str)
    return flag

def assert_element_index(element, str):
    flag = 0
    if element:
        print('%s成功' % str)
    else:
        flag = 1
        print('%s失败' % str)
    return flag

def swipe_down(element):
    x, y = poco(element).get_position()
    end = [x, 3 * y - 2]
    poco.swipe([x, y], end)
    sleep(3)
    return None

def swipe_up(element):
    x, y = poco(element).get_position()
    begin = [x, y + 1000]
    poco.swipe([x, y], begin)
    sleep(3)
    return None

def end():
    print('测试通过')

def exists(element):
    return True

def back(s=1):
    for i in range(s):
        try:
            poco("转到上一层级").click()
        except:
            keyevent("BACK")

def backcard():
    if poco(text="还没有银行卡?").exists():
        poco("com.puxin.accountant:id/tv_tip_add").click()
        poco("com.puxin.accountant:id/number_edit").set_text("62222200010001{}".format(random.randint(1000, 9999)))
        poco("com.puxin.accountant:id/name_edit").click()
        poco(text="中国银行").click()
        poco("com.puxin.accountant:id/location_edit").click()
        poco("com.puxin.accountant:id/btnSubmit").click()
        poco("com.puxin.accountant:id/branch_edit").set_text("东城区支行{}".format(random.randint(1000, 9999)))
        poco("com.puxin.accountant:id/card_front").click()
        poco(text="相册").click()
        poco("android.widget.LinearLayout").offspring("com.puxin.accountant:id/recycler").child(
            "android.widget.FrameLayout")[0].child("android.view.View").click()
        poco("com.puxin.accountant:id/card_back").click()
        poco(text="相册").click()
        poco("android.widget.LinearLayout").offspring("com.puxin.accountant:id/recycler").child(
            "android.widget.FrameLayout")[2].child("android.view.View").click()
        poco("com.puxin.accountant:id/btn_save").click()
        if poco("com.puxin.accountant:id/toolbar_title").get_text() == "添加银行卡":
            for i in range(5):
                poco("转到上一层级").click()
            print("新增银行卡输入的信息有误，或网络连接异常")
        else:
            pass
    poco("com.puxin.accountant:id/card_number").click()

# app截图，根据需求定制name
def snapp(name):
    snapshot(snapshot_path+name+'.png')