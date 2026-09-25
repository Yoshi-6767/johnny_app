// ═══════════════════════════════════════════════
// FLOW & WORD — АУДИРОВАНИЕ (Web Speech API)
// ═══════════════════════════════════════════════

(function() {
    // Проверка поддержки
    if (!('speechSynthesis' in window)) {
        window.FW_SPEECH_SUPPORTED = false;
        console.warn('[Flow & Word] Web Speech API не поддерживается');
        return;
    }
    window.FW_SPEECH_SUPPORTED = true;

    // Загружаем голоса (они асинхронные)
    let voices = [];
    function loadVoices() {
        voices = window.speechSynthesis.getVoices();
    }
    loadVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = loadVoices;
    }

    // Настройки из localStorage
    function getSettings() {
        return {
            accent: localStorage.getItem('audio_accent') || 'us',
            rate: parseFloat(localStorage.getItem('audio_rate') || '1.0')
        };
    }

    // Найти подходящий голос под акцент
    function pickVoice(accent) {
        if (!voices.length) loadVoices();
        const langMap = {
            'us': 'en-US',
            'uk': 'en-GB'
        };
        const targetLang = langMap[accent] || 'en-US';

        // Ищем точное совпадение
        let voice = voices.find(v => v.lang === targetLang);
        // Если нет — берём любой английский
        if (!voice) voice = voices.find(v => v.lang.startsWith('en'));
        // Фолбэк
        if (!voice && voices.length) voice = voices[0];
        return voice;
    }

    // Основная функция озвучки
    window.speak = function(text, options) {
        if (!window.FW_SPEECH_SUPPORTED) {
            alert('Твой браузер не поддерживает озвучку. Попробуй Chrome или Edge.');
            return;
        }
        if (!text) return;

        const settings = getSettings();
        const accent = (options && options.accent) || settings.accent;
        const rate = (options && options.rate) || settings.rate;

        // Отменяем текущую озвучку, если играет
        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = accent === 'uk' ? 'en-GB' : 'en-US';
        utterance.rate = rate;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;

        const voice = pickVoice(accent);
        if (voice) utterance.voice = voice;

        window.speechSynthesis.speak(utterance);
    };

    // Остановить озвучку
    window.stopSpeaking = function() {
        if (window.FW_SPEECH_SUPPORTED) window.speechSynthesis.cancel();
    };

    // Сохранить настройки
    window.setAudioAccent = function(accent) {
        localStorage.setItem('audio_accent', accent);
    };
    window.setAudioRate = function(rate) {
        localStorage.setItem('audio_rate', rate);
    };
    window.getAudioSettings = getSettings;

    // Проверка: доступны ли английские голоса
    window.hasEnglishVoice = function() {
        if (!voices.length) loadVoices();
        return voices.some(v => v.lang.startsWith('en'));

            window.hasEnglishVoice = function() {
        if (!voices.length) loadVoices();
        return voices.some(v => v.lang.startsWith('en'));
    };

    // ═══════════════════════════════════════════════
    // РАСПОЗНАВАНИЕ РЕЧИ (Web Speech Recognition)
    // ═══════════════════════════════════════════════

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    window.FW_RECOGNITION_SUPPORTED = !!SpeechRecognition;

    if (!window.FW_RECOGNITION_SUPPORTED) {
        console.warn('[Flow & Word] Web Speech Recognition не поддерживается');
    }

    window.recognizeSpeech = function(onResult, onError) {
        if (!window.FW_RECOGNITION_SUPPORTED) {
            if (onError) onError('not_supported');
            return null;
        }

        const settings = getSettings();
        const recognition = new SpeechRecognition();
        recognition.lang = settings.accent === 'uk' ? 'en-GB' : 'en-US';
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.maxAlternatives = 3;

        recognition.onresult = function(event) {
            const alternatives = [];
            for (let i = 0; i < event.results[0].length; i++) {
                alternatives.push(event.results[0][i].transcript.trim().toLowerCase());
            }
            const text = alternatives[0] || '';
            if (onResult) onResult(text, alternatives);
        };

        recognition.onerror = function(event) {
            if (onError) onError(event.error);
        };

        recognition.onend = function() {
            // Ничего — просто завершилось
        };

        try {
            recognition.start();
        } catch (e) {
            if (onError) onError('start_failed');
            return null;
        }

        return recognition;
    };

    // Сравнение распознанного текста с эталоном
    // Возвращает: "perfect" | "close" | "wrong"
    window.comparePronunciation = function(recognized, target) {
        if (!recognized || !target) return "wrong";
        const r = recognized.toLowerCase().trim();
        const t = target.toLowerCase().trim();

        // Точное совпадение
        if (r === t) return "perfect";

        // Если фраза состоит из нескольких слов — проверяем каждое
        const rWords = r.split(/\s+/);
        const tWords = t.split(/\s+/);

        // Полное совпадение по всем словам
        if (rWords.length === tWords.length) {
            let matches = 0;
            for (let i = 0; i < tWords.length; i++) {
                if (rWords[i] === tWords[i]) matches++;
            }
            const ratio = matches / tWords.length;
            if (ratio >= 0.8) return "close";
            if (ratio >= 0.5) return "wrong";
        }

        // Одно слово — сравнение по символам (расстояние Левенштейна упрощённое)
        if (tWords.length === 1 && rWords.length === 1) {
            const a = rWords[0];
            const b = tWords[0];
            const maxLen = Math.max(a.length, b.length);
            let diff = 0;
            for (let i = 0; i < Math.min(a.length, b.length); i++) {
                if (a[i] !== b[i]) diff++;
            }
            diff += Math.abs(a.length - b.length);
            const similarity = 1 - (diff / maxLen);

            if (similarity >= 0.8) return "close";
            if (similarity >= 0.5) return "wrong";
        }

        return "wrong";
    };
})();
