#!/usr/bin/python

text = "X-DSPAM-Confidence:    0.8475";
ftext = float(text.find('0.8475'))
print text[23:]
