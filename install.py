import os
import shutil

os.makedirs("./lib", exist_ok=True)
shutil.copy("./microbutton-core/button.py", "./lib/button.py")
