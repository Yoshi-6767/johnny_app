# ═══════════════════════════════════════════════
# ГРАММАТИКА — УРОКИ (полная версия)
# ═══════════════════════════════════════════════

GRAMMAR_LESSONS = [
    # ═══════════════════════════════════════════
    # УРОК 1 — PRESENT SIMPLE
    # ═══════════════════════════════════════════
    {
        "id": "present_simple",
        "title": "Present Simple",
        "emoji": "🕐",
        "level": "A1-A2",
        "intro": "Простое настоящее время — самое базовое в английском. Используется для фактов, привычек и повторяющихся действий.",
        "why": "Present Simple — это «фундамент» английского. Без него не обходится ни один разговор: ты рассказываешь о себе, о работе, о том, что любишь, что делаешь каждый день. Если ты не освоишь Present Simple, дальше двигаться будет очень сложно. Он используется в 30-40% всех предложений на английском. Изучи его как следует — и половина языка будет у тебя в кармане.",

        "rules": [
            {"h": "Когда использовать", "text": "1) Факты: I live in Russia. The Earth is round. 2) Привычки: I wake up at 7 every day. 3) Расписания: The train leaves at 9. 4) Постоянные состояния: She works in a bank."},
            {"h": "Как образуется (утверждение)", "text": "Для I / you / we / they — глагол в базовой форме: I work, you play, we study, they live. Для he / she / it — добавляем -s или -es: he works, she plays, it goes. Правило: 3-е лицо единственное число — всегда с окончанием."},
            {"h": "Правило -s / -es", "text": "Обычно просто -s: work → works. Если глагол кончается на -s, -sh, -ch, -x, -o: добавляем -es (go → goes, watch → watches, finish → finishes). Если кончается на согласную + y: y меняется на i + es (study → studies, fly → flies)."},
            {"h": "Отрицание", "text": "Для I / you / we / they — do not (don't) + глагол: I don't work, you don't play. Для he / she / it — does not (doesn't) + глагол в базовой форме: he doesn't work, she doesn't play. ВАЖНО: после doesn't глагол БЕЗ -s: не 'he doesn't works', а 'he doesn't work'."},
            {"h": "Вопрос", "text": "Do / Does + подлежащее + глагол: Do you work? Does he work? Ответы: Yes, I do. No, I don't. Yes, he does. No, he doesn't."},
            {"h": "Маркеры времени", "text": "always (всегда), usually (обычно), often (часто), sometimes (иногда), rarely (редко), never (никогда), every day / week / month (каждый день / неделю / месяц), on Mondays (по понедельникам)."},
            {"h": "Порядок слов", "text": "Прямой порядок: подлежащее + глагол + дополнение. I like coffee. She reads books. НЕ наоборот! В английском фиксированный порядок слов — в отличие от русского."},
            {"h": "Наречия частоты", "text": "always, usually, often, sometimes, rarely, never — стоят ПЕРЕД смысловым глаголом, но ПОСЛЕ глагола to be: I always drink coffee. She is never late. НЕ 'I drink always coffee'."}
        ],

        "tables": [
            {
                "title": "Спряжение глагола work",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "work", "don't work", "Do I work?"],
                    ["You", "work", "don't work", "Do you work?"],
                    ["He", "works", "doesn't work", "Does he work?"],
                    ["She", "works", "doesn't work", "Does she work?"],
                    ["It", "works", "doesn't work", "Does it work?"],
                    ["We", "work", "don't work", "Do we work?"],
                    ["They", "work", "don't work", "Do they work?"]
                ]
            },
            {
                "title": "Правило -s / -es в 3-м лице",
                "headers": ["Окончание глагола", "Что делаем", "Пример"],
                "rows": [
                    ["Любой", "Просто + s", "work → works"],
                    ["-s, -sh, -ch, -x, -o", "+ es", "go → goes, watch → watches"],
                    ["согласная + y", "y → i + es", "study → studies"],
                    ["гласная + y", "+ s", "play → plays"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "He go to school every day.", "right": "He goes to school every day.", "why": "3-е лицо единственное — обязательно -es/-s"},
            {"wrong": "She doesn't likes coffee.", "right": "She doesn't like coffee.", "why": "После doesn't глагол в базовой форме (без -s)"},
            {"wrong": "Does he works here?", "right": "Does he work here?", "why": "После does глагол без -s"},
            {"wrong": "I no like football.", "right": "I don't like football.", "why": "Отрицание через don't, а не через no"},
            {"wrong": "She always is late.", "right": "She is always late.", "why": "Наречие always идёт после is/am/are"},
            {"wrong": "I drink always coffee.", "right": "I always drink coffee.", "why": "Наречие always перед смысловым глаголом"}
        ],

        "lifehacks": [
            "Запомни: он/она/оно — всегда с 's' на конце глагола. Как будто ты уважаешь его и добавляешь ему 's'.",
            "Правило третьего лица: he/she/it → работает только с глаголом -s. Это как зарплата — он получает своё 's'.",
            "В отрицании и вопросе всегда используешь базовый глагол — do/does 'забирают' на себя роль 'главного'.",
            "Если сомневаешься — подставь 'does' и посмотри: после него всегда БЕЗ -s."
        ],

        "text": {
            "title": "My Daily Routine",
            "paragraphs": [
                "My name is Alex. I am a student. Every morning I wake up at 7 o'clock. I wash my face and have breakfast. I usually eat eggs and drink coffee. Then I go to university. I study computer science.",
                "In the evening I come home at 6 pm. I have dinner with my family. We often talk about our day. After dinner I read books or watch films. Sometimes I play computer games with my friends.",
                "I go to bed at 11 pm. I always sleep eight hours. On weekends I don't wake up early. I relax and spend time with my family. I love my routine."
            ]
        },

        "text_questions": [
            {"q": "What time does Alex wake up?", "options": ["At 6 o'clock", "At 7 o'clock", "At 8 o'clock", "At 9 o'clock"], "correct": "At 7 o'clock"},
            {"q": "What does Alex eat for breakfast?", "options": ["Pizza and juice", "Eggs and coffee", "Soup and tea", "Fruit and water"], "correct": "Eggs and coffee"},
            {"q": "What does Alex study?", "options": ["Medicine", "Computer science", "Art", "History"], "correct": "Computer science"},
            {"q": "What time does Alex come home?", "options": ["At 5 pm", "At 6 pm", "At 7 pm", "At 8 pm"], "correct": "At 6 pm"},
            {"q": "What does Alex do after dinner?", "options": ["Goes to work", "Reads books or watches films", "Plays football", "Studies languages"], "correct": "Reads books or watches films"},
            {"q": "What time does Alex go to bed?", "options": ["At 9 pm", "At 10 pm", "At 11 pm", "At 12 pm"], "correct": "At 11 pm"},
            {"q": "How many hours does Alex sleep?", "options": ["Six hours", "Seven hours", "Eight hours", "Nine hours"], "correct": "Eight hours"},
            {"q": "What does Alex do on weekends?", "options": ["Works hard", "Relaxes and spends time with family", "Studies at university", "Travels alone"], "correct": "Relaxes and spends time with family"}
        ],

        "test": [
            {"type": "choice", "q": "She ___ to school every day.", "options": ["go", "goes", "going", "went"], "correct": "goes"},
            {"type": "choice", "q": "They ___ like coffee.", "options": ["doesn't", "don't", "isn't", "aren't"], "correct": "don't"},
            {"type": "choice", "q": "___ he work here?", "options": ["Do", "Does", "Is", "Are"], "correct": "Does"},
            {"type": "choice", "q": "I ___ football every Sunday.", "options": ["play", "plays", "playing", "played"], "correct": "play"},
            {"type": "choice", "q": "My sister ___ French very well.", "options": ["speak", "speaks", "speaking", "spoke"], "correct": "speaks"},
            {"type": "fill", "q": "I ___ (work) in a bank.", "answer": "work"},
            {"type": "fill", "q": "He ___ (play) guitar.", "answer": "plays"},
            {"type": "fill", "q": "We ___ (not / like) rainy weather.", "answer": "don't like"},
            {"type": "fill", "q": "___ you ___ (speak) English?", "answer": "Do speak"},
            {"type": "error", "q": "Найди ошибку в предложении:", "options": ["He go to school", "He goes to school", "He is go to school", "He going to school"], "correct": "He goes to school"},
            {"type": "error", "q": "Найди ошибку в предложении:", "options": ["She doesn't likes coffee", "She doesn't like coffee", "She not like coffee", "She no like coffee"], "correct": "She doesn't like coffee"},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["Does he works here?", "Does he work here?", "Do he work here?", "Is he work here?"], "correct": "Does he work here?"},
            {"type": "translate", "q": "Переведи на английский: Я живу в Москве.", "answer": "I live in Moscow"},
            {"type": "translate", "q": "Переведи на английский: Она любит кофе.", "answer": "She likes coffee"},
            {"type": "translate", "q": "Переведи на английский: Они не говорят по-английски.", "answer": "They don't speak English"},
            {"type": "translate", "q": "Переведи на английский: Ты играешь в футбол?", "answer": "Do you play football"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 2 — PAST SIMPLE
    # ═══════════════════════════════════════════
    {
        "id": "past_simple",
        "title": "Past Simple",
        "emoji": "⏪",
        "level": "A1-A2",
        "intro": "Простое прошедшее время. Для действий, которые произошли и закончились в прошлом.",
        "why": "Past Simple — второе по важности время после Present Simple. Без него ты не сможешь рассказать, что делал вчера, на выходных, в прошлом году. Это время для историй, воспоминаний, отчётов. В английском есть точные временные маркеры (yesterday, last week, 2 hours ago) — если видишь их, сразу используй Past Simple.",

        "rules": [
            {"h": "Когда использовать", "text": "Когда действие произошло и закончилось в прошлом. Указывается конкретное время: yesterday, last week, 2 hours ago, in 2020, on Monday. Если ты можешь ответить на вопрос «когда?» — это Past Simple."},
            {"h": "Правильные глаголы", "text": "Добавляем -ed к базовой форме: work → worked, play → played, watch → watched, finish → finished. Работает для большинства глаголов."},
            {"h": "Правило -ed", "text": "Обычно + ed: work → worked. Если кончается на -e: + d (live → lived). Если кончается на согласную + y: y → i + ed (study → studied). Если короткий слог и ударение на него: удваиваем согласную (stop → stopped)."},
            {"h": "Неправильные глаголы", "text": "Их надо запомнить. Топ-10: go → went, see → saw, have → had, do → did, come → came, get → got, make → made, take → took, give → gave, say → said. Все — в разделе «Неправильные глаголы»."},
            {"h": "Отрицание", "text": "did not (didn't) + глагол в базовой форме: I didn't work, he didn't go. ВАЖНО: после didn't — глагол в НАЧАЛЬНОЙ форме, даже для неправильных: I didn't go (не 'went'), she didn't see (не 'saw')."},
            {"h": "Вопрос", "text": "Did + подлежащее + глагол: Did you work? Did he go? Ответы: Yes, I did. No, I didn't."},
            {"h": "Глагол to be в Past Simple", "text": "I / he / she / it → was. You / we / they → were. I was at home. They were happy. Отрицание: wasn't / weren't. Вопрос: Was he...? Were they...?"},
            {"h": "Маркеры времени", "text": "yesterday (вчера), last week / month / year (на прошлой неделе / в прошлом месяце / году), 2 days ago (2 дня назад), in 2020 (в 2020), when I was a child (когда я был ребёнком), on Monday (в понедельник)"}
        ],

        "tables": [
            {
                "title": "Спряжение work (правильный глагол)",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "worked", "didn't work", "Did I work?"],
                    ["You", "worked", "didn't work", "Did you work?"],
                    ["He", "worked", "didn't work", "Did he work?"],
                    ["She", "worked", "didn't work", "Did she work?"],
                    ["We", "worked", "didn't work", "Did we work?"],
                    ["They", "worked", "didn't work", "Did they work?"]
                ]
            },
            {
                "title": "Глагол to be в Past Simple",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "was", "wasn't", "Was I...?"],
                    ["He / She / It", "was", "wasn't", "Was he...?"],
                    ["You", "were", "weren't", "Were you...?"],
                    ["We / They", "were", "weren't", "Were they...?"]
                ]
            },
            {
                "title": "Топ-10 неправильных глаголов",
                "headers": ["Base", "Past", "Перевод"],
                "rows": [
                    ["go", "went", "идти"],
                    ["see", "saw", "видеть"],
                    ["have", "had", "иметь"],
                    ["do", "did", "делать"],
                    ["come", "came", "приходить"],
                    ["get", "got", "получать"],
                    ["make", "made", "делать"],
                    ["take", "took", "брать"],
                    ["give", "gave", "давать"],
                    ["say", "said", "говорить"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I didn't went to school.", "right": "I didn't go to school.", "why": "После didn't — глагол в базовой форме"},
            {"wrong": "Did you saw him?", "right": "Did you see him?", "why": "После did — глагол в базовой форме"},
            {"wrong": "I goed to the cinema.", "right": "I went to the cinema.", "why": "go — неправильный глагол, форма went"},
            {"wrong": "She was go to work.", "right": "She went to work.", "why": "Нельзя два глагола — либо was, либо went"},
            {"wrong": "They was happy.", "right": "They were happy.", "why": "They — множественное число → were"},
            {"wrong": "I did went home.", "right": "I went home.", "why": "did не используется в утверждении"}
        ],

        "lifehacks": [
            "Видишь yesterday, last week, 2 days ago — сразу Past Simple, даже не думай.",
            "Правило одной 't': did / didn't — глагол после них в начальной форме. Всегда.",
            "was — для одного (I, he, she, it). were — для многих (you, we, they). 'Мы были' = we were.",
            "Правильные глаголы на -ed — это 70% всех английских глаголов. Если не уверен — просто добавь -ed, скорее всего угадаешь."
        ],

        "text": {
            "title": "My Last Weekend",
            "paragraphs": [
                "Last weekend I had a great time. On Saturday morning I woke up late, at 10 o'clock. I made a big breakfast with eggs and bacon. Then I called my friend Tom. We decided to go to the cinema.",
                "We watched a new action film. The film was amazing. After the cinema we went to a café and talked for two hours. We drank coffee and ate cake. I got home at 8 pm.",
                "On Sunday I didn't go anywhere. I stayed at home and relaxed. I read a book and watched TV. In the evening I cooked dinner for my family. We were all together. It was a perfect weekend."
            ]
        },

        "text_questions": [
            {"q": "What time did the person wake up on Saturday?", "options": ["At 8 o'clock", "At 9 o'clock", "At 10 o'clock", "At 11 o'clock"], "correct": "At 10 o'clock"},
            {"q": "What did the person make for breakfast?", "options": ["Pizza and juice", "Eggs and bacon", "Soup and tea", "Salad and water"], "correct": "Eggs and bacon"},
            {"q": "Where did they go after the cinema?", "options": ["To the park", "To a café", "To the gym", "To a museum"], "correct": "To a café"},
            {"q": "What film did they watch?", "options": ["A comedy", "A new action film", "A drama", "A horror film"], "correct": "A new action film"},
            {"q": "What time did the person get home?", "options": ["At 6 pm", "At 7 pm", "At 8 pm", "At 9 pm"], "correct": "At 8 pm"},
            {"q": "What did the person do on Sunday?", "options": ["Went to work", "Stayed at home and relaxed", "Went to a friend's house", "Traveled"], "correct": "Stayed at home and relaxed"},
            {"q": "What did the person cook in the evening?", "options": ["Breakfast", "Lunch", "Dinner", "Nothing"], "correct": "Dinner"},
            {"q": "How was the weekend?", "options": ["Boring", "Perfect", "Terrible", "Long"], "correct": "Perfect"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ to school yesterday.", "options": ["go", "goes", "went", "gone"], "correct": "went"},
            {"type": "choice", "q": "She ___ the film last week.", "options": ["see", "saw", "seen", "sees"], "correct": "saw"},
            {"type": "choice", "q": "We ___ go to the party.", "options": ["doesn't", "don't", "didn't", "aren't"], "correct": "didn't"},
            {"type": "choice", "q": "___ you call me yesterday?", "options": ["Do", "Does", "Did", "Are"], "correct": "Did"},
            {"type": "choice", "q": "They ___ at home yesterday.", "options": ["was", "were", "are", "is"], "correct": "were"},
            {"type": "choice", "q": "I ___ very tired last night.", "options": ["was", "were", "am", "is"], "correct": "was"},
            {"type": "fill", "q": "He ___ (play) football yesterday.", "answer": "played"},
            {"type": "fill", "q": "Did you ___ (see) him?", "answer": "see"},
            {"type": "fill", "q": "I ___ (not / go) to the party.", "answer": "didn't go"},
            {"type": "fill", "q": "She ___ (be) at home yesterday.", "answer": "was"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I goed to school", "I went to school", "I go to school yesterday", "I going to school"], "correct": "I went to school"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I didn't went home", "I didn't go home", "I not went home", "I no go home"], "correct": "I didn't go home"},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["Did you saw him?", "Did you see him?", "Do you saw him?", "Are you see him?"], "correct": "Did you see him?"},
            {"type": "translate", "q": "Переведи: Я был дома вчера.", "answer": "I was at home yesterday"},
            {"type": "translate", "q": "Переведи: Она не пришла на вечеринку.", "answer": "She didn't come to the party"},
            {"type": "translate", "q": "Переведи: Ты смотрел фильм?", "answer": "Did you watch the film"},
            {"type": "translate", "q": "Переведи: Мы играли в футбол вчера.", "answer": "We played football yesterday"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 3 — PRESENT CONTINUOUS
    # ═══════════════════════════════════════════
    {
        "id": "present_continuous",
        "title": "Present Continuous",
        "emoji": "🎬",
        "level": "A1-A2",
        "intro": "Настоящее длительное. Для действий, которые происходят прямо сейчас или в этот период.",
        "why": "Present Continuous описывает то, что происходит в момент речи: 'Я сейчас читаю', 'Он сейчас работает'. Это время добавляет динамику в язык. Оно также используется для временных ситуаций ('Я живу у друга эту неделю') и запланированного будущего ('Я встречаюсь с ним завтра'). Если в предложении есть 'now', 'at the moment', 'look!', 'listen!' — это Present Continuous.",

        "rules": [
            {"h": "Когда использовать", "text": "1) Действие прямо сейчас: I am reading a book (сейчас). 2) Временная ситуация: I am living in Moscow this month. 3) Запланированное будущее: I am meeting him tomorrow. 4) Изменения/тренды: The climate is getting warmer."},
            {"h": "Как образуется", "text": "am / is / are + глагол с -ing. I am working. She is reading. They are playing. Без глагола to be (am/is/are) конструкция не работает."},
            {"h": "Правило -ing", "text": "Обычно + ing: work → working, play → playing. Если кончается на -e: убираем e + ing (write → writing, make → making). Если короткий слог и ударение: удваиваем согласную (run → running, sit → sitting). Если на -ie: ie → y + ing (die → dying, lie → lying)."},
            {"h": "Отрицание", "text": "am not / isn't / aren't + глагол-ing: I am not working, he isn't reading, they aren't playing."},
            {"h": "Вопрос", "text": "Am / Is / Are + подлежащее + глагол-ing: Are you working? Is she reading? Ответы: Yes, I am. No, I'm not. Yes, she is. No, she isn't."},
            {"h": "Глаголы-исключения", "text": "Некоторые глаголы НЕ используются в Continuous: like, love, hate, want, need, know, understand, believe, remember. Они обозначают состояние, а не действие. НЕ 'I am knowing', а 'I know'."},
            {"h": "Разница с Present Simple", "text": "Simple — привычка (I work every day). Continuous — прямо сейчас (I am working now). Маркеры: Simple — always, usually, every day. Continuous — now, at the moment, look!, listen!."},
            {"h": "Маркеры времени", "text": "now (сейчас), right now (прямо сейчас), at the moment (в данный момент), today (сегодня), this week / month (на этой неделе / в этом месяце), look! (смотри!), listen! (слушай!)"}
        ],

        "tables": [
            {
                "title": "Спряжение work (Present Continuous)",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "am working", "am not working", "Am I working?"],
                    ["You", "are working", "aren't working", "Are you working?"],
                    ["He", "is working", "isn't working", "Is he working?"],
                    ["She", "is working", "isn't working", "Is she working?"],
                    ["We", "are working", "aren't working", "Are we working?"],
                    ["They", "are working", "aren't working", "Are they working?"]
                ]
            },
            {
                "title": "Правило -ing",
                "headers": ["Окончание", "Что делаем", "Пример"],
                "rows": [
                    ["Обычный", "+ ing", "work → working"],
                    ["-e", "Убираем e + ing", "write → writing"],
                    ["1 слог + согласная", "Удваиваем + ing", "run → running"],
                    ["-ie", "ie → y + ing", "die → dying"]
                ]
            },
            {
                "title": "Present Simple vs Present Continuous",
                "headers": ["Аспект", "Present Simple", "Present Continuous"],
                "rows": [
                    ["Когда", "Привычка, факт", "Сейчас, в моменте"],
                    ["Маркеры", "always, usually, every day", "now, at the moment, look!"],
                    ["Пример", "I work every day.", "I am working now."]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I working now.", "right": "I am working now.", "why": "Нужен am/is/are перед -ing"},
            {"wrong": "She is work now.", "right": "She is working now.", "why": "После is глагол в -ing"},
            {"wrong": "I am knowing him.", "right": "I know him.", "why": "Know — глагол состояния, не используется в Continuous"},
            {"wrong": "He is runing.", "right": "He is running.", "why": "Удвоение согласной: run → running"},
            {"wrong": "They are play football.", "right": "They are playing football.", "why": "Глагол должен быть в -ing"},
            {"wrong": "I am like pizza.", "right": "I like pizza.", "why": "Like — состояние, не действие"}
        ],

        "lifehacks": [
            "Видишь 'now', 'look!', 'listen!' — сразу Continuous.",
            "am / is / are — это 'клей' между подлежащим и -ing. Без него не работает.",
            "Глаголы чувств (like, love, hate) и мысли (know, think) — НИКОГДА не в Continuous.",
            "Одна 'e' в конце → меняется на -ing без неё: write → writing."
        ],

        "text": {
            "title": "A Busy Day at Home",
            "paragraphs": [
                "It's Saturday morning. The whole family is at home. Mum is cooking breakfast in the kitchen. She is making pancakes. Dad is reading a newspaper in the living room.",
                "My brother Tom is playing computer games in his room. He is winning right now. My little sister Ann is drawing a picture at the table. She is using her new pencils.",
                "And me? I am sitting on the sofa and writing this text. I am drinking tea and listening to music. Our cat is sleeping near the window. It is a perfect lazy Saturday!"
            ]
        },

        "text_questions": [
            {"q": "What is Mum doing?", "options": ["Reading", "Cooking breakfast", "Sleeping", "Working"], "correct": "Cooking breakfast"},
            {"q": "What is Dad doing?", "options": ["Cooking", "Reading a newspaper", "Playing games", "Drawing"], "correct": "Reading a newspaper"},
            {"q": "What is Tom playing?", "options": ["Football", "Computer games", "Chess", "Cards"], "correct": "Computer games"},
            {"q": "What is Ann drawing?", "options": ["A cat", "A picture", "A house", "A car"], "correct": "A picture"},
            {"q": "Where is Ann drawing?", "options": ["In her room", "At the table", "In the garden", "On the sofa"], "correct": "At the table"},
            {"q": "What is the author drinking?", "options": ["Coffee", "Juice", "Tea", "Water"], "correct": "Tea"},
            {"q": "Where is the cat?", "options": ["In the kitchen", "Near the window", "On the bed", "Outside"], "correct": "Near the window"},
            {"q": "What kind of day is it?", "options": ["Busy", "Perfect lazy Saturday", "Stressful", "Boring"], "correct": "Perfect lazy Saturday"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ reading a book now.", "options": ["am", "is", "are", "be"], "correct": "am"},
            {"type": "choice", "q": "She ___ cooking dinner.", "options": ["am", "is", "are", "be"], "correct": "is"},
            {"type": "choice", "q": "They ___ playing football.", "options": ["am not", "isn't", "aren't", "don't"], "correct": "aren't"},
            {"type": "choice", "q": "Look! He ___ (run).", "options": ["runs", "is running", "run", "running"], "correct": "is running"},
            {"type": "choice", "q": "Listen! She ___ a song.", "options": ["sings", "sing", "is singing", "sang"], "correct": "is singing"},
            {"type": "choice", "q": "My mum ___ dinner right now.", "options": ["cooks", "cook", "is cooking", "cooked"], "correct": "is cooking"},
            {"type": "fill", "q": "Look! He ___ (run).", "answer": "is running"},
            {"type": "fill", "q": "We ___ (study) English now.", "answer": "are studying"},
            {"type": "fill", "q": "She ___ (not / sleep) — she is reading.", "answer": "isn't sleeping"},
            {"type": "fill", "q": "What ___ you ___ (do) right now?", "answer": "are doing"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I working now", "I am working now", "I is working now", "I be working now"], "correct": "I am working now"},
            {"type": "error", "q": "Найди ошибку:", "options": ["She is work now", "She is working now", "She working now", "She am working now"], "correct": "She is working now"},
            {"type": "error", "q": "Найди ошибку:", "options": ["He is runing", "He is running", "He runing", "He am running"], "correct": "He is running"},
            {"type": "translate", "q": "Переведи: Я сейчас читаю книгу.", "answer": "I am reading a book now"},
            {"type": "translate", "q": "Переведи: Она готовит ужин.", "answer": "She is cooking dinner"},
            {"type": "translate", "q": "Переведи: Они не смотрят телевизор.", "answer": "They aren't watching TV"},
            {"type": "translate", "q": "Переведи: Что ты делаешь сейчас?", "answer": "What are you doing now"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 4 — FUTURE SIMPLE
    # ═══════════════════════════════════════════
    {
        "id": "future_simple",
        "title": "Future Simple",
        "emoji": "🔮",
        "level": "A1-A2",
        "intro": "Простое будущее время. Для решений, предсказаний, обещаний и планов на будущее.",
        "why": "Future Simple — самое простое будущее время в английском. Оно используется для спонтанных решений («Ладно, я помогу тебе»), предсказаний («Будет дождь»), обещаний («Я позвоню») и планов, которые не очень конкретны. Если ты не уверен, какое будущее время использовать — Future Simple почти всегда сработает. Также оно часто используется с 'I think', 'I hope', 'probably'.",

        "rules": [
            {"h": "Когда использовать", "text": "1) Спонтанные решения: I'll help you! 2) Предсказания: It will rain tomorrow. 3) Обещания: I will call you. 4) Предложения: I'll open the window. 5) С 'I think / I hope': I think she will come."},
            {"h": "Как образуется", "text": "will + глагол в базовой форме для всех лиц: I will work, you will work, he will work, she will work, we will work, they will work. Форма 'will' одинакова для всех — никаких изменений!"},
            {"h": "Сокращения", "text": "I will = I'll. You will = you'll. He will = he'll. She will = she'll. We will = we'll. They will = they'll. Это стандарт в разговорной речи."},
            {"h": "Отрицание", "text": "will not (won't) + глагол: I won't work, he won't come. Сокращение won't — почти всегда используется."},
            {"h": "Вопрос", "text": "Will + подлежащее + глагол: Will you help me? Will it rain? Ответы: Yes, I will. No, I won't."},
            {"h": "Маркеры времени", "text": "tomorrow (завтра), next week / month / year (на следующей неделе / в следующем месяце / году), in 2030 (в 2030), soon (скоро), later (позже), in 2 hours (через 2 часа), tonight (сегодня вечером)"},
            {"h": "С 'I think / I hope / probably'", "text": "I think she will come. I hope it won't rain. He will probably be late. Эти фразы часто используются с Future Simple и показывают неуверенность."},
            {"h": "Разница с 'going to'", "text": "will — спонтанное решение (I'll make tea). 'be going to' — заранее спланированное (I'm going to visit my grandmother tomorrow). Если у тебя уже есть план — 'going to'. Если решил только что — will."}
        ],

        "tables": [
            {
                "title": "Спряжение work в Future Simple",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "will work", "won't work", "Will I work?"],
                    ["You", "will work", "won't work", "Will you work?"],
                    ["He", "will work", "won't work", "Will he work?"],
                    ["She", "will work", "won't work", "Will she work?"],
                    ["We", "will work", "won't work", "Will we work?"],
                    ["They", "will work", "won't work", "Will they work?"]
                ]
            },
            {
                "title": "will vs going to",
                "headers": ["will", "going to"],
                "rows": [
                    ["Спонтанное решение", "Заранее спланированное"],
                    ["I'll make coffee. (решил сейчас)", "I'm going to make coffee. (планировал)"],
                    ["Предсказание без оснований", "Предсказание с основанием"],
                    ["I think it will rain.", "Look at clouds! It's going to rain."]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I will to work tomorrow.", "right": "I will work tomorrow.", "why": "После will — глагол БЕЗ to"},
            {"wrong": "She wills come.", "right": "She will come.", "why": "will — одинаковый для всех лиц"},
            {"wrong": "I will can help you.", "right": "I will be able to help you.", "why": "Нельзя два модальных глагола"},
            {"wrong": "I will go in tomorrow.", "right": "I will go tomorrow.", "why": "С tomorrow не нужен 'in'"},
            {"wrong": "Will you to help me?", "right": "Will you help me?", "why": "После will — глагол БЕЗ to"},
            {"wrong": "I'll will go.", "right": "I'll go.", "why": "I'll = I will, нельзя удваивать"}
        ],

        "lifehacks": [
            "will — это 'стена'. Всегда одинаковый для всех. Запомни — никаких исключений.",
            "После will — глагол в БАЗОВОЙ форме. Всегда.",
            "Сокращение 'I'll' — твой друг. В разговоре так говорят 99% времени.",
            "Если сомневаешься между will и going to — для разговорного общения will всегда подойдёт."
        ],

        "text": {
            "title": "My Plans for Tomorrow",
            "paragraphs": [
                "Tomorrow will be a busy day for me. I will wake up at 7 o'clock. I will have a quick breakfast and then I will go to work. In the morning I will have an important meeting with my boss.",
                "At lunchtime I will meet my friend Mark. We will eat at a new Italian restaurant. I think the food will be delicious. After lunch I will go back to the office and finish my project.",
                "In the evening I will come home and relax. Maybe I will watch a film or read a book. My sister will call me, I hope. I will tell her about my day. Then I will go to bed early — tomorrow I need to be fresh!"
            ]
        },

        "text_questions": [
            {"q": "What time will the person wake up?", "options": ["At 6 o'clock", "At 7 o'clock", "At 8 o'clock", "At 9 o'clock"], "correct": "At 7 o'clock"},
            {"q": "Who will the person meet in the morning?", "options": ["His friend Mark", "His boss", "His mother", "His sister"], "correct": "His boss"},
            {"q": "Where will they eat lunch?", "options": ["At home", "At a new Italian restaurant", "At the office", "At a café"], "correct": "At a new Italian restaurant"},
            {"q": "What will they do after lunch?", "options": ["Go home", "Finish a project", "Watch a film", "Go shopping"], "correct": "Finish a project"},
            {"q": "What will the person do in the evening?", "options": ["Work more", "Relax and maybe watch a film", "Go to a party", "Travel"], "correct": "Relax and maybe watch a film"},
            {"q": "Who will call in the evening?", "options": ["Mark", "The boss", "His sister", "His mother"], "correct": "His sister"},
            {"q": "When will the person go to bed?", "options": ["Early", "Late", "At midnight", "At 9 pm"], "correct": "Early"},
            {"q": "Why will the person go to bed early?", "options": ["He is tired", "He needs to be fresh tomorrow", "He is sick", "His mum told him to"], "correct": "He needs to be fresh tomorrow"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ call you tomorrow.", "options": ["will", "am", "do", "did"], "correct": "will"},
            {"type": "choice", "q": "She ___ come to the party.", "options": ["will not", "doesn't", "isn't", "didn't"], "correct": "will not"},
            {"type": "choice", "q": "___ you help me?", "options": ["Will", "Do", "Are", "Did"], "correct": "Will"},
            {"type": "choice", "q": "I think it ___ rain tomorrow.", "options": ["will", "is", "does", "did"], "correct": "will"},
            {"type": "choice", "q": "He ___ arrive at 5 pm.", "options": ["will", "is", "does", "did"], "correct": "will"},
            {"type": "fill", "q": "It ___ (rain) tomorrow.", "answer": "will rain"},
            {"type": "fill", "q": "We ___ (go) to the cinema next week.", "answer": "will go"},
            {"type": "fill", "q": "She ___ (not / come) to the party.", "answer": "won't come"},
            {"type": "fill", "q": "___ you ___ (help) me?", "answer": "Will help"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I will to work", "I will work", "I wills work", "I will work to"], "correct": "I will work"},
            {"type": "error", "q": "Найди ошибку:", "options": ["She wills come", "She will come", "She will comes", "She will to come"], "correct": "She will come"},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["Will you to help me?", "Will you help me?", "Do you will help me?", "Are you will help me?"], "correct": "Will you help me?"},
            {"type": "translate", "q": "Переведи: Я позвоню тебе завтра.", "answer": "I will call you tomorrow"},
            {"type": "translate", "q": "Переведи: Она не придёт.", "answer": "She won't come"},
            {"type": "translate", "q": "Переведи: Ты мне поможешь?", "answer": "Will you help me"},
            {"type": "translate", "q": "Переведи: Будет дождь.", "answer": "It will rain"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 5 — АРТИКЛИ (A / AN / THE)
    # ═══════════════════════════════════════════
    {
        "id": "articles",
        "title": "Артикли (a / an / the)",
        "emoji": "🔤",
        "level": "A1-A2",
        "intro": "Артикли — самая сложная тема для русскоязычных. В русском их нет, поэтому нужно понять логику с нуля.",
        "why": "Артикли — это головная боль всех русскоязычных. В русском языке нет артиклей, поэтому 'a', 'an', 'the' кажутся ненужными. Но в английском они несут смысл: 'a' = какой-то один (неважно какой), 'the' = конкретный (тот самый). Если ты не используешь артикли, тебя поймут, но звучать это будет как речь иностранца. С артиклями ты будешь звучать естественно. Изучи это один раз — и пользуйся всю жизнь.",

        "rules": [
            {"h": "a / an — неопределённый артикль", "text": "Используется с ИСЧИСЛЯЕМЫМИ существительными в ЕДИНСТВЕННОМ числе, когда предмет упоминается ВПЕРВЫЕ. a + согласная: a book, a car, a university (звук 'ю'). an + гласная: an apple, an egg, an hour (звук гласный, потому что 'h' не читается)."},
            {"h": "the — определённый артикль", "text": "Используется, когда предмет УЖЕ ИЗВЕСТЕН или КОНКРЕТЕН. Ситуации: 1) уже упоминали: I have a cat. The cat is black. 2) единственный в своём роде: the sun, the moon, the sky. 3) с превосходной степенью: the best, the biggest. 4) с порядковыми: the first, the second."},
            {"h": "Когда артикль НЕ нужен", "text": "1) С множественным числом в общем: I like apples (яблоки вообще). 2) С именами: Anna, Moscow, Russia. 3) С неисчисляемыми в общем: Water is good for you. 4) С 'go to school / bed / work' (учиться, спать, работать — как деятельность). 5) Перед притяжательными: my book, his car."},
            {"h": "Устойчивые фразы", "text": "БЕЗ артикля: go to bed (спать), go to school (учиться), go to work (работать), at home, at work, in bed, on foot. С артиклем: go to THE school (именно в ту школу), at THE office, on THE bus."},
            {"h": "Географические названия", "text": "БЕЗ артикля: страны (Russia, France), города (Moscow, London), улицы, озёра. С артиклем THE: USA, UK, Netherlands, Philippines, океаны, моря, реки (the Volga, the Black Sea, the Pacific Ocean), горные массивы (the Alps)."},
            {"h": "Артикль с профессиями", "text": "С профессиями используем a/an: I am a doctor. She is an engineer. Даже если это первое предложение, но профессия указывает на принадлежность к группе — артикль нужен."},
            {"h": "Указатели вместо артикля", "text": "Если есть this / that / my / your / some / any / no — артикль НЕ нужен. Нельзя 'my a book', нужно 'my book'. Нельзя 'this the cat', нужно 'this cat'."},
            {"h": "Артикль с исчисляемыми и неисчисляемыми", "text": "Исчисляемые в единственном числе — ВСЕГДА с артиклем (a/the) или указателем (this/my). Нельзя 'I have cat'. Надо 'I have a cat' или 'I have the cat'. Неисчисляемые (water, money, time) — могут быть без артикля в общем смысле."}
        ],

        "tables": [
            {
                "title": "a vs an — правило звука",
                "headers": ["Артикль", "Когда", "Примеры"],
                "rows": [
                    ["a", "Перед согласным ЗВУКОМ", "a book, a car, a university (ю), a European (ю)"],
                    ["an", "Перед гласным ЗВУКОМ", "an apple, an egg, an hour (h не читается), an honest man"]
                ]
            },
            {
                "title": "Когда нужен the",
                "headers": ["Ситуация", "Пример"],
                "rows": [
                    ["Уже упоминали", "I bought a book. The book was interesting."],
                    ["Единственный в своём роде", "the sun, the moon, the sky"],
                    ["Превосходная степень", "the best, the most beautiful"],
                    ["Порядковые числительные", "the first, the second, the last"],
                    ["Океаны, реки, моря", "the Pacific, the Volga, the Black Sea"]
                ]
            },
            {
                "title": "Когда артикль НЕ нужен",
                "headers": ["Ситуация", "Пример"],
                "rows": [
                    ["Множественное в общем", "I like apples."],
                    ["Имена, города, страны", "Anna, Moscow, Russia"],
                    ["Неисчисляемые в общем", "Water is good for you."],
                    ["Устойчивые выражения", "go to bed, at home, at work"],
                    ["С притяжательными", "my book, his car"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I have cat.", "right": "I have a cat.", "why": "Исчисляемое в ед. числе — обязательно с артиклем"},
            {"wrong": "I saw a elephant.", "right": "I saw an elephant.", "why": "Перед гласным звуком — an"},
            {"wrong": "The sun is a star.", "right": "The sun is a star.", "why": "Здесь всё правильно — sun и star с разными артиклями"},
            {"wrong": "I like the apples.", "right": "I like apples.", "why": "Множественное в общем смысле — без the"},
            {"wrong": "She is doctor.", "right": "She is a doctor.", "why": "С профессией нужен a/an"},
            {"wrong": "I live in the Moscow.", "right": "I live in Moscow.", "why": "С городами — без артикля"}
        ],

        "lifehacks": [
            "Правило звука: a + согласный, an + гласный. Не буква, а ЗВУК. university = 'юниверсити' → a. hour = 'ауэр' → an.",
            "Первое упоминание — a/an. Второе — the. I have a cat. The cat is black.",
            "С профессией — всегда a/an. I am a doctor. She is a teacher.",
            "Если есть притяжательное (my, your, his) — артикль НЕ нужен. Никогда.",
            "Единственный в мире — the: the sun, the moon, the Earth, the sky."
        ],

        "text": {
            "title": "A Trip to the Zoo",
            "paragraphs": [
                "Yesterday I went to a zoo with my sister. We saw a lot of interesting animals there. First we visited an elephant. The elephant was huge and grey. Then we went to see a lion. The lion was sleeping and we couldn't wake him up.",
                "My sister liked a monkey most of all. The monkey was jumping and playing with a ball. It was very funny. We also saw a giraffe, a zebra, and a bear. The bear was eating honey.",
                "After the zoo we went to a café. I ordered a coffee and my sister ordered a tea. We talked about the animals we saw. It was the best day of the week. The zoo is my favourite place in the city."
            ]
        },

        "text_questions": [
            {"q": "Where did they go yesterday?", "options": ["To a park", "To a zoo", "To a museum", "To a cinema"], "correct": "To a zoo"},
            {"q": "What was the elephant like?", "options": ["Small and green", "Huge and grey", "Fast and angry", "Old and sad"], "correct": "Huge and grey"},
            {"q": "What was the lion doing?", "options": ["Eating", "Sleeping", "Running", "Roaring"], "correct": "Sleeping"},
            {"q": "What animal did the sister like most?", "options": ["An elephant", "A monkey", "A giraffe", "A bear"], "correct": "A monkey"},
            {"q": "What was the monkey doing?", "options": ["Sleeping", "Eating bananas", "Jumping and playing with a ball", "Climbing a tree"], "correct": "Jumping and playing with a ball"},
            {"q": "What was the bear eating?", "options": ["Fish", "Honey", "Bread", "Apples"], "correct": "Honey"},
            {"q": "What did they order at the café?", "options": ["Two coffees", "A coffee and a tea", "Two teas", "Juice and water"], "correct": "A coffee and a tea"},
            {"q": "What does the author think about the zoo?", "options": ["It's boring", "It's the best day of the week", "It's too small", "It's scary"], "correct": "It's the best day of the week"}
        ],

        "test": [
            {"type": "choice", "q": "I saw ___ elephant at the zoo.", "options": ["a", "an", "the", "—"], "correct": "an"},
            {"type": "choice", "q": "___ sun rises in the east.", "options": ["A", "An", "The", "—"], "correct": "The"},
            {"type": "choice", "q": "I like ___ apples.", "options": ["a", "an", "the", "—"], "correct": "—"},
            {"type": "choice", "q": "She is ___ doctor.", "options": ["a", "an", "the", "—"], "correct": "a"},
            {"type": "choice", "q": "I bought ___ book yesterday. ___ book is interesting.", "options": ["a / A", "a / The", "the / A", "an / The"], "correct": "a / The"},
            {"type": "choice", "q": "We went to ___ school to pick up the kids.", "options": ["a", "an", "the", "—"], "correct": "the"},
            {"type": "fill", "q": "She has ___ dog. (введи только артикль)", "answer": "a"},
            {"type": "fill", "q": "___ moon is beautiful tonight. (введи только артикль)", "answer": "the"},
            {"type": "fill", "q": "I am ___ engineer. (введи только артикль)", "answer": "an"},
            {"type": "fill", "q": "I like ___ music. (введи '—' если артикль не нужен)", "answer": "—"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I have cat", "I have a cat", "I have the cat", "I have an cat"], "correct": "I have a cat"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I saw a elephant", "I saw an elephant", "I saw the elephant", "I saw elephant"], "correct": "I saw an elephant"},
            {"type": "error", "q": "Найди правильное:", "options": ["She is doctor", "She is a doctor", "She is the doctor", "She is an doctor"], "correct": "She is a doctor"},
            {"type": "translate", "q": "Переведи: У меня есть кошка.", "answer": "I have a cat"},
            {"type": "translate", "q": "Переведи: Солнце яркое.", "answer": "The sun is bright"},
            {"type": "translate", "q": "Переведи: Я люблю музыку.", "answer": "I like music"},
            {"type": "translate", "q": "Переведи: Она инженер.", "answer": "She is an engineer"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 6 — ПРЕДЛОГИ (IN / ON / AT)
    # ═══════════════════════════════════════════
    {
        "id": "prepositions",
        "title": "Предлоги (in / on / at)",
        "emoji": "📍",
        "level": "A1-A2",
        "intro": "Три главных предлога времени и места. in — внутри, on — на поверхности, at — в точке.",
        "why": "Предлоги — вторая по сложности тема после артиклей. Но у них есть логика! in = что-то внутри большого, on = на поверхности или в конкретный день, at = в конкретной точке или в точное время. Освоив эту логику, ты перестанешь путать 'in Monday' и 'on Monday'. А правильное использование предлогов — признак хорошего английского.",

        "rules": [
            {"h": "in — время (большие периоды)", "text": "Месяцы: in May, in December. Годы: in 2020, in 1995. Времена года: in summer, in winter. Части дня: in the morning, in the afternoon, in the evening. Длительность: in 2 hours (через 2 часа), in a week (через неделю)."},
            {"h": "on — время (дни и даты)", "text": "Дни недели: on Monday, on Friday. Даты: on 5th May, on 1st September. Особые дни: on my birthday, on Christmas Day, on New Year's Day. Выходные: on the weekend (амер.) / at the weekend (брит.)."},
            {"h": "at — время (точки)", "text": "Точное время: at 5 o'clock, at 3:30 pm. Части суток: at night, at noon, at midnight. Праздники (общий период): at Christmas, at Easter, at New Year."},
            {"h": "in — место (внутри)", "text": "Внутри чего-то: in the box, in the room, in the building. В городах и странах: in Moscow, in Russia, in Europe. В жидкостях: in water, in the sea."},
            {"h": "on — место (на поверхности)", "text": "На поверхности: on the table, on the wall, on the floor, on the ceiling. На транспорте (кроме машин): on the bus, on the train, on the plane. На улице: on the street, on the road."},
            {"h": "at — место (в точке)", "text": "В конкретной точке: at the bus stop, at the door, at the traffic lights. Дома, на работе, в школе (как деятельность): at home, at work, at school, at university. На мероприятиях: at the party, at the concert, at the meeting."},
            {"h": "Особые случаи", "text": "in bed (в кровати как состояние), on the bed (на кровати как поверхность). at the cinema (в кино как событие), in the cinema (внутри здания кинотеатра). in the car (в машине), on the bus (в автобусе)."},
            {"h": "Запомни ключевые фразы", "text": "in the morning, in the afternoon, in the evening, BUT at night. on Monday morning, on Sunday evening. at the weekend (британский), on the weekend (американский)."}
        ],

        "tables": [
            {
                "title": "in / on / at — время",
                "headers": ["Предлог", "Когда", "Примеры"],
                "rows": [
                    ["in", "Месяцы, годы, сезоны, части дня", "in May, in 2020, in summer, in the morning"],
                    ["on", "Дни недели, даты, особые дни", "on Monday, on 5th May, on my birthday"],
                    ["at", "Точное время, at night/noon/midnight", "at 5 o'clock, at night, at Christmas"]
                ]
            },
            {
                "title": "in / on / at — место",
                "headers": ["Предлог", "Когда", "Примеры"],
                "rows": [
                    ["in", "Внутри, в городах/странах", "in the box, in Moscow, in Russia"],
                    ["on", "На поверхности, на транспорте", "on the table, on the bus, on the wall"],
                    ["at", "В точке, дома/на работе/в школе", "at the door, at home, at school"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I was born in 5th May.", "right": "I was born on 5th May.", "why": "Даты — с on"},
            {"wrong": "See you in Monday.", "right": "See you on Monday.", "why": "Дни недели — с on"},
            {"wrong": "The meeting is in 3 pm.", "right": "The meeting is at 3 pm.", "why": "Точное время — с at"},
            {"wrong": "I am at home. (если ты внутри)", "right": "I am at home.", "why": "Тут всё правильно — at home = дома как состояние"},
            {"wrong": "I am in the bus.", "right": "I am on the bus.", "why": "Транспорт (кроме машин) — с on"},
            {"wrong": "I was born on 2005.", "right": "I was born in 2005.", "why": "Годы — с in"}
        ],

        "lifehacks": [
            "in = большая коробка (месяц, год, страна, город). on = поверхность или конкретный день. at = точка.",
            "Дни недели — on Monday. Даты — on 5th May. Запомни: ON для дней.",
            "Точное время — at 5 o'clock. at — это точка. Всё остальное — in the morning, но at night.",
            "Запомни фразу 'on Monday morning' — тут два предлога, но идёт 'on' (день) → 'in' (часть дня)."
        ],

        "text": {
            "title": "A Busy Week",
            "paragraphs": [
                "My name is Kate. I have a very busy schedule this week. On Monday morning I have a meeting at 9 o'clock. In the afternoon I usually work in my office. At 5 pm I go to the gym.",
                "On Tuesday I have a doctor's appointment at 10 am. In the evening I meet my friends at a café. We usually stay there until 8 pm. On Wednesday I work from home and relax in the evening.",
                "On Thursday my brother comes to visit me. He arrives in the morning and stays until Sunday. On Friday we go to a concert at 7 pm. On Saturday we visit our parents. On Sunday we go to the beach in the morning. What a week!"
            ]
        },

        "text_questions": [
            {"q": "What does Kate have on Monday morning?", "options": ["A gym class", "A meeting", "A doctor's appointment", "A concert"], "correct": "A meeting"},
            {"q": "What time does Kate's meeting start on Monday?", "options": ["At 8 am", "At 9 am", "At 10 am", "At 11 am"], "correct": "At 9 am"},
            {"q": "Where does Kate work on Monday afternoon?", "options": ["At home", "In her office", "At a café", "At the gym"], "correct": "In her office"},
            {"q": "What does Kate do at 5 pm on Monday?", "options": ["Goes to the gym", "Goes home", "Meets friends", "Has a meeting"], "correct": "Goes to the gym"},
            {"q": "When does Kate have a doctor's appointment?", "options": ["On Monday", "On Tuesday at 10 am", "On Wednesday", "On Thursday"], "correct": "On Tuesday at 10 am"},
            {"q": "When does Kate's brother arrive?", "options": ["On Monday", "On Wednesday", "On Thursday morning", "On Friday"], "correct": "On Thursday morning"},
            {"q": "When do they go to the concert?", "options": ["On Monday", "On Wednesday", "On Friday at 7 pm", "On Sunday"], "correct": "On Friday at 7 pm"},
            {"q": "What do they do on Sunday morning?", "options": ["Visit parents", "Go to the beach", "Go shopping", "Sleep"], "correct": "Go to the beach"}
        ],

        "test": [
            {"type": "choice", "q": "I was born ___ 2005.", "options": ["in", "on", "at", "to"], "correct": "in"},
            {"type": "choice", "q": "See you ___ Monday.", "options": ["in", "on", "at", "by"], "correct": "on"},
            {"type": "choice", "q": "The meeting is ___ 3 pm.", "options": ["in", "on", "at", "to"], "correct": "at"},
            {"type": "choice", "q": "I live ___ Moscow.", "options": ["in", "on", "at", "by"], "correct": "in"},
            {"type": "choice", "q": "I go to work ___ the morning.", "options": ["in", "on", "at", "to"], "correct": "in"},
            {"type": "choice", "q": "My birthday is ___ 5th May.", "options": ["in", "on", "at", "by"], "correct": "on"},
            {"type": "fill", "q": "I live ___ Moscow.", "answer": "in"},
            {"type": "fill", "q": "The book is ___ the table.", "answer": "on"},
            {"type": "fill", "q": "The meeting is ___ 3 pm.", "answer": "at"},
            {"type": "fill", "q": "I wake up ___ 7 o'clock.", "answer": "at"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I was born on 2005", "I was born in 2005", "I was born at 2005", "I was born by 2005"], "correct": "I was born in 2005"},
            {"type": "error", "q": "Найди ошибку:", "options": ["See you in Monday", "See you on Monday", "See you at Monday", "See you by Monday"], "correct": "See you on Monday"},
            {"type": "error", "q": "Найди правильное:", "options": ["I am in the bus", "I am on the bus", "I am at the bus", "I am by the bus"], "correct": "I am on the bus"},
            {"type": "translate", "q": "Переведи: Я родился в 2005 году.", "answer": "I was born in 2005"},
            {"type": "translate", "q": "Переведи: Встретимся в понедельник.", "answer": "See you on Monday"},
            {"type": "translate", "q": "Переведи: Встреча в 3 часа.", "answer": "The meeting is at 3 o'clock"},
                        {"type": "translate", "q": "Переведи: Книга на столе.", "answer": "The book is on the table"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 7 — THERE IS / THERE ARE
    # ═══════════════════════════════════════════
    {
        "id": "there_is_are",
        "title": "There is / There are",
        "emoji": "🏠",
        "level": "A1-A2",
        "intro": "Конструкция «есть / находится». Используем, когда говорим о наличии чего-то впервые.",
        "why": "Конструкция There is / There are — это один из способов сказать «есть» или «находится». По-русски мы говорим «В комнате есть кошка», а по-английски — «There is a cat in the room». Это не просто «есть», а «существует где-то». Без этой конструкции ты не сможешь описать комнату, город, квартиру или любое место. Она используется очень часто — в описаниях, рассказах, объявлениях.",

        "rules": [
            {"h": "There is — для одного", "text": "There is a book on the table. (На столе (есть) книга.) There is a cat in the room. (В комнате (есть) кошка.) Всегда с исчисляемым в единственном числе или с неисчисляемым."},
            {"h": "There are — для многих", "text": "There are 3 books on the table. (На столе 3 книги.) There are many people here. (Здесь много людей.) Всегда с множественным числом."},
            {"h": "Отрицание", "text": "There isn't / There aren't: There isn't any milk. (Молока нет.) There aren't any chairs. (Стульев нет.) С неисчисляемыми и множественными используем 'any'."},
            {"h": "Вопрос", "text": "Is there...? Are there...?: Is there a bank near here? (Есть ли здесь банк?) Are there any shops? (Есть ли какие-нибудь магазины?) Ответы: Yes, there is. No, there isn't."},
            {"h": "Прошедшее время", "text": "There was — для одного (в прошлом). There were — для многих. There was a cat here yesterday. There were many people at the party."},
            {"h": "Будущее время", "text": "There will be — для всех. There will be a meeting tomorrow. There will be many people."},
            {"h": "Разница с 'it is / they are'", "text": "There is a cat — сообщаем, что кошка существует. It is a cat — уточняем, что это именно кошка (не собака). There are books — сообщаем, что книги есть. They are books — уточняем, что это книги."},
            {"h": "Порядок слов", "text": "There is / There are + предмет + место. There is a cat IN THE ROOM. There are books ON THE TABLE. Место в конце предложения."}
        ],

        "tables": [
            {
                "title": "Все формы There is/are",
                "headers": ["Время", "Один / Неисчисл.", "Много"],
                "rows": [
                    ["Настоящее", "There is a...", "There are ..."],
                    ["Отрицание сейчас", "There isn't any...", "There aren't any..."],
                    ["Вопрос сейчас", "Is there a...?", "Are there any...?"],
                    ["Прошедшее", "There was a...", "There were ..."],
                    ["Будущее", "There will be a...", "There will be ..."]
                ]
            },
            {
                "title": "There is / are vs It is / They are",
                "headers": ["Конструкция", "Когда", "Пример"],
                "rows": [
                    ["There is/are", "Сообщаем о наличии (впервые)", "There is a cat in the room."],
                    ["It is", "Уточняем что это (уже знаем)", "It is my cat."],
                    ["There are", "Сообщаем о наличии (много)", "There are 3 cats."],
                    ["They are", "Уточняем кто они", "They are my cats."]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "There is 3 books.", "right": "There are 3 books.", "why": "Множественное — there are"},
            {"wrong": "There are a cat.", "right": "There is a cat.", "why": "Один — there is"},
            {"wrong": "Is there any milk?", "right": "Is there any milk?", "why": "Всё правильно — milk неисчисляемое, is"},
            {"wrong": "There has a cat.", "right": "There is a cat.", "why": "There is, а не there has"},
            {"wrong": "There are a lot of peoples.", "right": "There are a lot of people.", "why": "People — уже множественное"},
            {"wrong": "There is many students.", "right": "There are many students.", "why": "Many + множественное → there are"}
        ],

        "lifehacks": [
            "Один предмет / неисчисляемое → there IS. Много → there ARE.",
            "There is = 'есть' в первый раз. It is = 'это' когда уже знаем о чём речь.",
            "С 'any' — в отрицаниях и вопросах: there isn't any, are there any.",
            "В прошедшем — was / were (как обычно). В будущем — only will be."
        ],

        "text": {
            "title": "My Flat",
            "paragraphs": [
                "I live in a small flat in the city centre. There are three rooms in my flat: a living room, a bedroom and a kitchen. There is also a bathroom and a small hall. The flat is on the fifth floor.",
                "In the living room there is a big sofa, a TV and a table. There are two armchairs near the window. On the walls there are some pictures. There isn't a fireplace, but I want one.",
                "In my bedroom there is a bed and a wardrobe. There are some books on the shelf. There isn't a desk, but I usually work at the kitchen table. In the kitchen there is a fridge, a cooker and a small table.",
                "There isn't a balcony, but there are big windows with a nice view. Is there a lift in my building? Yes, there is! It's very convenient."
            ]
        },

        "text_questions": [
            {"q": "How many rooms are there in the flat?", "options": ["Two", "Three", "Four", "Five"], "correct": "Three"},
            {"q": "What floor is the flat on?", "options": ["First", "Third", "Fifth", "Tenth"], "correct": "Fifth"},
            {"q": "What is there in the living room?", "options": ["A bed", "A sofa, a TV and a table", "A fridge", "A desk"], "correct": "A sofa, a TV and a table"},
            {"q": "What is there on the walls?", "options": ["Nothing", "Some pictures", "A clock", "A mirror"], "correct": "Some pictures"},
            {"q": "What is there in the bedroom?", "options": ["A bed and a wardrobe", "A sofa", "A fridge", "A cooker"], "correct": "A bed and a wardrobe"},
            {"q": "What is there on the shelf?", "options": ["Some books", "Some cups", "Some toys", "Nothing"], "correct": "Some books"},
            {"q": "What is there in the kitchen?", "options": ["Only a table", "A fridge, a cooker and a small table", "A bed", "A sofa"], "correct": "A fridge, a cooker and a small table"},
            {"q": "Is there a lift in the building?", "options": ["No", "Yes", "Only one", "I don't know"], "correct": "Yes"}
        ],

        "test": [
            {"type": "choice", "q": "___ a book on the table.", "options": ["There is", "There are", "It is", "They are"], "correct": "There is"},
            {"type": "choice", "q": "___ many students in the class.", "options": ["There is", "There are", "It is", "They are"], "correct": "There are"},
            {"type": "choice", "q": "___ any milk in the fridge?", "options": ["Is there", "Are there", "It is", "There is"], "correct": "Is there"},
            {"type": "choice", "q": "___ a cat and two dogs in the yard.", "options": ["There is", "There are", "It is", "They are"], "correct": "There are"},
            {"type": "choice", "q": "___ no people in the street.", "options": ["There is", "There are", "It is", "They are"], "correct": "There are"},
            {"type": "fill", "q": "___ a cat in the garden. (введи There is или There are)", "answer": "There is"},
            {"type": "fill", "q": "___ 3 cars on the street. (введи There is или There are)", "answer": "There are"},
            {"type": "fill", "q": "___ any chairs in the room? (введи Is there или Are there)", "answer": "Are there"},
            {"type": "fill", "q": "___ a bank near here? (введи Is there или Are there)", "answer": "Is there"},
            {"type": "error", "q": "Найди ошибку:", "options": ["There is 3 books", "There are 3 books", "There have 3 books", "There has 3 books"], "correct": "There are 3 books"},
            {"type": "error", "q": "Найди ошибку:", "options": ["There are a cat", "There is a cat", "There have a cat", "There has a cat"], "correct": "There is a cat"},
            {"type": "error", "q": "Найди правильное:", "options": ["There is many students", "There are many students", "There have many students", "There has many students"], "correct": "There are many students"},
            {"type": "translate", "q": "Переведи: В комнате есть кошка.", "answer": "There is a cat in the room"},
            {"type": "translate", "q": "Переведи: На столе 3 книги.", "answer": "There are 3 books on the table"},
            {"type": "translate", "q": "Переведи: Здесь есть банк?", "answer": "Is there a bank here"},
            {"type": "translate", "q": "Переведи: В комнате нет стульев.", "answer": "There aren't any chairs in the room"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 8 — МОДАЛЬНЫЕ ГЛАГОЛЫ (CAN / MUST / SHOULD)
    # ═══════════════════════════════════════════
    {
        "id": "modal_verbs",
        "title": "Модальные глаголы (can / must / should)",
        "emoji": "💪",
        "level": "A1-A2",
        "intro": "Модальные глаголы выражают возможность, необходимость, совет. Три главных: can, must, should.",
        "why": "Модальные глаголы — это «краски» английского. Без них ты не сможешь сказать «я умею», «ты должен», «тебе стоит». Они добавляют оттенки: возможность, запрет, совет, разрешение, вероятность. В русском языке мы выражаем это словами «могу», «должен», «стоит» — а в английском для этого есть специальные глаголы. Три самых важных: can (уметь), must (должен), should (стоит).",

        "rules": [
            {"h": "can — уметь / мочь", "text": "I can swim. (Я умею плавать.) Can you help me? (Можешь помочь?) Отрицание: cannot / can't. Отрицание: I can't come today."},
            {"h": "must — должен (сильная необходимость)", "text": "I must go. (Я должен идти.) You must not smoke here. (Нельзя курить здесь — запрет.) Must выражает личное решение или строгое правило."},
            {"h": "should — совет (стоит / не стоит)", "text": "You should sleep more. (Тебе стоит больше спать.) You shouldn't eat so much. (Не стоит так много есть.) Should — мягкий совет, рекомендация."},
            {"h": "Особенность модальных", "text": "После модальных — глагол БЕЗ to и БЕЗ -s: He can swim (не swims), She must go (не goes). Никаких окончаний!"},
            {"h": "Отрицания", "text": "can't / cannot (не могу). mustn't (нельзя — запрет). shouldn't (не советую). don't have to (не нужно — нет необходимости)."},
            {"h": "Разница must и have to", "text": "must — личное решение (I must study — сам решил). have to — внешнее правило (I have to wear a uniform — правило компании)."},
            {"h": "Вопросы", "text": "Can + подлежащее + глагол: Can you swim? Must + подлежащее + глагол: Must I go? Should + подлежащее + глагол: Should I call her?"},
            {"h": "Модальные в разных временах", "text": "Прошедшее: could (мог), had to (должен был), should have + V3 (следовало бы). Будущее: will be able to (смогу), will have to (должен буду)."}
        ],

        "tables": [
            {
                "title": "Три главных модальных",
                "headers": ["Глагол", "Значение", "Пример", "Отрицание"],
                "rows": [
                    ["can", "Уметь / мочь", "I can swim.", "can't / cannot"],
                    ["must", "Должен (сильно)", "I must go.", "mustn't (запрет)"],
                    ["should", "Стоит (совет)", "You should rest.", "shouldn't"]
                ]
            },
            {
                "title": "must vs have to",
                "headers": ["must", "have to"],
                "rows": [
                    ["Личное решение", "Внешнее правило"],
                    ["I must study. (сам решил)", "I have to wear a uniform. (правило)"],
                    ["Субъективное", "Объективное"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I can to swim.", "right": "I can swim.", "why": "После модальных — без to"},
            {"wrong": "She cans swim.", "right": "She can swim.", "why": "can не меняется — никакой -s"},
            {"wrong": "You must to go.", "right": "You must go.", "why": "После must — без to"},
            {"wrong": "I should to call her.", "right": "I should call her.", "why": "После should — без to"},
            {"wrong": "He musts work.", "right": "He must work.", "why": "must не меняется"},
            {"wrong": "I can not swim.", "right": "I cannot swim. / I can't swim.", "why": "Пишется слитно или с апострофом"}
        ],

        "lifehacks": [
            "can, must, should — это 'командиры'. После них глагол всегда в базовой форме, без to и без -s.",
            "Can = умею. Must = должен (я сам решил или правило). Should = стоит (совет).",
            "can't — не могу. mustn't — нельзя. shouldn't — не советую. Запомни разницу.",
            "По-русски 'могу' — модальный глагол. По-английски can — тоже. Только can не меняется."
        ],

        "text": {
            "title": "Rules at My Work",
            "paragraphs": [
                "I work in a big company. There are many rules here. I must arrive at 9 am. I mustn't be late. I can take a break every two hours. I should wear smart clothes, but I can wear jeans on Fridays.",
                "My boss says I must finish my projects on time. I can ask for help if I need it. I should check my email every hour. I mustn't use my phone during meetings. I can work from home one day a week.",
                "What about you? Can you work from home? Must you wear a uniform? Should you talk to your boss more often? Every job has its own rules."
            ]
        },

        "text_questions": [
            {"q": "What time must the person arrive at work?", "options": ["At 8 am", "At 9 am", "At 10 am", "At 11 am"], "correct": "At 9 am"},
            {"q": "How often can the person take a break?", "options": ["Every hour", "Every two hours", "Every three hours", "Once a day"], "correct": "Every two hours"},
            {"q": "What should the person wear?", "options": ["Jeans only", "Smart clothes", "Sport clothes", "Anything they want"], "correct": "Smart clothes"},
            {"q": "What can the person wear on Fridays?", "options": ["A suit", "Jeans", "A dress", "A uniform"], "correct": "Jeans"},
            {"q": "When must the person finish projects?", "options": ["Whenever they want", "On time", "Next week", "At midnight"], "correct": "On time"},
            {"q": "What should the person check every hour?", "options": ["Their watch", "Their email", "Their car", "Their desk"], "correct": "Their email"},
            {"q": "What mustn't the person do during meetings?", "options": ["Talk", "Listen", "Use phone", "Take notes"], "correct": "Use phone"},
            {"q": "How often can the person work from home?", "options": ["Every day", "Never", "One day a week", "Once a month"], "correct": "One day a week"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ swim very well.", "options": ["can", "cans", "can to", "am can"], "correct": "can"},
            {"type": "choice", "q": "You ___ wear a seatbelt. (закон)", "options": ["must", "should", "can", "may"], "correct": "must"},
            {"type": "choice", "q": "You ___ see a doctor. (совет)", "options": ["must", "should", "can", "will"], "correct": "should"},
            {"type": "choice", "q": "She ___ speak three languages.", "options": ["can", "cans", "can to", "is can"], "correct": "can"},
            {"type": "choice", "q": "You ___ smoke here. (запрет)", "options": ["mustn't", "shouldn't", "can't", "don't have to"], "correct": "mustn't"},
            {"type": "fill", "q": "She ___ (can) speak French.", "answer": "can"},
            {"type": "fill", "q": "They ___ (must) go now.", "answer": "must"},
            {"type": "fill", "q": "You ___ (should) sleep more.", "answer": "should"},
            {"type": "fill", "q": "I ___ (can not) come today.", "answer": "can't"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I can to swim", "I can swim", "I cans swim", "I am can swim"], "correct": "I can swim"},
            {"type": "error", "q": "Найди ошибку:", "options": ["She cans swim", "She can swim", "She can to swim", "She can swims"], "correct": "She can swim"},
            {"type": "error", "q": "Найди правильное:", "options": ["You must to go", "You must go", "You must go to", "You musts go"], "correct": "You must go"},
            {"type": "translate", "q": "Переведи: Я умею плавать.", "answer": "I can swim"},
            {"type": "translate", "q": "Переведи: Ты должен пристегнуться.", "answer": "You must wear a seatbelt"},
            {"type": "translate", "q": "Переведи: Тебе стоит больше спать.", "answer": "You should sleep more"},
            {"type": "translate", "q": "Переведи: Здесь нельзя курить.", "answer": "You mustn't smoke here"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 9 — СТЕПЕНИ СРАВНЕНИЯ
    # ═══════════════════════════════════════════
    {
        "id": "comparatives",
        "title": "Степени сравнения",
        "emoji": "📊",
        "level": "A1-A2",
        "intro": "Как сравнивать предметы: больше, меньше, самый большой. -er / more и -est / the most.",
        "why": "Степени сравнения — это способ сравнивать предметы и людей. «Этот дом выше», «Она самая умная», «Эта книга интереснее». Без степеней сравнения ты не сможешь описать мир вокруг: что лучше, что хуже, что самое красивое. В английском есть две формы — для коротких слов (bigger, biggest) и для длинных (more interesting, the most interesting). Выучить логику один раз — и пользуешься всю жизнь.",

        "rules": [
            {"h": "Короткие слова (1 слог)", "text": "Добавляем -er (сравнительная) или -est (превосходная): big → bigger → the biggest. tall → taller → the tallest. Если слово кончается на согласную + гласную + согласную (big), согласная удваивается: bigger, biggest."},
            {"h": "Длинные слова (3+ слога)", "text": "Используем more / the most: beautiful → more beautiful → the most beautiful. interesting → more interesting → the most interesting. comfortable → more comfortable → the most comfortable."},
            {"h": "Слова на -y", "text": "y → i + er/est: happy → happier → the happiest. busy → busier → the busiest. easy → easier → the easiest."},
            {"h": "Слова на -e", "text": "Просто добавляем -r / -st: nice → nicer → the nicest. large → larger → the largest."},
            {"h": "Исключения (запомни!)", "text": "good → better → the best. bad → worse → the worst. far → farther / further → the farthest / the furthest. little → less → the least. many / much → more → the most."},
            {"h": "Сравнение с 'than'", "text": "He is taller than me. (Он выше меня.) This book is more interesting than that one. Than — обязательное слово в сравнении."},
            {"h": "Превосходная степень с 'the'", "text": "She is the smartest. (Она самая умная.) This is the most beautiful place. Перед превосходной степенью ВСЕГДА 'the'."},
            {"h": "as...as — одинаковые", "text": "He is as tall as me. (Он такой же высокий, как я.) not as...as — не такой: She is not as smart as her sister."}
        ],

        "tables": [
            {
                "title": "Правила образования",
                "headers": ["Тип слова", "Сравнительная", "Превосходная"],
                "rows": [
                    ["1 слог (tall)", "-er (taller)", "-est (the tallest)"],
                    ["1 слог + удвоение (big)", "-ger (bigger)", "-gest (the biggest)"],
                    ["на -e (nice)", "-r (nicer)", "-st (the nicest)"],
                    ["на -y (happy)", "y→i+er (happier)", "y→i+est (the happiest)"],
                    ["3+ слога (beautiful)", "more (more beautiful)", "the most (the most beautiful)"]
                ]
            },
            {
                "title": "Исключения",
                "headers": ["Слово", "Сравнительная", "Превосходная"],
                "rows": [
                    ["good", "better", "the best"],
                    ["bad", "worse", "the worst"],
                    ["far", "farther / further", "the farthest / furthest"],
                    ["little", "less", "the least"],
                    ["many / much", "more", "the most"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "He is more taller than me.", "right": "He is taller than me.", "why": "Нельзя -er + more вместе"},
            {"wrong": "This is the most big house.", "right": "This is the biggest house.", "why": "Big — короткое, используй -est"},
            {"wrong": "She is the more beautiful.", "right": "She is the most beautiful.", "why": "Превосходная — the most"},
            {"wrong": "He is more better.", "right": "He is better.", "why": "Good — неправильный, better без more"},
            {"wrong": "He is taller that me.", "right": "He is taller than me.", "why": "Than, не that"},
            {"wrong": "I am the most tall in the class.", "right": "I am the tallest in the class.", "why": "Tall — короткое, -est"}
        ],

        "lifehacks": [
            "Правило слогов: 1 слог → -er/-est. 3+ слога → more/the most. 2 слога — обычно more, но есть исключения.",
            "Good / better / best — как в игре: хороший → лучше → лучший. Запомни как песню.",
            "Сравниваешь — обязательно 'than'. Превосходишь — обязательно 'the'.",
            "Если сомневаешься — используй more / the most. Для большинства длинных слов это правильно."
        ],

        "text": {
            "title": "My Two Friends",
            "paragraphs": [
                "I have two best friends: Tom and Kate. Tom is taller than me. He is the tallest person in our group. Kate is shorter than Tom, but she is the smartest of us all.",
                "Tom is very funny. He is funnier than any of us. He always tells the best jokes. Kate is quieter but she is more hardworking than Tom. She studies the hardest and gets the best marks.",
                "I am not as tall as Tom and not as smart as Kate. But I think I am the friendliest person in our group. My friends say I am the most loyal. We are all different, and that makes our friendship the best!"
            ]
        },

        "text_questions": [
            {"q": "Who is taller than the author?", "options": ["Kate", "Tom", "Both", "Neither"], "correct": "Tom"},
            {"q": "Who is the tallest in the group?", "options": ["Author", "Tom", "Kate", "Someone else"], "correct": "Tom"},
            {"q": "Who is the smartest?", "options": ["Author", "Tom", "Kate", "Tom and Kate"], "correct": "Kate"},
            {"q": "Who is the funniest?", "options": ["Author", "Tom", "Kate", "Nobody"], "correct": "Tom"},
            {"q": "Who is more hardworking?", "options": ["Tom", "Kate", "Author", "Everyone"], "correct": "Kate"},
            {"q": "Who gets the best marks?", "options": ["Tom", "Kate", "Author", "Nobody"], "correct": "Kate"},
            {"q": "What does the author think about themselves?", "options": ["Tallest", "Smartest", "Friendliest", "Funniest"], "correct": "Friendliest"},
            {"q": "What do the friends say about the author?", "options": ["Funniest", "Smartest", "Tallest", "Most loyal"], "correct": "Most loyal"}
        ],

        "test": [
            {"type": "choice", "q": "He is ___ than me.", "options": ["tall", "taller", "tallest", "more tall"], "correct": "taller"},
            {"type": "choice", "q": "She is the ___ in the class.", "options": ["smart", "smarter", "smartest", "most smart"], "correct": "smartest"},
            {"type": "choice", "q": "This film is ___ than that one.", "options": ["interesting", "interestinger", "more interesting", "most interesting"], "correct": "more interesting"},
            {"type": "choice", "q": "My car is ___ than yours.", "options": ["good", "gooder", "better", "best"], "correct": "better"},
            {"type": "choice", "q": "This is the ___ film I've ever seen.", "options": ["bad", "worse", "worst", "baddest"], "correct": "worst"},
            {"type": "fill", "q": "good → better → ___ (введи третью форму с the)", "answer": "the best"},
            {"type": "fill", "q": "big → ___ → the biggest (введи вторую форму)", "answer": "bigger"},
            {"type": "fill", "q": "happy → ___ → the happiest", "answer": "happier"},
            {"type": "fill", "q": "beautiful → more beautiful → ___ (введи третью форму с the)", "answer": "the most beautiful"},
            {"type": "error", "q": "Найди ошибку:", "options": ["He is more taller than me", "He is taller than me", "He is the tallest", "He is more tall"], "correct": "He is taller than me"},
            {"type": "error", "q": "Найди ошибку:", "options": ["She is the more beautiful", "She is the most beautiful", "She is more beautiful", "She is beautiful"], "correct": "She is the most beautiful"},
            {"type": "error", "q": "Найди правильное:", "options": ["He is taller that me", "He is taller than me", "He is more tall than me", "He is tall than me"], "correct": "He is taller than me"},
            {"type": "translate", "q": "Переведи: Он выше меня.", "answer": "He is taller than me"},
            {"type": "translate", "q": "Переведи: Она самая умная в классе.", "answer": "She is the smartest in the class"},
            {"type": "translate", "q": "Переведи: Эта книга интереснее.", "answer": "This book is more interesting"},
                        {"type": "translate", "q": "Переведи: Моя машина лучше твоей.", "answer": "My car is better than yours"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 10 — ГЕРУНДИЙ vs ИНФИНИТИВ
    # ═══════════════════════════════════════════
    {
        "id": "gerund_infinitive",
        "title": "Герундий vs Инфинитив",
        "emoji": "🎭",
        "level": "B1",
        "intro": "I like reading (герундий) или I want to read (инфинитив)? Всё зависит от глагола перед ним.",
        "why": "В русском языке мы говорим «я люблю читать» и «я хочу читать» одинаково. В английском — по-разному: I like READING (герундий) и I want TO READ (инфинитив). Правило не интуитивное — его надо запомнить. Но это важный шаг к B1: без герундия и инфинитива нельзя построить половину английских предложений. Плюс это покажет тебя как «продвинутого» юзера.",

        "rules": [
            {"h": "Герундий (-ing)", "text": "После глаголов: like, love, enjoy, hate, finish, stop (в значении 'прекратить'), mind, suggest, avoid, keep, practise. I enjoy reading. She finished working. Do you mind opening the window?"},
            {"h": "Инфинитив (to + глагол)", "text": "После глаголов: want, need, plan, hope, decide, promise, agree, would like, expect, try. I want to read. She decided to leave. He promised to help."},
            {"h": "После предлогов — ВСЕГДА -ing", "text": "I'm good at cooking. Thank you for helping. I'm interested in learning. Перед предлогом — герундий. Никогда инфинитив."},
            {"h": "После like / love / hate — оба варианта", "text": "like + -ing = нравится процесс. like + to = нравится результат. I like swimming (процесс). I like to swim in the morning (результат, привычка)."},
            {"h": "Stop / remember / forget — меняется смысл", "text": "stop + -ing = прекратить делать. stop + to = остановиться, чтобы сделать. remember + -ing = помню, как делал. remember + to = не забыл сделать. forget + -ing = забыл, как делал. forget + to = забыл сделать."},
            {"h": "Глаголы с двумя формами без разницы", "text": "begin, start, continue, prefer, love, hate, like — можно и -ing, и to. Смысл почти не меняется. Но в 90% случаев используется -ing."},
            {"h": "Make / let + глагол БЕЗ to", "text": "My mum made me clean my room. (Мама заставила меня убрать.) My dad let me go out. (Папа разрешил мне выйти.) После make/let — глагол БЕЗ to."},
            {"h": "After / before / when + -ing", "text": "After eating I went to work. Before going to bed, I read. When reading, I drink tea. После этих союзов — тоже герундий (если подлежащее то же)."}
        ],

        "tables": [
            {
                "title": "Глаголы + герундий (-ing)",
                "headers": ["Глагол", "Пример"],
                "rows": [
                    ["like / love", "I like reading"],
                    ["enjoy", "I enjoy cooking"],
                    ["hate", "She hates waiting"],
                    ["finish", "He finished working"],
                    ["stop (прекратить)", "Stop talking!"],
                    ["mind", "Do you mind helping?"],
                    ["suggest", "I suggest going home"],
                    ["avoid", "Avoid eating sugar"]
                ]
            },
            {
                "title": "Глаголы + инфинитив (to + V)",
                "headers": ["Глагол", "Пример"],
                "rows": [
                    ["want", "I want to sleep"],
                    ["need", "I need to go"],
                    ["plan", "We plan to travel"],
                    ["hope", "I hope to see you"],
                    ["decide", "She decided to stay"],
                    ["promise", "He promised to help"],
                    ["agree", "I agree to come"],
                    ["would like", "I would like to order"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I want reading a book.", "right": "I want to read a book.", "why": "Want + инфинитив"},
            {"wrong": "I enjoy to cook.", "right": "I enjoy cooking.", "why": "Enjoy + герундий"},
            {"wrong": "I'm good at cook.", "right": "I'm good at cooking.", "why": "После предлога — герундий"},
            {"wrong": "She decided going home.", "right": "She decided to go home.", "why": "Decide + инфинитив"},
            {"wrong": "Thank you for help.", "right": "Thank you for helping.", "why": "После предлога for — герундий"},
            {"wrong": "I finished to work.", "right": "I finished working.", "why": "Finish + герундий"}
        ],

        "lifehacks": [
            "Запомни ТОП-5 на -ing: like, love, enjoy, finish, mind. Остальное — обычно to + V.",
            "После предлога ВСЕГДА -ing. Никогда to + V. Это железное правило.",
            "Хочешь/планируешь/решишь — to + V. Нравится/наслаждаешься — -ing.",
            "С 'I like' можно и так, и так — не ошибешься."
        ],

        "text": {
            "title": "My Hobbies and Plans",
            "paragraphs": [
                "I enjoy learning languages. I love reading books and watching films in English. I also like to cook new dishes at the weekend. On Sundays, I usually finish working at noon and then I relax.",
                "I want to visit London next year. I plan to study English for two more years. My friend suggested going to a language school together. I agreed to think about it.",
                "I don't mind travelling alone, but I prefer to travel with friends. Last month I stopped eating fast food and started cooking at home. I hope to become healthier. What about you? What do you enjoy doing in your free time?"
            ]
        },

        "text_questions": [
            {"q": "What does the author enjoy?", "options": ["Learning languages", "Watching TV", "Playing sports", "Working"], "correct": "Learning languages"},
            {"q": "What does the author love doing?", "options": ["Cooking only", "Reading books and watching films in English", "Traveling", "Sleeping"], "correct": "Reading books and watching films in English"},
            {"q": "What does the author do on Sundays?", "options": ["Works all day", "Finishes working at noon and relaxes", "Travels", "Visits friends"], "correct": "Finishes working at noon and relaxes"},
            {"q": "Where does the author want to go next year?", "options": ["To New York", "To London", "To Paris", "To Moscow"], "correct": "To London"},
            {"q": "What did the friend suggest?", "options": ["Travelling alone", "Going to a language school together", "Eating more", "Stopping work"], "correct": "Going to a language school together"},
            {"q": "What does the author prefer?", "options": ["Traveling alone", "Traveling with friends", "Staying home", "Working"], "correct": "Traveling with friends"},
            {"q": "What did the author stop eating?", "options": ["Vegetables", "Fruit", "Fast food", "Meat"], "correct": "Fast food"},
            {"q": "What does the author hope to become?", "options": ["Richer", "Famous", "Healthier", "Taller"], "correct": "Healthier"}
        ],

        "test": [
            {"type": "choice", "q": "I want ___ a new car.", "options": ["buy", "buying", "to buy", "bought"], "correct": "to buy"},
            {"type": "choice", "q": "She enjoys ___.", "options": ["dance", "dancing", "to dance", "danced"], "correct": "dancing"},
            {"type": "choice", "q": "We decided ___ home.", "options": ["go", "going", "to go", "went"], "correct": "to go"},
            {"type": "choice", "q": "I finished ___ my homework.", "options": ["do", "doing", "to do", "did"], "correct": "doing"},
            {"type": "choice", "q": "Do you mind ___ the window?", "options": ["open", "opening", "to open", "opened"], "correct": "opening"},
            {"type": "fill", "q": "I like ___ (read) books. (введи форму -ing)", "answer": "reading"},
            {"type": "fill", "q": "She promised ___ (help) me. (введи с to)", "answer": "to help"},
            {"type": "fill", "q": "Thank you for ___ (come).", "answer": "coming"},
            {"type": "fill", "q": "I plan ___ (visit) London.", "answer": "to visit"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I want reading", "I want to read", "I want read", "I want reads"], "correct": "I want to read"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I enjoy to cook", "I enjoy cooking", "I enjoy cook", "I enjoy cooked"], "correct": "I enjoy cooking"},
            {"type": "error", "q": "Найди правильное:", "options": ["I'm good at cook", "I'm good at cooking", "I'm good at to cook", "I'm good at cooked"], "correct": "I'm good at cooking"},
            {"type": "translate", "q": "Переведи: Я люблю читать книги.", "answer": "I like reading books"},
            {"type": "translate", "q": "Переведи: Я хочу поехать домой.", "answer": "I want to go home"},
            {"type": "translate", "q": "Переведи: Она наслаждается танцами.", "answer": "She enjoys dancing"},
            {"type": "translate", "q": "Переведи: Спасибо за помощь.", "answer": "Thank you for helping"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 11 — COUNTABLE / UNCOUNTABLE
    # ═══════════════════════════════════════════
    {
        "id": "countable_uncountable",
        "title": "Считаемые / Несчитаемые",
        "emoji": "🔢",
        "level": "A1-A2",
        "intro": "Some / any / much / many / a lot of / few / little. Как правильно говорить о количестве.",
        "why": "В русском языке мы говорим «много воды» и «много книг» одинаково. В английском — по-разному: much water (неисчисляемое) vs many books (исчисляемое). Это правило нужно понимать, чтобы правильно говорить о количестве. Ошибки тут очень заметны для носителей, так что стоит освоить. Плюс — это одно из самых частых правил в повседневной речи.",

        "rules": [
            {"h": "Исчисляемые / неисчисляемые", "text": "Исчисляемые — можно посчитать: a book, two books, three books. Неисчисляемые — нельзя посчитать: water, milk, bread, money, time, information, advice. Их нельзя сказать 'a water' — только 'some water' или 'a glass of water'."},
            {"h": "some / any — немного, несколько", "text": "Some — в утверждениях (I have some books. I have some money.) Any — в вопросах и отрицаниях (Do you have any books? I don't have any money.)"},
            {"h": "much / many — много", "text": "Many — с исчисляемыми (many books, many people). Much — с неисчисляемыми (much water, much time). Much обычно в вопросах и отрицаниях: How much? Not much."},
            {"h": "a lot of — много (для всех)", "text": "a lot of = много. Работает и с исчисляемыми, и с неисчисляемыми: a lot of books, a lot of water. Самый универсальный вариант."},
            {"h": "few / a few — с исчисляемыми", "text": "few = мало (недостаточно): I have few friends (мало, плохо). a few = немного (нормально): I have a few friends (несколько, хорошо)."},
            {"h": "little / a little — с неисчисляемыми", "text": "little = мало (недостаточно): I have little time (мало, плохо). a little = немного (нормально): I have a little time (немного, хорошо)."},
            {"h": "Как посчитать неисчисляемое", "text": "Через контейнер: a glass of water, a cup of tea, a piece of cake, a bottle of milk, a kilo of meat, a slice of bread. Плюс: a bar of chocolate, a loaf of bread, a can of coke."},
            {"h": "Только единственное число", "text": "Неисчисляемые не имеют множественного: news, information, advice, money, bread, water. НЕ 'informations', НЕ 'advices', НЕ 'moneys'. Глагол в единственном числе: The news IS good."}
        ],

        "tables": [
            {
                "title": "Much/Many/Little/Few",
                "headers": ["Слово", "С чем", "Значение"],
                "rows": [
                    ["many", "Исчисляемые", "много"],
                    ["much", "Неисчисляемые", "много"],
                    ["a lot of", "Любые", "много (универсально)"],
                    ["few", "Исчисляемые", "мало (недостаток)"],
                    ["a few", "Исчисляемые", "немного (нормально)"],
                    ["little", "Неисчисляемые", "мало (недостаток)"],
                    ["a little", "Неисчисляемые", "немного (нормально)"]
                ]
            },
            {
                "title": "Как посчитать неисчисляемое",
                "headers": ["Неисчисляемое", "Через что", "Пример"],
                "rows": [
                    ["water", "a glass / a bottle of", "a glass of water"],
                    ["bread", "a loaf / a slice of", "a slice of bread"],
                    ["cake", "a piece of", "a piece of cake"],
                    ["chocolate", "a bar of", "a bar of chocolate"],
                    ["milk", "a carton / a glass of", "a glass of milk"],
                    ["meat", "a kilo of", "a kilo of meat"]
                ]
            },
            {
                "title": "Some / Any",
                "headers": ["Слово", "Когда", "Пример"],
                "rows": [
                    ["some", "Утверждение", "I have some books"],
                    ["any", "Вопрос", "Do you have any books?"],
                    ["any", "Отрицание", "I don't have any books"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I have much books.", "right": "I have many books.", "why": "Books — исчисляемое → many"},
            {"wrong": "I don't have many money.", "right": "I don't have much money.", "why": "Money — неисчисляемое → much"},
            {"wrong": "I have a water.", "right": "I have some water.", "why": "Water неисчисляемое — нельзя 'a'"},
            {"wrong": "How many money?", "right": "How much money?", "why": "Money — неисчисляемое → how much"},
            {"wrong": "I have informations.", "right": "I have information.", "why": "Information — неисчисляемое, без -s"},
            {"wrong": "Can I have a bread?", "right": "Can I have a slice of bread?", "why": "Bread неисчисляемое — через 'a slice of'"}
        ],

        "lifehacks": [
            "Считаешь → many. Не считаешь (вода, время, деньги) → much. Единый тест: могу ли я сказать 'two'? Если да — many. Если нет — much.",
            "a lot of — универсальное слово. Не ошибешься.",
            "a few / a little — позитивно ('немного есть'). few / little — негативно ('мало, не хватает').",
            "Неисчисляемое = нет множественного. Никогда не говори 'informations', 'advices', 'moneys'.",
            "Хочешь посчитать — используй контейнер: a glass of, a piece of, a slice of."
        ],

        "text": {
            "title": "Shopping for a Party",
            "paragraphs": [
                "Yesterday I went shopping for a party. I had a long list. I bought a lot of food and drinks. I bought some bread, some cheese and a few apples. I also bought a bottle of water and a carton of milk.",
                "For dessert I bought a bar of chocolate and a piece of cake. I wanted to buy a little ice cream, but there was no ice cream in the shop. I also bought some juice and a few oranges.",
                "There were not many people in the shop, so I finished quickly. I didn't have much money with me, but I managed to buy everything I needed. Now I'm ready for the party!"
            ]
        },

        "text_questions": [
            {"q": "What did the author buy?", "options": ["A book", "Food and drinks for a party", "Clothes", "A car"], "correct": "Food and drinks for a party"},
            {"q": "How many apples did the author buy?", "options": ["Many", "A few", "None", "A lot"], "correct": "A few"},
            {"q": "What did the author buy in a bottle?", "options": ["Milk", "Water", "Juice", "Coke"], "correct": "Water"},
            {"q": "What did the author buy in a carton?", "options": ["Water", "Juice", "Milk", "Tea"], "correct": "Milk"},
            {"q": "What did the author want to buy for dessert?", "options": ["Cake", "Ice cream", "Chocolate", "Fruit"], "correct": "Ice cream"},
            {"q": "Why didn't the author buy ice cream?", "options": ["It was expensive", "There was no ice cream", "Didn't want", "Forgot"], "correct": "There was no ice cream"},
            {"q": "Were there many people in the shop?", "options": ["Yes, a lot", "No, not many", "There were no people", "Only children"], "correct": "No, not many"},
            {"q": "How much money did the author have?", "options": ["A lot", "Not much", "None", "All money in the world"], "correct": "Not much"}
        ],

        "test": [
            {"type": "choice", "q": "How ___ books do you have?", "options": ["many", "much", "a lot", "few"], "correct": "many"},
            {"type": "choice", "q": "How ___ money do you have?", "options": ["many", "much", "a lot", "few"], "correct": "much"},
            {"type": "choice", "q": "I have ___ friends in Moscow.", "options": ["much", "a lot", "many", "a little"], "correct": "many"},
            {"type": "choice", "q": "I don't have ___ time today.", "options": ["many", "much", "a lot", "few"], "correct": "much"},
            {"type": "choice", "q": "Can I have ___ water, please?", "options": ["a", "some", "many", "few"], "correct": "some"},
            {"type": "fill", "q": "How ___ (many/much) water do you drink?", "answer": "much"},
            {"type": "fill", "q": "How ___ (many/much) people are here?", "answer": "many"},
            {"type": "fill", "q": "I have ___ (a few / a little) money. (немного)", "answer": "a little"},
            {"type": "fill", "q": "I have ___ (a few / a little) books. (немного)", "answer": "a few"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I have much books", "I have many books", "I have a lot of books", "I have a few books"], "correct": "I have many books"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I have a water", "I have some water", "I have a glass of water", "I have water"], "correct": "I have some water"},
            {"type": "error", "q": "Найди правильное:", "options": ["How many money?", "How much money?", "How a lot money?", "How few money?"], "correct": "How much money?"},
            {"type": "translate", "q": "Переведи: Сколько у тебя книг?", "answer": "How many books do you have"},
            {"type": "translate", "q": "Переведи: Сколько у тебя времени?", "answer": "How much time do you have"},
            {"type": "translate", "q": "Переведи: У меня мало друзей.", "answer": "I have few friends"},
            {"type": "translate", "q": "Переведи: Можно немного воды?", "answer": "Can I have some water"}
        ]
    },

    # ═══════════════════════════════════════════
    # УРОК 12 — NUMBERS & TIME
    # ═══════════════════════════════════════════
    {
        "id": "numbers_time",
        "title": "Numbers & Time",
        "emoji": "🕐",
        "level": "A1-A2",
        "intro": "Числа, время, даты. Как сказать 'полтретьего', 'без пятнадцати', 'тысяча двести'.",
        "why": "Числа и время — то, что нужно каждый день. Ты называешь время встречи, цену в магазине, дату рождения, номер телефона. Если ты не умеешь говорить время по-английски, ты как будто без часов. Это простой, но очень практичный урок. Выучишь один раз — и пользуешься всю жизнь.",

        "rules": [
            {"h": "Числа 1-20", "text": "one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty."},
            {"h": "Десятки", "text": "twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety. Для 21-99: двадцать один = twenty-one (через дефис). 45 = forty-five. 99 = ninety-nine."},
            {"h": "Сотни, тысячи, миллионы", "text": "100 = a hundred / one hundred. 200 = two hundred (без -s!). 1000 = a thousand. 2500 = two thousand five hundred. 1 000 000 = a million. 1 500 000 = one million five hundred thousand."},
            {"h": "Время — простой способ", "text": "Сначала часы, потом минуты: 3:15 = three fifteen. 5:30 = five thirty. 8:45 = eight forty-five. Самый простой и распространённый в США."},
            {"h": "Время — британский способ", "text": "past — после (1-30 минут): 3:15 = quarter past three. 3:20 = twenty past three. 3:30 = half past three. to — до (31-59 минут): 3:45 = quarter to four. 3:50 = ten to four. o'clock — только для ровного часа: 3:00 = three o'clock."},
            {"h": "Даты — американский формат", "text": "Месяц / день / год: December 25th, 2026 (или 12/25/2026). Читается: December twenty-fifth, twenty twenty-six."},
            {"h": "Даты — британский формат", "text": "День / месяц / год: 25th December 2026 (или 25/12/2026). Читается: the twenty-fifth of December, twenty twenty-six."},
            {"h": "Порядковые числительные", "text": "first (1st), second (2nd), third (3rd), fourth (4th), fifth (5th), sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, twentieth, twenty-first, thirtieth, thirty-first. Остальные — + th: fourth, tenth."}
        ],

        "tables": [
            {
                "title": "Числа 1-20",
                "headers": ["Число", "Английский", "Число", "Английский"],
                "rows": [
                    ["1", "one", "11", "eleven"],
                    ["2", "two", "12", "twelve"],
                    ["3", "three", "13", "thirteen"],
                    ["4", "four", "14", "fourteen"],
                    ["5", "five", "15", "fifteen"],
                    ["6", "six", "16", "sixteen"],
                    ["7", "seven", "17", "seventeen"],
                    ["8", "eight", "18", "eighteen"],
                    ["9", "nine", "19", "nineteen"],
                    ["10", "ten", "20", "twenty"]
                ]
            },
            {
                "title": "Время — два способа",
                "headers": ["Время", "Простой (US)", "Британский (UK)"],
                "rows": [
                    ["3:00", "three o'clock", "three o'clock"],
                    ["3:15", "three fifteen", "quarter past three"],
                    ["3:30", "three thirty", "half past three"],
                    ["3:45", "three forty-five", "quarter to four"],
                    ["3:50", "three fifty", "ten to four"],
                    ["4:05", "four oh five", "five past four"]
                ]
            },
            {
                "title": "Порядковые числительные",
                "headers": ["1-й", "first (1st)", "11-й", "eleventh (11th)"],
                "rows": [
                    ["2-й", "second (2nd)", "12-й", "twelfth (12th)"],
                    ["3-й", "third (3rd)", "13-й", "thirteenth (13th)"],
                    ["4-й", "fourth (4th)", "20-й", "twentieth (20th)"],
                    ["5-й", "fifth (5th)", "21-й", "twenty-first (21st)"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "It's three hour.", "right": "It's three o'clock.", "why": "Ровный час — o'clock"},
            {"wrong": "Two hundreds dollars.", "right": "Two hundred dollars.", "why": "После числительного hundred/thousand без -s"},
            {"wrong": "3:15 = three past fifteen.", "right": "3:15 = three fifteen (US) / quarter past three (UK).", "why": "Минуты не идут первыми в простом способе"},
            {"wrong": "I was born in 5 May.", "right": "I was born on 5th May.", "why": "Даты — с on"},
            {"wrong": "My birthday is in May 5.", "right": "My birthday is on May 5th.", "why": "Даты — с on"},
            {"wrong": "It's half to three (для 3:30).", "right": "It's half past three.", "why": "30 минут — это past, не to"}
        ],

        "lifehacks": [
            "Числа от 21 до 99 пишутся через дефис: twenty-one, forty-five, ninety-nine.",
            "После hundred / thousand / million НЕ добавляем -s. Two hundred, five thousand.",
            "Время в США — просто читай цифры: 3:15 = three fifteen. Работает всегда.",
            "В UK — до 30 минут past, после 30 — to. 3:45 = quarter to FOUR (не three).",
            "Даты: 'on + день + of + месяц' (британский) или 'месяц + день' (американский)."
        ],

        "text": {
            "title": "My Special Day",
            "paragraphs": [
                "My name is Maria. I was born on the fifteenth of June, 1999. My birthday is my favourite day of the year. Every year I celebrate it with my family and friends. My mother always cooks a big cake with twenty candles.",
                "My best friend's birthday is on March 2nd. Her name is Anna. She is two years older than me. We always celebrate our birthdays together — on the twentieth of June every summer.",
                "I have an exam on the tenth of December at 9:30 am. I need to arrive at 9 o'clock. In the evening I usually finish my work at half past six. My train leaves at 7:45 pm. It's a busy day!"
            ]
        },

        "text_questions": [
            {"q": "When was Maria born?", "options": ["On 15th June 1999", "On 15th July 1999", "On 5th June 1999", "On 15th June 2000"], "correct": "On 15th June 1999"},
            {"q": "How many candles does the mother put on the cake?", "options": ["Fifteen", "Twenty", "Twenty-five", "Ten"], "correct": "Twenty"},
            {"q": "When is Anna's birthday?", "options": ["On March 2nd", "On March 5th", "On May 2nd", "On 2nd June"], "correct": "On March 2nd"},
            {"q": "How much older is Anna than Maria?", "options": ["One year", "Two years", "Three years", "Same age"], "correct": "Two years"},
            {"q": "When do they celebrate their birthdays together?", "options": ["On the 20th of June", "On the 15th of June", "On the 10th of July", "In winter"], "correct": "On the 20th of June"},
            {"q": "When is the exam?", "options": ["10th December at 9:30 am", "10th November at 9 am", "1st December at 9 am", "15th December"], "correct": "10th December at 9:30 am"},
            {"q": "What time does the person finish work in the evening?", "options": ["At 6:00", "At 6:30", "At 7:00", "At 5:30"], "correct": "At 6:30"},
            {"q": "What time does the train leave?", "options": ["At 7:30", "At 7:45", "At 7:15", "At 8:00"], "correct": "At 7:45"}
        ],

        "test": [
            {"type": "choice", "q": "It's three ___ (ровный час).", "options": ["o'clock", "hour", "past", "to"], "correct": "o'clock"},
            {"type": "choice", "q": "3:15 — это...", "options": ["quarter past three", "quarter to three", "quarter three", "three quarter"], "correct": "quarter past three"},
            {"type": "choice", "q": "3:45 — это...", "options": ["quarter past four", "quarter to four", "quarter three", "three forty"], "correct": "quarter to four"},
            {"type": "choice", "q": "3:30 — это...", "options": ["half to three", "half past three", "half three", "thirty three"], "correct": "half past three"},
            {"type": "choice", "q": "1000 — это...", "options": ["one hundred", "one thousand", "ten hundred", "one million"], "correct": "one thousand"},
            {"type": "fill", "q": "Напиши 25 прописью:", "answer": "twenty-five"},
            {"type": "fill", "q": "Напиши 100 прописью:", "answer": "one hundred"},
            {"type": "fill", "q": "3:15 = ___ (британский способ)", "answer": "quarter past three"},
            {"type": "fill", "q": "Мой день рождения ___ 5 мая. (предлог)", "answer": "on"},
            {"type": "error", "q": "Найди ошибку:", "options": ["Two hundreds dollars", "Two hundred dollars", "Two hundred of dollars", "Two hundred dollar"], "correct": "Two hundred dollars"},
            {"type": "error", "q": "Найди ошибку:", "options": ["It's three o'clock", "It's three oclock", "It's three hour", "It's three hours"], "correct": "It's three o'clock"},
            {"type": "error", "q": "Найди правильное:", "options": ["I was born in 5 May", "I was born on 5th May", "I was born at 5 May", "I was born 5 May"], "correct": "I was born on 5th May"},
            {"type": "translate", "q": "Переведи: Сейчас полтретьего (2:30).", "answer": "It's half past two"},
            {"type": "translate", "q": "Переведи: Я родился 5 мая 1999.", "answer": "I was born on 5th May 1999"},
            {"type": "translate", "q": "Переведи: 2500 — это...", "answer": "two thousand five hundred"},
            {"type": "translate", "q": "Переведи: Встреча в 3:15.", "answer": "The meeting is at quarter past three"}
        ]
    },
]
