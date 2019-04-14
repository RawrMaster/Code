from core.methods.interface import Method
import ahocorasick

class AhoCorasik(Method):
    
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
            summary += int(res)                               # collecting all points

        score = summary / len(arr_shorter)                    # calculating average value
        return score

