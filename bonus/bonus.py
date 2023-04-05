import pandas as pd

tr = {
    1: "Active_Promoter"
    , 2: "Weak_Promoter"
    , 3: "Inactive/poised_promoter"
    , 4: "Strong_enhancer"
    , 5: "Strong_enhancer"
    , 6: "Weak/poised_enhancer"
    , 7: "Weak/poised_enhancer"
    , 8: "Insulator"
    , 9: "Transcriptional_transition"
    , 10: "Transcriptional_elongation"
    , 11: "Weak_transcribed"
    , 12: "Polycombed_repressed"
    , 13: "Heterochromatin;_low_signal"
}

df = pd.read_csv("Hsmm_13_dense.bed", sep='\t', skiprows=1, header=None)
df[3] = df[3].apply(lambda x: str(x) + "_" + tr[x])
print(len(df[3].unique()))
print(df.head())

df.to_csv("Hsmm_13_dense_bonus.bed", sep='\t', header=None, index=None)

with open("Hsmm_13_dense.bed", 'r') as f1:
    with open("Hsmm_13_dense_bonus.bed", 'r') as f2:
        text = f2.read()
    with open("Hsmm_13_dense_bonus.bed", 'w') as f2:
        f2.write(f1.readline() + text)