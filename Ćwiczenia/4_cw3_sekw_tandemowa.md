[Powrót do lekcji 4](</Lekcje/4 Typy danych II.md#cwiczenia>)

W kodzie poniżej znajduje się słownik zawierający liczby wystąpień poszczególnych nukleotydów w pewnej sekwencji DNA.
<br/>Wiesz, że jest to sekwencja tandemowa, której podstawowy motyw to "TTAGGG" - występuje ona w [telomerach](<https://pl.wikipedia.org/wiki/Telomer_(genetyka)>) kręgowców.
<br/>Nie posiadasz jednak samego zapisu tej sekwencji.

Sekwencje tandemowe są to sekwencje składające się z wielokrotnych powtórzeń krótszej sekwencji.
<br/>Sekwencja tandemowa o motywie "TTAGGG" składa się więc z wielokrotnych powtórzeń fragmentu "TTAGGG".

Na podstawie informacji o liczbie poszczególnych nukleotydów w pełnej sekwencji, oraz znajomości jej motywu, policz, ile razy motyw powtarza się w sekwencji.
<br/>Następnie odtwórz tę sekwencję.

Przyjmij, że nie występują w niej niepełne ani zmutowane fragmenty motywu.

<details>
    <summary>
        Wskazówka:
    </summary>
    Dane ze słownika możesz wyciągnąć stosując formułę `value = dict[key]`, na przykład `num_A = nuc_counts['A']`.

    Mogą ci się przydać [operatory matematyczne](</Lekcje/Typy danych I.md#matematyka>)
    <br/>W tym, [powielanie stringów](</Lekcje/Typy danych I.md#string>).

    Uwaga! Zauważ, że istnieją dwa różne operatory odpowiadające za dzielenie... ;)
</details>

```py
motif = "TTAGGG"

nuc_counts = {'A' : 57, 'T' : 114, 'C' : 0, 'G' : 171}

# ???

number_of_repeats = # ???

sequence = # ???
```

[Rozwiązanie](<Pliki/4_rozw3.py>)
