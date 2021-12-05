import json
import re
import argparse


def read_input(input_path):
    with open(input_path,'r',encoding='utf-8') as input_file:
        input_data = json.load(input_file)
        input_file.close()
    return input_data

#Constants Used
num2wordDict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred', 1000: 'thousand', 1000000: 'million',
    1000000000: 'billion', 1000000000000: 'trillion', 1000000000000000: 'quadrillion'
}

num2ordinalsDict = {
    0: 'zeroth',1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth',
    6: 'sixth', 7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth',
    11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth',
    15: 'fifteenth', 16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth',
    19: 'nineteenth', 20: 'twentieth',
    30: 'thirtieth', 40: 'fortieth', 50: 'fiftieth', 60: 'sixtieth',
    70: 'seventieth', 80: 'eightieth', 90: 'ninetieth',
    100: 'hundredth', 1000: 'thousandth', 1000000: 'millionth'
}

num2ordinalsList = ['zeroth','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth']

romansDict = {
    'II' : 'two' , 'III' : 'three' , 'IV' : 'four' , 'V' : 'five' , 'VI' : 'six' ,
    'VII' : 'seven' , 'VIII' : 'eight' , 'IX' : 'nine' , 'X' : 'ten' , 'XI' : 'eleven',
    'XII' : 'twelve', 'XIII' : 'thirteen' , 'XIV' : 'fourteen' , 'XV' :  'fifteen' , 'XVI' : 'sixteen',
    'XVII' : 'seventeen' , 'XVIII' : 'eighteen' , 'XIX' : 'nineteen' , 'XX' : 'twenty'
}

theromansDict = {
    'II' : 'the second' , 'III' : 'the third' , 'IV' : 'the fourth' , 'V' : 'the fifth' , 'VI' : 'the sixth' ,
    'VII' : 'the seventh' , 'VIII' : 'the eighth' , 'IX' : 'the ninth' , 'X' : 'the tenth' , 'XI' : 'the eleventh',
    'XII' : 'the twelfth', 'XIII' : 'the thirteenth' , 'XIV' : 'the fourteenth' , 'XV' :  'the fifteenth' , 'XVI' : 'the sixteenth',
    'XVII' : 'the seventeenth' , 'XVIII' : 'the eighteenth' , 'XIX' : 'the nineteenth' , 'XX' : 'the twentieth'
}



listNum = [1000000000000000,1000000000000, 1000000000, 1000000, 1000,
            100, 90, 80, 70, 60, 50, 40, 30, 20, 19,
         18, 17, 16, 15, 14, 13, 12, 11, 10,
          9, 8, 7, 6, 5, 4, 3, 2, 1]

unitsDict = {
    '/km²': 'per square kilometers' , 
    'mi' : 'miles', 
    'km' : 'kilometers', 
    '/km2' : 'per square kilometers', 
    'm' : 'meters',
    'km2' : 'square kilometers',
    'mm' : 'millimeters',
    'KB' : 'kilobytes', 
    'ha' : 'hectares',
    'PB' : 'petabytes',
    'Gb/s' : 'gigabits per second', 
    'MB' : 'megabytes',
    'cm' : 'centimeters',
    'GB' : 'gigabytes', 'Mb/s' : 'megabits per second' , 'km²' : 'square kilometers' , 'm²' : 'square meters',
    'Kb/s' : 'kilobits per second'

}

#(/km²|mi|km|/km2|m|km2|mm|KB|ha|PB|Gb/s|MB|cm|GB|Mb/s|km²|m²|Kb/s)
currencyDict = {
    'm' : 'million', 
    'M' : 'million',
    'million' : 'million',
    'Million' : 'million',
    'billion' : 'billion'
}

monthList = ['sil' , 'january' , 'february' , 'march' , 'april' , 'may' ,'june' , 'july' , 'august' , 'september' , 'october' , 'november' , 'december']


rupeeDict = {
    'cr' : 'crore', 'crore' : 'crore' , 'lakhs' : 'lakh' , 'lakh' : 'lakh' , 'crores' : 'crore'
}



