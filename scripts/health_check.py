#!/usr/bin/env python3
"""Check if URLs in links.json are reachable.

Usage:
  python health_check.py [limit] [--insecure]
  --insecure  skip TLS certificate verification (for hosts with broken certs)
"""

import json
import os
import sys
import ssl
import urllib.request
import urllib.error


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)


def check_url(url, timeout=10, insecure=False):
    ctx = None
    if insecure:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=timeout, context=ctx)
        return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return None


def main():
    with open(os.path.join(ROOT_DIR, 'links.json'), 'r') as f:
        links = json.load(f)

    insecure = '--insecure' in sys.argv[1:]
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    limit = int(args[0]) if args else len(links)
    links = links[:limit]

    print(f"Checking {len(links)} URLs... (TLS verification: {'OFF' if insecure else 'ON'})\n")
    broken = []
    for i, l in enumerate(links):
        status = check_url(l['url'], insecure=insecure)
        icon = '✓' if status and status < 400 else '✗'
        if icon == '✗':
            broken.append((l['name'], l['url'], status))
            print(f"  {icon} [{status}] {l['name']}: {l['url']}")
        elif (i + 1) % 50 == 0:
            print(f"  checked {i+1}/{len(links)}...")

    print(f"\nDone. {len(broken)} broken out of {len(links)} checked.")
    if broken:
        print("\nBroken links:")
        for name, url, status in broken:
            print(f"  [{status}] {name} — {url}")


if __name__ == '__main__':
    main()
