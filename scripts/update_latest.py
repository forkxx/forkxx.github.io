import json, sys, urllib.request, xml.etree.ElementTree as ET
CH = "UC1jG6PqikmZL1k1rgPkJApQ"
URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CH}"
try:
    data = urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read()
    ns = {"a": "http://www.w3.org/2005/Atom", "y": "http://www.youtube.com/xml/schemas/2015"}
    vids, seen = [], set()
    for e in ET.fromstring(data).findall("a:entry", ns):
        v = {"id": e.find("y:videoId", ns).text, "title": e.find("a:title", ns).text, "published": e.find("a:published", ns).text}
        if v["title"] in seen:
            continue
        seen.add(v["title"]); vids.append(v)
        if len(vids) == 3:
            break
    out = dict(vids[0]); out["videos"] = vids
except Exception as ex:
    print("feed indisponível:", ex); sys.exit(0)
json.dump(out, open("assets/latest.json", "w", encoding="utf-8"), ensure_ascii=False)
print(out)