def num2word(number_whole):
    num2string = ''
    # num2stringList = []
    for i in range(len(listNum)):
        # remainder = number_whole//listNum[i]
        remainder = number_whole/listNum[i]
        remainder_int = int(remainder)
        # while(True):
        if(remainder_int == 0):
            continue
        if(listNum[i] >= 100):
            num2string = num2string + num2word(remainder_int) + ' '
            number_whole = number_whole - (remainder_int * listNum[i])
            num2string = num2string + num2wordDict[listNum[i]]
        else:
            number_whole = number_whole - (remainder_int * listNum[i])
            num2string = num2string + num2wordDict[listNum[i]]
        if(number_whole > 0):
            num2string = num2string + ' '
        
    return num2string

def num2wordFrac(Number,o_check):
    StringNumber = ''
    digits = [int(digit) for digit in str(Number)]    
    if(o_check):
        StringDigits = ['o' if(d==0) else num2word(d) for d in digits]
    else:
        StringDigits = ['zero' if(d==0) else num2word(d) for d in digits]
    StringNumber = ' '.join(StringDigits)
    return StringNumber



def num2wordFrac1(token,o_check):
    fracstring = ''
    zero_check = False
    if(int(token) == 0):
        zero_check = True
    fracList = []
    for i in token:
        if(int(i)==0 and zero_check):
            fracList.append('zero')
        elif(int(i) == 0):
            fracList.append('o')
        else:
            fracList.append(num2word(int(i)))
        
    fracstring = ' '.join(fracList)
    return fracstring




#AllNumbersCode
def numberChecker(token,o_check):
    minus_flag = False
    FinalNumber = ''
    if(token[0] == '-'):
        token1 = token[1:]
        minus_flag = True
    else:
        token1 = token

    comma_count = token1.count(',')
    comma_removed_token = token1.replace(",",'')

    if(comma_removed_token.count('.')>0):
        #checks for decimal numbers
        list1 = comma_removed_token.split('.')
        number_ = list(map(int, comma_removed_token.split('.')))
        number_whole = number_[0]
        number_frac = number_[1]
        if(number_whole == 0):
            number_whole_word = 'zero'
        else:
            number_whole_word = num2word(number_whole)
        
        number_frac_word = num2wordFrac1(list1[1],o_check)
            
        if(minus_flag):
            FinalNumber += 'minus ' + number_whole_word + ' ' + 'point ' + number_frac_word
        else:
            FinalNumber += number_whole_word + ' ' + 'point ' + number_frac_word
         
    else:
        #normal algo for non decimal numbers
        
        comma_removed_token = token1.replace(",",'')
        number_token = int(comma_removed_token)
        if(number_token == 0):
            numberWord = 'zero'

        elif(((number_token >= 1100 and number_token < 2000) or (number_token >= 2010 and number_token < 2070)) and comma_count==0 ):
            number_token_string = str(number_token)
            yearList = list(map(''.join, zip(*[iter(number_token_string)]*2))) 
            yearList1 = int(yearList[0])
            yearList2 = int(yearList[1])   
            if(yearList2 == 0 ):
                numberWord = num2word(yearList1) + ' hundred'
            elif(yearList2<10):
                numberWord = num2word(yearList1) + ' o ' + num2word(yearList2) 
            else:
                numberWord = num2word(yearList1) + ' ' + num2word(yearList2)       
        else:
            numberWord = num2word(number_token)
        if(minus_flag):
            FinalNumber = FinalNumber + 'minus ' + numberWord
        else:
            FinalNumber = FinalNumber + numberWord
        
    return FinalNumber

