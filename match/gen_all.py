import sys
import os

from match.gen_random_match import gen_random_matches

sys.path.insert(0, os.path.abspath('.'))

from match.gen_preference_matches import gen_preference_matches
from match.gen_sy_matches import gen_sy_matches


def gen_all():
    gen_sy_matches()
    gen_preference_matches()
    gen_random_matches()

if __name__ == '__main__':
    gen_all()

