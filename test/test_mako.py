import unittest
from bottle import MakoTemplate

class TestMakoTemplate(unittest.TestCase):
    def test_string(self):
        """ Templates: Mako string"""
        t = MakoTemplate('start ${var} end').render(var='var')
        self.assertEqual('start var end', ''.join(t))

    def test_file(self):
        """ Templates: Mako file"""
        t = MakoTemplate(filename='./mako_simple.tpl').render(var='var')
        self.assertEqual('start var end', ''.join(t))

    def test_name(self):
        """ Templates: Mako lookup by name """
        t = MakoTemplate(name='mako_simple', lookup='./').render(var='var')
        self.assertEqual('start var end', ''.join(t))

    def test_notfound(self):
        """ Templates: Unavailable templates"""
        self.assertRaises(TemplateError, MakoTemplate, name="abcdef")

    def test_error(self):
        """ Templates: Exceptions"""
        self.assertRaises(Exception, MakoTemplate, '%for badsyntax')

    def test_inherit(self):
        """ Templates: Mako lookup and inherience """
        t = MakoTemplate(name='mako_inherit', lookup='./').render(var='v')
        self.assertEqual('o\ncvc\no\n', ''.join(t))

suite = unittest.TestSuite()
try:
  import mako
  suite.addTest(unittest.makeSuite(TestMakoTemplate))
except ImportError:
  print "WARNING: No Mako template support. Skipping tests."


if __name__ == '__main__':
    unittest.main()

