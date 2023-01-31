import hanlp
import os
import json

HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)

for i in os.listdir("hq_txt"):
    print("Processing: " + i)
    text = open("hq_txt/" + i, "r").read()

    try:
        with open("hq_txt/" + i + ".split", "w") as f:
            f.write(json.dumps(HanLP([text], tasks='pos')))
    except Exception as e:
        print(e)

