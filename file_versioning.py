import shutil
import datetime
import os

def save_checkpoint_version(source_dir, version_label=None):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    label = version_label or f"checkpoint_{timestamp}"
    dest = os.path.join("checkpoints", label)
    shutil.copytree(source_dir, dest)
    print(f"✅ Saved version: {label}")
