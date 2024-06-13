from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.game = SimilarityChecker()
        super().setUp()

    def set_alphas(self, str1, str2):
        self.game.alpha1 = str1
        self.game.alpha2 = str2

    def test1(self):
        self.set_alphas('ABC', 'CBA')
        self.assertEqual(100, self.game.guess())

    def test2(self):
        self.set_alphas('A', 'BB')
        self.assertEqual(0, self.game.guess())