def num2ordinal(token):
    OrdinalString = ''
    if(int(token) in num2ordinalsDict.keys()):
        int_token = int(token)
        return num2ordinalsDict[int_token]
    elif(token[-1]=='0' and len(token)==2):
        # print("hey")
        a = int(token[0])
        a = a*10
        OrdinalString =  num2word(a) + ' ' + num2ordinalsDict[int(token[-1])]
    elif(token[-1]=='0' and len(token)==3):
        a = int(token[0])
        a = a*100
        OrdinalString =  num2word(a) + ' ' + num2ordinalsDict[int(token[-2:])]
    # elif(token[-1]=='0' and token[-2] == '0'):
    #     print("hey")
    elif(token[-1]=='0' and token[-2]=='0'):
        a = int(token)
        num_string = num2word(a)
        num_stringList = num_string.split()
        if(num_stringList[-1] in num2wordDict.values()):
            OrdinalString = num_string + 'th'
    else:
        a = int(token)
        num_string = num2word(a)
        num_stringList = num_string.split()
        num_string_list = num_stringList[:-1]
        b = token[-1]
        c = int(b)
        OrdinalString = ' '.join(num_string_list)
        OrdinalString = OrdinalString +" " + num2ordinalsList[c]

    return OrdinalString


def currency2word(token):
    CurrencyString = ''
    token1 = token[1:]
    comma_removed_token = token1.replace(",",'')

    if(comma_removed_token.count('.')>0):
        #checks for decimal numbers
        
        number_ = list(map(int, comma_removed_token.split('.')))
        number_whole = number_[0]
        number_frac = number_[1]
        if(number_whole == 0):
            number_whole_word = 'zero'
        else:
            number_whole_word = num2word(number_whole)
        number_frac_word = num2word(number_frac)
        if(number_whole_word == 'one'):
            CurrencyString += number_whole_word + ' dollar and ' +  number_frac_word + (' cent' if number_frac_word=='one' else ' cents') 
        else:
            CurrencyString += number_whole_word + ' dollars and ' +  number_frac_word + (' cent' if number_frac_word=='one' else ' cents') 
    else:
        comma_removed_token = token1.replace(",",'')
        number_token = int(comma_removed_token)
        if(number_token == 'one'):
            CurrencyString += num2word(number_token) + ' dollar'
        else:
            CurrencyString += num2word(number_token) + ' dollars'

    return CurrencyString

def rupee2word(token):
    CurrencyString = ''
    
    a = re.fullmatch(r'^(Rs\.?|₹) ?([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]+)?$',token).groups()
    
    comma_removed_token = a[1].replace(",",'')

    if(a[3]):
        #checks for decimal numbers
        
        number_whole = int(comma_removed_token)
        number_frac = int(a[3][1:])
        if(number_whole == 0):
            number_whole_word = 'zero'
        else:
            number_whole_word = num2word(number_whole)
        number_frac_word = num2word(number_frac)
        if(number_whole_word == 'one'):
            CurrencyString += number_whole_word + ' rupee and ' +  number_frac_word + (' paisa' if number_frac_word=='one' else ' paise') 
        else:
            CurrencyString += number_whole_word + ' rupees and ' +  number_frac_word + (' paise' if number_frac_word=='one' else ' paise') 
    else:
        number_token = int(comma_removed_token)
        if(number_token == 'one'):
            CurrencyString += num2word(number_token) + ' rupee'
        else:
            CurrencyString += num2word(number_token) + ' rupees'

    return CurrencyString



def rupee2word2(token):
    CurrencyString = ''
    a = re.fullmatch(r'^(Rs\.?|₹) ?([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]+)? (crore|crores|cr|lakhs|lakh|lacs|lac)',token).groups()

    if(a[3]):
        amount = a[1] + a[3]
    else:
        amount = a[1]
    amountString = numberChecker(amount,True)

    

    CurrencyString = amountString + ' ' + rupeeDict[a[-1]].lower() + ' rupees'

    return CurrencyString

def currency2word2(token):
    CurrencyString = ''
    a = re.fullmatch(r'(\$|£|€)(\d+(\.?\d+)?) ?(million|billion|m|M|Million)',token).groups()
    
    curr = ''
    if(a[0] == '$'):
        curr = 'dollars'
    elif(a[0] == '€'):
        curr = 'euros'
    else:
        curr = 'pounds'
    # print(a)
    CurrencyString = numberChecker(a[1],False) + ' ' + currencyDict[a[-1]] + ' ' + curr
    return CurrencyString
