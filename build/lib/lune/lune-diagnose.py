# lune-diagnose.py

import os
import importlib.util
import subprocess
import sys

MODULE_DIR = "modules"
REQUIREMENTS = {
    "pyperclip": "pyperclip",
    "whois": "python-whois",
    "dns": "dnspython",
    "scapy": "scapy",
}

valid_modules = []
missing_main = []
import_errors = []

def try_import(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False
    except Exception as e:
        return str(e)

def auto_fix_imports(missing_libs):
    for lib in missing_libs:
        pip_name = REQUIREMENTS.get(lib)
        if pip_name:
            print(f"🛠 Installing missing package: {pip_name}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            except Exception as e:
                print(f"❌ Failed to install {pip_name}: {e}")

def diagnose_modules():
    print("\n🔍 Scanning modules in 'modules/'...\n")
    for module_file in os.listdir(MODULE_DIR):
        if module_file.endswith(".py"):
            name = module_file[:-3]
            path = os.path.join(MODULE_DIR, module_file)

            try:
                spec = importlib.util.spec_from_file_location(name, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

                if not hasattr(mod, "main"):
                    missing_main.append(name)
                else:
                    valid_modules.append(name)

            except ImportError as e:
                missing_mod = str(e).split("named")[-1].strip().strip("'\"")
                import_errors.append((name, missing_mod))
            except Exception as e:
                import_errors.append((name, str(e)))

def print_report():
    print("\n📋 DIAGNOSIS REPORT\n" + "─" * 30)
    print(f"\n✅ VALID MODULES ({len(valid_modules)}):")
    for mod in sorted(valid_modules):
        print(f"  - {mod}")
    print(f"\n⚠ MISSING MAIN() ({len(missing_main)}):")
    for mod in sorted(missing_main):
        print(f"  - {mod}")
    print(f"\n❌ IMPORT ERRORS ({len(import_errors)}):")
    for mod, err in sorted(import_errors):
        print(f"  - {mod}: {err}")
    print(f"\n📦 Total Scanned: {len(valid_modules) + len(missing_main) + len(import_errors)}")
    print("🧼 Suggested Fix: Add missing `main()` or fix broken import paths.")

if __name__ == "__main__":
    diagnose_modules()
    missing_libs = list(set(err for _, err in import_errors if err in REQUIREMENTS))
    if missing_libs:
        auto_fix_imports(missing_libs)
        import_errors.clear()
        valid_modules.clear()
        missing_main.clear()
        diagnose_modules()  # Rerun after fix attempt
    print_report()
