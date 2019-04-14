from operator import attrgetter
import ahocorasick

from typing import (
    Iterator,
    List,
    Dict
)

from core.methods import Method
from core.models import Token
import threading

def build_groups(
        normalized_tokens: List[Token],
        method: Method,
        convergence: float
) -> Dict[str, Token]:
    groups = dict()
 #   print('=' * 50)
 #   print('BUILD GROUPS')
 #   print('normalized_tokens', normalized_tokens)

    #A = ahocorasick.Automaton()
    # for idx, key in enumerate('he her hers she temporal'.split()):
    #   A.add_word(key, (idx, key))

    # for idx, key in enumerate('temporal_reasoning temporal'.split()):
    #   A.add_word(key, (idx, key))

    # for idx in range(4):
    #   key = normalized_tokens[idx].term
    #   A.add_word(key, (idx, key))
	#
    # A.make_automaton()
    # print(">>>>res: ", A.match('temporal reasoning', 'not exists'))


    while len(normalized_tokens) > 0:
        group_key = normalized_tokens.pop(0)
        group_variants = [group_key]
     #   print('>>>>>>' * 50)
        # print('group_key', group_key)
     #   print('>>>RANGE >>>', range(len(normalized_tokens) - 1, -1, -1))
        for i in range(len(normalized_tokens) - 1, -1, -1):
      #      print('>>>I >>>', i)
            # print('normalized_tokens[i].term', normalized_tokens[i].term)
            # print('group_key.term', group_key.term)
            score = method.score(
                w1=normalized_tokens[i].term,
                w2=group_key.term
            )
            # print('score', score)
            # print('convergence', convergence)
            if score >= convergence:
                # print('HERE>>>', normalized_tokens[i])
                group_token = normalized_tokens.pop(i)
                group_token.convergence = score

                group_variants.append(group_token)

            group_value = sum((x.value for x in group_variants))
            group_value = group_value / float(len(group_variants))
            print('term', group_key.term)
            print('value', group_value)
            print('>>>> group_variants', group_variants)
            groups[group_key.term] = Token(
                term=group_key.term,
                value=group_value
            )


    return groups


def where(
        tokens: Iterator[Token],
        attribute: str,
        operator: str,
        criterion: float,
        orderby: str,
        reverse: bool = True,
) -> List[Token]:
    if operator not in ['ge', 'gt', 'le', 'lt', 'eq', 'ne']:
        raise ValueError('Operator not found')

    operator = '__{operator}__'.format(
        operator=operator
    )

    generator = (
        token for token in tokens
        if getattr(getattr(token, attribute), operator)(criterion)
    )

    return sorted(generator, key=attrgetter(orderby), reverse=reverse)


def normalize(tokens: Iterator[Token]) -> Iterator[Token]:
    print("~" * 50)
    print("normalize tokens:", tokens)
    max_score = max((token.value for token in tokens))
    # print("max_score", max_score)
    for token in tokens:
        print("token ", token)
        yield Token(
            term=token.term,
            value=token.value / max_score
        )