# print(currency2word2('£300 million'))



def currency2word3(token):
    CurrencyString = ''
    
    token1 = token[1:]
    
    comma_removed_token = token1.replace(",",'')

    if(comma_removed_token.count('.')>0):
        #checks for decimal numbers
        
        number_ = list(map(int, comma_removed_token.split('.')))
        number_whole = number_[0]
        number_frac = number_[1]
        if(number_whole == 0):
            number_whole_word = 'zero'
        else:
            number_whole_word = num2word(number_whole)
        number_frac_word = num2word(number_frac)
        if(number_whole_word == 'one'):
            CurrencyString += number_whole_word + ' pounds and ' +  number_frac_word + (' penny' if number_frac_word=='one' else ' pence') 
        else:
            CurrencyString += number_whole_word + ' pounds and ' +  number_frac_word + (' penny' if number_frac_word=='one' else ' pence') 
    else:
        comma_removed_token = token1.replace(",",'')
        number_token = int(comma_removed_token)
        if(number_token == 'one'):
            CurrencyString += num2word(number_token) + ' pound'
        else:
            CurrencyString += num2word(number_token) + ' pounds'
    return CurrencyString

# print(currency2word3('£50,000'))

def currency2word4(token):
    CurrencyString = ''
    token1 = token[1:]
    comma_removed_token = token1.replace(",",'')

    if(comma_removed_token.count('.')>0):
        #checks for decimal numbers
        
        number_ = list(map(int, comma_removed_token.split('.')))
        number_whole = number_[0]
        number_frac = number_[1]
        if(number_whole == 0):
            number_whole_word = 'zero'
        else:
            number_whole_word = num2word(number_whole)
        number_frac_word = num2word(number_frac)
        if(number_whole_word == 'one'):
            CurrencyString += number_whole_word + ' euros and ' +  number_frac_word + (' cent' if number_frac_word=='one' else ' cents') 
        else:
            CurrencyString += number_whole_word + ' euros and ' +  number_frac_word + (' cent' if number_frac_word=='one' else ' cents') 
    else:
        comma_removed_token = token1.replace(",",'')
        number_token = int(comma_removed_token)
        if(number_token == 'one'):
            CurrencyString += num2word(number_token) + ' euro'
        else:
            CurrencyString += num2word(number_token) + ' euros'
    return CurrencyString

def abbr2word(token):
    AbbrString = ''
    if(token.count('.')>0):
        # print(token)
        a = token.replace('.','')
        # print(a)
        tokensList = [b for b in a]
        # tokensList = token.split('.')
        lower_list = [lt.lower() for lt in tokensList]
        AbbrString = ' '.join(lower_list)
    else:
        lower_string = token.lower()
        lower_list = [char for char in lower_string]
        AbbrString = ' '.join(lower_list)

    AbbrString1 = re.sub(' +', ' ', AbbrString)
    return str(AbbrString1)




def time2word(token):
    TimeString = ''
    a = re.fullmatch(r'(1[0-2]|0?[1-9])(:([0-5]\d))? ?([AaPp]\.?[Mm])\.?( ?PST)?',token).groups()
    suffix_ = a[-2].split('.')
    suffix = ''.join(suffix_)
    if(a[2] and int(a[2]) != 0):
        TimeString = num2word(int(a[0])) + ' ' +  num2word(int(a[2])) + ' ' +  suffix[0].lower() + ' ' + suffix[1].lower()
    else:
        TimeString = num2word(int(a[0])) + ' ' + suffix[0].lower() + ' ' + suffix[1].lower()
    
    # print("TIME LIST: " , a)
    if(a[-1]!=None):
        TimeString += ' p s t'

    return TimeString
    


def splNum(token):
    splnumstring = ''
    a = []
    # a = re.fullmatch('(\d+) \((\d+)\) (\d+)-(\d+)',token).groups()
    for i in token:
        
        if(re.fullmatch(r'([^\w\s]| )',i)):
            if(i == ' '):
                continue
            else:
                a.append('sil')
        else:
            a.append(num2wordFrac(i, True))
    splnumstring = ' '.join(a)
    return splnumstring


