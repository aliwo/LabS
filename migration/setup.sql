
-- 회원가입 term --
INSERT INTO terms(id, title, body) VALUES (1, '동의동의', '동의해');
INSERT INTO terms(id, title, body) VALUES (2, '의동의동', '정의동');

-- mbti 문제들 --
INSERT INTO production.mbti_questions (id, question, trait) VALUES (1, '나는 누군가와 친해질때 먼저 다가가는 편이다.', 'E');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (2, '나는 토론이나 회의에서 다른 사람의 감정과 관계를 고려하기보다는 맞다고 생각하는 의견을 주장하는 편이다', 'T');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (3, '나는 유명한 맛집 리스트를 알고 있고 다른 사람이 우리동네 맛집을 물어보면 바로 대답할 수 있다', 'S');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (4, '돌발상황에서 나는 나는 순발력있게 대처를 하는 편이다.', 'P');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (5, '나는 모임에 있을때보다 혼자 시간을 보낼때 에너지가 차오르며 편안함을 느낀다.', 'I');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (6, '일을할때 나는 서류작업 보다 독창적인 아이디어를 내는 일을 선호한다.', 'N');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (7, '연인을 찾을때 나는 지적인 대화보단 감정 표현방식이나 정서적 교류를 중요하게 보는 편이다.', 'F');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (8, '나는 일을 할때엔 하나의 일이 끝날때까진 한가지일을 하는것을 선호한다.', 'J');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (9, '데이트할때 주로 듣는 편이며 편안하다 느낄때 말문이 트이는 편이다.', 'I');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (10, '나는 편한 지인들과 일상이야기보다 예술이나 과학적인 이야기또는 이상에대해 이야기하는것을 좋아한다.', 'N');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (11, '다른 사람의 감정적요구보다 논리적인 헛점을 잘 캐치한다', 'T');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (12, '여행을 갈때엔 숙박할 곳 이동시간 교통편 미리 계획을 짜는 것을 선호한다 계획이 없다면 불안해진다.', 'J');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (13, '나는 내 논리가 반박 당했을 때보다 나의 감정이 존중되지 않는다 느꼈을때 화가 나는 편이다.', 'F');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (14, '나는 데이트할때 사람들이 많은 장소나 모임에서 즐기는것을 선호한다.', 'E');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (15, '나는 이론적인 지식보다 다른 사람의 경험을 더 우선시한다', 'S');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (16, '누군가와 관계가 깨졌을때 상처로 느껴지긴 하지만 마음을 정하면 빠른시일내 그사람을 정리할수있다.', 'T');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (17, '사교모임에서 시간이 지날수록 에너지를 얻으며 참석하면 가장 오래 남는 경향이 있다.', 'E');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (18, '상대와의 대화가 지루할때 혼자만의 생각에 빠져들곤 한다.', 'N');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (19, '나를 아는 사람들은 논리적이고 솔직하다 말하곤 한다.', 'T');
INSERT INTO production.mbti_questions (id, question, trait) VALUES (20, '일상이나 어떤 일을 하든 항상 순서가 정해져있는게 편하다', 'J');
-- 동물들 --
INSERT INTO animals(id, mbti, prefix, name) VALUES (1, 'ESFJ', '사교적인 여왕', '공작새');
INSERT INTO animals(id, mbti, prefix, name) VALUES (2, 'ESTJ', '무리를 이끄는 우두머리', '늑대');
INSERT INTO animals(id, mbti, prefix, name) VALUES (3, 'ESFP', '애교 넘치는', '강아지');
INSERT INTO animals(id, mbti, prefix, name) VALUES (4, 'ESTP', '만능 엔터테이너', '원숭이');

INSERT INTO animals(id, mbti, prefix, name) VALUES (5, 'ISFJ',  '배려심 가득한 간호사', '사슴');
INSERT INTO animals(id, mbti, prefix, name) VALUES (6, 'ISTJ',  '질서를 쌓는 반장', '비버');
INSERT INTO animals(id, mbti, prefix, name) VALUES (7, 'ISFP',  '포근한 귀염둥이', '코알라');
INSERT INTO animals(id, mbti, prefix, name) VALUES (8, 'ISTP',  '센스있는 해결사', '고양이');

INSERT INTO animals(id, mbti, prefix, name) VALUES (9, 'ENFJ',  '발랄한 응원단장', '팔색조');
INSERT INTO animals(id, mbti, prefix, name) VALUES (10, 'ENTJ', '카리스마를 지닌 대장', '독수리');
INSERT INTO animals(id, mbti, prefix, name) VALUES (11, 'ENFP', '노래부르는 핑크', '돌고래');
INSERT INTO animals(id, mbti, prefix, name) VALUES (12, 'ENTP', '창의력 넘치는 발명가', '라쿤');

INSERT INTO animals(id, mbti, prefix, name) VALUES (13, 'INFJ', '기품있는 사색가', '유니콘');
INSERT INTO animals(id, mbti, prefix, name) VALUES (14, 'INTJ', '인텔리한 전문가', '도베르만');
INSERT INTO animals(id, mbti, prefix, name) VALUES (15, 'INFP', '별을세는 예술가', '햄스터');
INSERT INTO animals(id, mbti, prefix, name) VALUES (16, 'INTP', '호기심 많은 인텔리', '올빼미');

-- mbti indicator --
INSERT INTO mbti_indicators(id, synonym, description) VALUES(1, 'II'	,'비슷한 내향적 에너지를 가지고 있어, 편안한 만남이 될수있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(2, 'IE'	,'서로 다른 에너지를 가지고 있어, 서로에게 좋은 자극이 될수있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(3, 'EE'	,'비슷한 외향적 에너지를 가지고 있어, 에너지 넘치는 즐거운 만남이 될수있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(4, 'NN'	,'서로의 철학적인 사고에 귀기울일 수 있는, 깊은 내면을 가지고 있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(5, 'NS'	,'다른 내면을 가지고 있어 서로의 생각에 귀를 기울인다면, 서로에게 발전이 있는 좋은 보완관계가 될수있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(6, 'SS'	,'비슷한 현실적인 사고를 가지고 있어, 편안한 만남이 될 수 있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(7, 'FF'	,'공감능력이 좋아 따뜻한 공감대를 잘 형성할 수 있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(8, 'TF'	,'서로 다른 공감 포인트를 이해하고 노력한다면, 서로에게 발전이 있는 좋은 보완관계가 될수있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(9, 'TT'	,'이성적이고 논리적인 공감대를 가지고 있어, 공감대를 잘 형성할 수 있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(10, 'PP'	,'비슷한 여유롭고 관용적인 생활방식을 가지고 있어 편안한 관계가 될 수 있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(11, 'PJ'	,'서로 다른 생활방식을 가지고 있어 이해하고 노력한다면, 서로에게 발전이 있는 좋은 보완관계가 될수있습니다');
INSERT INTO mbti_indicators(id, synonym, description) VALUES(12, 'JJ'	,'비슷한 철저하고 계획적인 생활방식을 가지고 있어 편안한 관계가 될 수 있습니다');






















