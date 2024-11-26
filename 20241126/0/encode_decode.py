s = "вопрос"
print(s.encode("cp1251").decode("koi8-r"))

for w in ("бМХЛЮМХЕ", "ОХРЮМХЕ"):
    print(w, w.encode("koi8-r").decode("cp1251"))