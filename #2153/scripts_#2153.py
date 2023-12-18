import sys
import time
import uiautomator2

# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect('emulator-5554')
# coding: utf-8

d(resourceId="net.gsantner.markor_test:id/action_go_to").click()

#先看一下最近浏览记录，方便后续对照
d.xpath('//android.widget.ListView/android.widget.LinearLayout[5]').click()
time.sleep(2)
d(resourceId="net.gsantner.markor_test:id/action_go_to").click()
d.xpath('//android.widget.ListView/android.widget.LinearLayout[3]').click()
d.xpath('//android.widget.LinearLayout').click()

#点击新建文件夹
d(resourceId="net.gsantner.markor_test:id/fab_add_new_item").click()
d(resourceId="net.gsantner.markor_test:id/new_file_dialog__name").click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_0"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_0"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.TextView[1]').click()
d.xpath('//android.widget.TextView').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_2_3"]/android.widget.TextView[1]').click()
d(resourceId="com.google.android.inputmethod.latin:id/key_pos_shift").click()
d.xpath('//android.widget.TextView').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_2"]/android.widget.TextView[1]').click()
d.xpath('//android.widget.TextView').click()
d(resourceId="android:id/button1").click()

#进入新页面
d(resourceId="net.gsantner.markor_test:id/document__fragment__edit__content_editor__scrolling_parent").click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_4"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_2"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_1_1"]/android.widget.TextView[1]').click()
d.xpath('//*[@resource-id="com.google.android.inputmethod.latin:id/key_pos_0_4"]/android.widget.TextView[1]').click()
d(resourceId="net.gsantner.markor_test:id/action_save").click()
time.sleep(2)
d.drag(0.153, 0.986,0.8, 0.988)
d.xpath('//*[@resource-id="net.gsantner.markor_test:id/action_go_to"]').click()
d.xpath('//android.widget.ListView/android.widget.LinearLayout[5]').click()


# #下面杀死进程
# d.drag(0.5,0.99,0.5,0.83)  #但这个拖拽一直有点问题
# d.drag(0.49, 0.734,0.447, 0.051)
# d(resourceId="net.gsantner.markor_test:id/main__view_pager_container").click()
# d.drag(0.5, 0.525,0.464, 0.204)
# d(resourceId="com.google.android.apps.nexuslauncher:id/icon", text="Marder").click()
# d(resourceId="net.gsantner.markor_test:id/action_go_to").click()
# d.xpath('//android.widget.ListView/android.widget.LinearLayout[5]').click()