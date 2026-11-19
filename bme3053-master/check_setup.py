import sys

REQUIRED = ["numpy", "scipy", "matplotlib", "pandas"]

print(f"Python {sys.version.split()[0]}")
missing = []
for pkg in REQUIRED:
    try:
        mod = __import__(pkg)
        print(f"  ok  {pkg} {getattr(mod, '__version__', '')}")
    except ImportError:
        missing.append(pkg)
        print(f"  MISSING  {pkg}")

if missing:
    sys.exit("Setup problem: run `uv sync` and try again.")
print("Setup OK")
