from pathlib import Path 

txt_files = sorted(Path("./infore").glob("*.txt"))

# write all word 
f = open("words.txt", "w", encoding="utf-8")
for txt_file in txt_files:
    wav_file = txt_file.with_suffix(".wav")
    if not wav_file.exists():
        continue
    line = open(txt_file, "r", encoding="utf-8").read()
    for word in line.strip().lower().split():
        f.write(word)
        f.write("\n")
f.close()



black_list = (
    []
    + ["q", "adn", "h", "stress", "b", "k", "mark", "gas", "cs", "test", "l", "hiv"]
    + ["v", "d", "c", "p", "martin", "visa", "euro", "laser", "x", "real", "shop"]
    + ["studio", "kelvin", "đt", "pop", "rock", "gara", "karaoke", "đicr", "đigiúp"]
    + ["khmer", "ii", "s", "tr", "xhcn", "casino", "guitar", "sex", "oxi", "radio"]
    + ["qúy", "asean", "hlv" "ts", "video", "virus", "usd", "robot", "ph", "album"]
    + ["s", "kg", "km", "g", "tr", "đ", "ak", "d", "m", "n"]
)



     
ws = open("words.txt").readlines()
f = open("lexicon.txt", "w")
for w in sorted(set(ws)):
    w = w.strip()

    # this is a hack to match phoneme set in the vietTTS repo
    p = list(w)
    p = " ".join(p)
    if w in black_list:
        continue
    else:
        f.write(f"{w}\t{p}\n")
f.close()
     
