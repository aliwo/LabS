import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from match.gen_preference_matches import gen_preference_matches
from match.gen_sy_matches import gen_sy_matches
# TODO: 랜덤 매칭도 추가하기

def gen_all():
    gen_sy_matches()
    gen_preference_matches()


