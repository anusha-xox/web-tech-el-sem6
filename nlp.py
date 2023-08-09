import spacy
import en_core_web_sm
# import en_core_web_md



def solve(text, evaluation_text):
    # nlp = spacy.load("en_core_web_lg")
    # nlp1 = spacy.load("en_core_web_md")
    nlp = en_core_web_sm.load()
    # nlp1 = en_core_web_md.load()
    input_answers = text
    correct_answers = evaluation_text

    string1 = nlp(input_answers)
    string2 = nlp(correct_answers)

    s1_verbs = [token.lemma_ for token in string1 if token.pos_ == "VERB"]
    s2_verbs = [token.lemma_ for token in string2 if token.pos_ == "VERB"]

    s1_nouns = [token.lemma_ for token in string1 if token.pos_ == "NOUN"]
    s2_nouns = [token.lemma_ for token in string2 if token.pos_ == "NOUN"]

    s1_adj = [token.lemma_ for token in string1 if token.pos_ == "ADJ"]
    s2_adj = [token.lemma_ for token in string2 if token.pos_ == "ADJ"]

    s1_pronoun = [token.lemma_ for token in string1 if token.pos_ == "PROPN"]
    s2_pronoun = [token.lemma_ for token in string1 if token.pos_ == "PROPN"]

    s1_adp = [token.lemma_ for token in string1 if token.pos_ == "ADP"]
    s2_adp = [token.lemma_ for token in string1 if token.pos_ == "ADP"]

    s1_sym = [token.lemma_ for token in string1 if token.pos_ == "SYM"]
    s2_sym = [token.lemma_ for token in string1 if token.pos_ == "SYM"]

    s1_num = [token.lemma_ for token in string1 if token.pos_ == "NUM"]
    s2_num = [token.lemma_ for token in string1 if token.pos_ == "NUM"]

    s1 = nlp(input_answers)
    s2 = nlp(correct_answers)

    similarity = s1.similarity(s2)

    verb_score = 0
    noun_score = 0
    adj_score = 0
    pro_score = 0
    adp_score = 0
    sym_score = 0
    num_score = 0

    for i in s1_verbs:
        if i in s2_verbs:
            verb_score += 1
    for i in s1_nouns:
        if i in s2_nouns:
            noun_score += 1
    for i in s1_adj:
        if i in s2_adj:
            adj_score += 1
    for i in s1_pronoun:
        if i in s2_pronoun:
            pro_score += 1
    for i in s1_adp:
        if i in s2_adp:
            adp_score += 1
    for i in s1_sym:
        if i in s2_sym:
            sym_score += 1
    for i in s1_num:
        if i in s2_num:
            num_score += 1

    print("verb_score = " + str(verb_score), end=" ")
    print("noun_score = " + str(noun_score), end=" ")
    print("adj_score = " + str(adj_score), end=" ")
    print("pro_score = " + str(pro_score), end=" ")
    print("adp_score = " + str(adp_score), end=" ")
    print("sym_score = " + str(sym_score), end=" ")
    print("num_score = " + str(num_score), end=" ")

    pre = (verb_score + noun_score + adj_score + pro_score + adp_score + sym_score + num_score) / (
                len(s1_verbs) + len(s1_nouns) + len(s1_adj) + len(s1_pronoun) + len(s1_adp) + len(s1_sym) + len(s1_num))
    print("similarity = " + str(similarity), end=" ")
    print(pre)
    if similarity > 0.75 and pre > 0.6:
        quiz_results = True
    else:
        quiz_results = False

    return quiz_results,[["Similarity score",str(int(similarity*100))+"%"],["Verbs matched",verb_score],["Nouns matched",noun_score],["Adjectives matched",adj_score],["Proverbs matched",pro_score],["Adpositions matched",adp_score],["Symbols matched",sym_score],["Numbers matched",num_score]]
