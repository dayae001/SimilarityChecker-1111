class SimilarityChecker:
    def guess(self, alpha1, alpha2):
        score = 0
        if len(alpha1) == len(alpha2):
            score += 60
        if set(alpha1) == set(alpha2):
            score += 40

        return score
