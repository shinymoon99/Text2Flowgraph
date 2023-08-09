import json

with open("procedure_flowgraph.json","r",encoding="utf-8") as f:
    ICTdata = json.load(f)
train_data = ICTdata[:int(0.8*(len(ICTdata)))]
eval_data = ICTdata[int(0.8*(len(ICTdata))):]
with open("./datasets/ICT_train.json","w",encoding="utf-8") as f1:
    json.dump(train_data,f1,ensure_ascii=False)
with open("./datasets/ICT_dev.json","w",encoding="utf-8") as f2:
    json.dump(eval_data,f2,ensure_ascii=False)