def time2word2(token):
    TimeString = ''
    timelist = token.split(':')
    # hours = num2word(int(timelist[0]))
    # minutes = num2word(int(timelist[1]))
    # seconds = num2word(int(timelist[2]))
    hours = numberChecker(timelist[0],False)
    minutes = numberChecker(timelist[1],False)
    seconds = numberChecker(timelist[2],False)
    TimeString = hours + " hours " + minutes + " minutes and " + seconds + " seconds"
    return TimeString


def time2word3(token):
    TimeString = ''
    timeListString = token.split(':')
    timeList = list(map(int, token.split(':')))
    if(timeList[0]==0 and timeList[1]==0):
        TimeString = 'zero hundred'
    elif(timeList[0] == 0):
        TimeString = 'zero' + ' ' + num2word(timeList[1])
    elif(timeList[1]==0):
        if(timeList[0]<12 and timeList[0]>0):
            TimeString =  num2word(timeList[0]) + ' ' + "o'clock"
        else:
            TimeString = num2word(timeList[0]) + ' ' + 'hundred'
    else:
        TimeString = num2word(timeList[0]) + ' ' + num2word(timeList[1])
    return TimeString
# test = '00:00'
# print(time2word3(test))


def date2word(token):
    DateString = ''
    dateList = token.split()
    DateString = dateList[0].lower() + " " + numberChecker(dateList[1],False)
    return DateString



def date2word2(token):
    DateString = ''
    dateList = token.split()
    DateString = 'the ' + num2ordinal(dateList[0]) + ' of ' + dateList[1].lower() + " " + numberChecker(dateList[2],False)
    return DateString
# print(date2word2('1 March 2021'))




def date2word3(token):
    DateString = ''
    # print("Token:" , token)
    a = re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) ([1-2]?\d),? (\d{4})',token).groups()
    DateString = a[0].lower() + ' ' + num2ordinal(a[1]) + ' ' + numberChecker(a[2],False)

    # dateList = token.split()
    # date = dateList[1]
    # numericalData = re.findall(r'\d+', date)
    # dateNum = list(map(int, numericalData))
    # # print("DateNum: " , dateNum[0])
    # DateString = 'the ' + num2ordinal(str(dateNum[0])) + ' of ' + dateList[0].lower() + " " + numberChecker(dateList[2],False)
    return DateString
# print(date2word3('May 29, 2013'))


def date2word4(token):
    DateString = ''
    a = re.fullmatch(r'(\d+) (January|February|March|April|May|June|July|August|September|October|November|December)',token).groups()
    DateString = 'the ' + num2ordinal(a[0]) + ' of ' + a[1].lower()
    return DateString



def date2word5(token):
    DateString = ''
    a = re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9])',token).groups()
    DateString = a[0].lower() + ' ' + num2ordinal(int(a[1]))
    return DateString


def date2word6(token):
    DateString = ''
    a = re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9])(st|nd|th|rd),? (\d{4})',token).groups()
    DateString = a[0].lower() + ' ' + num2ordinal(int(a[1])) + ' ' + numberChecker(a[3], False)
    return DateString


def date2word7(token):
    DateString = ''
    a = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})',token).groups()
    # print(a)
    DateString = 'the ' + num2ordinal(a[2]) + ' of ' + monthList[int(a[1])] + ' ' + numberChecker(a[0],False)
    return DateString

def isbn2word(token):
    IsbnString = ''
    isbnlist = ['sil' if(d=='-' or d == ' ') else num2wordFrac(int(d),True) for d in token]
    IsbnString = ' '.join(isbnlist)
    return IsbnString




