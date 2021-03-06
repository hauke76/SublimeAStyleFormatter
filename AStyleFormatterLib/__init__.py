"""
Copyright (c) 2012 Timon Wong

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

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

SYNTAX_MODE_MAPPING = {
    'c': 'c',
    'c++': 'c',
    'objc': 'c',
    'objc++': 'c',
    'opencl': 'c',
    'cuda-c++': 'c',
    'arduino': 'c',
    'cs': 'cs',
    'java': 'java',
    'pde': 'java',
    'apex': 'java',
}

SUPPORTED_SYNTAXES = set(SYNTAX_MODE_MAPPING.keys())


def get_syntax_mode_mapping(user_defined_syntax_mode_mapping=None):
    mapping = SYNTAX_MODE_MAPPING.copy()
    if user_defined_syntax_mode_mapping:
        mapping.update(user_defined_syntax_mode_mapping)
    return mapping
