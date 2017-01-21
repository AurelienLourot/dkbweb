#!/usr/bin/env python2.7

# this is not a real test, it is only used to test the regular expressions

import re

cardid = "0000"
label_text = "1234********0000 / Kreditkarte"
ccpattern = r'\b\S{12}(?<=%s)\b' % re.escape(cardid)
ccpattern_all = r'\b\d{4}\S{12}(?<=%s)\b' % re.escape(cardid)

print(re.search(ccpattern, label_text, re.I).group(0))
print(re.search(ccpattern_all, label_text, re.I).group(0))

cardid = "0000"
label_text = "DE12345678901234560000 / Girokonto"
bapattern = r'\b[A-Z]{2}\d{16}%s\b' % re.escape(cardid)

print(re.search(bapattern, label_text, re.I).group(0))