def fraction2word(token):
    FractionString = ''
    fractionList = token.split('/')
    if(fractionList[1] == '4'):
        if(fractionList[0] == '1'):
            FractionString = numberChecker(fractionList[0],False) + ' ' + 'quarter'  
        else:
            FractionString = numberChecker(fractionList[0],False) + ' ' + 'quarters'    
    elif(fractionList[1] == '2' and fractionList[0] == '1'):
        FractionString = 'one half'
    elif(fractionList[1] == '2' and fractionList[0] == '0'):
    # elif(int(fractionList[0])>1 and fractionList[1] == '2'):
        FractionString = 'zero half'
    else:
        FractionString = numberChecker(fractionList[0],False) + ' ' + num2ordinal(fractionList[1]) + 's'
    return FractionString


def units2word(token):
    UnitsString = ''
    a = re.fullmatch(r'(\d+(,?\d*)*(\.\d+)?) ?(/km²|mi|km|/km2|m|km2|mm|KB|ha|PB|Gb/s|MB|cm|GB|Mb/s|km²|m²|Kb/s)',token).groups()
    UnitsString = numberChecker(a[0],True) + ' ' + unitsDict[a[-1]]
    return UnitsString




def mixfrac2word(token):
    FracString = ''
    a = re.fullmatch(r'(\d+) ((\d+)/(\d+))',token).groups()
    if(a[1] == '1/2'):
        FracString = num2word(int(a[0])) + ' and a half'
    
    elif(a[3] == '4'):
        if(a[1] == '1/4'):
            FracString = num2word(int(a[0])) + ' and a quarter'
        else:
            FracString = num2word(int(a[0])) + ' and ' + num2word(int(a[2])) + ' ' + 'quarter' + 's'
    else:
        FracString = num2word(int(a[0])) + ' and ' + num2word(int(a[2])) + ' ' + num2ordinal(a[3]) + 's'
    # print(a)
    return FracString
# print(mixfrac2word('1 1/2'))


def specialCase2(token):
    splString = ''
    Number2Word = numberChecker(token[:-1],False)
    if(Number2Word[-1] == 'y'):
        splString = Number2Word[:-1] + 'ies'
    else:
        splString = Number2Word + 's'
    return splString


def roman2word(token,input_tokens):
    RomanString = ''
    idx = input_tokens.index(token)
    if(idx > 0):
        a = input_tokens[idx-1]
        if(a[0].isupper()):
            RomanString = theromansDict[token]
            return RomanString
    RomanString = romansDict[token]
    return RomanString



