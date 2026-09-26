# ─── КАТЕГОРИИ ───

SECTIONS = [
    {"id": "family", "title": "Family", "emoji": "👨‍👩‍👧", "level": "A1-A2"},
    {"id": "home", "title": "Home", "emoji": "🏠", "level": "A1-A2"},
    {"id": "routine", "title": "Daily Routine", "emoji": "⏰", "level": "A1-A2"},
    {"id": "food", "title": "Food", "emoji": "🍔", "level": "A1-A2"},
    {"id": "clothes", "title": "Clothes", "emoji": "👕", "level": "A1-A2"},
    {"id": "appearance", "title": "Appearance", "emoji": "👤", "level": "A1-A2"},
    {"id": "weather", "title": "Weather", "emoji": "☀️", "level": "A1-A2"},
    {"id": "transport", "title": "Transport", "emoji": "🚗", "level": "A1-A2"},
    {"id": "work", "title": "Work", "emoji": "💼", "level": "A1-A2"},
    {"id": "health", "title": "Health", "emoji": "💊", "level": "A1-A2"},
    {"id": "shopping", "title": "Shopping", "emoji": "🛒", "level": "A1-A2"},
    {"id": "holidays", "title": "Holidays", "emoji": "🏖️", "level": "A1-A2"},
    {"id": "feelings", "title": "Feelings", "emoji": "😊", "level": "B1"},
    {"id": "character", "title": "Character", "emoji": "🎭", "level": "B1"},
    {"id": "relationships", "title": "Relationships", "emoji": "💕", "level": "B1"},
    {"id": "communication", "title": "Communication", "emoji": "💬", "level": "B1"},
    {"id": "money", "title": "Money & Business", "emoji": "💰", "level": "B1"},
    {"id": "technology", "title": "Technology", "emoji": "💻", "level": "B1"},
    {"id": "education", "title": "Education", "emoji": "🎓", "level": "B1"},
    {"id": "media", "title": "Media", "emoji": "📰", "level": "B1"},
    {"id": "city", "title": "City & Town", "emoji": "🏙️", "level": "B1"},
    {"id": "nature", "title": "Nature", "emoji": "🌳", "level": "B1"},
    {"id": "time", "title": "Time", "emoji": "🕐", "level": "B1"},
    {"id": "housework", "title": "Housework", "emoji": "🧹", "level": "B1"},
    {"id": "business", "title": "Business & Negotiations", "emoji": "🤝", "level": "B2+"},
    {"id": "politics", "title": "Politics & Law", "emoji": "⚖️", "level": "B2+"},
    {"id": "environment", "title": "Environment", "emoji": "🌍", "level": "B2+"},
    {"id": "art", "title": "Art & Culture", "emoji": "🎨", "level": "B2+"},
    {"id": "science", "title": "Science", "emoji": "🔬", "level": "B2+"},
    {"id": "general", "title": "Общее", "emoji": "📦", "level": "general"},
]


def get_section(sid):
    return next((s for s in SECTIONS if s["id"] == sid), SECTIONS[-1])


# ─── ЦИТАТЫ ДНЯ ───

