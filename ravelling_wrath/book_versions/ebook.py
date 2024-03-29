import re
import datetime
import os.path

import utils
import ravelling_wrath.main
  
tags = "Fiction, Young Adult, Fantasy, Urban Fantasy, Adventure, Consent, Healthy Relationships, Mental Health, Coming of Age, LGBT, Lesbian,"
tags = [match.group (1) for match in re.finditer (r"([^,\s][^,]*)", tags)]

package = '''<?xml version='1.0' encoding='utf-8'?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uuid_id" version="2.0">
'''
metadata = '''<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:title>Ravelling Wrath</dc:title>
    <dc:creator opf:role="aut" opf:file-as="Dupree, Eli">Eli Dupree</dc:creator>
    <dc:publisher>Eli Dupree</dc:publisher>
    <dc:date>'''+datetime.date.today().isoformat()+'''</dc:date>
    <dc:contributor opf:role="cov" opf:file-as="Fensore, Sarah">Sarah Fensore</dc:contributor>
    <dc:contributor opf:role="ill" opf:file-as="Fensore, Sarah">Sarah Fensore</dc:contributor>
    <dc:creator opf:role="cov" opf:file-as="Dupree, Eli">Eli Dupree</dc:creator>
    <dc:creator opf:role="ill" opf:file-as="Dupree, Eli">Eli Dupree</dc:creator>
    <dc:identifier id="uuid_id" opf:scheme="uuid">c0b3ea68-aced-4746-966b-7b0fc27ba1fc</dc:identifier>
    '''+'''
    '''.join(f'''<dc:subject>{tag}</dc:subject>''' for tag in tags) + '''
    <dc:description>'''+utils.strip_tags(ravelling_wrath.main.long_blurb)+'''</dc:description>
    <dc:language>en</dc:language>
    <dc:identifier opf:scheme="ISBN">TODO</dc:identifier>
    <meta name="cover" content="cover"/>
    <meta name="dcterms:modified">'''+datetime.datetime.now().isoformat()+'''</meta>
  </metadata>'''
unused = '''
  <manifest>
  
  </manifest>
  <spine>
  
  </spine>
</package>
'''

def fix_converted_epub_contents(contents_path):
  opf_path = os.path.join(contents_path, "content.opf")
  with open(opf_path) as file:
    opf = file.read()
  assert package in opf
  
  opf = re.sub(r"<metadata.*?</metadata>", metadata, opf, flags=re.DOTALL)
  
  with open(opf_path, "w") as file:
    file.write(opf)
  
  