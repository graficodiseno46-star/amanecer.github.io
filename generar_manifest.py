"""Lee las carpetas archivos/Amanecer y archivos/Opal y escribe manifest.json."""
import json, os
res = {}
for marca in ("Amanecer", "Opal"):
    ruta = os.path.join("archivos", marca)
    res[marca] = sorted(f for f in os.listdir(ruta)
                        if not f.startswith(".") and f.upper() != "LEEME.TXT"
                        and os.path.isfile(os.path.join(ruta, f))) if os.path.isdir(ruta) else []
json.dump(res, open("manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in res.items()})
