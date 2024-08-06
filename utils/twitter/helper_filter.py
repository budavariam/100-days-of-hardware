import json
from progress import IDS

d = []
with open("./tweets.json", encoding="utf-8") as f:
    d = json.load(f)

all_ids = set([str(y) for _, y in IDS])
result = []
for x in d:
    tw = x.get("tweet")
    tid = tw.get("id")
    if str(tid) in all_ids:
        result.append(x)
print(all_ids)

with open("./tweets_filtered.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
