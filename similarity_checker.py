class SimilarityChecker:
    def __init__(self):
        self.alpha2 = None
        self.alpha1 = None

    def guess(self):
        score = 0
        if len(self.alpha1) == len(self.alpha2):
            score += 60
        if set(self.alpha1) == set(self.alpha2):
            score += 40

        return score
