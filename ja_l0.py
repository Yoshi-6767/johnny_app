# ja_l0.py
JA_L0_U1 = {
    "id": "ja-l0-u1",
    "lang": "ja",
    "level": 0,
    "order": 1,
    "prerequisites": [],
    "title": {
        "ru": "Хирагана: あ-お",
        "en": "Hiragana: a-o",
        "ja": "ひらがな：あ〜お"
    },
    "goals": [
        {"ru": "Выучить 5 базовых символов хираганы", "en": "Learn 5 basic hiragana", "ja": "5つのひらがなを覚える"}
    ],
    "lessons": [
        {
            "id": "ja-l0-u1-l1",
            "type": "text",
            "title": {"ru": "Введение", "en": "Introduction", "ja": "はじめに"},
            "blocks": [
                {"type": "paragraph", "text": {"ru": "Хирагана — это базовая японская азбука. Начнем с гласных.", "en": "Hiragana is the basic Japanese alphabet. Let's start with vowels.", "ja": "ひらがなは基本的な日本語の文字です。母音から始めましょう。"}},
                {"type": "table", "headers": [{"ru": "Символ", "en": "Char", "ja": "文字"}, {"ru": "Ромадзи", "en": "Romaji", "ja": "ローマ字"}], "rows": [[{"ru": "あ", "en": "あ", "ja": "あ"}, {"ru": "a", "en": "a", "ja": "a"}], [{"ru": "い", "en": "い", "ja": "い"}, {"ru": "i", "en": "i", "ja": "i"}], [{"ru": "う", "en": "う", "ja": "う"}, {"ru": "u", "en": "u", "ja": "u"}], [{"ru": "え", "en": "え", "ja": "え"}, {"ru": "e", "en": "e", "ja": "e"}], [{"ru": "お", "en": "お", "ja": "お"}, {"ru": "o", "en": "o", "ja": "o"}]]},
                {"type": "callout", "kind": "tip", "text": {"ru": "Запомни: あ похожа на антенну, い — на две палочки, う — на ухо, え — на энергичного человека, お — на рот с усами.", "en": "Remember: あ looks like an antenna, い like two sticks, う like an ear, え like an energetic person, お like a mouth with a mustache.", "ja": "覚えましょう：あはアンテナ、いは二本の棒、うは耳、えは元気な人、おは口ひげのようです。"}}
            ]
        }
    ],
    "vocab": [],
    "kanji": [],
    "exercises": [
        {
            "type": "multiple_choice",
            "id": "ja-l0-u1-ex1",
            "prompt": {"ru": "Какой звук соответствует символу あ?", "en": "Which sound corresponds to あ?", "ja": "「あ」はどの音ですか？"},
            "options": [
                {"id": "a", "text": {"ru": "a", "en": "a", "ja": "a"}},
                {"id": "i", "text": {"ru": "i", "en": "i", "ja": "i"}},
                {"id": "u", "text": {"ru": "u", "en": "u", "ja": "u"}}
            ],
            "answer": "a",
            "explain": {"ru": "Символ あ читается как 'а'.", "en": "The symbol あ reads as 'a'.", "ja": "「あ」は「a」と読みます。"}
        },
        {
            "type": "fill_blank",
            "id": "ja-l0-u1-ex2",
            "prompt": {"ru": "Вставь пропущенный символ: _ читается как 'i'.", "en": "Insert the missing symbol: _ reads as 'i'.", "ja": "「i」と読む文字は？"},
            "sentence": "_",
            "answer": "い",
            "alternatives": ["い"],
            "explain": {"ru": "Символ い читается как 'и'.", "en": "The symbol い reads as 'i'.", "ja": "「い」は「i」と読みます。"}
        },
                {
            "type": "handwrite",
            "id": "ja-l0-u1-ex3",
            "prompt": {"ru": "Напиши символ あ", "en": "Write the symbol あ", "ja": "「あ」を書いてください"},
            "target": "あ",
            "mode": "free",
            "strokeOrderText": "1. Горизонтальная черта. 2. Вертикальная черта. 3. Круг с хвостиком."
        }
    ],
    "handwriting": [
        {"target": "あ", "strokeOrderText": "1. Горизонтальная черта. 2. Вертикальная черта. 3. Круг с хвостиком."}
    ],
    "essayPrompt": None
}
