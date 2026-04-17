import re
import sys


REPLACEMENTS = [
    (r"\bi am\b", "ME"),
    (r"\bmy\b", "ME"),
    (r"\bmine\b", "ME"),
    (r"\bme\b", "ME"),
    (r"\bi\b", "ME"),
    (r"\bwe are\b", "WE"),
    (r"\byou are\b", "YOU"),
    (r"\bthey are\b", "THEY"),
    (r"\bhe is\b", "HIM"),
    (r"\bshe is\b", "HER"),
    (r"\bit is\b", "IT"),
    (r"\bare\b", "IS"),
    (r"\bwas\b", "WAS"),
    (r"\bwere\b", "WAS"),
    (r"\bhave\b", "HAS"),
    (r"\bhad\b", "HAD"),
    (r"\bwill\b", "WILL"),
    (r"\bwould\b", "WANT"),
    (r"\bcould\b", "CAN"),
    (r"\bshould\b", "MUST"),
    (r"\bnot\b", "NO"),
    (r"\bdont\b", "NO"),
    (r"\bdon't\b", "NO"),
    (r"\bdo not\b", "NO"),
    (r"\bvery\b", "MUCH"),
    (r"\breally\b", "MUCH"),
    (r"\bextremely\b", "MUCH MUCH"),
    (r"\bexcellent\b", "GOOD"),
    (r"\bwonderful\b", "GOOD"),
    (r"\bterrific\b", "GOOD"),
    (r"\bawful\b", "BAD"),
    (r"\bterrible\b", "BAD"),
    (r"\bhorrible\b", "BAD"),
    (r"\bfood\b", "FOOD"),
    (r"\beat\b", "EAT"),
    (r"\bdrink\b", "DRINK"),
    (r"\bfire\b", "FIRE"),
    (r"\bwater\b", "WATER"),
    (r"\brock\b", "ROCK"),
    (r"\brun\b", "RUN"),
    (r"\bsleep\b", "SLEEP"),
    (r"\bfriend\b", "FRIEND"),
    (r"\benemy\b", "ENEMY"),
    (r"\bwant\b", "WANT"),
    (r"\bneed\b", "NEED"),
    (r"\blike\b", "LIKE"),
    (r"\blove\b", "LOVE"),
    (r"\bhate\b", "HATE"),
    (r"\bgo\b", "GO"),
    (r"\bcome\b", "COME"),
    (r"\bsee\b", "SEE"),
    (r"\bhear\b", "HEAR"),
    (r"\bknow\b", "KNOW"),
    (r"\bthink\b", "THINK"),
    (r"\bsay\b", "SAY"),
    (r"\btell\b", "TELL"),
    (r"\bgive\b", "GIVE"),
    (r"\btake\b", "TAKE"),
    (r"\bmake\b", "MAKE"),
    (r"\bbig\b", "BIG"),
    (r"\bsmall\b", "SMALL"),
    (r"\blittle\b", "SMALL"),
    (r"\btiny\b", "SMALL"),
    (r"\bfast\b", "FAST"),
    (r"\bquick\b", "FAST"),
    (r"\bslow\b", "SLOW"),
    (r"\bstrong\b", "STRONG"),
    (r"\bweak\b", "WEAK"),
    (r"\bgood\b", "GOOD"),
    (r"\bbad\b", "BAD"),
    (r"\byes\b", "UGH YES"),
    (r"\bno\b", "UGH NO"),
    (r"\bhello\b", "OOG"),
    (r"\bhi\b", "OOG"),
    (r"\bhey\b", "OOG"),
    (r"\bgoodbye\b", "GRUNT"),
    (r"\bbye\b", "GRUNT"),
    (r"\bplease\b", ""),
    (r"\bthank you\b", ""),
    (r"\bthanks\b", ""),
    (r"\bsorry\b", ""),
]

ARTICLES = re.compile(r"\b(the|a|an)\b\s*", re.IGNORECASE)
TH_SOUND = re.compile(r"\bth", re.IGNORECASE)
ING_ENDING = re.compile(r"(\w{3,})ing\b", re.IGNORECASE)
ED_ENDING = re.compile(r"(\w{3,})ed\b", re.IGNORECASE)
LY_ENDING = re.compile(r"(\w{3,})ly\b", re.IGNORECASE)
MULTI_SPACE = re.compile(r"\s{2,}")
PUNCTUATION = re.compile(r"[.!?,;:]+")


def caveman(text: str) -> str:
    result = text.lower()

    for pattern, replacement in REPLACEMENTS:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

    result = ARTICLES.sub("", result)
    result = TH_SOUND.sub("D", result)
    result = ING_ENDING.sub(r"\1", result)
    result = ED_ENDING.sub(r"\1", result)
    result = LY_ENDING.sub(r"\1", result)
    result = PUNCTUATION.sub("!", result)
    result = MULTI_SPACE.sub(" ", result)
    result = result.strip().upper()

    if result and not result.startswith("UGH") and not result.startswith("OOG"):
        result = "UGH! " + result

    return result


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(caveman(text))
    else:
        print("CAVEMAN SPEAK! Enter text (Ctrl+D to quit):")
        for line in sys.stdin:
            line = line.strip()
            if line:
                print(caveman(line))


if __name__ == "__main__":
    main()
