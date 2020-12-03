# coding:utf-8
import time
from dingding import DingDing
from collections import namedtuple
import unittest

TOKEN = ""
PHONE = ""
SECRET = ""


class TestDingDing(unittest.TestCase):
    def test_parse_token(self):
        time.sleep(1)

        TestDing = namedtuple("TestDing", ["input", "want"])

        tests = [
            TestDing(
                "https://oapi.dingtalk.com/robot/send?access_token=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ",
                "https://oapi.dingtalk.com/robot/send?access_token=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ),
            TestDing(
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ",
                "https://oapi.dingtalk.com/robot/send?access_token=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            ),
        ]

        for test_ding in tests:
            d = DingDing(test_ding.input)
            self.assertEqual(d.url, test_ding.want)

    def test_send_text(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_text("天气不错")
        self.assertEqual(rep["errmsg"], "ok")

    def test_send_text2(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_text("天气不错", [PHONE])
        self.assertEqual(rep["errmsg"], "ok")

    def test_send_link(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_link(
            "天气提示",
            "天气不错",
            "http://www.weather.com.cn/",
            "https://cn.vuejs.org/images/logo.png",
        )
        self.assertEqual(rep["errmsg"], "ok")

    def test_send_markdown(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_markdown("天气提示", "# 天气不错\n> 雨一直下")
        self.assertEqual(rep["errmsg"], "ok")

    def test_send_single_action_card(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_single_action_card(
            "乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身",
            "![screenshot](@lADOpwk3K80C0M0FoA) \n #### 乔布斯 20 年前想打造的苹果咖啡厅 \n\n Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划",
            "阅读全文",
            "https://www.dingtalk.com/",
            0,
            1,
        )
        self.assertEqual(rep["errmsg"], "ok")

    def test_send_action_card(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_action_card(
            "新用户注册",
            "![screenshot](@lADOpwk3K80C0M0FoA) \n## 请及时审核",
            [("通过", "http://www.baidu.com"), ("不通过", "http://www.qq.com")],
        )
        self.assertEqual(rep["errmsg"], "ok")

    def test_send_feed_card(self):
        time.sleep(1)
        dingding = DingDing(TOKEN)
        dingding.set_secret(SECRET)
        rep = dingding.send_feed_card(
            [
                (
                    "学vue",
                    "https://cn.vuejs.org/",
                    "https://cn.vuejs.org/images/logo.png",
                ),
                (
                    "哪家强",
                    "https://cn.vuejs.org/",
                    "https://cn.vuejs.org/images/logo.png",
                ),
            ]
        )
        self.assertEqual(rep["errmsg"], "ok")


if __name__ == "__main__":
    unittest.main()
