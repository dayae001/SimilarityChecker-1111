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

        if len(self.alpha1) >= len(self.alpha2):
            len1 = len(self.alpha1)
            len2 = len(self.alpha2)
        else:
            len2 = len(self.alpha1)
            len1 = len(self.alpha2)

        if len1 == len2:
            score += 60
        elif len1 >= len2 * 2:
            score += 0
        else:
            score += (1 - (len1 - len2) / len2) * 60
        return score

    def calc_alpha(self):
        score = 0
        alpha1_set = set(self.alpha1)
        alpha2_set = set(self.alpha2)
        alpha1_alpha2_intersection = alpha1_set.intersection(alpha2_set)
        alpha1_alpha2_union = alpha1_set.union(alpha2_set)

        if alpha1_set == alpha2_set:
            score += 40
        elif len(alpha1_alpha2_intersection) == 0:
            score += 0
        else:
            score += (len(alpha1_alpha2_intersection) / len(alpha1_alpha2_union)) * 40
        return score
