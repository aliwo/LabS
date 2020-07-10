from match.rolling_match import rolling_match
from api.models.match import Match


def gen_sy_matches():
    rolling_match('gen_sy_query', Match.TYPE_SOYEON)
