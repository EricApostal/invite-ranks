import subprocess
import sys
# this just installs the requirements, there's likely a better way to do this
# but it turned out to be the most effective one I could find.
subprocess.check_call([sys.executable, "-m", "pip", "install", 'nextcord'])
