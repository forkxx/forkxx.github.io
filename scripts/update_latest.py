import json, sys, urllib.request, xml.etree.ElementTree as ET
CH = "UC1jG6PqikmZL1k1rgPkJApQ"
URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CH}"
try:
    data = urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read()
    e = ET.fromstring(data).find("{http://www.w3.org/2005/Atom}entry")
    ns = {"a": "http://www.w3.org/2005/Atom", "y": "http://www.youtube.com/xml/schemas/2015"}
    out = {"id": e.find("y:videoId", ns).text, "title": e.find("a:title", ns).text, "published": e.find("a:published", ns).text}
except Exception as ex:
    print("feed indisponível:", ex); sys.exit(0)
json.dump(out, open("assets/latest.json", "w", encoding="utf-8"), ensure_ascii=False)
print(out)