QUOTES = [
    {"text": "The limits of my language mean the limits of my world.", "author": "Ludwig Wittgenstein"},
    {"text": "Learning is a treasure that will follow its owner everywhere.", "author": "Chinese Proverb"},
    {"text": "The more that you read, the more things you will know.", "author": "Dr. Seuss"},
    {"text": "To have another language is to possess a second soul.", "author": "Charlemagne"},
    {"text": "Language is the road map of a culture.", "author": "Rita Mae Brown"},
    {"text": "A different language is a different vision of life.", "author": "Federico Fellini"},
    {"text": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"text": "Success is the sum of small efforts repeated day in and day out.", "author": "Robert Collier"},
    {"text": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"text": "Education is the most powerful weapon which you can use to change the world.", "author": "Nelson Mandela"},
    {"text": "The journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
    {"text": "Knowledge is power.", "author": "Francis Bacon"},
    {"text": "Practice makes perfect.", "author": "English Proverb"},
    {"text": "Where there is a will, there is a way.", "author": "English Proverb"},
    {"text": "Every day is a chance to get better.", "author": "Unknown"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "A word a day keeps the ignorance away.", "author": "Unknown"},
]


# ─── НЕПРАВИЛЬНЫЕ ГЛАГОЛЫ ───

IRREGULAR_VERBS = [
    {"base": "be", "past": "was/were", "pp": "been", "rus": "быть"},
    {"base": "become", "past": "became", "pp": "become", "rus": "становиться"},
    {"base": "begin", "past": "began", "pp": "begun", "rus": "начинать"},
    {"base": "break", "past": "broke", "pp": "broken", "rus": "ломать"},
    {"base": "bring", "past": "brought", "pp": "brought", "rus": "приносить"},
    {"base": "build", "past": "built", "pp": "built", "rus": "строить"},
    {"base": "buy", "past": "bought", "pp": "bought", "rus": "покупать"},
    {"base": "catch", "past": "caught", "pp": "caught", "rus": "ловить"},
    {"base": "choose", "past": "chose", "pp": "chosen", "rus": "выбирать"},
    {"base": "come", "past": "came", "pp": "come", "rus": "приходить"},
    {"base": "cost", "past": "cost", "pp": "cost", "rus": "стоить"},
    {"base": "cut", "past": "cut", "pp": "cut", "rus": "резать"},
    {"base": "do", "past": "did", "pp": "done", "rus": "делать"},
    {"base": "draw", "past": "drew", "pp": "drawn", "rus": "рисовать"},
    {"base": "drink", "past": "drank", "pp": "drunk", "rus": "пить"},
    {"base": "drive", "past": "drove", "pp": "driven", "rus": "водить"},
    {"base": "eat", "past": "ate", "pp": "eaten", "rus": "есть"},
    {"base": "fall", "past": "fell", "pp": "fallen", "rus": "падать"},
    {"base": "feel", "past": "felt", "pp": "felt", "rus": "чувствовать"},
    {"base": "fight", "past": "fought", "pp": "fought", "rus": "бороться"},
    {"base": "find", "past": "found", "pp": "found", "rus": "находить"},
    {"base": "fly", "past": "flew", "pp": "flown", "rus": "летать"},
    {"base": "forget", "past": "forgot", "pp": "forgotten", "rus": "забывать"},
    {"base": "get", "past": "got", "pp": "got/gotten", "rus": "получать"},
    {"base": "give", "past": "gave", "pp": "given", "rus": "давать"},
    {"base": "go", "past": "went", "pp": "gone", "rus": "идти"},
    {"base": "grow", "past": "grew", "pp": "grown", "rus": "расти"},
    {"base": "have", "past": "had", "pp": "had", "rus": "иметь"},
    {"base": "hear", "past": "heard", "pp": "heard", "rus": "слышать"},
    {"base": "hold", "past": "held", "pp": "held", "rus": "держать"},
    {"base": "keep", "past": "kept", "pp": "kept", "rus": "хранить"},
    {"base": "know", "past": "knew", "pp": "known", "rus": "знать"},
    {"base": "leave", "past": "left", "pp": "left", "rus": "уходить"},
    {"base": "lose", "past": "lost", "pp": "lost", "rus": "терять"},
    {"base": "make", "past": "made", "pp": "made", "rus": "делать"},
    {"base": "meet", "past": "met", "pp": "met", "rus": "встречать"},
    {"base": "pay", "past": "paid", "pp": "paid", "rus": "платить"},
    {"base": "put", "past": "put", "pp": "put", "rus": "класть"},
    {"base": "read", "past": "read", "pp": "read", "rus": "читать"},
    {"base": "ride", "past": "rode", "pp": "ridden", "rus": "ехать"},
    {"base": "run", "past": "ran", "pp": "run", "rus": "бегать"},
    {"base": "say", "past": "said", "pp": "said", "rus": "говорить"},
    {"base": "see", "past": "saw", "pp": "seen", "rus": "видеть"},
    {"base": "sell", "past": "sold", "pp": "sold", "rus": "продавать"},
    {"base": "send", "past": "sent", "pp": "sent", "rus": "отправлять"},
    {"base": "sing", "past": "sang", "pp": "sung", "rus": "петь"},
    {"base": "sit", "past": "sat", "pp": "sat", "rus": "сидеть"},
    {"base": "sleep", "past": "slept", "pp": "slept", "rus": "спать"},
    {"base": "speak", "past": "spoke", "pp": "spoken", "rus": "говорить"},
    {"base": "spend", "past": "spent", "pp": "spent", "rus": "тратить"},
    {"base": "stand", "past": "stood", "pp": "stood", "rus": "стоять"},
    {"base": "swim", "past": "swam", "pp": "swum", "rus": "плавать"},
    {"base": "take", "past": "took", "pp": "taken", "rus": "брать"},
    {"base": "teach", "past": "taught", "pp": "taught", "rus": "учить"},
    {"base": "tell", "past": "told", "pp": "told", "rus": "рассказывать"},
    {"base": "think", "past": "thought", "pp": "thought", "rus": "думать"},
    {"base": "understand", "past": "understood", "pp": "understood", "rus": "понимать"},
    {"base": "wake", "past": "woke", "pp": "woken", "rus": "просыпаться"},
    {"base": "wear", "past": "wore", "pp": "worn", "rus": "носить"},
    {"base": "win", "past": "won", "pp": "won", "rus": "побеждать"},
    {"base": "write", "past": "wrote", "pp": "written", "rus": "писать"},
]


# ─── ФРАЗОВЫЕ ГЛАГОЛЫ ───

PHRASAL_VERBS = [
    {"phrase": "give up", "rus": "бросить", "example": "I gave up smoking."},
    {"phrase": "look after", "rus": "заботиться", "example": "She looks after her sister."},
    {"phrase": "run out of", "rus": "закончиться", "example": "We ran out of milk."},
    {"phrase": "find out", "rus": "выяснить", "example": "I found out the truth."},
    {"phrase": "come back", "rus": "вернуться", "example": "He came back home."},
    {"phrase": "go on", "rus": "продолжать", "example": "Go on, tell me!"},
    {"phrase": "turn off", "rus": "выключить", "example": "Turn off the light."},
    {"phrase": "turn on", "rus": "включить", "example": "Turn on the TV."},
    {"phrase": "put on", "rus": "надеть", "example": "Put on your coat."},
    {"phrase": "take off", "rus": "снять", "example": "Take off your shoes."},
    {"phrase": "wake up", "rus": "проснуться", "example": "I wake up at 7."},
    {"phrase": "get up", "rus": "встать", "example": "Get up, sleepyhead!"},
    {"phrase": "sit down", "rus": "сесть", "example": "Sit down, please."},
    {"phrase": "stand up", "rus": "встать", "example": "Stand up straight."},
    {"phrase": "come in", "rus": "войти", "example": "Come in!"},
    {"phrase": "go out", "rus": "выйти", "example": "We go out on Fridays."},
    {"phrase": "look for", "rus": "искать", "example": "I'm looking for my keys."},
    {"phrase": "look forward to", "rus": "ждать с нетерпением", "example": "I look forward to seeing you."},
    {"phrase": "give back", "rus": "вернуть", "example": "Give back my book."},
    {"phrase": "take care of", "rus": "заботиться", "example": "Take care of yourself."},
    {"phrase": "get along with", "rus": "ладить", "example": "I get along with my brother."},
    {"phrase": "break down", "rus": "сломаться", "example": "My car broke down."},
    {"phrase": "carry on", "rus": "продолжать", "example": "Carry on with your work."},
    {"phrase": "check out", "rus": "проверить", "example": "Check out this song."},
    {"phrase": "figure out", "rus": "разобраться", "example": "I figured out the puzzle."},
    {"phrase": "grow up", "rus": "вырасти", "example": "I grew up in Moscow."},
    {"phrase": "hang out", "rus": "тусоваться", "example": "Let's hang out tomorrow."},
    {"phrase": "hold on", "rus": "подождать", "example": "Hold on a second."},
    {"phrase": "keep on", "rus": "продолжать", "example": "Keep on trying."},
    {"phrase": "move on", "rus": "двигаться дальше", "example": "Let's move on."},
    {"phrase": "pick up", "rus": "подобрать", "example": "Pick up the phone."},
    {"phrase": "point out", "rus": "указать", "example": "He pointed out my mistake."},
    {"phrase": "put off", "rus": "отложить", "example": "Put off the meeting."},
    {"phrase": "set up", "rus": "установить", "example": "Set up the tent."},
    {"phrase": "show up", "rus": "появиться", "example": "He showed up late."},
    {"phrase": "take over", "rus": "взять контроль", "example": "She took over the project."},
    {"phrase": "throw away", "rus": "выбросить", "example": "Throw away the trash."},
    {"phrase": "try on", "rus": "примерить", "example": "Try on this dress."},
    {"phrase": "work out", "rus": "тренироваться", "example": "I work out every day."},
    {"phrase": "write down", "rus": "записать", "example": "Write down the address."},
]


# ─── ИДИОМЫ ───

IDIOMS = [
    {"idiom": "break a leg", "rus": "ни пуха, ни пера", "literal": "сломай ногу"},
    {"idiom": "piece of cake", "rus": "проще простого", "literal": "кусок торта"},
    {"idiom": "hit the books", "rus": "засесть за учёбу", "literal": "ударить книги"},
    {"idiom": "under the weather", "rus": "неважно себя чувствовать", "literal": "под погодой"},
    {"idiom": "once in a blue moon", "rus": "очень редко", "literal": "раз в голубую луну"},
    {"idiom": "spill the beans", "rus": "проболтаться", "literal": "пролить бобы"},
    {"idiom": "cost an arm and a leg", "rus": "стоить очень дорого", "literal": "стоить руку и ногу"},
    {"idiom": "let the cat out of the bag", "rus": "раскрыть секрет", "literal": "выпустить кота из мешка"},
    {"idiom": "kill two birds with one stone", "rus": "убить двух зайцев", "literal": "убить двух птиц одним камнем"},
    {"idiom": "the ball is in your court", "rus": "твой ход", "literal": "мяч на твоём корте"},
    {"idiom": "bite the bullet", "rus": "стиснуть зубы", "literal": "укусить пулю"},
    {"idiom": "break the ice", "rus": "растопить лёд", "literal": "сломать лёд"},
    {"idiom": "cut corners", "rus": "халтурить", "literal": "резать углы"},
    {"idiom": "hit the sack", "rus": "пойти спать", "literal": "ударить мешок"},
    {"idiom": "it's raining cats and dogs", "rus": "льёт как из ведра", "literal": "дождь из кошек и собак"},
    {"idiom": "let sleeping dogs lie", "rus": "не буди лихо", "literal": "дай спящим собакам лежать"},
    {"idiom": "miss the boat", "rus": "упустить шанс", "literal": "пропустить лодку"},
    {"idiom": "on cloud nine", "rus": "на седьмом небе", "literal": "на девятом облаке"},
    {"idiom": "pull yourself together", "rus": "возьми себя в руки", "literal": "собери себя вместе"},
    {"idiom": "see eye to eye", "rus": "сходиться во мнениях", "literal": "видеть глаз в глаз"},
    {"idiom": "sit on the fence", "rus": "занимать нейтралитет", "literal": "сидеть на заборе"},
    {"idiom": "take it easy", "rus": "не напрягайся", "literal": "принимай это легко"},
    {"idiom": "the last straw", "rus": "последняя капля", "literal": "последняя соломинка"},
    {"idiom": "time flies", "rus": "время летит", "literal": "время летает"},
    {"idiom": "under your nose", "rus": "прямо под носом", "literal": "под твоим носом"},
    {"idiom": "when pigs fly", "rus": "когда рак на горе свистнет", "literal": "когда свиньи полетят"},
    {"idiom": "you can't judge a book by its cover", "rus": "не суди по обложке", "literal": "нельзя судить книгу по обложке"},
    {"idiom": "actions speak louder than words", "rus": "дела говорят громче слов", "literal": "действия говорят громче слов"},
    {"idiom": "better late than never", "rus": "лучше поздно, чем никогда", "literal": "лучше поздно, чем никогда"},
    {"idiom": "easier said than done", "rus": "легко сказать, да трудно сделать", "literal": "легче сказать, чем сделать"},
]


# ─── ЛОЖНЫЕ ДРУЗЬЯ ПЕРЕВОДЧИКА ───

FALSE_FRIENDS = [
    {"word": "magazine", "false_ru": "магазин", "real_ru": "журнал", "example": "I read a magazine."},
    {"word": "accurate", "false_ru": "аккуратный", "real_ru": "точный", "example": "Accurate data is important."},
    {"word": "actually", "false_ru": "актуально", "real_ru": "на самом деле", "example": "Actually, I disagree."},
    {"word": "artist", "false_ru": "артист", "real_ru": "художник", "example": "She is a famous artist."},
    {"word": "cabinet", "false_ru": "кабинет", "real_ru": "шкаф", "example": "Put it in the cabinet."},
    {"word": "data", "false_ru": "дата", "real_ru": "данные", "example": "The data is ready."},
    {"word": "fabric", "false_ru": "фабрика", "real_ru": "ткань", "example": "Soft fabric feels nice."},
    {"word": "intelligent", "false_ru": "интеллигентный", "real_ru": "умный", "example": "He is intelligent."},
    {"word": "killer", "false_ru": "киллер", "real_ru": "убийца", "example": "The killer was caught."},
    {"word": "lunatic", "false_ru": "лунатик", "real_ru": "сумасшедший", "example": "He drives like a lunatic."},
    {"word": "patron", "false_ru": "патрон", "real_ru": "покровитель, клиент", "example": "He is a regular patron."},
    {"word": "prospect", "false_ru": "проспект", "real_ru": "перспектива", "example": "Good job prospects."},
    {"word": "replica", "false_ru": "реплика", "real_ru": "копия", "example": "It's a replica of the painting."},
    {"word": "spectacles", "false_ru": "спектакль", "real_ru": "очки", "example": "He wears spectacles."},
    {"word": "sympathy", "false_ru": "симпатия", "real_ru": "сочувствие", "example": "I have sympathy for her."},
    {"word": "toxic", "false_ru": "токсичный", "real_ru": "ядовитый", "example": "Toxic waste is dangerous."},
    {"word": "velvet", "false_ru": "вельвет", "real_ru": "бархат", "example": "A velvet dress."},
    {"word": "warehouse", "false_ru": "варенье", "real_ru": "склад", "example": "The warehouse is full."},
    {"word": "argument", "false_ru": "аргумент", "real_ru": "спор, ссора", "example": "We had an argument."},
    {"word": "biscuit", "false_ru": "бисквит", "real_ru": "печенье", "example": "Have a biscuit."},
    {"word": "brilliant", "false_ru": "бриллиант", "real_ru": "блестящий, гениальный", "example": "A brilliant idea!"},
    {"word": "clay", "false_ru": "клей", "real_ru": "глина", "example": "Clay is used for pottery."},
    {"word": "comfort", "false_ru": "комфорт", "real_ru": "утешение, покой", "example": "Words of comfort."},
    {"word": "complexion", "false_ru": "комплекция", "real_ru": "цвет лица", "example": "A pale complexion."},
    {"word": "decade", "false_ru": "декада", "real_ru": "десятилетие", "example": "A decade passed."},
    {"word": "deposition", "false_ru": "депозит", "real_ru": "показания (в суде)", "example": "He gave a deposition."},
    {"word": "direction", "false_ru": "дирекция", "real_ru": "направление", "example": "Which direction?"},
    {"word": "diversion", "false_ru": "диверсия", "real_ru": "отвлечение, объезд", "example": "A traffic diversion."},
    {"word": "exam", "false_ru": "экзамен (так и есть)", "real_ru": "экзамен", "example": "I passed the exam."},
    {"word": "familiar", "false_ru": "фамильярный", "real_ru": "знакомый", "example": "A familiar face."},
    {"word": "gallon", "false_ru": "галон", "real_ru": "галлон (мера)", "example": "A gallon of milk."},
    {"word": "genial", "false_ru": "гениальный", "real_ru": "добродушный", "example": "A genial host."},
    {"word": "humor", "false_ru": "юмор", "real_ru": "юмор, настроение", "example": "Good sense of humor."},
    {"word": "insurance", "false_ru": "инсценировка", "real_ru": "страховка", "example": "Car insurance."},
    {"word": "list", "false_ru": "лист", "real_ru": "список", "example": "Make a list."},
    {"word": "liquor", "false_ru": "ликёр", "real_ru": "крепкий алкоголь", "example": "He sells liquor."},
    {"word": "marmalade", "false_ru": "мармелад", "real_ru": "апельсиновое варенье", "example": "Orange marmalade."},
    {"word": "obligation", "false_ru": "облигация", "real_ru": "обязательство", "example": "A moral obligation."},
    {"word": "officer", "false_ru": "офицер (так и есть)", "real_ru": "офицер, чиновник", "example": "A police officer."},
    {"word": "paragraph", "false_ru": "параграф", "real_ru": "абзац", "example": "Read the first paragraph."},
    {"word": "particular", "false_ru": "партикулярный", "real_ru": "конкретный, особый", "example": "In this particular case."},
    {"word": "photograph", "false_ru": "фотограф", "real_ru": "фотография", "example": "Take a photograph."},
    {"word": "principal", "false_ru": "принципал", "real_ru": "главный, директор школы", "example": "The school principal."},
    {"word": "reception", "false_ru": "рецепция (так и есть)", "real_ru": "приём, стойка", "example": "At the reception."},
    {"word": "reproduction", "false_ru": "репродукция", "real_ru": "воспроизведение", "example": "Sound reproduction."},
    {"word": "satin", "false_ru": "сатин", "real_ru": "атлас", "example": "A satin dress."},
    {"word": "serviette", "false_ru": "серветка", "real_ru": "салфетка", "example": "A paper serviette."},
    {"word": "speculation", "false_ru": "спекуляция", "real_ru": "предположение", "example": "Pure speculation."},
    {"word": "tribune", "false_ru": "трибуна", "real_ru": "народный защитник", "example": "A people's tribune."},
    {"word": "utilize", "false_ru": "утилизировать", "real_ru": "использовать", "example": "Utilize resources."},
]


# ─── СЛЕНГ И РАЗГОВОРНЫЕ ВЫРАЖЕНИЯ ───

SLANG = [
    {"word": "gonna", "rus": "собираюсь (going to)", "example": "I'm gonna call you."},
    {"word": "wanna", "rus": "хочу (want to)", "example": "I wanna go home."},
    {"word": "gotta", "rus": "должен (got to)", "example": "I gotta run."},
    {"word": "ain't", "rus": "не есть (am/is/are not)", "example": "I ain't ready."},
    {"word": "dunno", "rus": "не знаю (don't know)", "example": "I dunno, man."},
    {"word": "kinda", "rus": "вроде (kind of)", "example": "It's kinda cool."},
    {"word": "sorta", "rus": "типа (sort of)", "example": "I sorta like it."},
    {"word": "y'all", "rus": "вы все (you all)", "example": "How y'all doing?"},
    {"word": "cool", "rus": "крутой, классный", "example": "That's cool!"},
    {"word": "awesome", "rus": "офигенный", "example": "Awesome job!"},
    {"word": "lit", "rus": "отпад, огонь", "example": "That party was lit."},
    {"word": "epic", "rus": "эпичный", "example": "An epic fail."},
    {"word": "chill", "rus": "расслабься, спокойно", "example": "Just chill, man."},
    {"word": "hang out", "rus": "тусоваться", "example": "Let's hang out."},
    {"word": "chick", "rus": "девчонка (разг.)", "example": "She's a cool chick."},
    {"word": "dude", "rus": "чувак", "example": "Hey dude!"},
    {"word": "bro", "rus": "братан", "example": "What's up, bro?"},
    {"word": "mate", "rus": "приятель (брит.)", "example": "Alright, mate?"},
    {"word": "buddy", "rus": "дружок", "example": "Hey buddy!"},
    {"word": "pal", "rus": "товарищ", "example": "He's my pal."},
    {"word": "stuff", "rus": "штуки, вещи (разг.)", "example": "Where's my stuff?"},
    {"word": "thing", "rus": "штука, дело (разг.)", "example": "That thing is cool."},
    {"word": "guy", "rus": "парень", "example": "That guy is funny."},
    {"word": "kid", "rus": "ребёнок, парень (разг.)", "example": "That kid is smart."},
    {"word": "no way", "rus": "да ладно, не может быть", "example": "No way! Really?"},
    {"word": "shut up", "rus": "заткнись (разг.)", "example": "Shut up, seriously?"},
    {"word": "my bad", "rus": "моя вина", "example": "My bad, sorry."},
    {"word": "no worries", "rus": "без проблем", "example": "No worries, mate."},
    {"word": "you bet", "rus": "конечно", "example": "You bet I will!"},
    {"word": "what's up", "rus": "чё как, что нового", "example": "What's up, dude?"},
    {"word": "catch you later", "rus": "до связи", "example": "Catch you later!"},
    {"word": "hit me up", "rus": "набери меня, пиши", "example": "Hit me up later."},
    {"word": "bail", "rus": "свалить, отмазаться", "example": "He bailed on us."},
    {"word": "freak out", "rus": "паниковать, сходить с ума", "example": "Don't freak out!"},
    {"word": "screw up", "rus": "налажать", "example": "I screwed up."},
    {"word": "chill out", "rus": "успокойся", "example": "Chill out, bro."},
    {"word": "knock it off", "rus": "прекрати", "example": "Knock it off!"},
    {"word": "give a hand", "rus": "помочь", "example": "Give me a hand."},
    {"word": "not my cup of tea", "rus": "не моё", "example": "Horror is not my cup of tea."},
    {"word": "piece of cake", "rus": "проще простого", "example": "Easy, piece of cake."},
]


# ─── ФИКСИРОВАННЫЕ ТОПИКИ ───

FIXED_TOPICS = [
    {
        "id": "my_day", "title": "My Day", "emoji": "☀️",
        "helper": ["wake up", "breakfast", "work", "evening", "sleep", "morning", "lunch", "dinner"],
        "example": "I wake up at 7 in the morning. I have breakfast and go to work. In the afternoon I have lunch with my colleagues. In the evening I come home, have dinner and watch TV. I go to bed at 11 pm. My day is busy but I like it."
    },
    {
        "id": "my_family", "title": "My Family", "emoji": "👨‍👩‍👧",
        "helper": ["mother", "father", "brother", "sister", "love", "home", "parents", "children"],
        "example": "My family is not very big. I have a mother, a father and a younger sister. We live together in a flat. My mother is a doctor and my father is an engineer. We love each other and spend a lot of time together. On weekends we go for a walk or watch films."
    },
    {
        "id": "my_hobbies", "title": "My Hobbies", "emoji": "🎮",
        "helper": ["play", "read", "music", "sport", "game", "draw", "sing", "dance"],
        "example": "I have several hobbies. I like to read books and play computer games. In summer I ride a bike and swim in the lake. I also listen to music every day. Music helps me relax after a long day. My favourite hobby is reading, because it opens new worlds."
    },
    {
        "id": "my_city", "title": "My City", "emoji": "🏙️",
        "helper": ["street", "park", "shop", "museum", "beautiful", "big", "small", "center"],
        "example": "I live in a big city. There are many streets, parks and shops. In the city centre you can find museums and theatres. My favourite place is the central park. I like to walk there with my friends. The city is beautiful, especially at night with all the lights."
    },
    {
        "id": "my_dreams", "title": "My Dreams", "emoji": "💭",
        "helper": ["want", "future", "travel", "family", "success", "dream", "hope", "believe"],
        "example": "I have many dreams. I want to travel around the world and see new places. In the future I hope to have a big family and a good job. I believe that if you work hard, your dreams come true. My biggest dream is to visit Japan. I hope one day it will happen."
    },
    {
        "id": "my_job", "title": "My Job", "emoji": "💼",
        "helper": ["office", "boss", "meeting", "colleague", "task", "project", "career", "salary"],
        "example": "I work in an office. My job starts at 9 and ends at 6. I have meetings with my colleagues and work on different projects. My boss is strict but fair. I like my career because I learn new things every day. The salary is good and I can save money for my dreams."
    },
    {
        "id": "my_travels", "title": "My Travels", "emoji": "✈️",
        "helper": ["airport", "ticket", "hotel", "luggage", "passport", "flight", "beach", "tourist"],
        "example": "I love to travel. Last summer I went to the sea. I bought a ticket, packed my luggage and went to the airport. The flight was long but exciting. I stayed in a nice hotel near the beach. I met other tourists and tried local food. It was an amazing trip."
    },
    {
        "id": "my_food", "title": "My Food", "emoji": "🍕",
        "helper": ["breakfast", "lunch", "dinner", "tasty", "cook", "restaurant", "hungry", "delicious"],
        "example": "I like tasty food. For breakfast I usually have eggs and coffee. For lunch I eat soup or salad. In the evening I cook dinner with my family. My favourite dish is pizza, but I also like healthy food like vegetables and fruit. Sometimes we go to a restaurant on weekends."
    },
    {
        "id": "my_health", "title": "My Health", "emoji": "💪",
        "helper": ["sport", "gym", "doctor", "healthy", "sleep", "water", "vitamins", "energy"],
        "example": "I try to stay healthy. I go to the gym three times a week. I eat vegetables and drink a lot of water. I sleep eight hours every night. When I feel sick, I go to the doctor. I also take vitamins in winter. Sport gives me energy and good mood."
    },
    {
        "id": "my_future", "title": "My Future", "emoji": "🚀",
        "helper": ["career", "family", "travel", "success", "dream", "plan", "goal", "achieve"],
        "example": "In the future I want to achieve many goals. I plan to build a good career and start a family. I also want to travel and see different countries. My biggest goal is to open my own business. I know it will not be easy, but I believe in myself and work hard every day."
    },
]


# ─── ДИАЛОГИ ───

DIALOGUES = [
    {
        "id": "cafe", "title": "In a Café", "emoji": "☕", "level": "A1-A2",
        "characters": {"a": "Barista", "b": "Customer"},
        "lines": [
            {"who": "a", "text": "Hi! What can I get for you?", "rus": "Привет! Что вам принести?"},
            {"who": "b", "text": "Hi! Can I have a cappuccino, please?", "rus": "Привет! Можно капучино, пожалуйста?"},
            {"who": "a", "text": "Sure. Small or large?", "rus": "Конечно. Маленький или большой?"},
            {"who": "b", "text": "Large, please.", "rus": "Большой, пожалуйста."},
            {"who": "a", "text": "Anything else? Maybe a croissant?", "rus": "Что-нибудь ещё? Может, круассан?"},
            {"who": "b", "text": "No, thanks. Just the coffee.", "rus": "Нет, спасибо. Только кофе."},
            {"who": "a", "text": "That will be five dollars.", "rus": "С вас пять долларов."},
            {"who": "b", "text": "Here you go. Keep the change.", "rus": "Вот, возьмите. Сдачу оставьте себе."},
            {"who": "a", "text": "Thank you! Your coffee will be ready in a minute.", "rus": "Спасибо! Ваш кофе будет готов через минуту."},
        ],
    },
    {
        "id": "airport", "title": "At the Airport", "emoji": "✈️", "level": "A1-A2",
        "characters": {"a": "Agent", "b": "Passenger"},
        "lines": [
            {"who": "a", "text": "Good morning. Your passport, please.", "rus": "Доброе утро. Ваш паспорт, пожалуйста."},
            {"who": "b", "text": "Here it is.", "rus": "Вот, пожалуйста."},
            {"who": "a", "text": "Where are you flying today?", "rus": "Куда вы летите сегодня?"},
            {"who": "b", "text": "To London.", "rus": "В Лондон."},
            {"who": "a", "text": "How long will you stay?", "rus": "Как долго вы пробудете?"},
            {"who": "b", "text": "About two weeks.", "rus": "Около двух недель."},
            {"who": "a", "text": "Any liquids or sharp objects?", "rus": "Есть жидкости или острые предметы?"},
            {"who": "b", "text": "No, nothing.", "rus": "Нет, ничего."},
            {"who": "a", "text": "Alright. Have a nice flight!", "rus": "Хорошо. Хорошего полёта!"},
        ],
    },
    {
        "id": "hotel", "title": "At the Hotel", "emoji": "🏨", "level": "A1-A2",
        "characters": {"a": "Receptionist", "b": "Guest"},
        "lines": [
            {"who": "a", "text": "Good evening! How can I help you?", "rus": "Добрый вечер! Чем могу помочь?"},
            {"who": "b", "text": "Hi, I have a reservation for tonight.", "rus": "Здравствуйте, у меня бронь на сегодня."},
            {"who": "a", "text": "What's your name, please?", "rus": "Ваше имя, пожалуйста?"},
            {"who": "b", "text": "John Smith.", "rus": "Джон Смит."},
            {"who": "a", "text": "Yes, I see it. Room 305. Here's your key.", "rus": "Да, вижу. Номер 305. Вот ваш ключ."},
            {"who": "b", "text": "Great. What time is breakfast?", "rus": "Отлично. Во сколько завтрак?"},
            {"who": "a", "text": "From seven to ten in the morning.", "rus": "С семи до десяти утра."},
            {"who": "b", "text": "Perfect, thank you.", "rus": "Отлично, спасибо."},
        ],
    },
    {
        "id": "shop", "title": "In a Shop", "emoji": "🛍️", "level": "A1-A2",
        "characters": {"a": "Shop Assistant", "b": "Customer"},
        "lines": [
            {"who": "a", "text": "Hello! Can I help you?", "rus": "Здравствуйте! Могу я помочь?"},
            {"who": "b", "text": "Yes, I'm looking for a blue shirt.", "rus": "Да, я ищу синюю рубашку."},
            {"who": "a", "text": "What size do you need?", "rus": "Какой размер вам нужен?"},
            {"who": "b", "text": "Medium, please.", "rus": "Средний, пожалуйста."},
            {"who": "a", "text": "Here you are. The fitting room is over there.", "rus": "Вот, пожалуйста. Примерочная вон там."},
            {"who": "b", "text": "Thanks. How much is it?", "rus": "Спасибо. Сколько стоит?"},
            {"who": "a", "text": "It's thirty dollars.", "rus": "Тридцать долларов."},
            {"who": "b", "text": "I'll take it. Can I pay by card?", "rus": "Беру. Можно оплатить картой?"},
            {"who": "a", "text": "Of course.", "rus": "Конечно."},
        ],
    },
    {
        "id": "meeting", "title": "Meeting Someone New", "emoji": "👋", "level": "A1-A2",
        "characters": {"a": "Alex", "b": "Sam"},
        "lines": [
            {"who": "a", "text": "Hi! I'm Alex. Nice to meet you.", "rus": "Привет! Я Алекс. Приятно познакомиться."},
            {"who": "b", "text": "Hi Alex, I'm Sam. Nice to meet you too.", "rus": "Привет, Алекс, я Сэм. Мне тоже приятно."},
            {"who": "a", "text": "Where are you from, Sam?", "rus": "Откуда ты, Сэм?"},
            {"who": "b", "text": "I'm from Canada. And you?", "rus": "Я из Канады. А ты?"},
            {"who": "a", "text": "I'm from Russia.", "rus": "Я из России."},
            {"who": "b", "text": "Cool! What do you do?", "rus": "Круто! Чем занимаешься?"},
            {"who": "a", "text": "I'm a software developer. And you?", "rus": "Я разработчик. А ты?"},
            {"who": "b", "text": "I'm a student. I study design.", "rus": "Я студент. Учусь на дизайнера."},
            {"who": "a", "text": "That's interesting! Let's keep in touch.", "rus": "Интересно! Давай останемся на связи."},
        ],
    },
    {
        "id": "doctor", "title": "At the Doctor", "emoji": "🩺", "level": "A1-A2",
        "characters": {"a": "Doctor", "b": "Patient"},
        "lines": [
            {"who": "a", "text": "Good morning. What seems to be the problem?", "rus": "Доброе утро. Что вас беспокоит?"},
            {"who": "b", "text": "I have a headache and a sore throat.", "rus": "У меня болит голова и горло."},
            {"who": "a", "text": "How long have you had these symptoms?", "rus": "Как давно у вас эти симптомы?"},
            {"who": "b", "text": "Since yesterday.", "rus": "Со вчерашнего дня."},
            {"who": "a", "text": "Do you have a fever?", "rus": "У вас есть температура?"},
            {"who": "b", "text": "Yes, thirty-eight degrees.", "rus": "Да, тридцать восемь."},
            {"who": "a", "text": "You have a cold. I'll prescribe you some medicine.", "rus": "У вас простуда. Я выпишу вам лекарство."},
            {"who": "b", "text": "Thank you, doctor.", "rus": "Спасибо, доктор."},
            {"who": "a", "text": "Drink plenty of water and rest. Get well soon!", "rus": "Пейте много воды и отдыхайте. Выздоравливайте!"},
        ],
    },
    {
        "id": "job", "title": "Job Interview", "emoji": "💼", "level": "B1",
        "characters": {"a": "Interviewer", "b": "Candidate"},
        "lines": [
            {"who": "a", "text": "Good afternoon. Please, have a seat.", "rus": "Добрый день. Присаживайтесь."},
            {"who": "b", "text": "Thank you.", "rus": "Спасибо."},
            {"who": "a", "text": "Tell me about yourself.", "rus": "Расскажите о себе."},
            {"who": "b", "text": "I have five years of experience in marketing.", "rus": "У меня пять лет опыта в маркетинге."},
            {"who": "a", "text": "Why do you want to work with us?", "rus": "Почему вы хотите работать у нас?"},
            {"who": "b", "text": "I admire your company's innovative approach.", "rus": "Я восхищаюсь инновационным подходом вашей компании."},
            {"who": "a", "text": "What are your strengths?", "rus": "Каковы ваши сильные стороны?"},
            {"who": "b", "text": "I'm hardworking and I learn quickly.", "rus": "Я трудолюбив и быстро учусь."},
            {"who": "a", "text": "Great. We'll call you next week.", "rus": "Отлично. Мы позвоним вам на следующей неделе."},
        ],
    },
    {
        "id": "smalltalk", "title": "Small Talk about Weather", "emoji": "☀️", "level": "A1-A2",
        "characters": {"a": "Colleague 1", "b": "Colleague 2"},
        "lines": [
            {"who": "a", "text": "Nice weather today, isn't it?", "rus": "Хорошая погода сегодня, не так ли?"},
            {"who": "b", "text": "Yes, it's beautiful. Much better than yesterday.", "rus": "Да, прекрасная. Гораздо лучше, чем вчера."},
            {"who": "a", "text": "I heard it's going to rain tomorrow.", "rus": "Я слышал, завтра будет дождь."},
            {"who": "b", "text": "Really? That's a shame.", "rus": "Правда? Как жаль."},
            {"who": "a", "text": "Do you have any plans for the weekend?", "rus": "У тебя есть планы на выходные?"},
            {"who": "b", "text": "Yes, I'm going to the countryside.", "rus": "Да, я поеду за город."},
            {"who": "a", "text": "Sounds nice! Enjoy your weekend.", "rus": "Звучит здорово! Хороших выходных."},
            {"who": "b", "text": "Thanks, you too!", "rus": "Спасибо, тебе тоже!"},
        ],
    },
    {
        "id": "taxi", "title": "Taking a Taxi", "emoji": "🚕", "level": "A1-A2",
        "characters": {"a": "Driver", "b": "Passenger"},
        "lines": [
            {"who": "a", "text": "Hello! Where to?", "rus": "Здравствуйте! Куда едем?"},
            {"who": "b", "text": "To the train station, please.", "rus": "На вокзал, пожалуйста."},
            {"who": "a", "text": "Sure. Are you in a hurry?", "rus": "Конечно. Вы спешите?"},
            {"who": "b", "text": "Yes, my train leaves in an hour.", "rus": "Да, мой поезд через час."},
            {"who": "a", "text": "Don't worry, we'll make it.", "rus": "Не волнуйтесь, успеем."},
            {"who": "b", "text": "How much will it cost?", "rus": "Сколько будет стоить?"},
            {"who": "a", "text": "About fifteen dollars.", "rus": "Около пятнадцати долларов."},
            {"who": "b", "text": "Okay, that's fine.", "rus": "Хорошо, отлично."},
            {"who": "a", "text": "Here we are. That's twenty dollars.", "rus": "Приехали. С вас двадцать долларов."},
        ],
    },
    {
        "id": "date", "title": "Asking Someone Out", "emoji": "💕", "level": "B1",
        "characters": {"a": "Tom", "b": "Kate"},
        "lines": [
            {"who": "a", "text": "Hey Kate, how are you doing?", "rus": "Привет, Кейт, как дела?"},
            {"who": "b", "text": "Hi Tom! I'm good, thanks. And you?", "rus": "Привет, Том! Хорошо, спасибо. А ты?"},
            {"who": "a", "text": "Great! Listen, I was wondering...", "rus": "Отлично! Слушай, я хотел спросить..."},
            {"who": "b", "text": "Yes?", "rus": "Да?"},
            {"who": "a", "text": "Would you like to grab a coffee with me sometime?", "rus": "Не хочешь как-нибудь выпить со мной кофе?"},
            {"who": "b", "text": "That sounds nice! When?", "rus": "Звучит здорово! Когда?"},
            {"who": "a", "text": "How about Saturday afternoon?", "rus": "Как насчёт субботы днём?"},
            {"who": "b", "text": "Saturday works for me. Let's meet at three.", "rus": "Суббота подходит. Давай в три."},
            {"who": "a", "text": "Perfect! See you then.", "rus": "Отлично! До встречи."},
        ],
    },
]


# ─── ЭМОДЗИ-КВИЗ ───
# Формат: emoji показывает, юзер вводит английское слово

EMOJI_WORDS = [
    {"emoji": "🍎", "answer": "apple", "rus": "яблоко"},
    {"emoji": "🍌", "answer": "banana", "rus": "банан"},
    {"emoji": "🍞", "answer": "bread", "rus": "хлеб"},
    {"emoji": "🥛", "answer": "milk", "rus": "молоко"},
    {"emoji": "🍕", "answer": "pizza", "rus": "пицца"},
    {"emoji": "🍰", "answer": "cake", "rus": "торт"},
    {"emoji": "🐕", "answer": "dog", "rus": "собака"},
    {"emoji": "🐈", "answer": "cat", "rus": "кошка"},
    {"emoji": "🐟", "answer": "fish", "rus": "рыба"},
    {"emoji": "🐦", "answer": "bird", "rus": "птица"},
    {"emoji": "☀️", "answer": "sun", "rus": "солнце"},
    {"emoji": "🌙", "answer": "moon", "rus": "луна"},
    {"emoji": "⭐", "answer": "star", "rus": "звезда"},
    {"emoji": "🌧️", "answer": "rain", "rus": "дождь"},
    {"emoji": "❄️", "answer": "snow", "rus": "снег"},
    {"emoji": "🌈", "answer": "rainbow", "rus": "радуга"},
    {"emoji": "🏠", "answer": "house", "rus": "дом"},
    {"emoji": "🚗", "answer": "car", "rus": "машина"},
    {"emoji": "✈️", "answer": "plane", "rus": "самолёт"},
    {"emoji": "🚂", "answer": "train", "rus": "поезд"},
    {"emoji": "🚢", "answer": "ship", "rus": "корабль"},
    {"emoji": "🚲", "answer": "bicycle", "rus": "велосипед"},
    {"emoji": "💻", "answer": "computer", "rus": "компьютер"},
    {"emoji": "📱", "answer": "phone", "rus": "телефон"},
    {"emoji": "📚", "answer": "book", "rus": "книга"},
    {"emoji": "✏️", "answer": "pencil", "rus": "карандаш"},
    {"emoji": "🎂", "answer": "birthday", "rus": "день рождения"},
    {"emoji": "🎁", "answer": "gift", "rus": "подарок"},
    {"emoji": "❤️", "answer": "heart", "rus": "сердце"},
    {"emoji": "🔥", "answer": "fire", "rus": "огонь"},
    {"emoji": "💧", "answer": "water", "rus": "вода"},
    {"emoji": "🌳", "answer": "tree", "rus": "дерево"},
    {"emoji": "🌷", "answer": "flower", "rus": "цветок"},
    {"emoji": "🍄", "answer": "mushroom", "rus": "гриб"},
    {"emoji": "🍓", "answer": "strawberry", "rus": "клубника"},
    {"emoji": "🥕", "answer": "carrot", "rus": "морковь"},
    {"emoji": "🥚", "answer": "egg", "rus": "яйцо"},
    {"emoji": "🧀", "answer": "cheese", "rus": "сыр"},
    {"emoji": "🍫", "answer": "chocolate", "rus": "шоколад"},
    {"emoji": "☕", "answer": "coffee", "rus": "кофе"},
    {"emoji": "🍵", "answer": "tea", "rus": "чай"},
    {"emoji": "👁️", "answer": "eye", "rus": "глаз"},
    {"emoji": "👂", "answer": "ear", "rus": "ухо"},
    {"emoji": "👋", "answer": "hand", "rus": "рука"},
    {"emoji": "🦷", "answer": "tooth", "rus": "зуб"},
    {"emoji": "🦶", "answer": "foot", "rus": "нога"},
    {"emoji": "🏥", "answer": "hospital", "rus": "больница"},
    {"emoji": "🏫", "answer": "school", "rus": "школа"},
    {"emoji": "🎓", "answer": "graduation", "rus": "выпускной"},
    {"emoji": "⚽", "answer": "football", "rus": "футбол"},
    {"emoji": "🎸", "answer": "guitar", "rus": "гитара"},
    {"emoji": "🎨", "answer": "art", "rus": "искусство"},
    {"emoji": "💰", "answer": "money", "rus": "деньги"},
    {"emoji": "🌍", "answer": "earth", "rus": "земля"},
    {"emoji": "🌊", "answer": "sea", "rus": "море"},
    {"emoji": "🏔️", "answer": "mountain", "rus": "гора"},
    {"emoji": "🏖️", "answer": "beach", "rus": "пляж"},
    {"emoji": "🐝", "answer": "bee", "rus": "пчела"},
    {"emoji": "🦁", "answer": "lion", "rus": "лев"},
    {"emoji": "🐘", "answer": "elephant", "rus": "слон"},
    {"emoji": "🐻", "answer": "bear", "rus": "медведь"},
    {"emoji": "🦊", "answer": "fox", "rus": "лиса"},



# ═══════════════════════════════════════════════
# ГРАММАТИКА — УРОКИ
# ═══════════════════════════════════════════════
# Структура урока:
#   id, title, emoji, level, intro (короткое вступление)
#   theory: список блоков [{h: "заголовок", text: "текст"}]
#   examples: список примеров [{eng: "...", rus: "..."}]
#   test: список вопросов
#     type="choice" — 4 варианта, 1 правильный
#     type="fill" — вставить пропущенное слово (вводишь текст)

GRAMMAR_LESSONS = [
    # ─── УРОК 1 ───
    {
        "id": "present_simple",
        "title": "Present Simple",
        "emoji": "🕐",
        "level": "A1-A2",
        "intro": "Простое настоящее время. Используем для фактов, привычек, повторяющихся действий.",
        "theory": [
            {"h": "Когда использовать", "text": "Когда говорим о фактах (I live in Russia), привычках (I wake up at 7), расписаниях (The train leaves at 9)."},
            {"h": "Как образуется", "text": "Для I / you / we / they — глагол в базовой форме: I work, you play. Для he / she / it — добавляем -s или -es: he works, she plays, it goes."},
            {"h": "Отрицание", "text": "do not (don't) для I/you/we/they, does not (doesn't) для he/she/it + глагол в базовой форме: I don't work, he doesn't work."},
            {"h": "Вопрос", "text": "Do / Does + подлежащее + глагол: Do you work? Does he work?"},
            {"h": "Маркеры", "text": "always, usually, often, sometimes, never, every day, on Mondays."}
        ],
        "examples": [
            {"eng": "I work in an office.", "rus": "Я работаю в офисе."},
            {"eng": "She likes coffee.", "rus": "Она любит кофе."},
            {"eng": "They don't speak English.", "rus": "Они не говорят по-английски."},
            {"eng": "Do you play football?", "rus": "Ты играешь в футбол?"},
            {"eng": "He always gets up at 7.", "rus": "Он всегда встаёт в 7."}
        ],
        "test": [
            {"type": "choice", "q": "She ___ to school every day.", "options": ["go", "goes", "going", "went"], "correct": "goes"},
            {"type": "choice", "q": "They ___ like coffee.", "options": ["doesn't", "don't", "isn't", "aren't"], "correct": "don't"},
            {"type": "choice", "q": "___ he work here?", "options": ["Do", "Does", "Is", "Are"], "correct": "Does"},
            {"type": "fill", "q": "I ___ (work) in a bank.", "answer": "work"},
            {"type": "fill", "q": "He ___ (play) guitar.", "answer": "plays"}
        ]
    },

    # ─── УРОК 2 ───
    {
        "id": "past_simple",
        "title": "Past Simple",
        "emoji": "⏪",
        "level": "A1-A2",
        "intro": "Простое прошедшее время. Используем для законченных действий в прошлом.",
        "theory": [
            {"h": "Когда использовать", "text": "Когда действие произошло в прошлом и закончилось (вчера, в прошлом году, 2 часа назад). Есть конкретное время или подразумевается."},
            {"h": "Правильные глаголы", "text": "Добавляем -ed: work → worked, play → played, watch → watched."},
            {"h": "Неправильные глаголы", "text": "Формы надо запомнить: go → went, see → saw, have → had, do → did. Учи их в разделе «Неправильные глаголы»."},
            {"h": "Отрицание", "text": "did not (didn't) + глагол в базовой форме: I didn't work, he didn't go."},
            {"h": "Вопрос", "text": "Did + подлежащее + глагол: Did you work? Did he go?"},
            {"h": "Маркеры", "text": "yesterday, last week, 2 days ago, in 2020, when I was a child."}
        ],
        "examples": [
            {"eng": "I worked yesterday.", "rus": "Я работал вчера."},
            {"eng": "She went to London last year.", "rus": "Она ездила в Лондон в прошлом году."},
            {"eng": "We didn't see the film.", "rus": "Мы не смотрели фильм."},
            {"eng": "Did you call me?", "rus": "Ты мне звонил?"},
            {"eng": "He was at home.", "rus": "Он был дома."}
        ],
        "test": [
            {"type": "choice", "q": "I ___ to school yesterday.", "options": ["go", "goes", "went", "gone"], "correct": "went"},
            {"type": "choice", "q": "She ___ the film last week.", "options": ["see", "saw", "seen", "sees"], "correct": "saw"},
            {"type": "choice", "q": "We ___ go to the party.", "options": ["doesn't", "don't", "didn't", "aren't"], "correct": "didn't"},
            {"type": "fill", "q": "He ___ (play) football yesterday.", "answer": "played"},
            {"type": "fill", "q": "Did you ___ (see) him?", "answer": "see"}
        ]
    },

    # ─── УРОК 3 ───
    {
        "id": "present_continuous",
        "title": "Present Continuous",
        "emoji": "🎬",
        "level": "A1-A2",
        "intro": "Настоящее длительное. Используем для действий прямо сейчас или в этот период.",
        "theory": [
            {"h": "Когда использовать", "text": "Действие происходит прямо сейчас (I am reading) или в текущий период (I am learning English this year). Также для запланированного будущего (I am meeting him tomorrow)."},
            {"h": "Как образуется", "text": "am / is / are + глагол с -ing. I am working. She is reading. They are playing."},
            {"h": "Отрицание", "text": "am not / isn't / aren't + глагол-ing: I am not working, he isn't reading."},
            {"h": "Вопрос", "text": "Am / Is / Are + подлежащее + глагол-ing: Are you working? Is she reading?"},
            {"h": "Маркеры", "text": "now, right now, at the moment, today, this week, look!, listen!"}
        ],
        "examples": [
            {"eng": "I am reading a book.", "rus": "Я читаю книгу (сейчас)."},
            {"eng": "She is cooking dinner.", "rus": "Она готовит ужин."},
            {"eng": "They are not watching TV.", "rus": "Они не смотрят телевизор."},
            {"eng": "Are you listening to me?", "rus": "Ты меня слушаешь?"},
            {"eng": "Look! It is raining.", "rus": "Смотри! Идёт дождь."}
        ],
        "test": [
            {"type": "choice", "q": "I ___ reading a book now.", "options": ["am", "is", "are", "be"], "correct": "am"},
            {"type": "choice", "q": "She ___ cooking dinner.", "options": ["am", "is", "are", "be"], "correct": "is"},
            {"type": "choice", "q": "They ___ playing football.", "options": ["am not", "isn't", "aren't", "don't"], "correct": "aren't"},
            {"type": "fill", "q": "Look! He ___ (run).", "answer": "is running"},
            {"type": "fill", "q": "We ___ (study) English now.", "answer": "are studying"}
        ]
    },
]
