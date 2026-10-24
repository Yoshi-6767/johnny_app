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

JA_L0_U2 = {
  "id": "ja-l0-u2",
  "level": 0,
  "order": 2,
  "prerequisites": ["ja-l0-u1"],
  "title": {
    "ru": "Хирагана: か-こ",
    "en": "Hiragana: ka-ko",
    "ja": "ひらがな：か〜こ"
  },
  "goals": [
    {
      "ru": "Выучить символы か, き, く, け, こ",
      "en": "Learn the characters か, き, く, け, こ",
      "ja": "「か、き、く、け、こ」を覚える"
    },
    {
      "ru": "Научиться писать их правильно",
      "en": "Learn to write them correctly",
      "ja": "正しく書けるようになる"
    }
  ],
  "lessons": [
    {
      "type": "text",
      "title": {"ru": "Введение", "en": "Introduction", "ja": "はじめに"},
      "blocks": [
        {
          "type": "paragraph",
          "text": {
            "ru": "Продолжаем изучение хираганы. В этом юните мы разберем ряд «К» (ka, ki, ku, ke, ko). Эти символы очень важны, так как они часто встречаются в базовых словах.",
            "en": "Continuing with hiragana. In this unit we'll cover the 'K' row (ka, ki, ku, ke, ko). These characters are very important as they appear frequently in basic words.",
            "ja": "ひらがなの学習を続けます。このユニットでは「か行」（か、き、く、け、こ）を学びます。これらの文字は基本的な単語によく出てくるので非常に重要です。"
          }
        },
        {
          "type": "table",
          "headers": [
            {"ru": "Символ", "en": "Symbol", "ja": "文字"},
            {"ru": "Ромадзи", "en": "Romaji", "ja": "ローマ字"}
          ],
          "rows": [
            [{"ru": "か", "en": "か", "ja": "か"}, {"ru": "ka", "en": "ka", "ja": "ka"}],
            [{"ru": "き", "en": "き", "ja": "き"}, {"ru": "ki", "en": "ki", "ja": "ki"}],
            [{"ru": "く", "en": "く", "ja": "く"}, {"ru": "ku", "en": "ku", "ja": "ku"}],
            [{"ru": "け", "en": "け", "ja": "け"}, {"ru": "ke", "en": "ke", "ja": "ke"}],
            [{"ru": "こ", "en": "こ", "ja": "こ"}, {"ru": "ko", "en": "ko", "ja": "ko"}]
          ]
        },
        {
          "type": "callout",
          "kind": "mnemonic",
          "text": {
            "ru": "Запоминалки: か — это человек, который пьет коктейль через трубочку (сбоку). き — это ключ (key) с двумя зубчиками. く — это клюв птицы (открытый рот). け — это человек с оттопыренной ногой (кеды). こ — это два свернутых кольца (как у змеи).",
            "en": "Mnemonics: か looks like a person drinking a cocktail through a straw. き looks like a key with two teeth. く looks like a bird's beak. け looks like a person with a leg out (keds). こ looks like two curled rings.",
            "ja": "覚え方：かはストローでカクテルを飲む人。きは二つの歯がある鍵。くは鳥のくちばし。けは足を出した人。こは二つの巻いたリング。"
          }
        },
        {
          "type": "callout",
          "kind": "tip",
          "text": {
            "ru": "Обрати внимание: き (ki) и さ (sa) часто путают. У き сверху две горизонтальные черты, а у さ — одна.",
            "en": "Note: き (ki) and さ (sa) are often confused. き has two horizontal strokes on top, while さ has only one.",
            "ja": "注意：き（ki）とさ（sa）はよく混同されます。きは上に横棒が二本、さは一本です。"
          }
        }
      ]
    }
  ],
  "vocab": [
    {"id": "v-ka-1", "jp": "あか", "kana": "あか", "romaji": "aka", "translation": {"ru": "красный", "en": "red", "ja": "赤"}},
    {"id": "v-ka-2", "jp": "いか", "kana": "いか", "romaji": "ika", "translation": {"ru": "кальмар", "en": "squid", "ja": "烏賊"}},
    {"id": "v-ka-3", "jp": "きく", "kana": "きく", "romaji": "kiku", "translation": {"ru": "слушать", "en": "to listen", "ja": "聞く"}},
    {"id": "v-ka-4", "jp": "こえ", "kana": "こえ", "romaji": "koe", "translation": {"ru": "голос", "en": "voice", "ja": "声"}},
    {"id": "v-ka-5", "jp": "あき", "kana": "あき", "romaji": "aki", "translation": {"ru": "осень", "en": "autumn", "ja": "秋"}}
  ],
  "kanji": [],
  "exercises": [
    {
      "id": "ja-l0-u2-ex1",
      "type": "multiple_choice",
      "prompt": {"ru": "Какой звук соответствует символу か?", "en": "Which sound corresponds to the character か?", "ja": "「か」に対応する音はどれですか？"},
      "options": [
        {"id": "a", "text": {"ru": "ka", "en": "ka", "ja": "ka"}},
        {"id": "b", "text": {"ru": "ki", "en": "ki", "ja": "ki"}},
        {"id": "c", "text": {"ru": "sa", "en": "sa", "ja": "sa"}}
      ],
      "answer": "a",
      "explain": {"ru": "か читается как 'ка'.", "en": "か is read as 'ka'.", "ja": "かは「ka」と読みます。"}
    },
    {
      "id": "ja-l0-u2-ex2",
      "type": "multiple_choice",
      "prompt": {"ru": "Какой звук соответствует символу こ?", "en": "Which sound corresponds to the character こ?", "ja": "「こ」に対応する音はどれですか？"},
      "options": [
        {"id": "a", "text": {"ru": "ke", "en": "ke", "ja": "ke"}},
        {"id": "b", "text": {"ru": "ko", "en": "ko", "ja": "ko"}},
        {"id": "c", "text": {"ru": "ku", "en": "ku", "ja": "ku"}}
      ],
      "answer": "b",
      "explain": {"ru": "こ читается как 'ко'.", "en": "こ is read as 'ko'.", "ja": "こは「ko」と読みます。"}
    },
    {
      "id": "ja-l0-u2-ex3",
      "type": "fill_blank",
      "prompt": {"ru": "Вставь пропущенный символ: __ читается как 'ki'.", "en": "Insert the missing character: __ is read as 'ki'.", "ja": "抜けている文字を入れてください：__ は「ki」と読みます。"},
      "answer": "き",
      "alternatives": ["ki"],
      "explain": {"ru": "き — это 'ki'.", "en": "き is 'ki'.", "ja": "きは「ki」です。"}
    },
    {
      "id": "ja-l0-u2-ex4",
      "type": "fill_blank",
      "prompt": {"ru": "Вставь пропущенный символ: __ читается как 'ku'.", "en": "Insert the missing character: __ is read as 'ku'.", "ja": "抜けている文字を入れてください：__ は「ku」と読みます。"},
      "answer": "く",
      "alternatives": ["ku"],
      "explain": {"ru": "く — это 'ku'.", "en": "く is 'ku'.", "ja": "くは「ku」です。"}
    },
    {
      "id": "ja-l0-u2-ex5",
      "type": "multiple_choice",
      "prompt": {"ru": "Какой звук соответствует символу け?", "en": "Which sound corresponds to the character け?", "ja": "「け」に対応する音はどれですか？"},
      "options": [
        {"id": "a", "text": {"ru": "ke", "en": "ke", "ja": "ke"}},
        {"id": "b", "text": {"ru": "ka", "en": "ka", "ja": "ka"}},
        {"id": "c", "text": {"ru": "ko", "en": "ko", "ja": "ko"}}
      ],
      "answer": "a",
      "explain": {"ru": "け читается как 'ke'.", "en": "け is read as 'ke'.", "ja": "けは「ke」と読みます。"}
    },
    {
      "id": "ja-l0-u2-ex6",
      "type": "multiple_choice",
      "prompt": {"ru": "Выбери правильный символ для звука 'ka'.", "en": "Choose the correct character for the sound 'ka'.", "ja": "「ka」の音に正しい文字を選んでください。"},
      "options": [
        {"id": "a", "text": {"ru": "き"}},
        {"id": "b", "text": {"ru": "か"}},
        {"id": "c", "text": {"ru": "こ"}}
      ],
      "answer": "b",
      "explain": {"ru": "Звук 'ka' — это か.", "en": "'ka' is か.", "ja": "「ka」は「か」です。"}
    },
    {
      "id": "ja-l0-u2-ex7",
      "type": "multiple_choice",
      "prompt": {"ru": "Выбери правильный символ для звука 'ku'.", "en": "Choose the correct character for the sound 'ku'.", "ja": "「ku」の音に正しい文字を選んでください。"},
      "options": [
        {"id": "a", "text": {"ru": "け"}},
        {"id": "b", "text": {"ru": "こ"}},
        {"id": "c", "text": {"ru": "く"}}
      ],
      "answer": "c",
      "explain": {"ru": "Звук 'ku' — это く.", "en": "'ku' is く.", "ja": "「ku」は「く」です。"}
    },
    {
      "id": "ja-l0-u2-ex8",
      "type": "multiple_choice",
      "prompt": {"ru": "Какой звук соответствует символу き?", "en": "Which sound corresponds to the character き?", "ja": "「き」に対応する音はどれですか？"},
      "options": [
        {"id": "a", "text": {"ru": "ki", "en": "ki", "ja": "ki"}},
        {"id": "b", "text": {"ru": "ko", "en": "ko", "ja": "ko"}},
        {"id": "c", "text": {"ru": "ka", "en": "ka", "ja": "ka"}}
      ],
      "answer": "a",
      "explain": {"ru": "き читается как 'ki'.", "en": "き is read as 'ki'.", "ja": "きは「ki」と読みます。"}
    },
    {
      "id": "ja-l0-u2-ex9",
      "type": "fill_blank",
      "prompt": {"ru": "Вставь пропущенный символ: __ читается как 'ko'.", "en": "Insert the missing character: __ is read as 'ko'.", "ja": "抜けている文字を入れてください：__ は「ko」と読みます。"},
      "answer": "こ",
      "alternatives": ["ko"],
      "explain": {"ru": "こ — это 'ko'.", "en": "こ is 'ko'.", "ja": "こは「ko」です。"}
    },
    {
      "id": "ja-l0-u2-ex10",
      "type": "fill_blank",
      "prompt": {"ru": "Вставь пропущенный символ: __ читается как 'ke'.", "en": "Insert the missing character: __ is read as 'ke'.", "ja": "抜けている文字を入れてください：__ は「ke」と読みます。"},
      "answer": "け",
      "alternatives": ["ke"],
      "explain": {"ru": "け — это 'ke'.", "en": "け is 'ke'.", "ja": "けは「ke」です。"}
    },
    {
      "id": "ja-l0-u2-ex11",
      "type": "order_words",
      "prompt": {"ru": "Собери слово 'осень' (aki) из символов.", "en": "Assemble the word 'autumn' (aki) from characters.", "ja": "「秋」（aki）を文字から組み立ててください。"},
      "tokens": [{"ru": "き"}, {"ru": "あ"}],
      "answer": [1, 0] 
    },
    {
      "id": "ja-l0-u2-ex12",
      "type": "order_words",
      "prompt": {"ru": "Собери слово 'кальмар' (ika) из символов.", "en": "Assemble the word 'squid' (ika) from characters.", "ja": "「烏賊」（ika）を文字から組み立ててください。"},
      "tokens": [{"ru": "か"}, {"ru": "い"}],
      "answer": [1, 0]
    },
    {
      "id": "ja-l0-u2-ex13",
      "type": "handwrite",
      "target": "か",
      "mode": "free",
      "guideLines": "grid",
      "strokeOrderText": {"ru": "1. Горизонтальная черта. 2. Вертикальная черта с крючком влево. 3. Диагональ вправо-вниз с загибом.", "en": "1. Horizontal stroke. 2. Vertical stroke with a hook to the left. 3. Diagonal down-right with a curve.", "ja": "1. 横棒。2. 左に跳ねる縦棒。3. 右に曲がる斜めの棒。"}
    },
    {
      "id": "ja-l0-u2-ex14",
      "type": "handwrite",
      "target": "き",
      "mode": "free",
      "guideLines": "grid",
      "strokeOrderText": {"ru": "1. Горизонтальная черта. 2. Вторая горизонтальная черта. 3. Вертикальная черта. 4. Левая диагональ. 5. Правая диагональ с загибом.", "en": "1. Horizontal stroke. 2. Second horizontal stroke. 3. Vertical stroke. 4. Left diagonal. 5. Right diagonal with a curve.", "ja": "1. 横棒。2. 二本目の横棒。3. 縦棒。4. 左斜め。5. 右に曲がる斜め。"}
    },
    {
      "id": "ja-l0-u2-ex15",
      "type": "handwrite",
      "target": "く",
      "mode": "free",
      "guideLines": "grid",
      "strokeOrderText": {"ru": "1. Одна черта: начинается сверху, идет вниз влево, затем резко вправо-вниз.", "en": "1. One stroke: starts at the top, goes down-left, then sharply down-right.", "ja": "1. 一本の線：上から左下へ行き、急に右下へ曲がる。"}
    }
  ],
  "essayPrompt": None
}
