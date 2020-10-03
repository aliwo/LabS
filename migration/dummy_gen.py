
mbtis = [
    {'id':1,  'mbti':  'ESFJ'},
     {'id':2,  'mbti':  'ESTJ'},
      {'id':3,  'mbti':  'ESFP'},
       {'id':4,  'mbti':  'ESTP'},
        {'id':5,  'mbti':  'ISFJ'},
         {'id':6,  'mbti':  'ISTJ'},
          {'id':7,  'mbti':  'ISFP'},
           {'id':8,  'mbti':  'ISTP'},
            {'id':9,  'mbti':  'ENFJ'},
             {'id':10,  'mbti':  'ENTJ'},
              {'id':11,  'mbti':  'ENFP'},
               {'id':12,  'mbti':  'ENTP'},
                {'id':13,  'mbti':  'INFJ'},
                 {'id':14,  'mbti':  'INTJ'},
                  {'id':15,  'mbti':  'INFP'},
                   {'id':16,  'mbti':  'INTP'}
]

locations = ['서울', '경기북부', '경기남부', '경기동부', '경기서부']


# with open('dummy.sql', 'w+') as file:
#     file.write('a')

for elem in mbtis:
    for i, w in enumerate([1,3,5,7,9]):
        print(f"INSERT INTO users(nick_name, registration_confirmed, registration_confirmed_at, registration_phase, "
              f"animal_id, sex, rate,  el_time, location1, location2) "
              f"VALUES ('여_{elem['mbti']}_rate{w}', 1, NOW(), 'done', {elem['id']}, {0}, {w}, NOW(), '{locations[elem['id'] % 4]}', '{locations[(elem['id'] % 4) + 1]}');")


    for i, m in enumerate([1,3,5,7,9]):
        print(f"INSERT INTO users(nick_name, registration_confirmed, registration_confirmed_at, registration_phase, "
              f"animal_id, sex, rate,  el_time, location1, location2) "
              f"VALUES ('남_{elem['mbti']}_rate_{m}', 1, NOW(), 'done', {elem['id']}, {1}, {m}, NOW(), '{locations[elem['id'] % 4]}', '{locations[(elem['id'] % 4) + 1]}');")


