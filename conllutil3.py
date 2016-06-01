from __future__ import print_function

ID,FORM,LEMMA,CPOS,POS,FEAT,HEAD,DEPREL,DEPS,MISC=range(10)

allowed_pos="ADJ,ADV,INTJ,NOUN,PROPN,VERB,ADP,AUX,CONJ,DET,NUM,PRON,SONJ,PUNCT,SYM,X".split(",")


def read_conllu(f):
    sent=[]
    comment=[]
    for line in f:
        line=line.strip()
        if not line: # new sentence
            if sent:
                yield comment,sent
            comment=[]
            sent=[]
        elif line.startswith("#"):
            comment.append(line)
        else: #normal line
            sent.append(line.split("\t"))
    else:
        if sent:
            yield comment, sent


def sort_features(features):
    if features=="_":
        return features
    feats=[]
    for feat in features.split("|"):
        feat=feat.replace("_","=",1)
        feats.append(feat)
    return "|".join(sorted(feats))

def conll09_to_conllu(sent):
    """ Convert conll09 sentence into conllu.
        Sort features alphabetically and replace '_' with '='.
    """
    conllu=[]
    for line in sent:
        new=[]
        for _ in range(10):
            new.append("_")
        new[ID]=line[0]
        new[FORM]=line[1]
        new[LEMMA]=line[2]
        new[CPOS],new[POS]=line[4],line[4]
        new[FEAT]=sort_features(line[6])
        new[HEAD]=line[8]
        new[DEPREL]=line[10]
        conllu.append(new)
    return conllu

def conll09_to_conllu_no_features(sent):
    """ Convert conll09 sentence into conllu.
    """
    conllu=[]
    for line in sent:
        new=[]
        for _ in range(10):
            new.append("_")
        new[ID]=line[0]
        new[FORM]=line[1]
        new[LEMMA]=line[2]
        new[CPOS],new[POS]=line[4],line[4]
        new[FEAT]=line[6]
        new[HEAD]=line[8]
        new[DEPREL]=line[10]
        conllu.append(new)
    return conllu


def print_sent(out,comm,sent):
    for line in comm:
        print(line,file=out) #>> out, line.encode(u"utf-8")
    for line in sent:
        # sort DEPS field
        sorting=[]
        if line[DEPS]!="_":
            sorting=[]
            deps=line[DEPS].split("|")
            for d in deps:
                h,t=d.split(":",1)
                sorting.append((int(h),t))
            line[DEPS]="|".join(str(h)+":"+t for h,t in sorted(sorting))
        print("\t".join(line),file=out) # .encode(u"utf-8")
    print("",file=out)

def plain_print(out,comm,sent):
    for line in comm:
        print(line, file=out) #.encode("utf-8")
    for line in sent:
        print("\t".join(line), file=out) #.encode("utf-8")
    print("",file=out)


class Dep(object):
    """ Simple class to represent dependency. """

    def __init__(self,g,d,t,flag="l1"):
        self.gov=g
        self.dep=d
        self.type=t
        self.flag=flag

    def __eq__(self,other):
        return (self.gov==other.gov and self.dep==other.dep and self.type==other.type and self.flag==other.flag)

##    def __cmp__(self,other):
##        if self.dep<other.dep: return -1  self smaller than other
##        elif self.dep>other.dep: return 1
##        else:  same gov
##            if self.gov<other.gov: return -1
##            elif self.gov>other.gov: return 1
##            else:  also same dep
##                if self.type<other.type: return -1
##                elif self.type>other.type: return 1
##                else: return -1  the same, raise error?

    def __hash__(self):
        return hash("-".join(str(n) for n in (self.gov,self.dep,self.type,self.flag)))

    def __repr__(self):
        return ":".join(str(n) for n in (self.gov,self.dep,self.type,self.flag))

