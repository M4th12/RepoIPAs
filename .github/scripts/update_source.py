import json, os

app_id    = os.environ["APP_ID"]       # es. "com.spotify.client"
version   = os.environ["VERSION"]
date      = os.environ["DATE"]
dl_url    = os.environ["DOWNLOAD_URL"]
size      = int(os.environ["SIZE"])
desc      = os.environ["DESCRIPTION"]

with open("source.json", "r") as f:
    source = json.load(f)

for app in source["apps"]:
    if app["bundleIdentifier"] == app_id:
        app["version"]     = version
        app["versionDate"] = date
        app["downloadURL"] = dl_url
        app["size"]        = size
        app["versions"] = [{
            "version":             version,
            "date":                date,
            "localizedDescription": desc,
            "downloadURL":         dl_url,
            "size":                size,
            "minOSVersion":        "16.1"
        }]
        break

with open("source.json", "w") as f:
    json.dump(source, f, indent=2, ensure_ascii=False)

print(f"Updated {app_id} to {version}")
