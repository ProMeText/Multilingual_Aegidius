import json
import random
import sys
import glob
import os

def main(input_dir, split, output_dir, lang):
    json_dict = {
        "metadata": {"name": "",
                     "delimiter": "£"},
        "examples": []
    }
    all_examples = []
    all_words = 0
    all_chars = 0
    for dirLang in glob.glob(f"{input_dir}/*"):
        
        # On vérifie qu'on matche la langue le cas échéant
        current_lang = dirLang.split("/")[-1]
        if lang and current_lang != lang:
            continue
        for file in glob.glob(f"{dirLang}/*"):
            filename = file.split("/")[-1]
            
            # On verifie qu'on matche bien le split qu'on veut
            if split in filename:
                with open(file, "r") as input_file:
                    file_as_string = input_file.read()
                    file_as_list = file_as_string.split("\n")
                    examples_as_dict = [{"example": item, "lang": current_lang}
                                        for item in file_as_list]
                    all_chars += len(file_as_string.replace("\n", " "))
                    all_words += len(file_as_string.replace("\n", " ").split())
                    all_examples.extend(examples_as_dict)
    random.shuffle(all_examples)
    json_dict["examples"] = all_examples
    json_dict["metadata"]["examples_number"] = len(all_examples)
    json_dict["metadata"]["chars"] = all_chars
    json_dict["metadata"]["words"] = all_words
    json_dict["metadata"]["name"] = split
     
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/{split}.json", "w") as output_file:
        json.dump(json_dict, output_file)

if __name__ == '__main__':
    input_dir = sys.argv[1]
    split = sys.argv[2]
    output_dir = sys.argv[3]
    if len(sys.argv) == 4:
        lang = None
    else:
        lang = sys.argv[3]
    main(input_dir, split, output_dir, lang)
