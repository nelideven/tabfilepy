'''
tabfilepy; A simple Python library (with associated cmd/bash script) which allows file directory tab auto-completions. 
This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along with this library; if not, see <https://www.gnu.org/licenses/>.
'''

import subprocess
import os
import tempfile

class tabfilepy:
    def __init__(self, windows_script="fp_autocomplete.cmd", posix_script="fp_autocomplete.sh"):
        self.package_dir = os.path.dirname(os.path.abspath(__file__))
        self.windows_script = os.path.join(self.package_dir, windows_script)
        self.posix_script = os.path.join(self.package_dir, posix_script)

    def get_filename(self, prompt="Enter file path: "):
        """Run the autocomplete script and return the filename."""
        try:
            if os.name == 'nt':
                result = subprocess.run(["cmd", "/c", self.windows_script, prompt], stdout=subprocess.PIPE, text=True)
            else:
                result = subprocess.run(["bash", self.posix_script, prompt], stdout=subprocess.PIPE, text=True)
            extfilename = os.path.abspath(os.path.expanduser(result.stdout.strip()))
            return extfilename
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error executing script: {e}")
        except KeyboardInterrupt:
            print("tabfilepy interrupted by user.")

def get_filename(prompt="Enter file path: "):
    return tabfilepy().get_filename(prompt)

def main():
    print(tabfilepy().get_filename())
