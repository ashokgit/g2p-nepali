class NepaliG2P:
    def __init__(self):
        self.nepali_g2p = {
            "क": "k",
            "ख": "kh",
            "ग": "g",
            "घ": "gh",
            "ङ": "ŋ",
            "च": "c",
            "छ": "ch",
            "ज": "j",
            "झ": "jh",
            "ञ": "ñ",
            "ट": "ṭ",
            "ठ": "ṭh",
            "ड": "ḍ",
            "ढ": "ḍh",
            "ण": "ṇ",
            "त": "t",
            "थ": "th",
            "द": "d",
            "ध": "dh",
            "न": "n",
            "प": "p",
            "फ": "ph",
            "ब": "b",
            "भ": "bh",
            "म": "m",
            "य": "y",
            "र": "r",
            "ल": "l",
            "व": "v",
            "श": "ś",
            "ष": "ṣ",
            "स": "s",
            "ह": "h",
            "क्ष": "ksh",
            "त्र": "tra",
            "ज्ञ": "gya",
            "ा": "ā",
            "ि": "i",
            "ी": "ī",
            "ु": "u",
            "ू": "ū",
            "े": "e",
            "ै": "ai",
            "ो": "o",
            "ौ": "au",
            "ं": "ṃ",
            "ँ": "̃",
            "ः": "ḥ",
            "ृ": "ṛ",
            "ॄ": "ṝ",
            "ॢ": "ḷ",
            "ॣ": "ḹ",
            "अ": "a",
            "आ": "aa",
            "इ": "i",
            "ई": "ii",
            "उ": "u",
            "ऊ": "uu",
            "ए": "e",
            "ऐ": "ai",
            "ओ": "o",
            "औ": "au",
            "ॲ": "ô",
            "अं": "am",
            "अः": "aha",
        }

    def to_phonemes(self, text: str) -> str:
        phonemes = []
        for char in text:
            if char in self.nepali_g2p:
                phonemes.append(self.nepali_g2p[char])
            else:
                phonemes.append(char)  # Unrecognized characters are passed through
        return "".join(phonemes)
