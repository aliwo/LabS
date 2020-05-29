
-- 회원가입 term --
INSERT INTO terms(id, title, body) VALUES (1, '동의동의', '동의해');
INSERT INTO terms(id, title, body) VALUES (2, '의동의동', '정의동');

-- mbti 문제들 --
INSERT INTO mbti_questions(id, question, trait) VALUES (1, '집 밖에 나가 노는 것을 선호하시나요?', 'E');
INSERT INTO mbti_questions(id, question, trait) VALUES (2, '사교모임보다 혼자하는 비디오 게임이 즐거울 떄가 많나요?', 'I');
INSERT INTO mbti_questions(id, question, trait) VALUES (3, '창의적인 것 보다는 실용적인게 좋나요?', 'S');
INSERT INTO mbti_questions(id, question, trait) VALUES (4, '자주 공상에 빠져 주변 상황을 잊어버리곤 하나요?', 'N');
INSERT INTO mbti_questions(id, question, trait) VALUES (5, '결정을 내릴때 다른사람의 감정이나 상황보다
이론이나 사실이 중요한가요?', 'T');
INSERT INTO mbti_questions(id, question, trait) VALUES (6, '다른 사람에게 싫은 소리 하기를 어려워 하나요?', 'F');
INSERT INTO mbti_questions(id, question, trait) VALUES (7, '업무를 유연하게 하기보다는 미리 계획해서
실행하는 편인가요?', 'J');
INSERT INTO mbti_questions(id, question, trait) VALUES (8, '여행 계획을 구체적으로 짜기 보다는 상황에 맞춰서 여행하는 편 인가요?', 'P');

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
























