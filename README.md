**Copyright (c) 2023 tristanGIANDO**

*Permission is hereby granted, free of charge, to any person obtaining a copy*
*of this software and associated documentation files (the "Software"), to deal*
*in the Software without restriction, including without limitation the rights*
*to use, copy, modify, merge, publish, distribute, sublicense, and/or sell*
*copies of the Software, and to permit persons to whom the Software is*
*furnished to do so, subject to the following conditions:*

*The above copyright notice and this permission notice shall be included in all*
*copies or substantial portions of the Software.*

*THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR*
*IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,*
*FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE*
*AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER*
*LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,*
*OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE*
*SOFTWARE.*

# PEP8_CONVERTER
How to PEP8 your Python files

##
The script is written in **Python 3**.

### INSTALL
Download `convert_to_pep.py`
Install `autopep8` : `pip install autopep8`

## INSTRUCTIONS FOR USE
```py
from convert_to_pep import adapt_to_pep8

if __name__ == '__main__':
    # Path to the Python file to be adapted
    python_file = r"path/to/your/file.py"

    if os.path.isfile(python_file):
        adapt_to_pep8(python_file)
    else:
        print("The specified file does not exist.")
```

## PARAMETERS
Here are all the arguments to fill in before running the script.

|         Parameter           |   Type    |              Description              |
|:---------------------------:|:---------:|---------------------------------------|
|      python_file            |    str    | The Python file you want to correct.  |
