import json, os

app_id  = os.environ["APP_ID"]
version = os.environ["VERSION"]
date    = os.environ["DATE"]
dl_url  = os.environ["DOWNLOAD_URL"]
size    = int(os.environ["SIZE"])
desc    = os.environ["DESCRIPTION"]

with open("source.json", "r", encoding="utf-8") as f:
    source = json.load(f)

for app in source["apps"]:
    if app["bundleIdentifier"] != app_id:
        continue

    old_versions = app.get("versions", [])
    min_os = old_versions[0].get("minOSVersion", "16.1") if old_versions else "16.1"

    new_entry = {
        "version": version,
        "date": date,
        "localizedDescription": desc,
        "downloadURL": dl_url,
        "size": size,
        "minOSVersion": min_os,
    }

    # rimuove un'eventuale voce con la stessa versione (re-run) e mette la nuova in cima
    others = [v for v in old_versions if v["version"] != version]
    app["versions"] = [new_entry] + others

    app["version"]     = version
    app["versionDate"] = date
    app["downloadURL"] = dl_url
    app["size"]        = size
    break
else:
    raise SystemExit(f"App {app_id} non trovata in source.json")

with open("source.json", "w", encoding="utf-8") as f:
    json.dump(source, f, indent=2, ensure_ascii=False)

print(f"Updated {app_id} to {version}")
