file = "book.bib"

data = []
must_key = {}
# 必要的 key
must_key["article"] = "author, title, journal, year, volume"
must_key["book"] = "author, title, publisher, year"
must_key["inproceedings"] = "author, title, booktitle, year"
must_key["techreport"] = "author, title, institution, year"
must_key["inbook"] = "author, pages, title, publisher, year"

for key in must_key.keys():
    tmp = must_key[key].split(',')
    tmp = [i.strip() for i in tmp]
    must_key[key] = tmp

is_bib = False
tmp_entry = set()
invalid = []

with open(file, encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) <= 0:
            is_bib = False
            must_keys = must_key[bib_key]
            cnt = 0
            for item in must_keys:
                if item not in tmp_entry:
                    if cnt == 0:
                        print(bib_name, "miss key: ", end=" ")
                        cnt += 1
                    print(item, end=", ")
            if cnt != 0:
                print()
        elif line[0] == '@':
            bib_key = line.split('{')[0][1:].lower()
            is_bib = True
            bib_name = line
            tmp_entry = set()
        elif is_bib and "=" in line:
            bib_entry = line.split('=')[0].strip().lower()
            tmp_entry.add(bib_entry)
