# Ade Romadhony
# Contoh sederhana NER berbasis aturan yang didefinisikan secara manual

# read the file
lines = []
with open('kalimat_POSTag.txt', 'r') as f:
    lines = f.readlines()

counter_line = 0
tokens = []
postags = []
tamp = []
org = ['Walt','Disney', 'Picture', 'Marvel', 'Comic', 'Studios', 'Motion', 'IMAX', 'DC', 'Pixar', 'Animation', 'Hai', 'NETPAC', 'Frederica', 'Film', 'Starvision', 'Plus', 'Miles', 'Screenplay', 'Legacy', 'Lembaga', 'Sensor']
for line in lines:
    line = line.rstrip('\n')
    if len(line)>1:
        line_part = line.split(" ")
        tokens.append(line_part[0])
        postags.append(line_part[1])
    else:
        print(tokens)
        print(postags)
        NE_labels = []
        counter_token = 0
        prev_NE_label = ""
        for token in tokens:
            if token[0].isupper() and postags[counter_token]=='NNP':
                if prev_NE_label=='B-LOC':
                    NE_labels.append('I-LOC')
                elif prev_NE_label=='I-LOC':
                    NE_labels.append('I-LOC')
                elif tokens[counter_token-1] == 'di' or tokens[counter_token-1]=='ke':
                    NE_labels.append('B-LOC')
                elif prev_NE_label=='B-PER':
                    NE_labels.append('I-PER')
                elif prev_NE_label=='I-PER':
                    NE_labels.append('I-PER')
                elif token in org:
                    if prev_NE_label=='B-ORG':
                        NE_labels.append('I-ORG')
                    elif prev_NE_label=='I-ORG':
                        NE_labels.append('I-ORG')
                    else:
                        NE_labels.append('B-ORG')
                else:
                    NE_labels.append('B-PER')
            else:
                NE_labels.append("O")
            prev_NE_label = NE_labels[counter_token]
            tamp.append([token,postags[counter_token],NE_labels[counter_token]])
            counter_token += 1
        print(tokens)
        print(NE_labels)
        tokens = []
        postags = []
print(tamp)

# SPLIT DATA TRAIN DAN DATA TEST
data_train_split = round((len(tamp)*0.8)) # split data train 80%, data test 20%

# SAVE DATA TRAIN AND DATA TEST TO TXT FILE
with open ("Kalimat_POS_NER_Jiddy_train.txt", "w") as a:
    for line in tamp[:data_train_split]:
        a.write(" ".join(line)+"\n")
        if line[1] == '.':
            a.write("\n")

with open ("Kalimat_POS_NER_Jiddy_test.txt", "w") as a:
    for line in tamp[data_train_split:]:
        a.write(" ".join(line)+"\n")
        if line[1] == '.':
           a.write("\n")

print("\nDone save to txt file!")