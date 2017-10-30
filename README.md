```
from dingding import DingDing
access_token="xxxxxxxxxxxxxxxxxxxxxxxxxx"
ding = DingDing(access_token)
# @所有人
ding.send_text('hello', all_all=True)

# @手机号为1333333333的人
ding.send_text('hello', ['13333333333'])

ding.send_link('title', 'text', 'message_url')

ding.send_markdown('title', 'text')

ding.send_action_card('title', 'text', [('title1', 'url1'), ('title2', 'url2')])

```
