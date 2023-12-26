import requests
import json
import random
import time
import re
import traceback

def get_context(auth):
    # TODO 上传代码仓库前 把dc的token处理掉
    dc_wallet_map = {
        # 主
        "OTQwODYwNTQyMjU4NjY3NTMw.G3mF0J.":"0x0B024DD5E004582219A6E56778142f280fe5C5e0",
        # 副2
    "OTc4OTMzNTk0MDg3MTEyNzE0.GpCa8e.WRuZuiFcsVBm52e-": "0x32b3c29D55E1E60ce91d843B7c07401401C79FD9",

    # 比特
    "OTc4OTM4NDM4NTk2MzE3MTg1.GAWH0X.egVrarSOpcF0hs-": "0x7EEfc492CcbD7B7E0Eeece6c39a8bC96908cfeae",
    "MTA3Njc2NzM0Mzg5MzU0NTAyMA.G-8tWb.": "0x404318AcB632B18cA8084b7E3F9fBcC342eab50a",
    "MTA3MTI0MjE1Mjc5OTEwOTIxMg.GSBZ8T.": "0x6de2721f3E99e6E3E818a6dC76a502643b9A0c5B",
    "MTAxNDM2NjE4ODEzNjA0NjY0Mg.GfZiPv.R1lJ-": "0x1c9C10A460AA77485f3Cd93dd8032CC6D6743163",
    "OTg1MTMxODk1MTY1NzEwMzc2.GAR1mq.": "0x58bBE4Eb4d32daa7bD5C244EC732ad5Ff38F70b7",
    "MTA3Mjg1MDMwMTEwMDQ5OTAyNg.GA5G2I.": "0x4D5Cf6d9a78Ceb0f4cF9b2992488b3886C5D1335",
    "MTA3Njc3NDI1Mzk2NzQ1MDEzMw.GUdVT8.-z1TCXR8": "0xA47d67b938B353685F42a13Ec124f74f648762A6",
    "MTA3Mjg2MDE0MDMwNDMzODk0NA.Gm8cOx.": "0xAcB00e4568308Cd805A464B0297EE7efA83D764b",
    "MTA3Mjg2NDU0MDM1MTUyODk4MQ.GSZqwM.": "0x5AE30c0BA6Dd53AEb6d4Ac84Ed200F9D1cA49C80",
    "MTA3Njc4MTE5MDYyNDg1MDA1MQ.GI0HgN.": "0xD9b4A96C0B78b54981CB4F0a7B451c320F1779A6",

    # ads
    "MTEwMDQxMDAwMzE3ODkxNzk3MA.GuNkcz.-k": "0xd4f60061ae48C8D4a1E1291190B6EA6aB678fF08",
    "MTEwMDQxMjg5NjEzNzE5OTcwOA.Gj28Vg.VVU6iUwbt-": "0x7FCD0C124d3762E2219A2D0c0E5FEF4ccC8dA02f",
    "MTEwMDQxMzU0MTM2Mzc0ODkwNA.GrRJAa.": "0x597700A392C369aa3Ef1d34179262245b219412b",
    "MTEwMDQxNDE1OTUzMjg2NzY4NA.Ge5Dly.": "0xf84F5661F31ef85cb2D0F2e9d8138F9F21586B10",
    "MTEwMDQxNTY3OTQ1NjM2MjU1Ng.GpvLqq.": "0x0C097d11adFFedcFFf62FCb88A4970cA08e3390B",
    "MTEwMDQxNjk1MjA3NTI5Mjc0Mg.GWonCX.-yx8sA0Fn9Jg": "0xD104CC852F4D1512FED4e0006eC79debB1024D6a",
    "MTEwMDQxNzYwMzI5NTUxMDU5MA.GpQVtj.r-": "0xcB6dfFCD0AF1195059225A7E379E622E3Aab381d",
    "MTEwMDQxMjE1MzQ1NTk3MjM2Mw.GsPeGu.7FE--Txt9P1Q0": "0x4912e4d80176b684Eb4761cc9371948E9CDF83e8",
    "MTEwMDQxNDkzNTM3MDAzOTM3MA.G_JqTz.-KEeVrjxZZFY": "0x0bb0C4EC8bb2508972FF22122C4fB93F9063BE30",
    "MTEwMDQxNjI5OTQwMzg1Mzg5NQ.GhFc3A.": "0xd9eD90456F1bb097185e8dd4eCdd56Ac6A088175",
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

# 随机生成请求头的User-Agent
def get_user_agent():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    ]

    return random.choice(user_agent_list)


def chat():
    # 测试频道
    chanel_list = ['961884232546918450']
    # zeta 领水频道
    chanel_list = ['922357353423175680']

    # dc号列表 主 + 副2 + 比特
    # TODO 上传代码仓库前 把dc的token处理掉
    auth_list = [
        # 主
        "OTQwODYwNTQyMjU4NjY3NTMw.G3mF0J.",
        # 副2
        "OTc4OTMzNTk0MDg3MTEyNzE0.GpCa8e.WRuZuiFcsVBm52e-",

        # 比特
        "OTc4OTM4NDM4NTk2MzE3MTg1.GAWH0X.egVrarSOpcF0hs-",
        "MTA3Njc2NzM0Mzg5MzU0NTAyMA.G-8tWb.",
        "MTA3MTI0MjE1Mjc5OTEwOTIxMg.GSBZ8T.",
        "MTAxNDM2NjE4ODEzNjA0NjY0Mg.GfZiPv.R1lJ-",
        "OTg1MTMxODk1MTY1NzEwMzc2.GAR1mq.",
        "MTA3Mjg1MDMwMTEwMDQ5OTAyNg.GA5G2I.",
        "MTA3Njc3NDI1Mzk2NzQ1MDEzMw.GUdVT8.-z1TCXR8",
        "MTA3Mjg2MDE0MDMwNDMzODk0NA.Gm8cOx.",
        "MTA3Mjg2NDU0MDM1MTUyODk4MQ.GSZqwM.",
        "MTA3Njc4MTE5MDYyNDg1MDA1MQ.GI0HgN.",
    ]
    for auth in auth_list:
        header = {
            "Authorization": auth,
            "Content-Type": "application/json",
            "User-Agent": get_user_agent()
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
