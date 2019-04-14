from core.methods.interface import Method
import ahocorasick

class AhoCorasik(Method):
    def __init__(self):
        self.first_tokens = None
        self.second_tokens = None

    def score(self, w1: str, w2: str) -> float:
        shorter, longer = w1.lower(), w2.lower()

        if len(w1) > len(w2):
            longer, shorter = shorter, longer

        A = ahocorasick.Automaton()
        for idx, key in enumerate(longer.split()):
            A.add_word(key, (idx, key))
        A.make_automaton()

        result = []
        summary = 0
        arr_shorter = shorter.split()
        for idx, key in enumerate(arr_shorter):
            res = A.match(key, 'not exists')
            summary += int(res) # собираем все баллы

        score = summary / len(arr_shorter) # находим среднее
        return score

    @property
    def intersection(self) -> set:
        return set.intersection(self.first_tokens, self.second_tokens)

    @property
    def union(self) -> set:
        return set.union(self.first_tokens, self.second_tokens)

    @staticmethod
    def _build_tokens(word: str) -> set:
        return set(word)

