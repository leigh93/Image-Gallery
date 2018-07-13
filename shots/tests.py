# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.test import TestCase
from models import Image, Category, Location
from arcade import settings

# Create your tests here.

# def funcname(self, parameter_list):
#     pass
class TestImage(TestCase):

    def setUp(self):
        self.newimage = Image('3.jpg','house','kilimani', 'interior-design')

    def test_init(self):
        self.assertEqual(self.newimage.image,"3.jpg")
        self.assertEqual(self.newimage.image_name,"house")
        self.assertEqual(self.newimage.image_location,"kilimani")
        self.assertEqual(self.newimage.image_category,"interior-design")

    def test_save_image(self):
        self.new_image.image_contact()
        self.assertEqual(len(Image.image_list),1)

    def tearDown(self):
        Image.image_list = []

    def test_save_multiple(self):
        self.new_image.save_image()
        test_image=Image("test.jpg", "user", "kileleshwa", "testuser")
        test_Image.save_image()
        self.assertEqual(len(Image.image_list),2)

    def test_delete_image(self):
        test_image = Image("test", "user","700000000", "user@mail.com")
        test_image.save_image()
        test_image2=Contact("test", "user", "978899877766", "testuser@gmail.com")
        test_image2.save_image()
        test_image.delete_image()
        self.assertEqual(len(Image.image_list),1)

    def test_find_by_location(self):
        test_image = Image("test", "user","700000000", "user@mail.com")
        test_image.save_image()
        found_image = Image.find_by_location("Kilimani")
        self.assertEqual(found_image.name,test_image.name)
        
           
# if __name__=='__main__':
#     unittest.main()
        