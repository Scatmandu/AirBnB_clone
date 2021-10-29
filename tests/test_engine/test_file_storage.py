#!/usr/bin/python3
""" FileStorage class test module """

import os
import pep8
import unittest
from models import base_model
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestPep8(unittest.TestCase):
    """ Validates PEP8 style """

    def test_pep8(self):
        """ Validates PEP8 style conformance """

        style = pep8.StyleGuide(quiet=True)
        f1 = 'models/engine/file_storage.py'
        f2 = 'tests/test_models/test_engine/test_file_storage.py'
        res = style.check_files([f1, f2])
        self.assertEqual(res.total_errors, 0, "Code has style errors.")


class TestDocs(unittest.TestCase):
    """ Validates docstring """

    def test_module_doc(self):
        """ Validates module doc """

        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """ Validates class doc """

        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """ Validates methods doc """

        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class BaseModelclassTests(unittest.TestCase):
    """ Test Case for base_model moudle """

    def setUp(self):
        """ Setup of test object """

        self.obj = FileStorage()

    def tearDown(self):
        """ Clear test cases """

        pass

    def test_permissions(self):
        """ Validates R-W-X permissions """

        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)

    def test_isinstance(self):
        """ Validates that created object is a FileStorage object """

        self.assertIsInstance(self.obj, FileStorage)

    def test_all(self):
        """ Validates all() returns a dictionary """

        dic = self.obj.all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, self.obj._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
