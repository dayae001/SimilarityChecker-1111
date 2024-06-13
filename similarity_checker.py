class SimilarityChecker:
    def __init__(self):
        self.alpha1 = None
        self.alpha2 = None

    def guess(self):
        score = 0
        score += self.calc_length()
        score += self.calc_alpha()
        return score

    def calc_length(self):
        score = 0
        
        if len(self.alpha1) == len(self.alpha2):
            score += 60
        elif len(self.alpha1) <= len(self.alpha2) * 0.5 or \
                len(self.alpha1) >= len(self.alpha2) * 2:
            score += 0
        return score

    def calc_alpha(self):
        score = 0
        alpha1_set = set(self.alpha1)
        alpha2_set = set(self.alpha2)

        if alpha1_set == alpha2_set:
            score += 40
        elif len(alpha1_set.intersection(alpha2_set)) == 0:
            score += 0
        return score
