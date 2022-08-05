from bilibili_api import Credential, rank
import asyncio

SESSDATA = '64660c21%2C1675277136%2C7eb29%2A81'
BILI_JCT = '51641e30b43eef803cc8b62a08933dee'
BU_VID3 = 'EAC791BC-66CB-7DB7-F62D-2A2571EB1A1650950infoc'
DEDE_USERID = '294718686'

credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3=BU_VID3, dedeuserid=DEDE_USERID)

if __name__ == '__main__':
    print(asyncio.get_event_loop().run_until_complete(rank.get_hot_videos()))