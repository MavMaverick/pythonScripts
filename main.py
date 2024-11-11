from wordWrap import wrapper

words = "This is a sample text to demonstrate the monospace supercalifragilisticexpialidocious lens line-breaking algorithm. I have extended this string to further test the capability of the line breaking. It seems to be working well, which is very good. Hopefully."
max_char_limit = 29


result = wrapper(words, max_char_limit)

for i in result:
    print(i)