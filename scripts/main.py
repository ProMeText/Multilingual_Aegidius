import lxml.etree as ET
import sys

tei = {'tei': 'http://www.tei-c.org/ns/1.0'}
tei_namespace_url = 'http://www.tei-c.org/ns/1.0'

def main(input_file):
    output_file = input_file.replace(".xml", ".txt")
    
    as_tree = ET.parse(input_file)
    all_lines = as_tree.xpath("//tei:lb", namespaces=tei)
    lines_and_break = []
    for line in all_lines:
        br = line.xpath("@break")[0]
        line_text = line.tail
        print(line_text)
        lines_and_break.append((br, line_text))
    
    out_file = ""
    for br, line in lines_and_break:
        print(line)
        if br == "yes":
            out_file += " "
        out_file += line
    
    with open(output_file, "w") as output:
        output.write(out_file)
    print(f"Result written to {output_file}")

if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)