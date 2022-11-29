import unittest

from question3 import Person

class TestClassif_Obesity(unittest.TestCase):
    def test_classif_obesity(self):
        # Test the classification for different BMIs
        self.assertEqual(Person(1.70,65).classif_obesity(),['Normal', None])
        self.assertEqual(Person(1.90,65).classif_obesity(),['Thinness', None])
        self.assertEqual(Person(1.75,100).classif_obesity(),['Obesity', "I"])
        self.assertEqual(Person(1.75,120).classif_obesity(),['Obesity', "II"])

        # seguir vídeo a partir de 6 min: https://www.youtube.com/watch?v=1Lfv5tUGsn8&ab_channel=Socratica