import sys

ID,FORM,LEMMA,UPOS,XPOS,FEAT,HEAD,DEPREL,DEPS,MISC=range(10)

def read_conllu(fname):
    f=open(fname,"rt",encoding="utf-8")
    sentence=[]
    comments=[]
    for line in f:
        line=line.strip()
        if not line:
            if sentence:
                yield sentence
            sentence=[]
            comments=[]
        elif line.startswith("#"):
            comments.append(line)
        else:
            sentence.append(line.split("\t"))
            
def remove_nulls(s):
    # remove null nodes because those are not evaluated here
    # TODO multiword?
    new=[]
    for token in s:
        if "." not in token[ID]:
            new.append(token)
        else:
            print("Skipping token:",token)
    return new
            
            
def eval(gold_file,predicted_file):

    keys=u"UPOS,XPOS,FEAT,UPOS+FEAT,UAS,LAS,TOKEN_COUNT,SANITY_CHECK".split(u",")

    scores={}
    for key in keys:
        scores[key]=0.0
        
    gold_sentences=[s for s in read_conllu(gold_file)]
    predicted_sentences=[s for s in read_conllu(predicted_file)]
    if len(gold_sentences)!=len(predicted_sentences):
        print("Different number of sentences, evaluation is not supported.")
        return 1

    for gold_s,predicted_s in zip(gold_sentences,predicted_sentences):
    
        gold_s=remove_nulls(gold_s)
        predicted_s=remove_nulls(predicted_s)
        if len(gold_s)!=len(predicted_s):
            print("Different number of tokens in a sentence, evaluation is not supported yet.")
            print(gold_s,predicted_S)
            return 1

        for gold_t,predicted_t in zip(gold_s,predicted_s):
        
            # POS, CPOS, FEAT, ULAS
            for (i,name) in [(UPOS,u"UPOS"),(XPOS,u"XPOS"),(FEAT,u"FEAT"),(HEAD,u"UAS"),(FORM,"SANITY_CHECK")]:
                if gold_t[i]==predicted_t[i]:
                    scores[name]+=1.0
            # POS+FEAT
            if gold_t[UPOS]==predicted_t[UPOS] and gold_t[FEAT]==predicted_t[FEAT]:
                scores[u"UPOS+FEAT"]+=1.0
            # LAS
            if gold_t[HEAD]==predicted_t[HEAD] and gold_t[DEPREL]==predicted_t[DEPREL]:
                scores[u"LAS"]+=1.0
                
            # TOKEN_COUNT
            scores[u"TOKEN_COUNT"]+=1.0

    for key in keys:
        if key==u"TOKEN_COUNT":
            print(key, int(scores[key]))
        elif key==u"SANITY_CHECK":
            print(key, scores[key]==scores[u"TOKEN_COUNT"])
        else:
            print(key, "%.2f" %(scores[key]/scores[u"TOKEN_COUNT"]*100))
            
    return 0
            
if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--gold', dest='gold', action='store',help='Gold standard.')     
    parser.add_argument('--predicted', dest='predicted', action='store',help='System predictions.')
    args = parser.parse_args()
    
    i=eval(args.gold,args.predicted)
 
 
            
