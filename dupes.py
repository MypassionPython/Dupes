#!/usr/bin/env python3
import argparse, hashlib, os, pathlib

def sha256(path: pathlib.Path, chunk=1024*1024):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b: break
            h.update(b)
    return h.hexdigest()

def main(argv=None):
    p = argparse.ArgumentParser(description="Find duplicate files by SHA256")
    p.add_argument("root", help="folder to scan")
    p.add_argument("--min-size", type=int, default=1, help="bytes, default 1")
    args = p.parse_args(argv)
    root = pathlib.Path(args.root)
    hashes = {}
    for dirpath, _, files in os.walk(root):
        for name in files:
            pth = pathlib.Path(dirpath) / name
            try:
                if pth.stat().st_size < args.min_size: 
                    continue
                h = sha256(pth)
                hashes.setdefault(h, []).append(str(pth))
            except Exception as e:
                print(f"skip {pth}: {e}")
    for h, paths in hashes.items():
        if len(paths) > 1:
            print(f"\nhash {h}:")
            for p in paths:
                print(f" - {p}")

if __name__ == "__main__":
    main()
