import random
import vk
import time
import pandas as pd


def unix(timein):
    time_tuple = time.strptime(timein, "%Y %m %d")
    timestamp = time.mktime(time_tuple)
    return timestamp


dates = [36000, 14400, 10800]
session = vk.AuthSession(
    access_token='token')
vk_api = vk.API(session)
dogs = pd.ExcelFile("vk.xlsx")
df = dogs.parse(u'Лист1')
df = df[:60]
Instr = input()
pdate = unix(Instr)
i = 0
n = 1
print(df.head())
for index, post in df.iterrows():
    minutes = [random.randrange(0, 34) * 60, random.randrange(0, 35) * 60, random.randrange(0, 35) * 60]
    if post["IsIn"] == "да":
        continue
    if i == 3:
        i = 0
        pdate = unix(Instr) + 86400*n
        n = n + 1
        time.sleep(1)
    pdate = pdate + dates[i] + minutes[i]

    vk_api.wall.post(owner_id=-19366044, message=post["Text"], attachments=post["Photo"], publish_date=pdate, v=5.122, from_group=1)
    i = i + 1
