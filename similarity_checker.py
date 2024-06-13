class SimilarityChecker:
    def __init__(self):
        self.alpha1 = None
        self.alpha2 = None

    def guess(self):
        score = 0
        if len(self.alpha1) == len(self.alpha2):
            score += 60

        elif len(self.alpha1) <= len(self.alpha2) * 0.5 or \
                len(self.alpha1) >= len(self.alpha2) * 2:
            score += 0

        if set(self.alpha1) == set(self.alpha2):
            score += 40

        elif len(set(self.alpha1).intersection(set(self.alpha2))) == 0:
            score += 0

        return score
