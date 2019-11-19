# 在线安装

`pip install dingding`

# 例子
```
from dingding import DingDing
access_token="xxxxxxxxxxxxxxxxxxxxxxxxxx"
ding = DingDing(access_token)
# @所有人
ding.send_text('hello', at_all=True)

# @手机号为1333333333的人
ding.send_text('hello', ['13333333333'])

ding.send_link('title', 'text', 'message_url')

ding.send_markdown('title', 'text')

ding.send_action_card('title', 'text', [('title1', 'url1'), ('title2', 'url2')])

```

```
ding.send_text('我就是我, 是不一样的烟火', ['13333333333'])
```

![](https://img.alicdn.com/tfs/TB1jFpqaRxRMKJjy0FdXXaifFXa-497-133.png)

```
ding.send_link('时代的火车向前开', '这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红
    树林”？', 'https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI')
```

![](https://img.alicdn.com/tfs/TB1VfZtaUgQMeJjy0FeXXXOEVXa-498-193.png)

```
ding.send_feed_card([('学vue','https://cn.vuejs.org/','https://cn.vuejs.org/images/logo.png'),
                     ('哪家强', 'https://cn.vuejs.org/', 'https://cn.vuejs.org/images/logo.png')])
```
![](http://ozrgxic3l.bkt.clouddn.com/TIM%E5%9B%BE%E7%89%8720171121171532.jpg)


## 添加签名秘钥

```python
d = DingDing(
    "https://oapi.dingtalk.com/robot/send?access_token=tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"
)
# 如果使用了签名秘钥,需要添加下面这条语句
d.set_secret("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
d.send_text("hello")
```

## 返回结果

如果发送正常
```
{'errcode': 0, 'errmsg': 'ok'}
```