from match.rolling_match import rolling_match
from api.models.match import Match


def gen_random_matches():
    rolling_match('gen_random_query', Match.TYPE_RANDOM)


if __name__ == '__main__':
    gen_random_matches()

