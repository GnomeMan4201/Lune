import os
import importlib.util

def load_modules_from_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                module_path = os.path.join(root, file)
                module_name = os.path.relpath(module_path, directory).replace("/", ".").replace("\\", ".")[:-3]
                try:
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                except Exception as e:
                    print(f"[!] Failed to load {module_name}: {e}")

if __name__ == "__main__":
    load_modules_from_directory("modules")
