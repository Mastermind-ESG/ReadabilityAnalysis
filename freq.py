
import os
import json

from collections import Counter

fail = 0
total = 0

res = []

for i in os.listdir("hq_txt"):

    if i.endswith(".split"):
        continue

    print("Processing: " + i)

    data = {
        'id': i
    }

    try:
        text = open("hq_txt/" + i, "r").read()
        sp = json.loads(open("hq_txt/" + i + ".split", "r").read())

        words = sp['pos/ctb'][0]
        words_count = Counter(words)

        length = len(text)
        sentence_num = len(list(filter(lambda x: x == "。" or x == "！" or x == "？", list(text))))
        passive_num = len(list(filter(lambda x: x == "被", list(text))))

        adv_num = len(list(filter(lambda x: x == "被", list(text))))

        data['长度'] = length
        data['句数'] = sentence_num
        data['被动'] = passive_num

        data['总词数'] = len(words)
        data['连副词'] = words_count['AD']

        res.append(data)
        
    except Exception as e:
        print(e)
        fail += 1

    total += 1
    print(fail / total, total)
    

import pandas

df = pandas.DataFrame(res)
df.to_csv("data.csv")
