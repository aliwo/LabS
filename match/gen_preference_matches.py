from match.rolling_match import rolling_match
from api.models.match import Match


def gen_preference_matches():
    rolling_match('gen_preference_query', Match.TYPE_PREFER)


if __name__ == '__main__':
    gen_preference_matches()

