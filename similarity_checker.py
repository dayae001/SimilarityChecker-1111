class SimilarityChecker:
    def __init__(self):
        self.alpha1 = ""
        self.alpha2 = ""

    def guess(self):
        score = 0
        score += self.calc_length()
        score += self.calc_alpha()
        return score

    def calc_length(self):
        score = 0
        len1, len2 = self.get_more_long_alpha()

        if len1 == len2:
            score += 60
        elif len1 >= len2 * 2:
            score += 0
        else:
            score += (1 - (len1 - len2) / len2) * 60
        return score

    def get_more_long_alpha(self):
        len1 = max(len(self.alpha1), len(self.alpha2))
        len2 = min(len(self.alpha1), len(self.alpha2))
        return len1, len2

    def calc_alpha(self):
        score = 0
        alpha1_alpha2_intersection, alpha1_alpha2_union, alpha1_set, alpha2_set = self.get_alpha_sets()

        if alpha1_set == alpha2_set:
            score += 40
        elif len(alpha1_alpha2_intersection) == 0:
            score += 0
        else:
            score += (len(alpha1_alpha2_intersection) / len(alpha1_alpha2_union)) * 40
        return score

    def get_alpha_sets(self):
        alpha1_set = set(self.alpha1)
        alpha2_set = set(self.alpha2)
        alpha1_alpha2_intersection = alpha1_set.intersection(alpha2_set)
        alpha1_alpha2_union = alpha1_set.union(alpha2_set)
        return alpha1_alpha2_intersection, alpha1_alpha2_union, alpha1_set, alpha2_set
