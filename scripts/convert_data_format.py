import json
import random
import re
import sys
import glob
import os


def clean_text(text, delimiter):
    # On teste si on a des délimiteurs qui précèdent une espace
    
    text = text.replace("’", "'")
    
    regexp_strip = re.compile(r"[#*•|α^<>]")
    text = re.sub(regexp_strip, "", text)
    
    regexp_punct = re.compile(rf"{delimiter}([\(\)\[\].·,,;¿?¦“…/’‘>«»'¡\-—–―\"])\s?")
    search = re.search(regexp_punct, text)
    if search:
        text = re.sub(regexp_punct, rf"\1{delimiter}", text)

    regexp_space = re.compile(rf"{delimiter}\s")
    search = re.search(regexp_space, text)
    if search:
        text = re.sub(regexp_space, delimiter, text)

    text = text.replace(f"{delimiter}{delimiter}", delimiter)
    
    regexp = re.compile(rf"{delimiter}([^A-Za-zẽ\d+çÇÉÁÍòãÓȝïÈũèÚéçáíƷàÞóúýþ&])\s?")
    search = re.search(regexp, text)
    if search:
        print(text)
        print(search)
        print("Recursinving!")
        text = clean_text(text, delimiter)
    
    # On supprime le délimiteur en fin d'exemple
    try:
        if text[-1] == delimiter:
            text = text[:-1]
    except IndexError:
        print(f"Error with example |{text}|")
        exit()
    
    return text


def main(input_dir, split, output_dir, delimiter, lang):
    json_dict = {
        "metadata": {"name": "",
                     "delimiter": delimiter},
        "examples": []
    }
    all_examples = []
    all_words = 0
    all_chars = 0
    langs = []
    for dirLang in glob.glob(f"{input_dir}/*"):

        # On vérifie qu'on matche la langue le cas échéant
        current_lang = dirLang.split("/")[-1]
        if lang and current_lang != lang:
            continue
        langs.append(current_lang)
        for file in glob.glob(f"{dirLang}/*"):
            if ".json" in file:
                continue
            filename = file.split("/")[-1]

            # On verifie qu'on matche bien le split qu'on veut
            if split in filename:
                with open(file, "r") as input_file:
                    file_as_string = input_file.read()
                    file_as_list = file_as_string.split("\n")
                    examples_as_dict = [{"example": clean_text(item, delimiter), "lang": current_lang}
                                        for item in file_as_list if item != ""]
                    all_chars += len(file_as_string.replace("\n", " "))
                    all_words += len(file_as_string.replace("\n", " ").split())
                    all_examples.extend(examples_as_dict)
    random.shuffle(all_examples)
    json_dict["examples"] = all_examples
    json_dict["metadata"]["examples_number"] = len(all_examples)
    json_dict["metadata"]["chars"] = all_chars
    json_dict["metadata"]["words"] = all_words
    json_dict["metadata"]["name"] = split
    json_dict["metadata"]["langs"] = langs

    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/{split}.json", "w") as output_file:
        json.dump(json_dict, output_file)


if __name__ == '__main__':
    input_dir = sys.argv[1]
    split = sys.argv[2]
    output_dir = sys.argv[3]
    delimiter = sys.argv[4]
    if len(sys.argv) == 5:
        lang = None
    else:
        lang = sys.argv[5]
    main(input_dir, split, output_dir, delimiter, lang)
