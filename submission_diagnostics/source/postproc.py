import re, zipfile, os
def to_diagnostics(src, dst):
    zin = zipfile.ZipFile(src)
    h3 = zin.read('word/header3.xml').decode('utf8')
    m = re.search(r'<w:r><w:rPr>(?:(?!</w:rPr>).)*</w:rPr><w:drawing>(?:(?!</w:drawing>).)*?Journal of Clinical Medicine logo(?:(?!</w:drawing>).)*</w:drawing></w:r>', h3, flags=re.S)
    assert m
    rid = re.search(r'r:embed="([^"]+)"', m.group(0)).group(1)
    rels = zin.read('word/_rels/header3.xml.rels').decode('utf8')
    target = re.search(r'<Relationship Id="%s"[^>]*Target="([^"]+)"' % rid, rels).group(1)
    new_run = '<w:r><w:rPr><w:rFonts w:ascii="Palatino Linotype" w:hAnsi="Palatino Linotype"/><w:b/><w:i/><w:color w:val="1F4E79"/><w:sz w:val="40"/></w:rPr><w:t>Diagnostics</w:t></w:r>'
    h3 = h3.replace(m.group(0), new_run)
    rels = re.sub(r'<Relationship Id="%s"[^>]*/>' % rid, '', rels)
    zout = zipfile.ZipFile(dst + '.tmp', 'w', zipfile.ZIP_DEFLATED)
    for it in zin.infolist():
        data = zin.read(it.filename)
        if it.filename == 'word/' + target: continue
        if it.filename == 'word/header3.xml': data = h3.encode('utf8')
        elif it.filename == 'word/_rels/header3.xml.rels': data = rels.encode('utf8')
        elif re.match(r'word/(header|footer)\d\.xml', it.filename):
            s = data.decode('utf8').replace('J. Clin. Med.', 'Diagnostics')
            s = re.sub(r'(<w:t[^>]*>)\s*15(</w:t>)', r'\g<1> 16\2', s); data = s.encode('utf8')
        zout.writestr(it, data)
    zout.close(); zin.close()
    os.replace(dst + '.tmp', dst)
