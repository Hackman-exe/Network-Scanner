# Network-Scanner

Scan your WiFi and see every device connected to it. Built with Python and nmap.

> Only use this on your own network. Educational purposes only.

---

## What you need first

**Python** — get from python.org, tick "Add to PATH" when installing

**nmap** — get from nmap.org/download, run the .exe installer, keep defaults

**python-nmap** — once nmap is installed, run this in terminal:
```
pip install python-nmap
```

---

## Before you run it

- Open your terminal as **Administrator** or it won't detect manufacturers
- Make sure you're on **WiFi** — if you're plugged into ethernet on a separate router you might not see everything on your main network

---

## Run it

Navigate to wherever you saved the file, then run it:
```
cd path/to/your/folder
python Network-Scanner.py
```

For example if you saved it to your Documents:
```
cd C:\Users\YourName\Documents
python Network-Scanner.py
```

---

## Why are some devices Unknown?

Apple devices randomise their MAC address since iOS 14 — so if you see Unknown, it's almost certainly an Apple device. Everything else should show the manufacturer fine.

---

TikTok: [@hackman.exe](https://tiktok.com/@hackman.exe)
