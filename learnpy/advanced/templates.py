from  string import Template


s1 = Template('$who likes $what')
print(s1.substitute(who='tim', what='kung pao'))

s2 = Template('${who}likes $what')
print(s2.substitute(who='tim', what='kung pao'))

s2 = Template('$${who}likes $what')
print(s2.substitute(who='tim', what='kung pao'))


d = dict(who='java')
print(Template('$who need $100').safe_substitute(d))
print(Template('$who need 100').substitute(d))


# substitute is more strict. Identifiers and variants must be one-one, otherwise it will throw error.
# While for safe_subtitue, it will print $XXX if its variant is not found