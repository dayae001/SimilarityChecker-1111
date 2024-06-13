from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test1(self):
        test = SimilarityChecker()
        self.assertEqual(1, 1)
