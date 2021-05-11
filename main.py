import null as null

file = open("DictAll词都词库 copy/马列主义,毛泽东思想,邓小平理论.txt")
raw_data = file.readline()

while raw_data != null:
    raw_data = file.readline()
    fix_data = raw_data.split("：")

    chn_lexi = open("中文词库.txt", "a")
    eng_lexi = open("英文词库.txt", "a")

    chn_lexi.writelines(fix_data[0])
    chn_lexi.writelines("\n")
    eng_lexi.writelines(fix_data[1])
