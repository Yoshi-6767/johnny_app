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
    };
})();
