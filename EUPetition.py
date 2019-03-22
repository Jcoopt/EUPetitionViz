#!/usr/bin/env python3
import urllib.request, json,time

from time import gmtime, strftime
while True:
    with urllib.request.urlopen("https://petition.parliament.uk/petitions/241584/count.json") as url:
        importData = json.loads(url.read().decode())
        file= open("results.txt","a")
        file.write("\n"+str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+","+str(importData['signature_count']))
        file.close()
        time.sleep(300)
