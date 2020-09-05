import sys
import os
sys.path.insert(0, os.path.abspath('.')) # 현재 디렉터리가 Labs (루트)인 상태에서 실행하기 때문에 . 을 sys.path 에 추가
from match.gen_preference_matches import gen_preference_matches
from match.gen_sy_matches import gen_sy_matches
from match.gen_random_match import gen_random_matches


def gen_all():
    gen_sy_matches()
    gen_preference_matches()
    gen_random_matches()

if __name__ == '__main__':
    gen_all()

