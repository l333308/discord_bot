import requests
import json
import random
import time
import re
import traceback

def gen_context():
    context_list_en = [
        "hello bro", "let's go !", "to the moon!", "nice", "project", "have a good day",
        "good", "luck", "how's going", "so do i", "yeah", "same to me", "1", "cool", "so far so good",
        "hi~", "of course", "really", "cool~", "ok", "what?", "why?", "not bad", "well done", "great",
        "perferct", "thanks", "ture", "yes", "no", "here", "interesting", "it's funny", "i am tired"
    ]

    context_list_cn = [
        "这样的啊", "冲鸭！", "继续", "不急，慢慢来", "继续吧", "（键盘你不要自己打字",
        "继续继续~", "冲起来", "晚上肝通宵就解放咯", "我要跟上大家的步伐", "兄弟们休息休息吧，别继续干了",
        "在下币圈首富  币安赵长鹏   尔等小辈见我还不下跪",
        "加油干", "勤奋的人哪有休息", "大家一起加油干", "升级速度慢起来了啊", "不知道多久才能到7", "我3还没到呢",
        "冲冲冲", "困了就去睡觉，别熬着",
        "to the moon~", "nice", "因缺思厅~", "都是人才", "最近是不是行情不行呀", "肝肝肝肝肝肝", "不随便还要注意啥吗",
        "乾起來~", "燥起来燥起来",
        "今天就在这肝了"
    ]

    text = random.choice(context_list_cn)
    return text


def get_context():
    # 测试dc
    chanel_list = ['961884232546918450']

    # omni中文频道
    # chanel_list = ['928014684571992205']

    # 此处填在对应频道有权限的账号的token 否则报错401
    # TODO 此处记得省略真正dc账号token
    header = {
        "Authorization": "a.b.c",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4 Safari/537.36"
    }
    chanel_id = random.choice(chanel_list)

    # 230211 SUI领水
    # seed = "!faucet "
    # seed = seed + dc_wallet_map[auth]

    # print(seed)
    # return seed

    url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(
        chanel_id)
    res = requests.get(url=url, headers=header)
    result = json.loads(res.content)
    result_list = []
    for context in result:
        if ('<') not in context['content']:
            if ('@') not in context['content']:
                if ('http') not in context['content']:
                    if ('?') not in context['content']:
                        result_list.append(context['content'])

    return random.choice(result_list)

def chat():
    # 测试频道
    chanel_list = ['961884232546918450']
    # omni中文频道
    # chanel_list = ['928014684571992205']

    # TODO 此处记得省略真正dc账号token
    # dc号列表 主 + 副2 + 比特
    authorization_list = [
        "a.b.c",
    ]
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json"
        }
        for chanel_id in chanel_list:
            msg = {
                "content": get_context(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False
            }
            url = 'https://discord.com/api/v9/channels/{}/messages'.format(
                chanel_id)
            try:
                res = requests.post(url=url, headers=header,
                                    data=json.dumps(msg))
                print(res.content)
            except Exception:
                print(Exception)
            continue
        # 取随机数，作为不同auth发言间隔时间（秒）
        time.sleep(random.randrange(5, 20))


if __name__ == '__main__':
    while True:
        try:
            print('start')
            chat()
            # 取180秒到240之间的一个随机数，作为机器人发送消息的间隔时间。
            sleeptime = random.randrange(5, 20)
            time.sleep(sleeptime)
        except Exception as e:
            print(traceback.format_exc())
            exit()
        continue