def solution(input_tokens):
    solutionTokens = []

    for i,_token_ in enumerate(input_tokens):
        _token = _token_.rstrip()
        token = _token.lstrip()
        #checks the punctuation
        # print("TOKEN: ", token)

        try:

            if(re.match(r'([^\w\s]|\_)$',token)):
                solutionTokens.append('sil')
            
            elif(token in romansDict.keys()):
                # print("HEY")
                Roman2Word = roman2word(token,input_tokens)
                # print("HEY")
                solutionTokens.append(Roman2Word)

            elif(re.fullmatch(r'[0]\d{4,}',token)):
                Number2Word = num2wordFrac(token, True)
                solutionTokens.append(Number2Word)
            #checks for numbers
            elif(re.fullmatch(r'(-?[0-9]+|-?[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]+)?',token)):
                Number2Word = numberChecker(token,False)
                solutionTokens.append(Number2Word)   
            # checks for price starting with $
            elif(re.fullmatch(r'\$([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]{1,2})?',token)):
                Currency2Word = currency2word(token)
                solutionTokens.append(Currency2Word)

            elif(re.fullmatch(r'(£)([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]{1,2})?',token)):
                
                Currency2Word = currency2word3(token)
                solutionTokens.append(Currency2Word)

            elif(re.fullmatch(r'(€)([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]{1,2})?',token)):
                # print(token)
                Currency2Word = currency2word4(token)
                solutionTokens.append(Currency2Word)
            
            elif(re.fullmatch(r'(\$|£|€)(\d+(\.?\d+)?) ?(million|billion|m|M|Million)',token)):
            # elif(re.fullmatch(r'(\$|\xa3|\xc2\xa3|\u20ac|£|€)(\d+(\.?\d+)) ?(million|billion|m|M)',token)):
                Currency2Word = currency2word2(token)
                solutionTokens.append(Currency2Word)
            
            elif(re.fullmatch(r'([A-Za-z]+)(-)',token)):
                # print("HEYYYYY" , token)
                # print("1: " ,token)
                a = re.fullmatch(r'([A-Za-z]+)(-)',token).groups()
                Abbr2Word = abbr2word(a[0])
                solutionTokens.append(Abbr2Word)

            elif(re.fullmatch(r'([A-Z]{3,})s',token)):
                a = re.fullmatch(r'([A-Z]{3,})s',token).groups()
                # print('2: ' , token)
                Abbr2Word = abbr2word(a[0]) + "'s"
                solutionTokens.append(Abbr2Word)

            #checks for abbr
            elif(re.fullmatch(r'([A-Z][^a-z]{1,9}\.?)+',token)):
                # print('3: ' , token)
                Abbr2Word1 = abbr2word(token)
                Abbr2Word = Abbr2Word1.rstrip()
                solutionTokens.append(Abbr2Word)

            elif(re.fullmatch(r'([A-Z]{3,}[a-z]+)',token)):
                Abbr2Word = abbr2word(token)
                solutionTokens.append(Abbr2Word)
            #checks for Time in HH:MM format
            elif(re.fullmatch(r'(1[0-2]|0?[1-9])(:([0-5]\d))? ?([AaPp]\.?[Mm])\.?( ?PST)?',token)):
                Time2Word = time2word(token)
                solutionTokens.append(Time2Word)

            #checks for time in hh:mm:ss
            elif(re.fullmatch(r'([01][0-9]|2[0-3]|[1-9]):([0-5][0-9]):([0-5][0-9])',token)):
                Time2Word = time2word2(token)
                solutionTokens.append(Time2Word)

            #checks for Time in HH:mm format
            elif(re.fullmatch(r'(([0-2])?[0-9]): ?([0-5][0-9])',token)):
                Time2Word = time2word3(token)
                solutionTokens.append(Time2Word)
            
            #checks for month year format
            elif(re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})',token)):
                Date2Word = date2word(token)
                solutionTokens.append(Date2Word)

            elif(re.fullmatch(r'([0-3]?[0-9]) (January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})',token)):
                # print(token)
                Date2Word = date2word2(token)
                solutionTokens.append(Date2Word)

            elif(re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) ([1-2]?\d),? (\d{4})',token) ):
                Date2Word = date2word3(token)
                solutionTokens.append(Date2Word)

            elif(re.fullmatch(r'(\d{2}) (January|February|March|April|May|June|July|August|September|October|November|December)',token)):
                Date2Word = date2word4(token)
                solutionTokens.append(Date2Word)

            elif(re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9])',token) ):
                Date2Word = date2word5(token)
                solutionTokens.append(Date2Word)
                
            elif(re.fullmatch(r'(January|February|March|April|May|June|July|August|September|October|November|December) ([0-3]?[0-9])(st|nd|th|rd),? (\d{4})',token)):
                Date2Word = date2word6(token)
                solutionTokens.append(Date2Word)

            
            elif(re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})',token)):
                Date2Word = date2word7(token)
                solutionTokens.append(Date2Word)
            
            #ordinals 
            elif(re.fullmatch(r'(\d+)(th|st|nd|rd)',token)):
                a = re.fullmatch(r'(\d+)(th|st|nd|rd)',token).groups()
                Ordinal2Word = num2ordinal(a[0])
                solutionTokens.append(Ordinal2Word)

            #checks for percentages
            elif(re.fullmatch(r'(\d+(\.\d+)?) ?(\%|percent|Percent|pc)',token)):
                a = re.fullmatch(r'(\d+(\.\d+)?) ?(\%|percent|Percent|pc)',token).groups()
                Percent2Word = numberChecker(a[0],True) + ' percent'
                solutionTokens.append(Percent2Word)

            #checks for isbn/numbers of same kind
            elif(re.fullmatch(r'\d+-?(\d+-\d+)+?((-\d+)+)?',token)):
                Isbn2Word = isbn2word(token)
                solutionTokens.append(Isbn2Word)

            #3 9806773 4 6
            elif(re.fullmatch(r'\d+ ?(\d+ \d+)+?(( \d+)+)?',token)):
                Isbn2Word = isbn2word(token)
                solutionTokens.append(Isbn2Word)

            #fractions
            elif(re.fullmatch(r'-?\d+/\d+',token)):  
                Fraction2Word = fraction2word(token) 
                solutionTokens.append(Fraction2Word)

            
            elif(re.fullmatch(r'(\d+(,?\d*)*(\.\d+)?) ?(/km²|mi|km|/km2|m|km2|mm|KB|ha|PB|Gb/s|MB|cm|GB|Mb/s|km²|m²|Kb/s)',token)):
                Units2Word = units2word(token)
                solutionTokens.append(Units2Word)
            
            #mixed fractions
            elif(re.fullmatch(r'\d+ ((\d+)/(\d+))',token)):
                MixedFrac2Word = mixfrac2word(token)
                solutionTokens.append(MixedFrac2Word)

            elif(re.fullmatch(r'(\d+) \((\d+\)) (\d+)-(\d+)',token)):
                SplNum = splNum(token)
                solutionTokens.append(SplNum)

            elif(re.fullmatch(r'\d+( |-)?(\d+( |-)\d+)+?((( |-)\d+)+)?',token)):
                Isbn2Word = isbn2word(token)
                solutionTokens.append(Isbn2Word)
        
            elif(re.fullmatch(r'(\d+(\.\d+)?) ?(million|Million|billion|Billion|trillion|Trillion)',token)):
                a = re.fullmatch(r'(\d+(\.\d+)?) ?(million|Million|billion|Billion|trillion|Trillion)',token).groups()
                splNum1 = numberChecker(a[0], False) + ' ' + a[-1].lower()
                solutionTokens.append(splNum1)

            elif(re.fullmatch(r'^(Rs\.?|₹) ?([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]+)?$',token)):
                Rupee2Word = rupee2word(token)
                solutionTokens.append(Rupee2Word)
            
            elif(re.fullmatch(r'^(Rs\.?|₹) ?([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(\.[0-9]+)? (crore|crores|cr|lakhs|lakh|lacs|lac)',token)):
                Rupee2Word = rupee2word2(token)
                solutionTokens.append(Rupee2Word)

            elif(re.fullmatch(r'\d{4}s',token)):
                Number2Word = specialCase2(token)
                solutionTokens.append(Number2Word)
            #Self Token nothing special        
            else:
                solutionTokens.append('<self>')
        except (RuntimeError, TypeError, NameError , ArithmeticError , LookupError , FloatingPointError , IndexError ,KeyError , NameError , UnicodeError ,  ValueError ) as e:
            #Error Occurs, fallback to self
        # except (RuntimeError) as e:
            # print("ERROR TOKEN: " , token)
            # print(e)
            # print("Error occured, falling back to self")
            solutionTokens.append('<self>')

    assert len(solutionTokens) == len(input_tokens), "Input Output Length not same"

    return solutionTokens





def solution_dump(args):
    solution_data = []
    input_data = read_input(args.input_path)
    for input_sentence in input_data:
        solution_sid = input_sentence['sid']
        solution_tokens = solution(input_sentence['input_tokens'])
        solution_data.append({'sid':solution_sid,
                            'output_tokens':solution_tokens})

    with open(args.solution_path,'w') as solution_file:
        json.dump(solution_data, solution_file, indent=2, ensure_ascii=False)
        solution_file.close()
    

def starter():
    parser = argparse.ArgumentParser(description='COL 772 Assignment 1')
    parser.add_argument('--input_path', default='input.json', type=str, help='Path to input file')
    parser.add_argument('--solution_path', default='solution.json', type=str, help='Path to solution file')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = starter()
    solution_dump(args)