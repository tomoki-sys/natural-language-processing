from janome.tokenizer import Tokenizer
from nltk.corpus import wordnet

t=Tokenizer()#インスタントの作成
s=input("文章を入力して下さい\n")
tokens=t.tokenize(s)#メソッドに文字列を渡す
list=[]

for token in tokens:
    #品詞の取り出し
    partofspeech=token.part_of_speech.split(',')[0]
    
    if partofspeech == "名詞" or partofspeech == "動詞" or partofspeech == "形容詞":

        list.append(str(token.surface))

for i in list:
    synsets = wordnet.synsets(i,lang='jpn')
    if(len(synsets)!=0):
        print('\033[31m'+i+'\033[0m')
        for k in range(len(synsets)):
            this_synset=synsets[k]
            synonyms=this_synset.lemma_names("jpn")
            print(synonyms)

