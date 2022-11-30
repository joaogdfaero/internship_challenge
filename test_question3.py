import unittest

from question3 import Person

class TestClassif_Obesity(unittest.TestCase):
    def test_classif_obesity(self):
        # test the classification for different BMIs
        self.assertEqual(Person(1.70,65).classif_obesity(),['Normal', None])
        self.assertEqual(Person(1.90,65).classif_obesity(),['Thinness', None])
        self.assertEqual(Person(1.75,100).classif_obesity(),['Obesity', "I"])
        self.assertEqual(Person(1.75,120).classif_obesity(),['Obesity', "II"])

    def test_values(self): 
        # makes sure value errors are raised when necessary
        self.assertRaises(ValueError,Person(-1.75,-200).classif_obesity)
    
    def test_types(self):
        # makes sure type errors are raised when necessary
        self.assertRaises(TypeError,Person("-1.75","-200").classif_obesity)
        self.assertRaises(TypeError,Person("-1.75",-200).classif_obesity)
