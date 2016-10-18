import codecs
import re
#---------------------------Begin Tokenization Function ----------------------
#                   input: senternse  output: listtoken sentense
def Tokenization(sentense):
    token=""
    arrayToken=[]
    for i in range(0,len(sentense)):
        if((ord(sentense[i]) != 32) & (ord(sentense[i]) != 13)):
            token=token+sentense[i]
        else:
            if(len(token)>0):
                arrayToken.append(token)
                token="";
    if (len(token) > 0):
        arrayToken.append(token)
    token=""
    return  arrayToken
#---------------------------------End Tokenization Function------------------



def Normalization(sentens):
    sentens = sentens.strip()   # remove space from begin and end of sentense
    sentens = re.sub(' +', ' ', sentens)  # remove extra space
    sentens = re.sub('([\d+])\.([\d+])', r'\1/\2', sentens)  # replace dot with point
    sentens = re.sub(r'[ـ\r]', '', sentens)  # replace character keshide
    sentens = re.sub(r'[ةۀ]', 'ه', sentens)  # change arabic character ةۀ to ه
    sentens = re.sub(r'[آأإ]', 'ا', sentens)  # change arabic character آأإ to ا
    sentens = re.sub(r'[ئي]', 'ی', sentens)  # change arabic character ي ئ to ی
    sentens = re.sub(r'[ك]', 'ک', sentens)  # change arabic character ك to ک
    sentens = re.sub(r'[ؤ]', 'و', sentens)  # # change arabic character ؤ to و
    sentens = re.sub(r'[‌]', ' ', sentens)  # change nim fasele to fasele
    sentens = re.sub(r'[ًٌٍَُِّْ]', '', sentens)  # remove arabic elemnts (eerab)
    sentens = re.sub(r'[({}<>»«“]', '', sentens)  # remove non text character
    sentens = sentens.replace('[', '')  # change arabic character ة to ه
    sentens = sentens.replace(']', '')  # change arabic character ة to ه
    sentens = re.sub(r'[۰٠]', '0', sentens)  # change arabic & farsi digit to english digit 0
    sentens = re.sub(r'[۱١]', '1', sentens)  # change arabic & farsi digit to english digit 1
    sentens = re.sub(r'[۲٢]', '2', sentens)  # change arabic & farsi digit to english digit 2
    sentens = re.sub(r'[۳٣]', '3', sentens)  # change arabic & farsi digit to english digit 3
    sentens = re.sub(r'[۴٤]', '4', sentens)  # change arabic & farsi digit to english digit 4
    sentens = re.sub(r'[۵٥]', '5', sentens)  # change arabic & farsi digit to english digit 5
    sentens = re.sub(r'[۶٦]', '6', sentens)  # change arabic & farsi digit to english digit 6
    sentens = re.sub(r'[۷٧]', '7', sentens)  # change arabic & farsi digit to english digit 7
    sentens = re.sub(r'[۸٨]', '8', sentens)  # change arabic & farsi digit to english digit 8
    sentens = re.sub(r'[۹٩]', '9', sentens)  # change arabic & farsi digit to english digit 9

    return sentens


ListToken=[]
sent=""
file = codecs.open('sent.txt' , 'r','utf-8')
line=file.read().splitlines()
sent = " ".join(line)
file.close()

print(sent)
normalsent=Normalization(sent)
print(normalsent)

ListToken=Tokenization(normalsent)
print("Tokens Count: ",len(ListToken))
AllToken=""
for token in ListToken:
    AllToken=AllToken+'['+token+'], '
print(AllToken)



quit()