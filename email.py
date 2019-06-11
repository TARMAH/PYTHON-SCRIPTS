text='maestrobhs@gmail.com blah blah blah tiqbal.bscs16seecs@seecs.edu.pk'

pattern = re.compile(r"[\w]+\.*[\w]*@[a-zA-Z]+\.([a-z]{2,3}) | [\w]+\.*[\w]*@[a-zA-Z]+\.([a-z]{2,3})\.([a-z]{2,3})")

matches = pattern.finditer(text)

for match in matches:
    print(match)
