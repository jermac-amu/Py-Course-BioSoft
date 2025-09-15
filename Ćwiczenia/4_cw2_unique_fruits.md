[Powrót do lekcji 4](</Lekcje/4 Typy danych II.md#cwiczenia>)

Wyobraź sobie, że przygotowujesz owocową sałatkę dla dwojga ważnych gości.
<br/>Przygotowałem dla ciebie listę owoców, które posiadasz, oraz dwa zbiory owoców, których poszczególni goście nie lubią.

Użyj tych informacji, aby **znaleźć zbiór owoców**, które są **lubiane** przez oboje gości, i których możesz użyć w sałatce.

Ktoś *(któż to mógł być...)* przez "pomyłkę", niektóre posiadane owoce dopisał do listy kilkukrotnie - na szczęście można łatwo rozwiązać ten problem, *zmieniając ją w zbiór...*

<details>
    <summary>
        Wskazówka: ${\color{gray} \small \textit{(naciśnij aby rozwinąć)}}$
    </summary>

> Możesz zmienić listę w zbiór - i tym samym usunąć zduplikowane elementy - za pomocą polecenia `set()`.
>
> Myślę, żę przyda ci się również coś, żeby obliczyć *[różnicę zbiorów](</Lekcje/4 Typy danych II.md#operacje-set>)*...
</details>

<br/>

```py
available_fruits = ["Lychee", "Apple", "Mango", "Pear", "Pineapple", "Peach",
                    "Nectarine", "Orange","Lychee", "Papaya", "Pineapple",
                    "Peach", "Pear", "Pineapple", "Apple", "Mandarine", "Plum",
                    "Melon", "Passionfruit", "Nectarine", "Plum"]

wrong_fruits1 = {"Peach", "Nectarine", "Orange", "Pineapple", "Melon"}
wrong_fruits2 = {"Mandarine", "Plum", "Lychee", "Orange", "Peach", "Papaya"}

available_set = # ???

liked_fruits1 = # ???
liked_fruits_both = # ???
```

[Rozwiązanie](<Pliki/4_rozw2.py>)
