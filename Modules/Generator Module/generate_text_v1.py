def generate_to_read():   #Module to get the basic text for the person to read ! 
    from essential_generators import DocumentGenerator
    from cleantext import clean
    gen = DocumentGenerator()
    para = gen.paragraph()
    l = len(para)


    while(l<400):
        para = gen.paragraph()
        l = len(para)
        
    para = clean(para,
        fix_unicode=True,               # fix various unicode errors
        to_ascii=True,                  # transliterate to closest ASCII representation
        lower=True,                     # lowercase text
        no_line_breaks=False,           # fully strip line breaks as opposed to only normalizing them
        no_urls=False,                  # replace all URLs with a special token
        no_emails=False,                # replace all email addresses with a special token
        no_phone_numbers=False,         # replace all phone numbers with a special token
        no_numbers=False,               # replace all numbers with a special token
        no_digits=False,                # replace all digits with a special token
        no_currency_symbols=False,      # replace all currency symbols with a special token
        no_punct=False,                 # remove punctuations
        replace_with_punct="",          # instead of removing punctuations you may replace them
        replace_with_url="<URL>",
        replace_with_email="<EMAIL>",
        replace_with_phone_number="<PHONE>",
        replace_with_number="<NUMBER>",
        replace_with_digit="0",
        replace_with_currency_symbol="<CUR>",
        lang="en"                       # set to 'de' for German special handling
    )

    return para

def clean_to_pass(para):   #Module to get the read text from the user and convert it into sentence for comparison
    import re
    import string
    import nltk
    stopwords = nltk.corpus.stopwords.words('english')
    para = "".join([i for i in para if i not in string.punctuation])
    para = "".join([i.lower() for i in para if i not in string.punctuation])
    para = para.replace('\n',' ')
    para = para.replace("%"," Percentage")
    return para
