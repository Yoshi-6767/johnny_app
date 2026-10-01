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

        # ═══════════════════════════════════════════
    # УРОК — PRESENT PERFECT (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "present_perfect",
        "title": "Present Perfect",
        "emoji": "✨",
        "level": "B1",
        "intro": "Настоящее совершённое время. Связывает прошлое с настоящим: действие уже произошло, но результат важен сейчас. Это одно из самых сложных времён для русскоговорящих, потому что в русском такого времени нет.",
        "why": "Present Perfect — это «мост» между прошлым и настоящим. Ты говоришь не о том, КОГДА что-то случилось, а о том, что это УЖЕ случилось и результат виден сейчас. Без Present Perfect ты не сможешь сказать «Я уже поел», «Я никогда не был в Лондоне», «Она только что позвонила». Это время используется в 15-20% всех английских предложений. Особенно часто — в разговорах о жизненном опыте, новостях, достижениях и недавних событиях. Если ты его не освоишь — будешь звучать как иностранец, который говорит «I ate already» вместо «I have already eaten».",

        "rules": [
            {"h": "Когда использовать", "text": "1) Опыт в жизни (когда — неважно): I have visited Paris. 2) Результат важен сейчас: I have lost my keys (и сейчас не могу войти). 3) Недавние действия: She has just called. 4) Действие началось в прошлом и продолжается: I have lived here for 5 years. 5) С новостями: The president has signed a new law."},
            {"h": "Как образуется", "text": "have / has + Past Participle (третья форма глагола). Для I / you / we / they — have. Для he / she / it — has. Например: I have worked, she has worked, they have gone, he has eaten. Past Participle у правильных глаголов = глагол + -ed (worked, played). У неправильных — третья форма из таблицы (go → gone, eat → eaten, see → seen)."},
            {"h": "Правильные глаголы", "text": "Формула: глагол + -ed. work → worked, play → played, watch → watched, finish → finished. Правило добавления -ed такое же, как в Past Simple: если глагол кончается на -e → +d (live → lived). Если согласная + y → y меняется на i + ed (study → studied). Если короткий слог с ударением → удваиваем согласную (stop → stopped)."},
            {"h": "Неправильные глаголы", "text": "Третья форма из таблицы неправильных глаголов. Топ-10: go → gone, eat → eaten, see → seen, do → done, have → had, be → been, take → taken, give → given, write → written, speak → spoken. ВАЖНО: у неправильных глаголов вторая и третья формы могут совпадать (buy → bought → bought) или различаться (write → wrote → written)."},
            {"h": "Отрицание", "text": "have not / has not + Past Participle. Сокращения: haven't / hasn't. I haven't finished. She hasn't called. They haven't arrived. ВАЖНО: отрицание всегда с have/has, не с do/does!"},
            {"h": "Вопрос", "text": "Have / Has + подлежащее + Past Participle? Have you finished? Has she called? Where have you been? What has he done? Ответы: Yes, I have. No, I haven't. Yes, she has. No, she hasn't."},
            {"h": "Маркеры времени", "text": "already (уже), yet (ещё / уже в вопросах), just (только что), ever (когда-либо), never (никогда), recently (недавно), lately (в последнее время), so far (пока что), today (сегодня), this week (на этой неделе), this year (в этом году). Если видишь эти маркеры — почти всегда Present Perfect."},
            {"h": "Present Perfect vs Past Simple", "text": "ГЛАВНОЕ отличие: Present Perfect — время НЕВАЖНО или НЕ УКАЗАНО (I have visited Paris — когда-то). Past Simple — время УКАЗАНО или ПОДРАЗУМЕВАЕТСЯ (I visited Paris in 2020). Сравни: I have lost my keys (и сейчас не могу войти) vs I lost my keys yesterday (просто факт). Если есть конкретное время (yesterday, last week, in 2020, 2 hours ago) → Past Simple. Если время неважно или не указано → Present Perfect."},
            {"h": "For и Since", "text": "FOR + период времени: for 5 years, for 2 hours, for a long time. SINCE + точка отсчёта: since 2020, since Monday, since I was a child. Пример: I have lived here for 5 years (период). I have lived here since 2020 (точка). ВАЖНО: если действие закончилось — используем Past Simple. Если продолжается — Present Perfect."},
            {"h": "Just, Already, Yet", "text": "JUST — только что (недавно, буквально минуту назад): I have just finished. ALREADY — уже (раньше, чем ожидалось): I have already eaten. YET — ещё (в отрицаниях) / уже (в вопросах): I haven't finished yet. Have you finished yet? Эти три слова — самые частые маркеры Present Perfect."},
            {"h": "Ever и Never", "text": "EVER — когда-либо (в вопросах о жизненном опыте): Have you ever been to London? NEVER — никогда (в утверждениях): I have never been to London. Эти слова используются, когда ты говоришь о жизненном опыте, без конкретного времени."},
            {"h": "Been vs Gone", "text": "HAVE BEEN TO — был и вернулся: I have been to Paris (я там был, сейчас вернулся). HAVE GONE TO — уехал и ещё не вернулся: He has gone to Paris (он в Париже сейчас). Разница важная — неправильное использование меняет смысл."},
            {"h": "Present Perfect с сегодняшним временем", "text": "С today, this week, this month, this year можно использовать и Present Perfect, и Past Simple. Present Perfect — если период ещё не закончился: I have read 3 books this month (месяц продолжается). Past Simple — если период закончился: I read 3 books last month (месяц закончился)."},
            {"h": "Частая ошибка с русским", "text": "В русском «Я уже поел» — прошедшее время. В английском — Present Perfect: I have already eaten. Русское «Я был в Лондоне» = I have been to London (не I was in London, если не указано время). Это главная ловушка для русскоговорящих."},
            {"h": "Past Participle неправильных", "text": "Запомни ключевые: be → been, do → done, go → gone, see → seen, eat → eaten, have → had, make → made, take → taken, give → given, write → written, speak → spoken, break → broken, choose → chosen, drive → driven, forget → forgotten, get → gotten/got, know → known, ride → ridden, sing → sung, swim → swum."}
        ],

        "tables": [
            {
                "title": "Спряжение глагола work (правильный)",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "have worked", "haven't worked", "Have I worked?"],
                    ["You", "have worked", "haven't worked", "Have you worked?"],
                    ["He", "has worked", "hasn't worked", "Has he worked?"],
                    ["She", "has worked", "hasn't worked", "Has she worked?"],
                    ["It", "has worked", "hasn't worked", "Has it worked?"],
                    ["We", "have worked", "haven't worked", "Have we worked?"],
                    ["They", "have worked", "haven't worked", "Have they worked?"]
                ]
            },
            {
                "title": "Спряжение глагола go (неправильный)",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "have gone", "haven't gone", "Have I gone?"],
                    ["You", "have gone", "haven't gone", "Have you gone?"],
                    ["He", "has gone", "hasn't gone", "Has he gone?"],
                    ["She", "has gone", "hasn't gone", "Has she gone?"],
                    ["It", "has gone", "hasn't gone", "Has it gone?"],
                    ["We", "have gone", "haven't gone", "Have we gone?"],
                    ["They", "have gone", "haven't gone", "Have they gone?"]
                ]
            },
            {
                "title": "Present Perfect vs Past Simple",
                "headers": ["Ситуация", "Present Perfect", "Past Simple"],
                "rows": [
                    ["Опыт без времени", "I have visited Paris.", "❌ Нельзя"],
                    ["Опыт с временем", "❌ Нельзя", "I visited Paris in 2020."],
                    ["Результат важен", "I have lost my keys.", "❌ Нельзя"],
                    ["Просто факт", "❌ Нельзя", "I lost my keys yesterday."],
                    ["Недавнее действие", "She has just called.", "❌ Нельзя"],
                    ["Давнее действие", "❌ Нельзя", "She called 2 hours ago."],
                    ["For / Since", "I have lived here for 5 years.", "❌ Нельзя"],
                    ["Законченное действие", "❌ Нельзя", "I lived there for 5 years."]
                ]
            },
            {
                "title": "Маркеры и их значения",
                "headers": ["Маркер", "Перевод", "Где используется"],
                "rows": [
                    ["already", "уже", "Утверждение"],
                    ["yet", "ещё / уже", "Отрицание / вопрос"],
                    ["just", "только что", "Утверждение"],
                    ["ever", "когда-либо", "Вопрос"],
                    ["never", "никогда", "Утверждение"],
                    ["recently", "недавно", "Утверждение"],
                    ["lately", "в последнее время", "Утверждение"],
                    ["so far", "пока что", "Утверждение"],
                    ["for + период", "в течение", "Утверждение"],
                    ["since + точка", "с", "Утверждение"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I have saw this film.", "right": "I have seen this film.", "why": "После have/has — третья форма (seen), не вторая (saw)"},
            {"wrong": "She has went home.", "right": "She has gone home.", "why": "Go → went → gone. После has — gone"},
            {"wrong": "I have finished yesterday.", "right": "I finished yesterday.", "why": "С конкретным временем (yesterday) — Past Simple"},
            {"wrong": "Did you have ever been to London?", "right": "Have you ever been to London?", "why": "Present Perfect в вопросах — без did"},
            {"wrong": "I have ate already.", "right": "I have already eaten.", "why": "Eat → ate → eaten. И already перед глаголом"},
            {"wrong": "He has wrote a letter.", "right": "He has written a letter.", "why": "Write → wrote → written. После has — written"},
            {"wrong": "I am living here for 5 years.", "right": "I have lived here for 5 years.", "why": "For + период → Present Perfect, не Present Continuous"},
            {"wrong": "I have seen him yesterday.", "right": "I saw him yesterday.", "why": "Yesterday — маркер Past Simple, не Present Perfect"},
            {"wrong": "She has just went out.", "right": "She has just gone out.", "why": "Go → gone, не went"},
            {"wrong": "I don't have finished.", "right": "I haven't finished.", "why": "Отрицание в Present Perfect — haven't, не don't"},
            {"wrong": "Have you ever went to Paris?", "right": "Have you ever been to Paris?", "why": "Go → been, когда речь о посещении"},
            {"wrong": "I have already eat.", "right": "I have already eaten.", "why": "Eat → eaten — третья форма"}
        ],

        "lifehacks": [
            "Если можешь ответить на вопрос «КОГДА?» конкретным временем — это Past Simple. Если «когда» неважно — Present Perfect.",
            "Слова-маркеры Present Perfect: already, yet, just, ever, never, recently, lately. Увидел — почти наверняка Present Perfect.",
            "For — период (5 years), since — точка (2020). Если путаешься — спроси: «это длительность или момент?»",
            "Been to — был и вернулся. Gone to — уехал и не вернулся. Разница меняет смысл предложения.",
            "Для русскоговорящих: думай «Я уже сделал» = I have already done. Не переводи буквально как «I already did».",
            "С today, this week, this month — Present Perfect, потому что период ещё не закончился.",
            "Учи 3 формы глаголов сразу: base → past → past participle. Не отдельно, а тройками."
        ],

        "text": {
            "title": "A Letter from Emma",
            "paragraphs": [
                "Hi Tom! How are you? I'm sorry I haven't written for so long, but so many things have happened since we last met. I have just returned from a two-week trip to Italy. It was amazing! I have visited Rome, Florence and Venice. I have never seen such beautiful architecture before. I have taken hundreds of photos — you have to see them!",
                "I have also started a new job at a design studio. I have worked there for three months now, and I absolutely love it. The team is very friendly and the projects are exciting. My boss has already given me two big projects to lead. I have never felt so motivated in my life. Of course, I have made some mistakes, but I have learned a lot.",
                "On the personal side, I have some news too. My sister has just got engaged! We have known her boyfriend for five years, and he is a wonderful person. They haven't set a date yet, but they are thinking about next summer. I have already started looking for a dress. Have you ever been to a wedding in Italy? I haven't — but I can't wait!",
                "I have also decided to start learning Spanish. I have wanted to learn it for years, but I have never had enough time. Now I have found a good online course, and I have already finished the first module. It's difficult, but I have enjoyed every lesson. So far, I have learned about 200 words.",
                "Anyway, I have to go — my Italian class starts in 10 minutes. I have already packed my bag. Have you heard from Sarah recently? I haven't seen her since last summer. Write back when you have time. I have missed our long conversations! Love, Emma"
            ]
        },

        "text_questions": [
            {"q": "Where has Emma just returned from?", "options": ["From Spain", "From Italy", "From France", "From Germany"], "correct": "From Italy"},
            {"q": "Which cities has Emma visited?", "options": ["Paris, Lyon, Nice", "Rome, Florence, Venice", "Madrid, Barcelona, Seville", "Berlin, Munich, Hamburg"], "correct": "Rome, Florence, Venice"},
            {"q": "How long has Emma worked at the new job?", "options": ["One week", "One month", "Three months", "One year"], "correct": "Three months"},
            {"q": "What has Emma's boss already given her?", "options": ["A holiday", "Two big projects", "A new office", "A pay rise"], "correct": "Two big projects"},
            {"q": "What news does Emma have about her sister?", "options": ["She has got a new job", "She has got engaged", "She has moved abroad", "She has had a baby"], "correct": "She has got engaged"},
            {"q": "How long has the family known the sister's boyfriend?", "options": ["One year", "Two years", "Three years", "Five years"], "correct": "Five years"},
            {"q": "What language has Emma decided to learn?", "options": ["French", "Italian", "Spanish", "German"], "correct": "Spanish"},
            {"q": "How many words has Emma learned so far?", "options": ["About 100", "About 200", "About 500", "About 1000"], "correct": "About 200"},
            {"q": "What has Emma packed before writing?", "options": ["Her luggage", "Her bag", "Her books", "Her lunch"], "correct": "Her bag"},
            {"q": "When has Emma last seen Sarah?", "options": ["Last week", "Last month", "Last summer", "Last year"], "correct": "Last summer"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ never ___ to Japan.", "options": ["have / been", "has / been", "have / went", "did / go"], "correct": "have / been"},
            {"type": "choice", "q": "She ___ just ___ the phone.", "options": ["have / answered", "has / answered", "has / answering", "have / answer"], "correct": "has / answered"},
            {"type": "choice", "q": "___ you ever ___ Indian food?", "options": ["Did / try", "Have / tried", "Has / tried", "Do / try"], "correct": "Have / tried"},
            {"type": "choice", "q": "We ___ here for 10 years.", "options": ["live", "lived", "have lived", "are living"], "correct": "have lived"},
            {"type": "choice", "q": "He ___ his keys. He can't open the door.", "options": ["loses", "lost", "has lost", "is losing"], "correct": "has lost"},
            {"type": "choice", "q": "I ___ my homework already.", "options": ["do", "did", "have done", "am doing"], "correct": "have done"},
            {"type": "choice", "q": "They ___ to Paris three times.", "options": ["have been", "has been", "went", "have go"], "correct": "have been"},
            {"type": "choice", "q": "___ she ___ her breakfast yet?", "options": ["Did / eat", "Has / eaten", "Have / eaten", "Is / eating"], "correct": "Has / eaten"},
            {"type": "fill", "q": "I ___ (finish) my report.", "answer": "have finished"},
            {"type": "fill", "q": "She ___ (not / call) me yet.", "answer": "hasn't called"},
            {"type": "fill", "q": "They ___ (live) here since 2015.", "answer": "have lived"},
            {"type": "fill", "q": "We ___ (see) this film already.", "answer": "have seen"},
            {"type": "fill", "q": "He ___ (never / be) to London.", "answer": "has never been"},
            {"type": "fill", "q": "___ you ___ (ever / try) sushi?", "answer": "Have tried"},
            {"type": "fill", "q": "I ___ (not / eat) today.", "answer": "haven't eaten"},
            {"type": "fill", "q": "She ___ (just / arrive).", "answer": "has just arrived"},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["I have saw this film.", "I have seen this film.", "I have see this film.", "I has seen this film."], "correct": "I have seen this film."},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["She has went home.", "She have gone home.", "She has gone home.", "She has go home."], "correct": "She has gone home."},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["I have finished yesterday.", "I finished yesterday.", "I have finish yesterday.", "I did have finished yesterday."], "correct": "I finished yesterday."},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["Did you have ever been to Paris?", "Have you ever been to Paris?", "Have you ever went to Paris?", "Did you ever been to Paris?"], "correct": "Have you ever been to Paris?"},
            {"type": "error", "q": "Найди правильное предложение:", "options": ["I haven't finished yet.", "I don't have finished yet.", "I haven't finish yet.", "I not finished yet."], "correct": "I haven't finished yet."},
            {"type": "translate", "q": "Переведи на английский: Я уже поел.", "answer": "I have already eaten"},
            {"type": "translate", "q": "Переведи на английский: Она никогда не была в Лондоне.", "answer": "She has never been to London"},
            {"type": "translate", "q": "Переведи на английский: Ты когда-нибудь пробовал суши?", "answer": "Have you ever tried sushi"},
            {"type": "translate", "q": "Переведи на английский: Мы живём здесь 5 лет.", "answer": "We have lived here for 5 years"},
            {"type": "translate", "q": "Переведи на английский: Он только что ушёл.", "answer": "He has just left"},
            {"type": "write", "q": "Напиши 3-5 предложений на тему «Что я уже сделал сегодня».", "sample": "Today I have already woken up early, had breakfast and finished my morning workout. I have also checked my emails and read the news. I haven't started my work project yet, but I have planned it. I have drunk two cups of coffee so far."}
        ]
    },

        # ═══════════════════════════════════════════
    # УРОК — PAST CONTINUOUS (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "past_continuous",
        "title": "Past Continuous",
        "emoji": "⏳",
        "level": "B1",
        "intro": "Прошедшее длительное время. Действие, которое происходило в определённый момент в прошлом. «Я читал в 8 вечера», «Она спала, когда он позвонил». Ключевое время для рассказа историй.",
        "why": "Past Continuous — это «фон» для прошедших событий. Он описывает, ЧТО происходило, когда случилось что-то другое. Без него ты не сможешь рассказать историю: «Я шёл по улице, когда увидел друга». Русские говорят «шёл» — английские «was walking». В 80% случаев Past Continuous используется вместе с Past Simple — они идут парой. Если ты не освоишь Past Continuous, твои истории будут звучать рвано и неуклюже.",

        "rules": [
            {"h": "Когда использовать", "text": "1) Действие в конкретный момент в прошлом: At 8 pm I was reading a book. 2) Фон для другого действия: I was cooking when he called. 3) Два одновременных действия: I was reading while she was cooking. 4) Повторяющиеся раздражающие действия (с always): He was always losing his keys."},
            {"h": "Как образуется", "text": "was / were + глагол-ing. I was working. He was sleeping. They were playing. was — для I, he, she, it. were — для you, we, they. Без was/were — конструкция не работает."},
            {"h": "Правило -ing", "text": "Обычно + ing: work → working, play → playing. Если кончается на -e: убираем e + ing (write → writing, make → making). Если короткий слог и ударение: удваиваем согласную (run → running, sit → sitting). Если на -ie: ie → y + ing (die → dying, lie → lying)."},
            {"h": "Отрицание", "text": "was not / were not + глагол-ing. Сокращения: wasn't / weren't. I wasn't sleeping. They weren't working. She wasn't listening."},
            {"h": "Вопрос", "text": "Was / Were + подлежащее + глагол-ing? Was he working? Were you sleeping? What were you doing at 8 pm? Ответы: Yes, I was. No, I wasn't. Yes, they were. No, they weren't."},
            {"h": "Past Continuous + Past Simple", "text": "Самая частая конструкция. Past Continuous — длительное действие (фон). Past Simple — короткое действие, которое прервало фон. I was reading a book WHEN the phone rang. She was cooking dinner WHEN he came home. Союзы: when (когда), while (пока). While — обычно с Continuous, when — с Simple."},
            {"h": "While vs When", "text": "WHILE + Past Continuous: While I was reading, she called. (Пока я читал...). WHEN + Past Simple: I was reading when she called. (Я читал, когда она позвонила). While подчёркивает длительность, when — момент."},
            {"h": "Два одновременных действия", "text": "I was reading while she was cooking. (Я читал, пока она готовила.) Past Continuous + Past Continuous. Союз while (пока). Оба действия длились одновременно."},
            {"h": "Маркеры времени", "text": "at 5 o'clock yesterday, at 8 pm last night, all day, all morning, the whole evening, from 6 to 8 pm, when, while. Также: yesterday at this time, last week at this time."},
            {"h": "Глаголы-исключения", "text": "Как и в Present Continuous, глаголы состояния НЕ используются в Past Continuous: know, like, love, hate, want, need, understand, believe. Нельзя 'I was knowing'. Только I knew."},
            {"h": "Past Continuous vs Past Simple", "text": "Past Simple — законченное действие: I read a book yesterday. Past Continuous — длительное действие в процессе: I was reading a book at 8 pm yesterday. Past Simple отвечает на «что случилось?». Past Continuous отвечает на «что происходило?»."},
            {"h": "Для описания атмосферы", "text": "Past Continuous используется для описания обстановки в начале истории: The sun was shining, the birds were singing, and the children were playing in the park. This sets the scene before the main action."},
            {"h": "Always + Past Continuous", "text": "Конструкция was always + -ing выражает раздражение или повторяющееся действие в прошлом: He was always losing his keys. (Он вечно терял ключи.) She was always complaining. (Она вечно жаловалась.)"},
            {"h": "Порядок действий в истории", "text": "Обычно: Past Continuous (фон) → Past Simple (событие) → Past Continuous (что происходило после). Например: I was walking home (фон). Suddenly I saw a cat (событие). The cat was sitting on a tree (продолжение)."},
            {"h": "Разница с Present Continuous", "text": "Present Continuous — сейчас: I am reading. Past Continuous — тогда: I was reading. Смысл тот же, только перенесён в прошлое. Если понимаешь Present Continuous — поймёшь и Past."}
        ],

        "tables": [
            {
                "title": "Спряжение глагола work",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "was working", "wasn't working", "Was I working?"],
                    ["You", "were working", "weren't working", "Were you working?"],
                    ["He", "was working", "wasn't working", "Was he working?"],
                    ["She", "was working", "wasn't working", "Was she working?"],
                    ["It", "was working", "wasn't working", "Was it working?"],
                    ["We", "were working", "weren't working", "Were we working?"],
                    ["They", "were working", "weren't working", "Were they working?"]
                ]
            },
            {
                "title": "was vs were",
                "headers": ["Местоимение", "Форма", "Пример"],
                "rows": [
                    ["I", "was", "I was reading"],
                    ["He / She / It", "was", "He was sleeping"],
                    ["You", "were", "You were working"],
                    ["We / They", "were", "We were playing"]
                ]
            },
            {
                "title": "Past Continuous + Past Simple",
                "headers": ["Фон (Continuous)", "Событие (Simple)", "Пример"],
                "rows": [
                    ["I was reading", "the phone rang", "I was reading when the phone rang"],
                    ["She was cooking", "he came home", "She was cooking when he came home"],
                    ["They were walking", "it started to rain", "They were walking when it started to rain"],
                    ["We were sleeping", "the alarm went off", "We were sleeping when the alarm went off"]
                ]
            },
            {
                "title": "While vs When",
                "headers": ["Союз", "С каким временем", "Пример"],
                "rows": [
                    ["while", "Past Continuous", "While I was reading, she called"],
                    ["when", "Past Simple", "I was reading when she called"],
                    ["while", "Оба действия длились", "I was reading while she was cooking"],
                    ["when", "Прерывание", "I was reading when the bell rang"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I was read a book.", "right": "I was reading a book.", "why": "После was/were — глагол в -ing"},
            {"wrong": "They was playing.", "right": "They were playing.", "why": "They — множественное → were"},
            {"wrong": "He were sleeping.", "right": "He was sleeping.", "why": "He — единственное → was"},
            {"wrong": "I was knowing him.", "right": "I knew him.", "why": "Know — глагол состояния, не используется в Continuous"},
            {"wrong": "I was reading when she was calling.", "right": "I was reading when she called.", "why": "Короткое действие (звонок) — Past Simple"},
            {"wrong": "While I read, she was cooking.", "right": "While I was reading, she was cooking.", "why": "While + длительное действие → Past Continuous"},
            {"wrong": "I were working at 8 pm.", "right": "I was working at 8 pm.", "why": "I → was"},
            {"wrong": "She was cook when I came.", "right": "She was cooking when I came.", "why": "После was — глагол в -ing"},
            {"wrong": "What you were doing?", "right": "What were you doing?", "why": "В вопросе — were перед you"},
            {"wrong": "He was always complain.", "right": "He was always complaining.", "why": "После was always — глагол в -ing"},
            {"wrong": "When I was arrived, she was cooking.", "right": "When I arrived, she was cooking.", "why": "Arrive — короткое действие, Past Simple"},
            {"wrong": "We was watching TV.", "right": "We were watching TV.", "why": "We → were"}
        ],

        "lifehacks": [
            "Запомни пару: Past Continuous (фон) + Past Simple (событие). 'Я читал, когда зазвонил телефон.'",
            "was — для I, he, she, it. were — для you, we, they. Одна буква 'a' — один предмет, 'e' — много.",
            "While + длительное. When + короткое. While я читал — When она позвонила.",
            "Глаголы состояния (know, like, want) — НИКОГДА в Past Continuous. Только Past Simple.",
            "Описание обстановки в рассказе — всегда Past Continuous: 'Солнце светило, дети играли...'",
            "Видишь 'at 5 pm yesterday' — почти всегда Past Continuous.",
            "After 'was always' — глагол в -ing. Показывает раздражение: 'Он вечно терял ключи'."
        ],

        "text": {
            "title": "The Day Everything Went Wrong",
            "paragraphs": [
                "It was a beautiful Saturday morning. The sun was shining, the birds were singing, and I was walking to the park with my dog. We were both enjoying the weather. I was listening to music while my dog was running around me.",
                "Suddenly, my phone rang. I stopped to answer, but my dog was still running. When I looked up, I saw that he was running towards the lake. 'No!' I shouted, but it was too late.",
                "While I was running after him, my phone fell into a puddle. At that moment, my dog jumped into the lake. I was wet, my phone was broken, and my dog was swimming happily in the water. What a disaster!",
                "While I was trying to get my dog out of the lake, a kind woman came to help me. She was walking her dog too. Together we got my dog out. The woman smiled and said, 'It happens to everyone.' I was thinking about how lucky I was to meet her.",
                "Later that day, I was telling my family about the morning. They were laughing while I was describing the whole story. In the end, even I was laughing. It was a terrible morning, but now it's one of my favourite stories."
            ]
        },

        "text_questions": [
            {"q": "What was the weather like?", "options": ["It was raining", "The sun was shining", "It was cloudy", "It was snowing"], "correct": "The sun was shining"},
            {"q": "Where was the person going?", "options": ["To work", "To the park", "To the lake", "Home"], "correct": "To the park"},
            {"q": "What did the person hear suddenly?", "options": ["A dog barking", "The phone ringing", "A car honking", "Music"], "correct": "The phone ringing"},
            {"q": "Where was the dog running?", "options": ["To the tree", "Towards the lake", "To the house", "Home"], "correct": "Towards the lake"},
            {"q": "What happened to the phone?", "options": ["It rang", "It fell into a puddle", "It broke the screen", "It was stolen"], "correct": "It fell into a puddle"},
            {"q": "Who came to help?", "options": ["A policeman", "A kind woman", "Another dog owner's friend", "A child"], "correct": "A kind woman"},
            {"q": "What did the woman say?", "options": ["Call 911", "It happens to everyone", "Be careful next time", "Where is the dog?"], "correct": "It happens to everyone"},
            {"q": "How does the person feel about the story now?", "options": ["Still angry", "It's one of favourite stories", "Doesn't want to remember", "Sad"], "correct": "It's one of favourite stories"},
            {"q": "What was the woman doing when she met the person?", "options": ["Running", "Walking her dog", "Swimming", "Reading"], "correct": "Walking her dog"},
            {"q": "What were the family doing while the person was telling the story?", "options": ["Sleeping", "Laughing", "Crying", "Working"], "correct": "Laughing"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ TV at 8 pm yesterday.", "options": ["watched", "was watching", "watch", "am watching"], "correct": "was watching"},
            {"type": "choice", "q": "She ___ when I called her.", "options": ["slept", "was sleeping", "sleeps", "is sleeping"], "correct": "was sleeping"},
            {"type": "choice", "q": "They ___ football when it started to rain.", "options": ["played", "were playing", "play", "are playing"], "correct": "were playing"},
            {"type": "choice", "q": "What ___ you ___ at 8 pm?", "options": ["was / doing", "were / doing", "did / do", "are / doing"], "correct": "were / doing"},
            {"type": "choice", "q": "He ___ his keys again — he was always ___.", "options": ["lost / losing", "was losing / lost", "loses / losing", "lost / loses"], "correct": "lost / losing"},
            {"type": "choice", "q": "While I ___ dinner, my sister ___ TV.", "options": ["cooked / watched", "was cooking / was watching", "cooked / was watching", "was cooking / watched"], "correct": "was cooking / was watching"},
            {"type": "choice", "q": "I ___ home when I ___ my old friend.", "options": ["walked / was seeing", "was walking / saw", "walked / saw", "was walking / was seeing"], "correct": "was walking / saw"},
            {"type": "choice", "q": "They ___ all morning yesterday.", "options": ["studied", "were studying", "study", "are studying"], "correct": "were studying"},
            {"type": "fill", "q": "I ___ (read) a book at 8 pm yesterday.", "answer": "was reading"},
            {"type": "fill", "q": "She ___ (not / sleep) when I called.", "answer": "wasn't sleeping"},
            {"type": "fill", "q": "They ___ (play) football when it started to rain.", "answer": "were playing"},
            {"type": "fill", "q": "What ___ you ___ (do) at 5 pm?", "answer": "were doing"},
            {"type": "fill", "q": "While she ___ (cook), he ___ (watch) TV.", "answer": "was cooking / was watching"},
            {"type": "fill", "q": "I ___ (walk) home when I ___ (see) him.", "answer": "was walking / saw"},
            {"type": "fill", "q": "We ___ (not / work) at 10 pm.", "answer": "weren't working"},
            {"type": "error", "q": "Найди ошибку:", "options": ["I was read a book", "I was reading a book", "I were reading a book", "I am reading a book"], "correct": "I was reading a book"},
            {"type": "error", "q": "Найди ошибку:", "options": ["They was playing", "They were playing", "They are playing", "They is playing"], "correct": "They were playing"},
            {"type": "error", "q": "Найди правильное:", "options": ["I was knowing him", "I knew him", "I was known him", "I know him yesterday"], "correct": "I knew him"},
            {"type": "error", "q": "Найди правильное:", "options": ["While I read, she was cooking", "While I was reading, she was cooking", "While I read, she cooked", "While I reading, she was cooking"], "correct": "While I was reading, she was cooking"},
            {"type": "error", "q": "Найди правильное:", "options": ["I was reading when she was calling", "I was reading when she called", "I read when she was calling", "I was reading when she calls"], "correct": "I was reading when she called"},
            {"type": "translate", "q": "Переведи: Я читал книгу в 8 вечера.", "answer": "I was reading a book at 8 pm"},
            {"type": "translate", "q": "Переведи: Она спала, когда он позвонил.", "answer": "She was sleeping when he called"},
            {"type": "translate", "q": "Переведи: Что ты делал вчера в 5 часов?", "answer": "What were you doing yesterday at 5"},
            {"type": "translate", "q": "Переведи: Они играли в футбол, когда начался дождь.", "answer": "They were playing football when it started to rain"},
            {"type": "translate", "q": "Переведи: Пока я готовил, она смотрела ТВ.", "answer": "While I was cooking, she was watching TV"},
            {"type": "translate", "q": "Переведи: Я шёл домой, когда увидел друга.", "answer": "I was walking home when I saw a friend"},
            {"type": "write", "q": "Напиши 3-5 предложений на тему «Что я делал вчера в разное время».", "sample": "Yesterday at 8 am I was having breakfast and reading the news. At noon I was working on a new project. In the evening I was cooking dinner when my friend called. We were talking for an hour. Later I was watching a film while my wife was reading a book."}
        ]
    },

        # ═══════════════════════════════════════════
    # УРОК — PAST PERFECT (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "past_perfect",
        "title": "Past Perfect",
        "emoji": "⏮️",
        "level": "B1",
        "intro": "Предпрошедшее время. Действие, которое произошло РАНЬШЕ другого действия в прошлом. «Когда я пришёл, они уже ушли» — вот здесь нужен Past Perfect. Ключевое время для последовательности событий.",
        "why": "Past Perfect — это «прошлое в прошлом». Он нужен, когда ты рассказываешь о двух событиях, и одно случилось РАНЬШЕ другого. Без него невозможно выстроить хронологию: «Я пришёл на вокзал, но поезд уже ушёл» — тут два действия, и поезд ушёл раньше. Английский требует Past Perfect для того, что случилось раньше, и Past Simple — для того, что позже. Это время часто используется в историях, отчётах, объяснениях: «Я не пошёл в кино, потому что уже посмотрел фильм».",

        "rules": [
            {"h": "Когда использовать", "text": "1) Действие раньше другого в прошлом: When I arrived, they had already left. 2) С before / after: After I had finished work, I went home. 3) Причина в прошлом: I was tired because I hadn't slept. 4) С reported speech: He said he had finished. 5) С third conditional: If I had known, I would have told you."},
            {"h": "Как образуется", "text": "had + Past Participle (третья форма глагола). Форма 'had' одинакова для ВСЕХ лиц — I had worked, you had worked, he had worked, she had worked, we had worked, they had worked. Никаких изменений! Это самая простая часть."},
            {"h": "Правильные глаголы", "text": "had + глагол + -ed. work → had worked, play → had played, finish → had finished. Правило добавления -ed такое же, как в Past Simple и Present Perfect."},
            {"h": "Неправильные глаголы", "text": "had + третья форма из таблицы. go → had gone, eat → had eaten, see → had seen, do → had done, take → had taken, write → had written. Третья форма — та же, что в Present Perfect."},
            {"h": "Отрицание", "text": "had not (hadn't) + Past Participle. I hadn't finished. She hadn't called. They hadn't arrived. Всегда с 'had', не с did!"},
            {"h": "Вопрос", "text": "Had + подлежащее + Past Participle? Had you finished? Had she called? Where had you been? Ответы: Yes, I had. No, I hadn't."},
            {"h": "Past Perfect + Past Simple", "text": "ГЛАВНАЯ конструкция. Past Perfect — что случилось РАНЬШЕ. Past Simple — что случилось ПОЗЖЕ. When I arrived at the station, the train had already left. (Сначала поезд ушёл, потом я пришёл.) Порядок в предложении может быть любым — время указывает на хронологию."},
            {"h": "Before и After", "text": "BEFORE + Past Simple (позже): Before I went to work, I had had breakfast. AFTER + Past Perfect (раньше): After I had finished work, I went home. Логика: after — что раньше (Perfect), before — что позже (Simple)."},
            {"h": "Already, Just, Never, Ever", "text": "Те же маркеры, что в Present Perfect, но для Past Perfect. They had already left. She had just finished. I had never seen such a thing. Had you ever been there before?"},
            {"h": "For и Since", "text": "Как в Present Perfect: for + период, since + точка. But: I had lived there for 5 years (до определённого момента в прошлом). He had worked there since 2010 (до какого-то события)."},
            {"h": "Past Perfect vs Past Simple", "text": "Past Simple — просто факт из прошлого: I ate breakfast. Past Perfect — что было РАНЬШЕ другого события: I had eaten breakfast before I left. Если нет второго события в прошлом — Past Perfect не нужен."},
            {"h": "Past Perfect Continuous", "text": "Отдельное время: had been + -ing. Используется, когда действие длилось какое-то время ДО другого события. I had been waiting for 2 hours when she finally arrived. (Я ждал 2 часа до того, как она пришла.)"},
            {"h": "В рассказах", "text": "Past Perfect используется, когда автор возвращается назад во времени: 'Он вошёл в комнату (Past Simple). Он был здесь раньше (Past Perfect). Всё изменилось (Past Simple).' Возврат назад — всегда Past Perfect."},
            {"h": "С 'by the time'", "text": "By the time — к тому моменту, как. By the time I arrived, they had already eaten. By the time she called, I had finished. Всегда Past Perfect после by the time."},
            {"h": "С глаголами мысли", "text": "После think, know, realize, remember — можно использовать Past Perfect: I thought I had seen him before. I realized I had forgotten my keys. Особенно когда говоришь о воспоминании в прошлом."}
        ],

        "tables": [
            {
                "title": "Спряжение глагола work (правильный)",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "had worked", "hadn't worked", "Had I worked?"],
                    ["You", "had worked", "hadn't worked", "Had you worked?"],
                    ["He", "had worked", "hadn't worked", "Had he worked?"],
                    ["She", "had worked", "hadn't worked", "Had she worked?"],
                    ["It", "had worked", "hadn't worked", "Had it worked?"],
                    ["We", "had worked", "hadn't worked", "Had we worked?"],
                    ["They", "had worked", "hadn't worked", "Had they worked?"]
                ]
            },
            {
                "title": "Спряжение глагола go (неправильный)",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "had gone", "hadn't gone", "Had I gone?"],
                    ["You", "had gone", "hadn't gone", "Had you gone?"],
                    ["He", "had gone", "hadn't gone", "Had he gone?"],
                    ["She", "had gone", "hadn't gone", "Had she gone?"],
                    ["We", "had gone", "hadn't gone", "Had we gone?"],
                    ["They", "had gone", "hadn't gone", "Had they gone?"]
                ]
            },
            {
                "title": "Past Perfect + Past Simple",
                "headers": ["Что раньше (Past Perfect)", "Что позже (Past Simple)", "Пример"],
                "rows": [
                    ["Train left", "I arrived", "When I arrived, the train had left"],
                    ["She ate", "He came", "When he came, she had already eaten"],
                    ["We finished", "They called", "When they called, we had finished"],
                    ["He wrote a book", "He became famous", "He had written a book before he became famous"]
                ]
            },
            {
                "title": "Before vs After",
                "headers": ["Союз", "Что используется", "Пример"],
                "rows": [
                    ["before", "Past Simple (что позже)", "Before I left, I had eaten"],
                    ["after", "Past Perfect (что раньше)", "After I had eaten, I left"],
                    ["before", "Проще: Before I left, I ate", "Both are correct"],
                    ["after", "Проще: After I ate, I left", "Both are correct"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "When I arrived, they already left.", "right": "When I arrived, they had already left.", "why": "Действие раньше — Past Perfect"},
            {"wrong": "I had went home.", "right": "I had gone home.", "why": "После had — третья форма (gone)"},
            {"wrong": "She had saw him.", "right": "She had seen him.", "why": "See → saw → seen. После had — seen"},
            {"wrong": "I had eat breakfast.", "right": "I had eaten breakfast.", "why": "Eat → ate → eaten. После had — eaten"},
            {"wrong": "Did you had finished?", "right": "Had you finished?", "why": "Вопрос в Past Perfect — без did"},
            {"wrong": "I didn't had finished.", "right": "I hadn't finished.", "why": "Отрицание — hadn't, не didn't had"},
            {"wrong": "After I finished work, I had gone home.", "right": "After I had finished work, I went home.", "why": "После after — Past Perfect (что раньше), потом Past Simple"},
            {"wrong": "He had wrote a book.", "right": "He had written a book.", "why": "Write → wrote → written"},
            {"wrong": "She was tired because she didn't slept.", "right": "She was tired because she hadn't slept.", "why": "Причина в прошлом — Past Perfect"},
            {"wrong": "I had been knowing him.", "right": "I had known him.", "why": "Know — глагол состояния, не используется в Continuous"},
            {"wrong": "By the time I arrived, they ate.", "right": "By the time I arrived, they had eaten.", "why": "После by the time — Past Perfect"},
            {"wrong": "When she came, I already finished.", "right": "When she came, I had already finished.", "why": "Раньше — Past Perfect"}
        ],

        "lifehacks": [
            "Past Perfect — это «прошлое в прошлом». Если есть два события, и одно раньше — оно в Past Perfect.",
            "had — одинаковый для всех. Запомни, никаких hads, haded и т.д.",
            "После had — ТРЕТЬЯ форма (как в Present Perfect). go → had gone, eat → had eaten.",
            "After + Past Perfect, потом Past Simple. Порядок как в жизни: сначала первое, потом второе.",
            "By the time + Past Simple → Past Perfect. Запомни пару.",
            "Если в предложении только одно действие в прошлом — Past Perfect не нужен. Только Past Simple.",
            "Причина в прошлом — тоже Past Perfect: 'Я устал, потому что не спал' = I was tired because I hadn't slept."
        ],

        "text": {
            "title": "The Lost Concert Ticket",
            "paragraphs": [
                "Last summer, I had been planning to go to a concert for months. It was my favourite band, and I had bought the tickets six months before the show. I had told all my friends about it. Everyone had said it would be amazing.",
                "On the day of the concert, I woke up early. I had already prepared everything the night before. My ticket was in my bag, my phone was charged, and my clothes were ready. I had even learned all the songs.",
                "When I arrived at the station to catch the train, I realized something terrible. I had left my ticket at home! I had taken it out of my bag to show my mum, and then I had forgotten to put it back. I couldn't believe it.",
                "I called my mum. She had already left for work, but my brother was still at home. He had just woken up. He quickly found the ticket and agreed to bring it to the station. By the time he arrived, I had been waiting for 40 minutes.",
                "We got to the concert just in time. The show had already started, but we hadn't missed much. When my favourite song began, I felt so happy. I had almost missed the whole concert, but thanks to my brother, everything worked out. After the concert, I thanked him a hundred times."
            ]
        },

        "text_questions": [
            {"q": "How long before the concert had the person bought the tickets?", "options": ["One month", "Three months", "Six months", "One year"], "correct": "Six months"},
            {"q": "What had the person already done the night before?", "options": ["Bought tickets", "Prepared everything", "Called friends", "Learned songs"], "correct": "Prepared everything"},
            {"q": "Where did the person realize the ticket was missing?", "options": ["At home", "At the station", "At the concert", "In the taxi"], "correct": "At the station"},
            {"q": "Where had the person left the ticket?", "options": ["At work", "At home", "In the car", "At a friend's"], "correct": "At home"},
            {"q": "Who found the ticket?", "options": ["Mum", "Brother", "Friend", "Nobody"], "correct": "Brother"},
            {"q": "Where had mum already gone?", "options": ["To work", "To the concert", "To the shop", "To the station"], "correct": "To work"},
            {"q": "How long had the person been waiting by the time the brother arrived?", "options": ["10 minutes", "20 minutes", "40 minutes", "One hour"], "correct": "40 minutes"},
            {"q": "Had the show started when they arrived?", "options": ["No", "Yes, but not much had been missed", "Yes, they missed everything", "It was cancelled"], "correct": "Yes, but not much had been missed"},
            {"q": "What did the person do after the concert?", "options": ["Left immediately", "Thanked the brother", "Bought more tickets", "Called mum"], "correct": "Thanked the brother"},
            {"q": "Why had the person taken the ticket out of the bag?", "options": ["To show mum", "To check it", "To take a photo", "To give it to a friend"], "correct": "To show mum"}
        ],

        "test": [
            {"type": "choice", "q": "When I arrived, they ___ already ___.", "options": ["have / left", "had / left", "has / left", "was / leaving"], "correct": "had / left"},
            {"type": "choice", "q": "She was tired because she ___ well.", "options": ["didn't slept", "hadn't slept", "hasn't slept", "wasn't sleeping"], "correct": "hadn't slept"},
            {"type": "choice", "q": "___ you ___ the film before?", "options": ["Did / see", "Had / seen", "Have / saw", "Were / seeing"], "correct": "Had / seen"},
            {"type": "choice", "q": "After I ___ work, I went home.", "options": ["finished", "had finished", "was finishing", "have finished"], "correct": "had finished"},
            {"type": "choice", "q": "By the time she called, I ___ already ___.", "options": ["have / left", "had / left", "was / leaving", "did / leave"], "correct": "had / left"},
            {"type": "choice", "q": "He said he ___ the book.", "options": ["read", "had read", "reads", "was reading"], "correct": "had read"},
            {"type": "choice", "q": "They ___ their homework before they went out.", "options": ["finished", "had finished", "were finishing", "have finished"], "correct": "had finished"},
            {"type": "choice", "q": "I ___ never ___ such a thing before.", "options": ["have / seen", "had / seen", "was / seeing", "did / see"], "correct": "had / seen"},
            {"type": "fill", "q": "When I arrived, the train ___ (leave).", "answer": "had left"},
            {"type": "fill", "q": "She ___ (not / eat) before the meeting.", "answer": "hadn't eaten"},
            {"type": "fill", "q": "___ you ___ (see) him before?", "answer": "Had seen"},
            {"type": "fill", "q": "After I ___ (finish) my work, I went home.", "answer": "had finished"},
            {"type": "fill", "q": "By the time they came, we ___ (already / eat).", "answer": "had already eaten"},
            {"type": "fill", "q": "He said he ___ (finish) the project.", "answer": "had finished"},
            {"type": "fill", "q": "I was tired because I ___ (not / sleep).", "answer": "hadn't slept"},
            {"type": "error", "q": "Найди правильное:", "options": ["I had went home", "I had gone home", "I had go home", "I had going home"], "correct": "I had gone home"},
            {"type": "error", "q": "Найди правильное:", "options": ["She had saw him", "She had seen him", "She had see him", "She had seeing him"], "correct": "She had seen him"},
            {"type": "error", "q": "Найди правильное:", "options": ["When I arrived, they already left", "When I arrived, they had already left", "When I arrived, they have already left", "When I arrived, they were already left"], "correct": "When I arrived, they had already left"},
            {"type": "error", "q": "Найди правильное:", "options": ["Did you had finished?", "Had you finished?", "Have you had finished?", "Were you finished?"], "correct": "Had you finished?"},
            {"type": "error", "q": "Найди правильное:", "options": ["I didn't had finished", "I hadn't finished", "I hadn't finish", "I not finished"], "correct": "I hadn't finished"},
            {"type": "translate", "q": "Переведи: Когда я пришёл, они уже ушли.", "answer": "When I arrived, they had already left"},
            {"type": "translate", "q": "Переведи: Я устал, потому что не спал.", "answer": "I was tired because I hadn't slept"},
            {"type": "translate", "q": "Переведи: После того как я закончил работу, я пошёл домой.", "answer": "After I had finished work, I went home"},
            {"type": "translate", "q": "Переведи: К тому моменту, как она позвонила, я уже закончил.", "answer": "By the time she called, I had already finished"},
            {"type": "translate", "q": "Переведи: Он сказал, что прочитал книгу.", "answer": "He said he had read the book"},
            {"type": "write", "q": "Напиши 3-5 предложений на тему «Что я сделал до того, как что-то случилось вчера».", "sample": "Yesterday I had already had breakfast before I went to work. I had finished all my emails by 10 am. By the time my colleague arrived, I had already prepared the presentation. I had almost forgotten my lunch, but I remembered in time. After I had finished work, I went to the gym."}
        ]
    },

        # ═══════════════════════════════════════════
    # УРОК — PRESENT PERFECT CONTINUOUS (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "present_perfect_continuous",
        "title": "Present Perfect Continuous",
        "emoji": "🔄",
        "level": "B1",
        "intro": "Настоящее совершённое длительное время. Действие началось в прошлом, продолжается сейчас или только что закончилось. «Я жду уже 2 часа», «Она работает здесь с 2020». Ключевое время для выражения длительности.",
        "why": "Present Perfect Continuous — это «мостик» между Present Perfect и Present Continuous. Он говорит о действии, которое ДЛИТСЯ уже какое-то время и ещё не закончилось. Или только что закончилось, но результат виден. Без него ты не скажешь «Я учу английский 5 лет», «Он ждёт с утра», «Мы работаем над проектом уже месяц». Это время звучит очень естественно для носителей и показывает, что ты не просто «знаешь правила», а реально используешь язык. Особенно часто — с for и since.",

        "rules": [
            {"h": "Когда использовать", "text": "1) Действие длится до сих пор: I have been learning English for 5 years (и сейчас учу). 2) Только что закончилось, результат виден: I have been running (и я запыхался). 3) С for / since: She has been working here since 2020. 4) Временные ситуации: I have been staying with my parents this week. 5) Объяснение текущей ситуации: Why are you so tired? — I have been cleaning all day."},
            {"h": "Как образуется", "text": "have been / has been + глагол-ing. I have been working. She has been reading. They have been playing. have been — для I / you / we / they. has been — для he / she / it. ВАЖНО: 'been' — это третья форма от 'be'. Всегда 'been', не 'be'."},
            {"h": "Правило -ing", "text": "Обычно + ing: work → working, play → playing. Если кончается на -e: убираем e + ing (write → writing, make → making). Если короткий слог и ударение: удваиваем согласную (run → running, sit → sitting). Если на -ie: ie → y + ing (die → dying, lie → lying)."},
            {"h": "Отрицание", "text": "haven't been / hasn't been + глагол-ing. I haven't been sleeping well. She hasn't been feeling good. They haven't been working much lately."},
            {"h": "Вопрос", "text": "Have / Has + подлежащее + been + глагол-ing? Have you been waiting long? Has she been crying? How long have you been studying English? Ответы: Yes, I have. No, I haven't."},
            {"h": "Разница с Present Perfect", "text": "Present Perfect — результат (I have read 5 books this year). Present Perfect Continuous — длительность (I have been reading for 3 hours). Первый отвечает на 'что сделал?', второй на 'сколько делал?'."},
            {"h": "Разница с Present Continuous", "text": "Present Continuous — прямо сейчас: I am reading (в моменте). Present Perfect Continuous — длится уже какое-то время: I have been reading for 3 hours (с прошлого, ещё не закончил)."},
            {"h": "For и Since", "text": "FOR + период времени: for 5 years, for 3 hours, for a week. SINCE + точка отсчёта: since 2020, since Monday, since 9 am. Пример: I have been waiting for 2 hours. I have been waiting since 9 am. Оба правильны, но с разной логикой."},
            {"h": "Только что закончилось", "text": "Когда действие только что закончилось, но результат виден: I have been running — I'm tired. She has been cooking — the kitchen smells great. They have been painting — their hands are dirty."},
            {"h": "Не используется с глаголами состояния", "text": "Как и Present Continuous, Present Perfect Continuous НЕ используется с глаголами состояния: know, like, love, want, need, understand, believe. НЕ 'I have been knowing him for 5 years', а 'I have known him for 5 years'."},
            {"h": "С 'how long'", "text": "How long have you been learning English? How long has she been waiting? Это самая частая конструкция — вопрос о длительности. Отвечаем: I have been learning for 5 years."},
            {"h": "Маркеры времени", "text": "for (в течение), since (с), how long (как долго), all day (весь день), all morning (всё утро), lately (в последнее время), recently (недавно), these days (в эти дни)."},
            {"h": "Состояние vs процесс", "text": "Иногда разница между Present Perfect и Present Perfect Continuous тонкая. Present Perfect подчёркивает результат: I have painted the wall (стена готова). Present Perfect Continuous подчёркивает процесс: I have been painting the wall (и я весь в краске)."},
            {"h": "В новостях и объяснениях", "text": "Why is the ground wet? — It has been raining. Why are your eyes red? — I have been crying. Это классические примеры: действие только что закончилось, но результат виден сейчас."},
            {"h": "Изменения и развитие", "text": "Present Perfect Continuous может показывать постепенные изменения: The climate has been getting warmer. My English has been improving. Ключевое слово — 'gradually' или 'slowly'."}
        ],

        "tables": [
            {
                "title": "Спряжение глагола work",
                "headers": ["Местоимение", "Утверждение", "Отрицание", "Вопрос"],
                "rows": [
                    ["I", "have been working", "haven't been working", "Have I been working?"],
                    ["You", "have been working", "haven't been working", "Have you been working?"],
                    ["He", "has been working", "hasn't been working", "Has he been working?"],
                    ["She", "has been working", "hasn't been working", "Has she been working?"],
                    ["It", "has been working", "hasn't been working", "Has it been working?"],
                    ["We", "have been working", "haven't been working", "Have we been working?"],
                    ["They", "have been working", "haven't been working", "Have they been working?"]
                ]
            },
            {
                "title": "Present Perfect vs Present Perfect Continuous",
                "headers": ["Аспект", "Present Perfect", "Present Perfect Continuous"],
                "rows": [
                    ["Акцент", "Результат", "Длительность / процесс"],
                    ["Пример", "I have read 5 books.", "I have been reading for 3 hours."],
                    ["Вопрос", "Сколько сделал?", "Сколько делаю?"],
                    ["Маркеры", "already, just, yet", "for, since, how long"]
                ]
            },
            {
                "title": "For vs Since",
                "headers": ["Слово", "Значение", "Пример"],
                "rows": [
                    ["for", "период времени", "for 5 years, for 3 hours, for a week"],
                    ["since", "точка отсчёта", "since 2020, since Monday, since 9 am"]
                ]
            },
            {
                "title": "Глаголы состояния — исключения",
                "headers": ["Глагол", "Нельзя (PPC)", "Правильно (PP)"],
                "rows": [
                    ["know", "I have been knowing him", "I have known him"],
                    ["like", "I have been liking pizza", "I have liked pizza"],
                    ["want", "I have been wanting a car", "I have wanted a car"],
                    ["believe", "I have been believing", "I have believed"],
                    ["understand", "I have been understanding", "I have understood"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "I have been know him for 5 years.", "right": "I have known him for 5 years.", "why": "Know — глагол состояния, не используется в Continuous"},
            {"wrong": "I have working here for 2 years.", "right": "I have been working here for 2 years.", "why": "Нужен 'been' — have been + -ing"},
            {"wrong": "She has work here since 2020.", "right": "She has been working here since 2020.", "why": "После has — been + глагол в -ing"},
            {"wrong": "I am waiting for 2 hours.", "right": "I have been waiting for 2 hours.", "why": "For + период → Present Perfect Continuous, не Present Continuous"},
            {"wrong": "How long you have been learning?", "right": "How long have you been learning?", "why": "В вопросе — have перед you"},
            {"wrong": "I have been read a book.", "right": "I have been reading a book.", "why": "После been — глагол в -ing"},
            {"wrong": "She has been cook dinner.", "right": "She has been cooking dinner.", "why": "После been — глагол в -ing"},
            {"wrong": "We have been friends for 10 years.", "right": "We have been friends for 10 years.", "why": "Здесь 'have been friends' — правильно, потому что это состояние, не действие. Форма без -ing."},
            {"wrong": "I have been wanting to go.", "right": "I have wanted to go.", "why": "Want — глагол состояния"},
            {"wrong": "They have been played football.", "right": "They have been playing football.", "why": "После been — глагол в -ing, не Past Participle"},
            {"wrong": "I have been live here for a year.", "right": "I have been living here for a year.", "why": "После been — глагол в -ing"},
            {"wrong": "He has been runing.", "right": "He has been running.", "why": "Удвоение согласной: run → running"}
        ],

        "lifehacks": [
            "Present Perfect Continuous — про ДЛИТЕЛЬНОСТЬ. Если можешь спросить 'как долго?', 'сколько уже?' — используй его.",
            "For — период (5 лет). Since — точка (2020). Если путаешься — спроси: 'это длительность или момент старта?'",
            "Глаголы состояния (know, like, want) — НЕ используются в этой форме. Только Present Perfect: I have known.",
            "После 'been' — всегда -ing. been working, been reading, been doing. Не 'been work'.",
            "Только что закончилось, но результат виден: 'I have been running' (я запыхался). Классика.",
            "How long have you been...? — самая частая конструкция. Отвечай: for / since + время.",
            "Если путаешь с Present Perfect — спроси себя: тебе важен РЕЗУЛЬТАТ (Perfect) или ПРОЦЕСС (Perfect Continuous)?"
        ],

        "text": {
            "title": "Maria's Big Project",
            "paragraphs": [
                "Maria has been working at a design studio for three years now. She has been doing really well — her boss has already given her two big projects. Right now, she has been working on a new project for about two months. It has been taking all her energy.",
                "Her colleagues have been helping her a lot. They have been meeting every morning to discuss the work. Some of them have been staying late with her to finish the details. Maria has been feeling very grateful for their support.",
                "Her husband has been cooking dinner every night because Maria has been coming home so late. Their children have been missing her, but they understand. Maria has been promising to take a holiday after this project.",
                "The project has been going well, but it has been quite stressful. Maria has been sleeping only 5 hours a night. She has been drinking too much coffee, and she hasn't been exercising at all. She knows she has been neglecting her health.",
                "But she hasn't been complaining. She has been learning so much, and her skills have been improving every week. She has been dreaming about the moment when the project is finished and she can finally relax. Just two more weeks to go!"
            ]
        },

        "text_questions": [
            {"q": "How long has Maria been working at the design studio?", "options": ["One year", "Two years", "Three years", "Five years"], "correct": "Three years"},
            {"q": "How long has she been working on the new project?", "options": ["One month", "Two months", "Six months", "A year"], "correct": "Two months"},
            {"q": "What have Maria's colleagues been doing?", "options": ["Ignoring her", "Helping her", "Complaining", "Working on other projects"], "correct": "Helping her"},
            {"q": "What has Maria's husband been doing?", "options": ["Cooking dinner", "Working late", "Traveling", "Resting"], "correct": "Cooking dinner"},
            {"q": "Why has Maria been coming home late?", "options": ["Traffic", "Working on the project", "Visiting friends", "Going to the gym"], "correct": "Working on the project"},
            {"q": "How many hours has Maria been sleeping?", "options": ["8 hours", "6 hours", "5 hours", "4 hours"], "correct": "5 hours"},
            {"q": "What has Maria been dreaming about?", "options": ["A new job", "The project finishing", "Going on holiday", "Buying a car"], "correct": "The project finishing"},
            {"q": "Has Maria been complaining?", "options": ["Yes, a lot", "No, she hasn't", "Sometimes", "Only to her husband"], "correct": "No, she hasn't"},
            {"q": "What has been improving every week?", "options": ["Her salary", "Her skills", "The office", "The project"], "correct": "Her skills"},
            {"q": "How much longer until the project is done?", "options": ["One week", "Two weeks", "One month", "Six months"], "correct": "Two weeks"}
        ],

        "test": [
            {"type": "choice", "q": "I ___ English for 5 years.", "options": ["learn", "have learned", "have been learning", "am learning"], "correct": "have been learning"},
            {"type": "choice", "q": "She ___ here since 2020.", "options": ["works", "has worked", "has been working", "is working"], "correct": "has been working"},
            {"type": "choice", "q": "How long ___ you ___ for me?", "options": ["are / waiting", "have / waited", "have / been waiting", "did / wait"], "correct": "have / been waiting"},
            {"type": "choice", "q": "They ___ for 3 hours.", "options": ["have walked", "have been walking", "walked", "are walking"], "correct": "have been walking"},
            {"type": "choice", "q": "Why are your eyes red? — I ___.", "options": ["cried", "have cried", "have been crying", "am crying"], "correct": "have been crying"},
            {"type": "choice", "q": "The ground is wet. It ___ raining.", "options": ["has been", "is", "was", "has"], "correct": "has been"},
            {"type": "choice", "q": "She ___ a lot of coffee lately.", "options": ["drinks", "drank", "has drunk", "has been drinking"], "correct": "has been drinking"},
            {"type": "choice", "q": "I ___ for this company for 10 years.", "options": ["work", "have worked", "have been working", "am working"], "correct": "have been working"},
            {"type": "fill", "q": "I ___ (wait) for you for 2 hours.", "answer": "have been waiting"},
            {"type": "fill", "q": "She ___ (work) here since Monday.", "answer": "has been working"},
            {"type": "fill", "q": "They ___ (study) all morning.", "answer": "have been studying"},
            {"type": "fill", "q": "How long ___ you ___ (learn) English?", "answer": "have been learning"},
            {"type": "fill", "q": "He ___ (not / sleep) well lately.", "answer": "hasn't been sleeping"},
            {"type": "fill", "q": "The children ___ (play) in the garden all day.", "answer": "have been playing"},
            {"type": "fill", "q": "Why is she tired? — She ___ (clean) the house.", "answer": "has been cleaning"},
            {"type": "error", "q": "Найди правильное:", "options": ["I have working here for a year", "I have been working here for a year", "I have been work here for a year", "I am working here for a year"], "correct": "I have been working here for a year"},
            {"type": "error", "q": "Найди правильное:", "options": ["She has work here since 2020", "She has been working here since 2020", "She has been work here since 2020", "She is working here since 2020"], "correct": "She has been working here since 2020"},
            {"type": "error", "q": "Найди правильное:", "options": ["I have been knowing him for 5 years", "I have known him for 5 years", "I have been know him for 5 years", "I know him for 5 years"], "correct": "I have known him for 5 years"},
            {"type": "error", "q": "Найди правильное:", "options": ["How long you have been waiting?", "How long have you been waiting?", "How long are you waiting?", "How long did you wait?"], "correct": "How long have you been waiting?"},
            {"type": "error", "q": "Найди правильное:", "options": ["I have been read a book", "I have been reading a book", "I have read a book for 2 hours", "I read a book for 2 hours"], "correct": "I have been reading a book"},
            {"type": "translate", "q": "Переведи: Я учу английский 5 лет.", "answer": "I have been learning English for 5 years"},
            {"type": "translate", "q": "Переведи: Она работает здесь с 2020.", "answer": "She has been working here since 2020"},
            {"type": "translate", "q": "Переведи: Как долго ты меня ждёшь?", "answer": "How long have you been waiting for me"},
            {"type": "translate", "q": "Переведи: Я так устал — я весь день работал.", "answer": "I am so tired — I have been working all day"},
            {"type": "translate", "q": "Переведи: Земля мокрая. Шёл дождь.", "answer": "The ground is wet. It has been raining"},
            {"type": "write", "q": "Напиши 3-5 предложений на тему «Чем я занимался в последнее время».", "sample": "Lately I have been learning to play the guitar. I have been practising for one hour every day. I have also been reading more books in English. I have been trying to eat healthier, so I have been cooking at home. I have been feeling much better these days."}
        ]
    },

        # ═══════════════════════════════════════════
    # УРОК — CONDITIONALS (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "conditionals",
        "title": "Условные предложения",
        "emoji": "🔀",
        "level": "B1",
        "intro": "Четыре типа условий: реальные, возможные, нереальные и невозможные. «Если пойдёт дождь — останусь дома», «Если бы у меня было время — поехал бы», «Если бы я знал раньше — сделал бы по-другому». Одна из самых важных тем для B1-B2.",
        "why": "Условные предложения — это «мозг» английского. Они показывают, как ты думаешь: что реально, что возможно, что уже не случится. Без них ты не сможешь сказать «если», «бы», «если бы». А это огромный пласт языка: договорённости, планы, сожаления, мечты. Носители используют Conditionals постоянно. Если ты не освоишь их — будешь звучать как иностранец, который говорит только в настоящем времени. Это тема, которая отличает A2 от B1 и B2.",

        "rules": [
            {"h": "Zero Conditional (0 тип)", "text": "Реальные, всегда истинные факты. If + Present Simple, Present Simple. If you heat water to 100°C, it boils. If I don't sleep, I feel tired. Используется для научных фактов, привычек, общих правил. If можно заменить на when — смысл тот же."},
            {"h": "First Conditional (1 тип)", "text": "Реальное будущее. If + Present Simple, will + глагол. If it rains tomorrow, I will stay home. If you study hard, you will pass the exam. Реальное условие в будущем, которое может случиться. Очень часто используется в повседневной речи."},
            {"h": "Second Conditional (2 тип)", "text": "Нереальное настоящее. If + Past Simple, would + глагол. If I had more money, I would travel the world. If I were you, I would accept the offer. Действие нереально или маловероятно в настоящем. Внимание: с 'to be' используем WERE для всех лиц (If I were you)."},
            {"h": "Third Conditional (3 тип)", "text": "Нереальное прошлое (сожаление). If + Past Perfect, would have + V3. If I had studied harder, I would have passed the exam. If she had called, I would have answered. Действие уже не случилось, и мы сожалеем. Это время для «если бы я тогда знал»."},
            {"h": "Mixed Conditional (смешанный)", "text": "Смешивает 2 и 3 тип. Условие — в прошлом, результат — сейчас. If I had studied medicine, I would be a doctor now. (Если бы я учил медицину тогда — был бы врачом сейчас.) Или условие — сейчас, результат — в прошлом (реже)."},
            {"h": "Порядок частей", "text": "Условная часть (if) может идти первой или второй. Если она первая — между частями запятая. If it rains, I will stay home. I will stay home if it rains. Оба варианта правильны."},
            {"h": "Unless = if not", "text": "Unless = if... not. Unless you hurry, you will be late = If you don't hurry, you will be late. Unless используется в любом типе: Unless it rains, we will go out (1 тип)."},
            {"h": "Второй тип с to be", "text": "В 2 типе с глаголом to be используем WERE для всех лиц: If I were you, If he were here, If she were taller. В разговорной речи 'was' тоже допустимо, но 'were' — правильнее."},
            {"h": "Просьбы и советы", "text": "Второй тип используется для вежливых просьб: Would you mind if I opened the window? (Вы не против, если я открою окно?). И для советов: If I were you, I would... (На твоём месте я бы...)."},
            {"h": "Разница между 1 и 2 типом", "text": "1 тип — реально (может случиться): If I win the lottery, I will buy a house. 2 тип — нереально (фантазия): If I won the lottery, I would buy a house. Разница — в вероятности."},
            {"h": "Разница между 2 и 3 типом", "text": "2 тип — нереально сейчас: If I had time, I would help (но у меня нет времени сейчас). 3 тип — нереально в прошлом: If I had had time, I would have helped (но тогда не было времени)."},
            {"h": "Модальные глаголы в Conditionals", "text": "Вместо will / would можно использовать can, could, might, may, should, must. If you finish early, you can go home. If I had time, I could help. If I had studied, I might have passed."},
            {"h": "Inverted Conditionals (формальный стиль)", "text": "В формальном английском 'if' можно убрать и инвертировать: Were I you, I would... (вместо If I were you). Had I known, I would have told you. Should you need help, call me. Используется в литературе и официальных текстах."},
            {"h": "I wish = сожаление", "text": "I wish + Past Simple — сожаление о настоящем: I wish I had more time. I wish + Past Perfect — сожаление о прошлом: I wish I had studied harder. I wish + would — раздражение: I wish he would stop calling."},
            {"h": "Частые ошибки с русским", "text": "В русском 'если' одно — в английском 4 типа. Русское 'если будет дождь' = If it rains (Present Simple, не will). Русское 'если бы знал' = If I knew (Past Simple, не would). Главное — не использовать will в if-части."}
        ],

        "tables": [
            {
                "title": "Все четыре типа Conditionals",
                "headers": ["Тип", "Формула", "Пример"],
                "rows": [
                    ["0", "If + Present Simple, Present Simple", "If you heat water, it boils"],
                    ["1", "If + Present Simple, will + V", "If it rains, I will stay home"],
                    ["2", "If + Past Simple, would + V", "If I had money, I would travel"],
                    ["3", "If + Past Perfect, would have + V3", "If I had known, I would have helped"]
                ]
            },
            {
                "title": "Когда какой тип",
                "headers": ["Тип", "Вероятность", "Когда"],
                "rows": [
                    ["0", "100%", "Всегда, научные факты"],
                    ["1", "Реально (50-90%)", "Возможное будущее"],
                    ["2", "Маловероятно (10-40%)", "Нереальное настоящее"],
                    ["3", "0% (уже не случится)", "Сожаление о прошлом"]
                ]
            },
            {
                "title": "Сравнение примеров",
                "headers": ["Тип", "Пример", "Смысл"],
                "rows": [
                    ["1", "If I win the lottery, I will buy a house", "Реально (могу выиграть)"],
                    ["2", "If I won the lottery, I would buy a house", "Фантазия (не выиграю)"],
                    ["3", "If I had won the lottery, I would have bought a house", "Сожаление (не выиграл тогда)"]
                ]
            },
            {
                "title": "I wish — сожаления",
                "headers": ["Форма", "О чём", "Пример"],
                "rows": [
                    ["I wish + Past Simple", "Настоящее", "I wish I had more time"],
                    ["I wish + Past Perfect", "Прошлое", "I wish I had studied harder"],
                    ["I wish + would", "Раздражение", "I wish he would stop talking"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "If it will rain, I will stay home.", "right": "If it rains, I will stay home.", "why": "После if — НЕ will, а Present Simple"},
            {"wrong": "If I would have money, I would travel.", "right": "If I had money, I would travel.", "why": "В условии 2 типа — Past Simple, не would"},
            {"wrong": "If I was you, I would accept.", "right": "If I were you, I would accept.", "why": "В 2 типе с to be — were для всех лиц"},
            {"wrong": "If I had studied, I would pass.", "right": "If I had studied, I would have passed.", "why": "3 тип: would have + третья форма"},
            {"wrong": "If I would have known, I would have told you.", "right": "If I had known, I would have told you.", "why": "В условии 3 типа — Past Perfect, не would have"},
            {"wrong": "If I will have time, I will call you.", "right": "If I have time, I will call you.", "why": "После if — Present Simple, не will"},
            {"wrong": "I wish I would have more time.", "right": "I wish I had more time.", "why": "I wish + Past Simple (для настоящего)"},
            {"wrong": "If she will come, tell me.", "right": "If she comes, tell me.", "why": "После if — Present Simple"},
            {"wrong": "When it will rain, we will stay home.", "right": "When it rains, we will stay home.", "why": "После when — тоже Present Simple"},
            {"wrong": "If I knew, I would have told you.", "right": "If I had known, I would have told you.", "why": "Для прошлого — 3 тип, Past Perfect"},
            {"wrong": "Unless you don't hurry, you will be late.", "right": "Unless you hurry, you will be late.", "why": "Unless = if not, двойное отрицание не нужно"},
            {"wrong": "If I am you, I would call her.", "right": "If I were you, I would call her.", "why": "2 тип: were + would"}
        ],

        "lifehacks": [
            "Главное правило: после IF никогда не ставим WILL. If it rains (не will rain), I will stay home.",
            "Запомни связку: 1 тип — Present Simple + will. 2 тип — Past Simple + would. 3 тип — Past Perfect + would have.",
            "If I were you — фиксированная фраза для советов. Всегда were, не was.",
            "Unless = if not. Не удваивай отрицание: Unless you hurry (не don't hurry).",
            "I wish + Past Simple = сожаление о настоящем. I wish + Past Perfect = сожаление о прошлом.",
            "3 тип — это «поезд ушёл». Уже не случится, только сожаление.",
            "Если путаешь 1 и 2 тип — спроси: реально это или фантазия? Реально — 1. Фантазия — 2."
        ],

        "text": {
            "title": "If I Had Known",
            "paragraphs": [
                "Last year, I had a big opportunity. My company offered me a job in London. If I had accepted it, I would have moved to England. I would have learned so much and met amazing people. But I said no. I said no because my family was here and I didn't want to leave them. Now I sometimes think: if I had said yes, my life would be completely different.",
                "If I had more free time now, I would study more languages. I would learn Spanish and maybe Italian. If I were richer, I would travel the world. I would visit Japan, Australia and South America. If I had a bigger flat, I would have a home office and a small gym.",
                "But these are just dreams. In reality, if I want to change something, I need to start today. If I study English for one hour every day, I will speak fluently in two years. If I save money every month, I will travel next summer. If I exercise three times a week, I will feel better.",
                "My friend Tom always says: 'If you don't try, you will never know.' He is right. If I hadn't tried to change my career five years ago, I would still be unhappy. If I hadn't met my wife, I wouldn't have my wonderful children. Sometimes the best things happen when you take a risk.",
                "So here is my advice for you: If I were you, I would start today. Don't wait. If you wait for the perfect moment, it will never come. Unless you take action now, nothing will change. If you want something, go and get it. That is the only way."
            ]
        },

        "text_questions": [
            {"q": "What opportunity did the person have last year?", "options": ["A new car", "A job in London", "A house", "A holiday"], "correct": "A job in London"},
            {"q": "Why did the person say no?", "options": ["Didn't like London", "Family was here", "Salary was low", "Bad weather"], "correct": "Family was here"},
            {"q": "What would the person do if they had more free time?", "options": ["Sleep more", "Study languages", "Travel", "Work more"], "correct": "Study languages"},
            {"q": "What would the person do if they were richer?", "options": ["Buy a car", "Travel the world", "Move abroad", "Buy a house"], "correct": "Travel the world"},
            {"q": "How long does the person plan to study English every day?", "options": ["30 minutes", "One hour", "Two hours", "Three hours"], "correct": "One hour"},
            {"q": "What does the person's friend Tom always say?", "options": ["Money is everything", "If you don't try, you will never know", "Don't take risks", "Wait for the perfect moment"], "correct": "If you don't try, you will never know"},
            {"q": "What would have happened if the person hadn't changed career?", "options": ["Would be rich", "Would still be unhappy", "Would be in London", "Would have more friends"], "correct": "Would still be unhappy"},
            {"q": "What advice does the person give?", "options": ["Wait for the perfect moment", "If I were you, I would start today", "Don't take risks", "Stay in your comfort zone"], "correct": "If I were you, I would start today"},
            {"q": "What happens if you wait for the perfect moment?", "options": ["It comes", "It never comes", "It comes once", "It lasts forever"], "correct": "It never comes"},
            {"q": "What is the only way to get what you want?", "options": ["Wait", "Ask friends", "Go and get it", "Dream about it"], "correct": "Go and get it"}
        ],

        "test": [
            {"type": "choice", "q": "If it ___ tomorrow, I will stay home.", "options": ["will rain", "rains", "rained", "would rain"], "correct": "rains"},
            {"type": "choice", "q": "If I ___ more money, I would travel.", "options": ["have", "will have", "had", "would have"], "correct": "had"},
            {"type": "choice", "q": "If I ___ you, I would accept.", "options": ["was", "were", "am", "be"], "correct": "were"},
            {"type": "choice", "q": "If I had studied, I ___ the exam.", "options": ["would pass", "would have passed", "passed", "will pass"], "correct": "would have passed"},
            {"type": "choice", "q": "If you heat water, it ___.", "options": ["will boil", "boils", "boiled", "would boil"], "correct": "boils"},
            {"type": "choice", "q": "If I had known, I ___ you.", "options": ["would tell", "would have told", "told", "will tell"], "correct": "would have told"},
            {"type": "choice", "q": "___ you hurry, you will be late.", "options": ["If", "Unless", "When", "While"], "correct": "Unless"},
            {"type": "choice", "q": "I wish I ___ more time.", "options": ["have", "had", "will have", "would have"], "correct": "had"},
            {"type": "fill", "q": "If it ___ (rain), I will stay home.", "answer": "rains"},
            {"type": "fill", "q": "If I ___ (have) more money, I would travel.", "answer": "had"},
            {"type": "fill", "q": "If I ___ (be) you, I would accept.", "answer": "were"},
            {"type": "fill", "q": "If I ___ (study) harder, I would have passed.", "answer": "had studied"},
            {"type": "fill", "q": "If you ___ (heat) water, it boils.", "answer": "heat"},
            {"type": "fill", "q": "If I had known, I ___ (tell) you.", "answer": "would have told"},
            {"type": "fill", "q": "___ (Unless / If) you hurry, you will be late.", "answer": "Unless"},
            {"type": "error", "q": "Найди правильное:", "options": ["If it will rain, I will stay home", "If it rains, I will stay home", "If it rain, I will stay home", "If it would rain, I will stay home"], "correct": "If it rains, I will stay home"},
            {"type": "error", "q": "Найди правильное:", "options": ["If I would have money, I would travel", "If I had money, I would travel", "If I have money, I would travel", "If I will have money, I would travel"], "correct": "If I had money, I would travel"},
            {"type": "error", "q": "Найди правильное:", "options": ["If I was you, I would accept", "If I were you, I would accept", "If I am you, I would accept", "If I be you, I would accept"], "correct": "If I were you, I would accept"},
            {"type": "error", "q": "Найди правильное:", "options": ["If I had studied, I would pass", "If I had studied, I would have passed", "If I studied, I would have passed", "If I would study, I would have passed"], "correct": "If I had studied, I would have passed"},
            {"type": "error", "q": "Найди правильное:", "options": ["If I would have known, I would have told you", "If I had known, I would have told you", "If I knew, I would have told you", "If I have known, I would have told you"], "correct": "If I had known, I would have told you"},
            {"type": "translate", "q": "Переведи: Если пойдёт дождь, я останусь дома.", "answer": "If it rains, I will stay home"},
            {"type": "translate", "q": "Переведи: Если бы у меня было больше денег, я бы путешествовал.", "answer": "If I had more money, I would travel"},
            {"type": "translate", "q": "Переведи: На твоём месте я бы согласился.", "answer": "If I were you, I would accept"},
            {"type": "translate", "q": "Переведи: Если бы я знал раньше, я бы помог.", "answer": "If I had known, I would have helped"},
            {"type": "translate", "q": "Переведи: Если нагреть воду, она закипает.", "answer": "If you heat water, it boils"},
            {"type": "translate", "q": "Переведи: Если не поторопишься, опоздаешь.", "answer": "Unless you hurry, you will be late"},
            {"type": "write", "q": "Напиши 3-5 предложений на тему «Что бы я сделал, если бы у меня было больше времени / денег / возможностей».", "sample": "If I had more free time, I would learn to play the piano. I would also read more books and travel to new countries. If I were richer, I would buy a house near the sea and invite all my friends. If I had started learning English earlier, I would speak it fluently by now. But I know that if I start today and study every day, I will achieve my goals."}
        ]
    },

        # ═══════════════════════════════════════════
    # УРОК — PASSIVE VOICE (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "passive_voice",
        "title": "Пассивный залог",
        "emoji": "🎭",
        "level": "B1",
        "intro": "Пассивный залог — когда действие важнее, чем тот, кто его совершает. «Дом построили в 1990», «Письмо отправлено», «Машину украли». Одна из самых недооценённых тем: без неё ты не поймёшь новости, объявления, научные тексты и не сможешь звучать формально.",
        "why": "Пассивный залог — это «взгляд со стороны действия». В русском мы тоже используем пассив: «Дом строится», «Письмо было отправлено». В английском это делается через be + V3. Без пассива ты не поймёшь половину новостей (The law was passed yesterday), объявлений (English is spoken here), инструкций (The form must be filled in). Плюс пассив звучит формально и вежливо: вместо «Ты сломал вазу» — «Ваза была сломана». Если ты не освоишь пассив — будешь звучать по-детски в формальных ситуациях.",

        "rules": [
            {"h": "Что такое пассив", "text": "Активный залог: Кто-то делает что-то. The chef cooked the meal. (Шеф приготовил блюдо.) Пассивный: Что-то делается кем-то. The meal was cooked by the chef. (Блюдо было приготовлено шефом.) Акцент смещается с того, КТО делает, на то, ЧТО происходит."},
            {"h": "Как образуется", "text": "be + Past Participle (V3). Время глагола 'be' меняется, а V3 остаётся неизменным. Present Simple: The letter is written. Past Simple: The letter was written. Present Perfect: The letter has been written. Future: The letter will be written."},
            {"h": "Когда использовать", "text": "1) Исполнитель неизвестен: My car was stolen. 2) Исполнитель неважен: The bridge was built in 1990. 3) Исполнитель очевиден: He was arrested (полицией). 4) Формальный стиль: The report has been submitted. 5) В новостях: The law was passed yesterday."},
            {"h": "By — кем", "text": "Если нужно указать исполнителя, используем BY. The book was written by Tolstoy. The song was performed by the Beatles. Но в 80% случаев 'by' не нужен — исполнитель неважен."},
            {"h": "Пассив в Present Simple", "text": "am / is / are + V3. English is spoken all over the world. These cars are made in Germany. The office is cleaned every day."},
            {"h": "Пассив в Past Simple", "text": "was / were + V3. The house was built in 1990. The letters were sent yesterday. I was born in Russia (born — это пассив от bear)."},
            {"h": "Пассив в Present Perfect", "text": "have been / has been + V3. The project has been finished. The emails have been sent. The window has been broken."},
            {"h": "Пассив в Future Simple", "text": "will be + V3. The meeting will be held tomorrow. The results will be published soon. The decision will be made by the manager."},
            {"h": "Пассив с модальными глаголами", "text": "modal + be + V3. The form must be filled in. The work should be done today. The email can be sent later. This book may be interesting."},
            {"h": "Пассив в Continuous", "text": "is / are being + V3 (сейчас). was / were being + V3 (тогда). The road is being repaired. The house was being painted when I arrived."},
            {"h": "Пассив с 'get' (разговорный)", "text": "В разговорной речи вместо be используется get: I got fired. She got promoted. He got hit by a car. Это неформальный вариант, но очень частый."},
            {"h": "Безличный пассив", "text": "It is said that... It is believed that... It is known that... It is reported that... Используется в формальных текстах. It is said that he is a genius. It is believed that the Earth is round."},
            {"h": "Когда НЕ использовать пассив", "text": "1) С непереходными глаголами (нет объекта): нельзя 'was arrived', 'was happened'. 2) Когда исполнитель важен: I broke the vase — не The vase was broken by me. 3) В разговорной речи, если можно сказать активно."},
            {"h": "Активный vs пассивный — как выбрать", "text": "Актив: я делаю акцент на том, КТО делает. Пассив: я делаю акцент на том, ЧТО происходит. The chef cooked the meal (важен шеф). The meal was cooked (важно блюдо). Выбор зависит от того, что ты хочешь подчеркнуть."},
            {"h": "В русском и английском", "text": "В русском пассив образуется через 'быть' + краткое причастие: 'Дом построен', 'Письмо отправлено'. В английском — через be + V3. Логика похожа, но в английском пассив используется чаще, особенно в новостях и официальных текстах."}
        ],

        "tables": [
            {
                "title": "Пассив во всех временах",
                "headers": ["Время", "Формула", "Пример"],
                "rows": [
                    ["Present Simple", "am / is / are + V3", "The letter is written"],
                    ["Past Simple", "was / were + V3", "The letter was written"],
                    ["Present Perfect", "have / has been + V3", "The letter has been written"],
                    ["Past Perfect", "had been + V3", "The letter had been written"],
                    ["Future Simple", "will be + V3", "The letter will be written"],
                    ["Modal", "modal + be + V3", "The letter must be written"],
                    ["Present Continuous", "am / is / are being + V3", "The letter is being written"],
                    ["Past Continuous", "was / were being + V3", "The letter was being written"]
                ]
            },
            {
                "title": "Активный → Пассивный",
                "headers": ["Активный", "Пассивный", "Перевод"],
                "rows": [
                    ["The chef cooked the meal.", "The meal was cooked by the chef.", "Блюдо было приготовлено шефом"],
                    ["Someone stole my car.", "My car was stolen.", "Машину украли"],
                    ["They built the house in 1990.", "The house was built in 1990.", "Дом построили в 1990"],
                    ["People speak English everywhere.", "English is spoken everywhere.", "На английском говорят везде"],
                    ["They will publish the book.", "The book will be published.", "Книгу опубликуют"]
                ]
            },
            {
                "title": "Модальные глаголы + пассив",
                "headers": ["Модальный", "Формула", "Пример"],
                "rows": [
                    ["can", "can be + V3", "The email can be sent"],
                    ["must", "must be + V3", "The form must be filled"],
                    ["should", "should be + V3", "The work should be done"],
                    ["may", "may be + V3", "The book may be interesting"],
                    ["might", "might be + V3", "The results might be published"]
                ]
            },
            {
                "title": "Безличные конструкции",
                "headers": ["Фраза", "Перевод", "Пример"],
                "rows": [
                    ["It is said that...", "Говорят, что...", "It is said that he is rich"],
                    ["It is believed that...", "Считается, что...", "It is believed that the Earth is round"],
                    ["It is known that...", "Известно, что...", "It is known that smoking is bad"],
                    ["It is reported that...", "Сообщается, что...", "It is reported that the president is ill"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "The letter was wrote yesterday.", "right": "The letter was written yesterday.", "why": "После was/were — V3, не V2"},
            {"wrong": "The house is build in 1990.", "right": "The house was built in 1990.", "why": "Прошлое — was + V3"},
            {"wrong": "English speaks all over the world.", "right": "English is spoken all over the world.", "why": "Актив говорит о английском как о субъекте; нужно пассив"},
            {"wrong": "The work must done.", "right": "The work must be done.", "why": "Modal + be + V3, не просто V3"},
            {"wrong": "The project has finished.", "right": "The project has been finished.", "why": "Пассив в Perfect: has been + V3"},
            {"wrong": "I was borned in Russia.", "right": "I was born in Russia.", "why": "Born — уже V3 от bear, не borned"},
            {"wrong": "The email was send.", "right": "The email was sent.", "why": "Send → sent (V3), не send"},
            {"wrong": "The car is being repair.", "right": "The car is being repaired.", "why": "Continuous пассив: be being + V3"},
            {"wrong": "The book will published.", "right": "The book will be published.", "why": "Future пассив: will be + V3"},
            {"wrong": "The song was performed from the Beatles.", "right": "The song was performed by the Beatles.", "why": "Исполнитель — с 'by', не 'from'"},
            {"wrong": "It is say that he is rich.", "right": "It is said that he is rich.", "why": "It is said (V3), не it is say"},
            {"wrong": "The window has broke.", "right": "The window has been broken.", "why": "Пассив: has been + V3"}
        ],

        "lifehacks": [
            "Пассив = be + V3. Меняешь время только у 'be' — V3 никогда не меняется.",
            "Не знаешь, кто сделал — пассив. Кто сделал неважен — пассив. Кто очевиден — пассив.",
            "'By' указывает исполнителя. Но в 80% случаев он не нужен.",
            "It is said, it is believed — формальные фразы для новостей и эссе. Запомни их.",
            "Born — всегда пассив. I was born. She was born. He was born. Никогда не 'borned'.",
            "Если глагол непереходный (arrive, happen, come) — пассив невозможен. Нет объекта — нечего ставить в начало.",
            "В новостях 70% предложений — пассив. Читай BBC, CNN — увидишь."
        ],

        "text": {
            "title": "The Discovery of Penicillin",
            "paragraphs": [
                "Penicillin was discovered by Alexander Fleming in 1928. It was found almost by accident. Fleming was working in his laboratory when he noticed that some bacteria had been killed by a strange mould. He didn't understand what had happened at first.",
                "The discovery was published in a scientific journal, but at first it was ignored by most scientists. Years later, penicillin was developed into a medicine by Howard Florey and Ernst Chain. Their work was supported by the American and British governments during World War II.",
                "Penicillin has been used to save millions of lives. Before its discovery, many people died from simple infections. Today, this medicine is produced all over the world. It is still considered one of the most important medical discoveries of the 20th century.",
                "However, today many bacteria are becoming resistant to antibiotics. New medicines must be developed to fight them. If nothing is done, we may return to the time when simple infections cannot be cured. Scientists say that new antibiotics will be needed in the next 20 years.",
                "Fleming's work is still celebrated today. His laboratory has been turned into a museum. Books have been written about him, and films have been made. It is said that his discovery was accidental, but it was also the result of years of hard work."
            ]
        },

        "text_questions": [
            {"q": "Who discovered penicillin?", "options": ["Howard Florey", "Ernst Chain", "Alexander Fleming", "Louis Pasteur"], "correct": "Alexander Fleming"},
            {"q": "When was penicillin discovered?", "options": ["1908", "1918", "1928", "1938"], "correct": "1928"},
            {"q": "How was penicillin discovered?", "options": ["Planned", "Almost by accident", "By a group of scientists", "In a hospital"], "correct": "Almost by accident"},
            {"q": "What killed the bacteria in Fleming's lab?", "options": ["Heat", "Cold", "Mould", "Water"], "correct": "Mould"},
            {"q": "Who developed penicillin into a medicine?", "options": ["Fleming only", "Florey and Chain", "American scientists", "British scientists only"], "correct": "Florey and Chain"},
            {"q": "When was penicillin developed into a medicine?", "options": ["During WWI", "During WWII", "After 1990", "In 2000"], "correct": "During WWII"},
            {"q": "What has penicillin been used for?", "options": ["To save lives", "To make food", "To clean water", "To grow plants"], "correct": "To save lives"},
            {"q": "What happened to Fleming's laboratory?", "options": ["It was destroyed", "It was turned into a museum", "It was sold", "It's still a lab"], "correct": "It was turned into a museum"},
            {"q": "What is a problem today with antibiotics?", "options": ["They are expensive", "Bacteria are becoming resistant", "They don't work at all", "They are illegal"], "correct": "Bacteria are becoming resistant"},
            {"q": "What do scientists say about new antibiotics?", "options": ["They are not needed", "They will be needed in 20 years", "They already exist", "They are impossible to make"], "correct": "They will be needed in 20 years"}
        ],

        "test": [
            {"type": "choice", "q": "The letter ___ yesterday.", "options": ["wrote", "was written", "is written", "has written"], "correct": "was written"},
            {"type": "choice", "q": "English ___ all over the world.", "options": ["speaks", "is spoken", "was spoken", "has spoken"], "correct": "is spoken"},
            {"type": "choice", "q": "The project ___ already ___.", "options": ["has / finished", "has / been finished", "is / finished", "was / finished"], "correct": "has / been finished"},
            {"type": "choice", "q": "The form must ___ in.", "options": ["be filled", "fill", "be fill", "filled"], "correct": "be filled"},
            {"type": "choice", "q": "The meeting ___ tomorrow.", "options": ["will hold", "will be held", "is holding", "held"], "correct": "will be held"},
            {"type": "choice", "q": "The window ___ by the boys.", "options": ["broke", "was broken", "has broken", "is breaking"], "correct": "was broken"},
            {"type": "choice", "q": "The house ___ in 1990.", "options": ["built", "was built", "is built", "has built"], "correct": "was built"},
            {"type": "choice", "q": "The road ___ repaired right now.", "options": ["is", "is being", "was", "has been"], "correct": "is being"},
            {"type": "fill", "q": "The letter ___ (write) yesterday.", "answer": "was written"},
            {"type": "fill", "q": "English ___ (speak) all over the world.", "answer": "is spoken"},
            {"type": "fill", "q": "The project ___ (already / finish).", "answer": "has already been finished"},
            {"type": "fill", "q": "The form must ___ (fill) in.", "answer": "be filled"},
            {"type": "fill", "q": "The meeting ___ (hold) tomorrow.", "answer": "will be held"},
            {"type": "fill", "q": "The window ___ (break) by the boys.", "answer": "was broken"},
            {"type": "fill", "q": "The road ___ (repair) right now.", "answer": "is being repaired"},
            {"type": "error", "q": "Найди правильное:", "options": ["The letter was wrote yesterday", "The letter was written yesterday", "The letter was write yesterday", "The letter was writing yesterday"], "correct": "The letter was written yesterday"},
            {"type": "error", "q": "Найди правильное:", "options": ["English speaks all over the world", "English is spoken all over the world", "English was spoken all over the world", "English is speaking all over the world"], "correct": "English is spoken all over the world"},
            {"type": "error", "q": "Найди правильное:", "options": ["The project has finished", "The project has been finished", "The project is finished already", "The project finished"], "correct": "The project has been finished"},
            {"type": "error", "q": "Найди правильное:", "options": ["The form must fill in", "The form must be filled in", "The form must be fill in", "The form must filled in"], "correct": "The form must be filled in"},
            {"type": "error", "q": "Найди правильное:", "options": ["I was borned in Russia", "I was born in Russia", "I borned in Russia", "I am born in Russia"], "correct": "I was born in Russia"},
            {"type": "translate", "q": "Переведи: Письмо было отправлено вчера.", "answer": "The letter was sent yesterday"},
            {"type": "translate", "q": "Переведи: На английском говорят по всему миру.", "answer": "English is spoken all over the world"},
            {"type": "translate", "q": "Переведи: Проект уже закончен.", "answer": "The project has already been finished"},
            {"type": "translate", "q": "Переведи: Форму нужно заполнить.", "answer": "The form must be filled in"},
            {"type": "translate", "q": "Переведи: Дом был построен в 1990.", "answer": "The house was built in 1990"},
            {"type": "translate", "q": "Переведи: Говорят, что он богат.", "answer": "It is said that he is rich"},
            {"type": "write", "q": "Напиши 3-5 предложений на тему «Известное изобретение или открытие» с использованием пассива.", "sample": "The telephone was invented by Alexander Graham Bell in 1876. At first, it was not taken seriously by most people. Years later, it was developed into a device that changed the world. Today, billions of phones are produced every year. It is believed that the telephone is one of the most important inventions in history."}
        ]
    },

        # ═══════════════════════════════════════════
    # УРОК — REPORTED SPEECH (расширенный формат)
    # ═══════════════════════════════════════════
    {
        "id": "reported_speech",
        "title": "Косвенная речь",
        "emoji": "💬",
        "level": "B1",
        "intro": "Косвенная речь — как передать чужие слова, не цитируя их напрямую. «Он сказал, что устал» вместо «Он сказал: \"Я устал\"». Ключевая тема для B1: без неё ты не сможешь пересказать разговор, новость или чьё-то мнение.",
        "why": "Косвенная речь — это «пересказ» чужих слов. В жизни мы постоянно пересказываем: «Она сказала, что придёт позже», «Он спросил, где я живу». Без этой темы ты не сможешь передать чужую речь, а это огромный пласт языка. Особенно важно: при переводе из прямой речи в косвенную меняются времена, местоимения, время и место. Носители используют это постоянно. Если не освоишь — будешь путаться в «он сказал, что...» и говорить «He said that I am tired» вместо «He said that he was tired».",

        "rules": [
            {"h": "Что такое косвенная речь", "text": "Прямая речь (direct speech): He said, 'I am tired.' (Он сказал: «Я устал».) Косвенная (reported speech): He said that he was tired. (Он сказал, что устал.) В косвенной речи мы не цитируем, а пересказываем. Меняются времена, местоимения, время и место."},
            {"h": "Сдвиг времён (backshift)", "text": "Когда главный глагол в прошедшем (said, told), время в придаточном сдвигается НАЗАД: Present Simple → Past Simple. Present Continuous → Past Continuous. Past Simple → Past Perfect. Present Perfect → Past Perfect. Will → Would. Can → Could. May → Might. Must → Had to."},
            {"h": "Сдвиг — таблица", "text": "am / is → was. are → were. do / does → did. have / has → had. will → would. can → could. may → might. must → had to. Past Simple → Past Perfect. Present Perfect → Past Perfect."},
            {"h": "Местоимения", "text": "Местоимения меняются по смыслу: I → he / she. We → they. My → his / her. Our → their. You → I / he / she (зависит от контекста). Пример: 'I love my job', he said → He said he loved his job."},
            {"h": "Время и место", "text": "now → then. today → that day. tomorrow → the next day / the following day. yesterday → the day before / the previous day. last week → the week before. next week → the following week. here → there. this → that. these → those."},
            {"h": "Say vs Tell", "text": "SAY — без объекта: He said that he was tired. TELL — с объектом: He told me that he was tired. Нельзя 'He said me', нужно 'He told me'. SAY + to + человек допустимо: He said to me."},
            {"h": "Косвенные вопросы (Yes / No)", "text": "Прямой: 'Do you like coffee?' Косвенный: He asked if / whether I liked coffee. Меняем порядок слов на прямой, убираем do / does / did, добавляем if / whether. Не нужен вопросительный знак."},
            {"h": "Косвенные вопросы (Wh-)", "text": "Прямой: 'Where do you live?' Косвенный: He asked where I lived. Убираем do / does / did, ставим прямой порядок слов. What → what, where → where, when → when, why → why, how → how."},
            {"h": "Косвенные команды и просьбы", "text": "Прямой: 'Close the door!' Косвенный: He told me to close the door. Прямой: 'Please help me.' Косвенный: She asked me to help her. Tell + to + V (команда). Ask + to + V (просьба). Отрицание: tell + not to + V: He told me not to go."},
            {"h": "Когда НЕ сдвигаем времена", "text": "1) Если главный глагол в настоящем: He says he is tired. 2) Если говорим о факте, который всегда верен: He said that the Earth is round. 3) С модальными: would, could, should, might, ought to — не меняются. 4) Если указано точное время: He said he was born in 1995."},
            {"h": "That — можно опускать", "text": "В разговорной речи 'that' часто опускается: He said (that) he was tired. Оба варианта правильны. В формальном стиле 'that' чаще оставляют."},
            {"h": "Reported Speech в новостях", "text": "В новостях часто используют пассив + reported speech: It is reported that the president will visit France. The minister said that new laws would be introduced. Это стандартный стиль новостей."},
            {"h": "С указанием времени", "text": "Если в прямой речи было точное время (yesterday, last week, in 2020), сдвиг всё равно работает, но иногда можно сохранить указание: 'I saw him yesterday' → He said he had seen him the day before. Или He said he saw him yesterday (если говорим в тот же день)."},
            {"h": "Смешанные случаи", "text": "Иногда в одном предложении могут быть разные сдвиги. 'I am reading a book I bought yesterday', she said. → She said she was reading a book she had bought the day before. Каждое время сдвигается по своему правилу."},
            {"h": "Частые ошибки с русским", "text": "В русском мы сдвигаем времена реже: «Он сказал, что устал» — «устал» в прошедшем. В английском: 'I am tired' → He said he was tired. Запомни: главный глагол в прошедшем → время в придаточном сдвигается назад."}
        ],

        "tables": [
            {
                "title": "Сдвиг времён (backshift)",
                "headers": ["Прямая речь", "Косвенная речь", "Пример"],
                "rows": [
                    ["Present Simple", "Past Simple", "am → was"],
                    ["Present Continuous", "Past Continuous", "am doing → was doing"],
                    ["Past Simple", "Past Perfect", "did → had done"],
                    ["Present Perfect", "Past Perfect", "have done → had done"],
                    ["Past Perfect", "Past Perfect", "had done → had done"],
                    ["will", "would", "will do → would do"],
                    ["can", "could", "can do → could do"],
                    ["may", "might", "may do → might do"],
                    ["must", "had to", "must do → had to do"]
                ]
            },
            {
                "title": "Сдвиг времени и места",
                "headers": ["Прямая", "Косвенная"],
                "rows": [
                    ["now", "then"],
                    ["today", "that day"],
                    ["tomorrow", "the next day"],
                    ["yesterday", "the day before"],
                    ["last week", "the week before"],
                    ["next week", "the following week"],
                    ["here", "there"],
                    ["this", "that"],
                    ["these", "those"]
                ]
            },
            {
                "title": "Say vs Tell",
                "headers": ["Глагол", "Правильно", "Неправильно"],
                "rows": [
                    ["say", "He said (that) he was tired", "He said me"],
                    ["tell", "He told me (that) he was tired", "He told that he was tired"],
                    ["say to", "He said to me (that) he was tired", "—"],
                    ["ask", "He asked me if I was tired", "He asked that I was tired"]
                ]
            },
            {
                "title": "Косвенные вопросы",
                "headers": ["Прямой вопрос", "Косвенный"],
                "rows": [
                    ["Do you like coffee?", "He asked if I liked coffee"],
                    ["Where do you live?", "He asked where I lived"],
                    ["What are you doing?", "He asked what I was doing"],
                    ["Have you seen him?", "He asked if I had seen him"],
                    ["Will you come?", "He asked if I would come"]
                ]
            }
        ],

        "mistakes": [
            {"wrong": "He said me that he was tired.", "right": "He told me that he was tired.", "why": "Tell + объект, say без объекта"},
            {"wrong": "He said he is tired.", "right": "He said he was tired.", "why": "Backshift: is → was"},
            {"wrong": "He asked me where do I live.", "right": "He asked me where I lived.", "why": "В косвенном вопросе — прямой порядок слов, без do"},
            {"wrong": "She said she will come.", "right": "She said she would come.", "why": "Backshift: will → would"},
            {"wrong": "He told that he was tired.", "right": "He told me that he was tired.", "why": "Tell нужен объект (me, him, her)"},
            {"wrong": "He said I am reading.", "right": "He said he was reading.", "why": "И местоимение, и время меняются"},
            {"wrong": "She asked me if I like coffee.", "right": "She asked me if I liked coffee.", "why": "Backshift: like → liked"},
            {"wrong": "He asked where was I.", "right": "He asked where I was.", "why": "Прямой порядок слов в косвенном вопросе"},
            {"wrong": "She told me close the door.", "right": "She told me to close the door.", "why": "Tell + to + V (команда)"},
            {"wrong": "He asked me to not go.", "right": "He asked me not to go.", "why": "Отрицание: not + to + V"},
            {"wrong": "She said she had went there.", "right": "She said she had gone there.", "why": "Go → went → gone. После had — gone"},
            {"wrong": "He said that he can swim.", "right": "He said that he could swim.", "why": "Backshift: can → could"}
        ],

        "lifehacks": [
            "Запомни главное: главный глагол в прошедшем (said, told) → время в придаточном сдвигается НАЗАД на один шаг.",
            "Say — без 'me'. Tell — только с 'me / him / her'. Запомни раз и навсегда.",
            "В косвенных вопросах — всегда ПРЯМОЙ порядок слов. Никаких 'where do you' — только 'where you'.",
            "Меняются 4 вещи: время, местоимение, время-маркер (yesterday → the day before), место (here → there).",
            "If / whether — для вопросов 'да / нет'. Where / when / why — для Wh-вопросов.",
            "Команда: tell + to + V. Просьба: ask + to + V. Отрицание: not + to + V.",
            "Если в прямой речи был факт (Earth is round) — можно не сдвигать: He said the Earth is round."
        ],

        "text": {
            "title": "The Job Interview Story",
            "paragraphs": [
                "Yesterday my friend Tom told me about his job interview. He said that he had applied for a job at a big IT company. He said he was very nervous before the interview. 'I have never been so nervous in my life,' he told me.",
                "Tom said that the interviewer had asked him many questions. She asked him where he had studied and what he had done before. She also asked him if he had any experience with programming. Tom told her that he had been learning Python for two years.",
                "The interviewer asked him if he could start next week. Tom said that he could. She also asked him if he had any questions. He asked her what the company's main projects were. She told him that they were working on an AI project.",
                "At the end, the interviewer told Tom to wait for their answer by email. She said they would contact him within a week. Tom told me that he was feeling optimistic. He said that the interview had gone well.",
                "This morning Tom called me again. He said that he had received an email. They had offered him the job! He said he was so happy. He told me that he would start on Monday. 'I can't believe it,' he said. 'I am going to celebrate tonight!'"
            ]
        },

        "text_questions": [
            {"q": "Where did Tom apply for a job?", "options": ["A bank", "A big IT company", "A school", "A hospital"], "correct": "A big IT company"},
            {"q": "What language had Tom been learning?", "options": ["Java", "C++", "Python", "JavaScript"], "correct": "Python"},
            {"q": "What did the interviewer ask Tom about his studies?", "options": ["Where he had studied", "What he liked", "Why he wanted the job", "How old he was"], "correct": "Where he had studied"},
            {"q": "What did Tom ask the interviewer?", "options": ["About salary", "About main projects", "About holidays", "About dress code"], "correct": "About main projects"},
            {"q": "What project is the company working on?", "options": ["A game", "An AI project", "A website", "A mobile app"], "correct": "An AI project"},
            {"q": "How did the interviewer say they would contact Tom?", "options": ["By phone", "By email", "By letter", "In person"], "correct": "By email"},
            {"q": "How long did they say Tom should wait?", "options": ["One day", "Within a week", "One month", "Three days"], "correct": "Within a week"},
            {"q": "What happened the next morning?", "options": ["Tom got the job", "Tom was rejected", "Tom called the interviewer", "Tom forgot about it"], "correct": "Tom got the job"},
            {"q": "When will Tom start?", "options": ["Next week", "On Monday", "In a month", "Tomorrow"], "correct": "On Monday"},
            {"q": "How does Tom feel?", "options": ["Sad", "Nervous", "Happy", "Angry"], "correct": "Happy"}
        ],

        "test": [
            {"type": "choice", "q": "'I am tired,' he said. → He said he ___ tired.", "options": ["is", "was", "were", "will be"], "correct": "was"},
            {"type": "choice", "q": "'I will call you,' she said. → She said she ___ call me.", "options": ["will", "would", "can", "could"], "correct": "would"},
            {"type": "choice", "q": "'Do you like tea?' he asked. → He asked if I ___ tea.", "options": ["like", "liked", "am liking", "will like"], "correct": "liked"},
            {"type": "choice", "q": "'Where do you live?' she asked. → She asked where I ___.", "options": ["live", "do live", "lived", "am living"], "correct": "lived"},
            {"type": "choice", "q": "'Close the door!' he said. → He told me ___ the door.", "options": ["close", "to close", "closing", "closed"], "correct": "to close"},
            {"type": "choice", "q": "'I have finished,' he said. → He said he ___ finished.", "options": ["has", "had", "have", "was"], "correct": "had"},
            {"type": "choice", "q": "'Can you help?' she asked. → She asked if I ___ help.", "options": ["can", "could", "will", "would"], "correct": "could"},
            {"type": "choice", "q": "He ___ me that he was busy.", "options": ["said", "told", "spoke", "talked"], "correct": "told"},
            {"type": "fill", "q": "'I am reading,' he said. → He said he ___ reading.", "answer": "was"},
            {"type": "fill", "q": "'I will come,' she said. → She said she ___ come.", "answer": "would"},
            {"type": "fill", "q": "'Do you speak English?' he asked. → He asked if I ___ English.", "answer": "spoke"},
            {"type": "fill", "q": "'Where is the bank?' she asked. → She asked where the bank ___.", "answer": "was"},
            {"type": "fill", "q": "'Help me!' he said. → He asked me ___ him.", "answer": "to help"},
            {"type": "fill", "q": "'I have seen him,' she said. → She said she ___ seen him.", "answer": "had"},
            {"type": "error", "q": "Найди правильное:", "options": ["He said me that he was tired", "He told me that he was tired", "He said to me that he is tired", "He told that he was tired"], "correct": "He told me that he was tired"},
            {"type": "error", "q": "Найди правильное:", "options": ["He said he is tired", "He said he was tired", "He says he was tired", "He said he were tired"], "correct": "He said he was tired"},
            {"type": "error", "q": "Найди правильное:", "options": ["He asked me where do I live", "He asked me where I lived", "He asked me where I live", "He asked me where did I live"], "correct": "He asked me where I lived"},
            {"type": "error", "q": "Найди правильное:", "options": ["She said she will come", "She said she would come", "She said she come", "She said she was come"], "correct": "She said she would come"},
            {"type": "error", "q": "Найди правильное:", "options": ["He told me close the door", "He told me to close the door", "He told me closing the door", "He said me close the door"], "correct": "He told me to close the door"},
            {"type": "translate", "q": "Переведи: Он сказал, что устал.", "answer": "He said that he was tired"},
            {"type": "translate", "q": "Переведи: Она спросила, где я живу.", "answer": "She asked where I lived"},
            {"type": "translate", "q": "Переведи: Он сказал мне закрыть дверь.", "answer": "He told me to close the door"},
            {"type": "translate", "q": "Переведи: Она спросила, люблю ли я кофе.", "answer": "She asked if I liked coffee"},
            {"type": "translate", "q": "Переведи: Он сказал, что приедет завтра.", "answer": "He said he would come the next day"},
            {"type": "translate", "q": "Переведи: Том сказал, что закончил проект.", "answer": "Tom said that he had finished the project"},
            {"type": "write", "q": "Напиши 3-5 предложений — пересказ любого короткого разговора в косвенной речи.", "sample": "Yesterday my friend asked me if I wanted to go to the cinema. I told her that I was busy, but I said I could go on Saturday. She asked what film I wanted to see. I told her I had heard about a new comedy. She said she would buy the tickets online. She also told me not to be late."}
        ]
    },
]
