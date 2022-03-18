
def usuwanie_bialych_znakow(text):
    nowy_text = text.replace(' ','')
    nowy_text.join('-')
    print(nowy_text)

usuwanie_bialych_znakow('k       o,t e!  m:a  _ (/          8 ')