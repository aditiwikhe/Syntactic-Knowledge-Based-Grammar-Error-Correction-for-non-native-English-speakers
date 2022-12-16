import json

flag = 0
edit_types = []
editor_0 = []
editor_1 = []
language_dict = {}


with open('fce.train.lang.m2', encoding='ISO-8859-1') as file:
    for line in file:
        a = line.rstrip()
        if len(a) > 0 and a[0] == 'S':
            continue
        else:
            if len(a) == 0:
                continue

            elif a[0] == 'A':
                sentence = a.split("|||")
                lang = sentence[-1]
                if lang in language_dict:
                    if sentence[1] in language_dict[lang]:
                        language_dict[lang][sentence[1]] = language_dict[lang][sentence[1]] + 1
                    else:
                        language_dict[lang][sentence[1]] = 1
                else:
                    language_dict[lang] = {}
                    language_dict[lang][sentence[1]] = 1

for x in language_dict.keys():
    language_dict[x] = {k: v for k, v in sorted(language_dict[x].items(), key=lambda item: item[1])}

out_file = open("lang_tags.json", "w")
json.dump(language_dict, out_file, indent=6)
print(language_dict)