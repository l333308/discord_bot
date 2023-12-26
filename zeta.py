import requests
import json
import random
import time
import re
import traceback

def get_context(auth):
    # TODO 上传代码仓库前 把dc的token处理掉
    dc_wallet_map = {

    }

    # 测试dc
    chanel_list = ['961884232546918450']

    # zeta领水频道
    chanel_id = '922357353423175680'

    # 230802 zeta领水
    seed = "Zeta faucet drip "
    seed = seed + dc_wallet_map[auth] + " goerli"

    print(seed)
    return seed


def chat():
    # 测试频道
    chanel_list = ['961884232546918450']
    # zeta 领水频道
    chanel_list = ['922357353423175680']

    # dc号列表 主 + 副2 + 比特
    # TODO 上传代码仓库前 把dc的token处理掉
    auth_list = [

    ]
    for auth in auth_list:
        header = {
            "Authorization": auth,
            "Content-Type": "application/json"
        }
        for chanel_id in chanel_list:
            msg = {
                "content": get_context(auth),
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
        time.sleep(random.randrange(5, 10))


if __name__ == '__main__':
    try:
        print('start')
        chat()
    except Exception as e:
        print(traceback.format_exc())
        exit()
