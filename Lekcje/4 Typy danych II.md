${\color{gray} \small \texttt{Napisał Jeremi Maciejewski}}$
<br/>*[Spis treści kursu](<../README.md#spis-treści>)*

# Typy danych II
Omówiliśmy już kilka [podstawowych typów danych](<3 Typy danych I.md>).
<br/>Aby umożliwić przechowywanie i pracę z bardziej złożonymi danymi, potrzebna będzie ci również znajomość typów kolekcji.

Służą one do przechowywania wielu wartości jednocześnie.

## Spis treści
- [Lista](#lista)
  - [Operacje na typach sekwencyjnych](#operacje-sekwencje)
  - [Operacje typowe dla listy](#operacje-lista)
- [Tuple](#tuple)
  - [Operacje typowe dla tuple](#operacje-tuple)
- [Zbiór](#zbiór)

<br/>

## Lista
### [🠉](#spis-treści)
W Pythonie nazywana `list`.
<br/>Sama nazwa tego typu danych wskazuje na jego naturę.
<br/>Jest to po prostu lista, czy sekwencja, wielu wartości (elementów).
<br/>Warto zaznaczyć, że lista może przechowywać wartości różnych typów (np. zarówno `string` jak i `int`) jednocześnie.

Zmienną tego typu można utworzyć za pomocą polecenia `list()`, lub umieszczając wartości oddzielone przecinkami wewnątrz **nawiasów kwadratowych**:

```py
example_list = [0, True, 13, "piętnaście", 19.5] # lista z elementami różnych typów
empty_list = [] # pusta lista
another_empty_list = list() # również pusta lista
```

<br/><a name="operacje-sekwencje"></a>

${\color{blue} \huge \textbf{Operacje na typach sekwencyjnych}}$

Typy *sekwencyjne* opisują uporządkowane sekwencje wartości.
<br/>Należą do nich między innymi **lista**, **tuple** oraz **string** (w końcu string jest sekwencją znaków).
<br/>Na danych takich typów można przeprowadzać *[slicing](<3 Typy danych I.md#slicing>)*.

```py
third = example_list[2]
print(third)
```

`13`

Można je również *konkatenować* (łączyć) za pomocą operatora `+`, oraz *powielać* za pomocą operatora `*`.

```py
list1 = [1, 2, 3]
list2 = [4.5, 5.5, 6.5]

print(list1 + list2)
```

`[1, 2, 3, 4.5, 5.5, 6.5]`

```py
print(list1 * 3)
```

`[1, 2, 3, 1, 2, 3, 1, 2, 3]`

<br/><details>
  <summary>
    Istnieje wiele metod oraz funkcji, których można używać z takimi typami:
  </summary>
  
  - `len(s)` - zwraca liczbę elementów w sekwencji, np. `len([0,1,2,3,4])` = `5`
  - `s.count(x)` - zwraca liczbę wystąpień podanego elementu w sekwencji, np. `[3,8,1,7,8].count(8)` = `2`
  - `s.index(x)`
    > Zwraca indeks, (pozycję) pod którym znajduje się podana wartość.
    > Jeśli taka wartość nie występuje w sekwencji, zwraca błąd.
    > Jeśli taka wartość występuje kilkukrotnie, zwraca indeks, pod którym występuje po raz pierwszy.
    > `[3,8,1,7,8].index(8)` = '1'
  
  - `min(s)` oraz `max(s)`
    > Zwracają, odpowiednio, najmniejszy oraz największy element w sekwencji.
    > Zwrócą błąd, jeśli w sekwencji znajdują się dane różnych typów (których nie można łatwo porównać).
    > `min([11, 3.4, 5, 2])` = `2`, ale: `max(["a", 12, 4])` = `TypeError`
    >
    > Możliwe jest też użycie ich na sekwencjach zawierających stringi, wtedy otrzymamy pierwszy lub ostatni element w przypadku ich uporządkowania alfabetycznego.
    > `min(["basia", "dorota", "Ania", "ania"])` = `"Ania"`
</details>

<br/><a name="operacje-lista"></a>

${\color{blue} \huge \textbf{Operacje typowe dla listy}}$

Istnieją także metody oraz funkcje wykorzystywane konkretnie z listami.
<br/>(niemniej, wszystkich powyższych operacji również można z nimi używać)

- `l.append(x)` - dodaje element `x` na koniec listy.
- `l.insert(i, x)` - wstawia element `x` pod indeks `i`.
- `l.remove(x)` - usuwa z listy element o wartości `x`. Jeśli występuje on kilka razy, usuwa tylko pierwszy.
- `l.pop()` - usuwa, oraz zwraca, ostatni element z listy.
- `l.pop(i)` - usuwa oraz zwraca element spod indeksu `i`.
- `l.clear()` - usuwa wszystkie elementy z listy.
- `l.copy()` - zwraca (płytką) kopię listy. (dla ekspertów, głęboką kopię można utworzyć za pomocą funkcji `deepcopy(l)` z modułu `copy`)
- `l.sort(reverse=False)`
  <details>
    <summary>
      Sortuje elementy listy.
    </summary>

    > Podobnie jak `min()` oraz `max()`, zwróci błąd, jeśli lista zawiera elementy, których nie da się porównywać.
    > Listy stringów są sortowane alfabetycznie.
    > Domyślnie sortuje od najmniejszej do największej wartości, jednak można ustawić parametr `reverse` na `True` aby sortować malejąco.
    >
    > ```py
    > a = [5, 1, 8, 12]
    > a.sort()
    >
    > b = [5, 1, 8, 12]
    > b.sort(reverse=True)
    > print(a)
    > print(b)
    > ```
    > `[1, 5, 8, 12]`
    > `[12, 8, 5, 1]`
  </details>

- `sorted(l, reverse=False)` - alternatywa dla powyższej metody, zamiast zmieniać listę, zwraca posortowaną kopię.

<br/>

## Tuple
### [🠉](#spis-treści)
Tak właściwie, to ten typ danych w języku Polskim nazywa się ***krotką***, ale osobiście nie lubię tej nazwy...
<br/>W każdym razie, Python używa nazwy `tuple`.

Typ tuple jest właściwie zupełnie jak lista - tylko *niemutowalna*, a za to *haszowalna*.
<br/>*Niemutowalność* (jak w przypadku typu string!) oznacza, że danych tego typu nie da się modyfikować.
<br/>Natomiast *haszowalność* w praktyce oznacza tyle, że tuple może być kluczem w *słowniku*... ale o słownikach powiem później.

Dane tego typu tworzy się poleceniem `tuple()`, lub poprzez zapisanie wartości oddzielonych przecinkiem.
<br/>Można, właściwie wypada, umieszczać je wewnątrz nawiasów okrągłych, ale nie trzeba.

```py
example_tuple = (0, True, 13, "piętnaście", 19.5) # lista z elementami różnych typów
another_tuple = 0, True, 13, "piętnaście", 19.5 # nawiasy w gruncie rzeczy nie są potrzebne. Choć ten zapis jest mniej zrozumiały.

empty_tuple = () # pusta krotka
another_empty_tuple = tuple() # również pusta krotka
```

<br/><a name="operacje-tuple"></a>

${\color{blue} \huge \textbf{Operacje typowe dla tuple}}$

Tuple jest sekwencyjnym typem danych, a zatem można na nim stosować [charakterystyczne dla nich operacje](#operacje-sekwencje).
<br/>Poza tym, można na nim także stosować funkcję `sorted(t, reverse=False)`, która zwraca posortowaną wersję krotki.

<br/>

## Zbiór
### [🠉](#spis-treści)

Zbiór, w Pythonie (i po angielsku) nazywany `set`, różni się dość znacząco od `list` oraz `tuple`.
<br/>Zapewne znasz pojęcie zbiorów w matematyce - ten typ danych służy jako ich odwzorowanie.

Jest on ***nieuporządkowany***, a więc znajdujące się w nim elementy nie są ustawione w żadnej konkretnej kolejności.
<br/>Jest także ***mutowalny*** oraz ***niehaszowalny***.
<br/>Każdy element zbioru musi być **unikalny**, czyli żadna wartość nie może wystąpić w nim dwukrotnie (przy próbie dodania wielu identycznych wartości, zostanie dodana jedna, a kopie zostaną zignorowane).

Wartość tego typu tworzy się za pomocą polecenia `set`, lub umieszczając wartości oddzielone przecinkami wewnątrz nawiasów **klamrowych**.
<br/>Koniecznie trzeba tu zaznaczyć, że **nie można** stworzyć pustego zbioru za pomocą pustych nawiasów klamrowych - w ten sposób utworzymy słownik (o którym za chwilę).

```py
example_set = {0, True, 13, "piętnaście", 19.5} # zbiór z elementami różnych typów

empty_set = set() # pusty zbiór
not_actually_a_set = {} # To NIE jest pusty zbiór, tylko słownik.
```

Jak wspominałem, elementy zbioru nie powtarzają się.

```py
example_set = {1, 2, 3, 3, 2, 1} # próba stworzenia zbioru z powtarzającymi się elementami.
print(example_set)
```

```py
{1, 2, 3}
# Kopie elementów zostały automatycznie usunięte
```
