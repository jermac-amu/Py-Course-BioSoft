motif = "TTAGGG"

nuc_counts = {'A' : 57, 'T' : 114, 'C' : 0, 'G' : 171}

num_T_in_motif = motif.count('T')
num_T_in_seq = nuc_counts['T']

number_of_repeats = num_T_in_seq // num_T_in_motif
# Dzielenie całkowite - przy mnożeniu stringów musimy użyć liczby całkowitej.
# Można też zrobić to tak:
number_of_repeats = int(num_T_in_seq / num_T_in_motif)

sequence = motif * number_of_repeats

print(number_of_repeats) # 57
print(f"A: {sequence.count('A')} T: {sequence.count('T')} C: {sequence.count('C')} G: {sequence.count('G')}")
print()
print(sequence)
