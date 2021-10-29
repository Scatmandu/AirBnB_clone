#!/usr/bin/python3
"""
Unittest Review class
"""
import unittest
import pep8
import sys
from datetime import datetime
from models import review
from models.review import Review
import os


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)


class ReviewclassTests(unittest.TestCase):
    """ Test Case for review module """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = Review()
        self.ins1 = Review()

    def tearDown(self):
        """ Clean All test case """
        pass

    def test_instance(self):
        """ Test Case to check instance  """
        self.assertIsInstance(self.ins0, Review)
        self.assertIsInstance(self.ins1, Review)

    def test_id(self):
        """
        Test id of instances
        instance id will be not equal
        type, will be str
        """
        self.assertNotEqual(self.ins0.id, self.ins1.id)
        self.assertEqual(type(self.ins0.id), str)
        self.assertEqual(type(self.ins1.id), str)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/review.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/review.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/review.py', os.X_OK)
        self.assertTrue(exe)

    def test_datetime_save(self):
        """ Test datetime to compare format """
        cre = self.ins0.created_at
        self.ins0.save()
        up = self.ins0.updated_at
        self.assertEqual(type(cre), datetime)
        self.assertEqual(type(up), datetime)
        self.assertNotEqual(cre, up)  # time create and update are diff

    def test_to_dict(self):
        """ The dict return is the same """
        dateform = '%Y-%m-%dT%H:%M:%S.%f'
        dic = self.ins0.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(dic['created_at'],
                         self.ins0.created_at.strftime(dateform))
        self.assertEqual(dic['updated_at'],
                         self.ins0.updated_at.strftime(dateform))

    def test_place_id_str(self):
        """ Test type of date. Will be str"""
        idplacestr = self.ins0.place_id
        self.assertEqual(type(idplacestr), str)

    def test_user_id_str(self):
        """ Test type of date. Will be str"""
        iduserstr = self.ins0.user_id
        self.assertEqual(type(iduserstr), str)

    def test_text_str(self):
        """ Test type of date. Will be str"""
        textstr = self.ins0.text
        self.assertEqual(type(textstr), str)


if __name__ == '__main__':
    unittest.main()