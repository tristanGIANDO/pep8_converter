"""
MIT License

Copyright (c) 2023 tristanGIANDO

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import autopep8
import os

def adapt_to_pep8(input_file):
    with open(input_file, "r") as file:
        code = file.read()

    adapted_code = autopep8.fix_code(code)

    with open(input_file, "w") as file:
        file.write(adapted_code)

    print("Adaptation to PEP8 conventions completed!")

if __name__ == '__main__':
    # Path to the Python file to be adapted
    python_file = r"path/to/your/file.py"

    if os.path.isfile(python_file):
        adapt_to_pep8(python_file)
    else:
        print("The specified file does not exist.")
