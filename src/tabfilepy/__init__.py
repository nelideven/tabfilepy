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
    PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
    windows_script = os.path.join(PACKAGE_DIR, "fp_autocomplete.cmd")
    posix_script = os.path.join(PACKAGE_DIR, "fp_autocomplete.sh")
    temp_file = os.path.join(tempfile.gettempdir(), 'filename_output.txt')

    @classmethod
    def get_filename(cls):
        """Retrieve the filename using the appropriate autocomplete script."""
        try:
            if os.name == "nt":
                subprocess.run(['cmd', '/c', cls.windows_script], check=True)
            else:
                subprocess.run(['bash', cls.posix_script], check=True)
            return cls._read_output()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error executing script: {e}")

    @classmethod
    def _read_output(cls):
        """Reads the filename from the temporary output file."""
        if os.path.exists(cls.temp_file):
            with open(cls.temp_file, 'r') as file:
                return file.read().strip()
        raise FileNotFoundError("Output file not found.")

def main():
    result = tabfilepy.get_filename()
    print(result)
