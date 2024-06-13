from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test1(self):
        game = SimilarityChecker()
        game.alpha1 = 'ABC'
        game.alpha2 = 'CBA'
        self.assertEqual(100, game.guess(game.alpha1, game.alpha2))
