"""
MIT License

Copyright (c) 2025 Omkaar

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


# pylint: skip-file

import unittest
import pirate

class TestTranslate(unittest.TestCase):
    def test_translate_returns_string(self):
        result = pirate.translate("Hello, friend!")
        self.assertIsInstance(result, str)

    def test_translate_not_empty(self):
        result = pirate.translate("Where is the treasure?")
        self.assertTrue(len(result) > 0)

    def test_translate_no_whitespace_only(self):
        result = pirate.translate("Give me the map!")
        self.assertNotEqual(result.strip(), "")

    def test_translate_changes_text(self):
        text = "Hello, friend!"
        result = pirate.translate(text)
        self.assertNotEqual(result, text)

if __name__ == '__main__':
    unittest.main()
