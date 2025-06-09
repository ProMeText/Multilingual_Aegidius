import lxml.etree as ET
import sys

def main():
    source_file = sys.argv[1]
    target_file = sys.argv[2]
    
    tei_ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    source_as_xml = ET.parse(source_file)
    target_as_xml = ET.parse(target_file)
    
    all_lb_source = source_as_xml.xpath("//tei:lb", namespaces=tei_ns)
    all_lb_source_id = source_as_xml.xpath("//tei:lb/@xml:id", namespaces=tei_ns)
    all_lb_source_break = source_as_xml.xpath("//tei:lb/@break", namespaces=tei_ns)
    
    
    all_lb_target = target_as_xml.xpath("//tei:lb", namespaces=tei_ns)
    all_lb_target_id = target_as_xml.xpath("//tei:lb/@xml:id", namespaces=tei_ns)
    
    zipped_source = {ident: br for ident, br in zip(all_lb_target_id, all_lb_source_break)}
    zipped_target = zip(all_lb_target, all_lb_target_id)
    
    for lb_target, target_id in zipped_target:
        try:
            br = zipped_source[target_id]
            if br != "no":
                br = "yes"
            lb_target.set('break', br)
        except KeyError:
            continue
    
    with open(target_file, "w") as output_file:
        output_file.write(ET.tostring(target_as_xml, encoding='utf-8').decode())
        
        
if __name__ == "__main__":
    main()
