# Tematy dodatkowe do lekcji "Przygotowanie do kursu"
<br/>

## Spis treści

- [Języki interpretowane vs kompilowane](#języki-interpretowane-vs-kompilowane)
- [Środowiska wirtualne](#środowiska-wirtualne)
<br/>

## Języki interpretowane vs kompilowane
### [🠉](#spis-treści)
Jak być może słyszałeś/aś, komputer "rozumie" tylko informacje w postaci kodu binarnego.
<br/>Jeśli natomiast kiedykolwiek widziałeś/aś jak wygląda zdanie zapisane w nim, to zapewne wiesz też, że z kolei ludzie nie za bardzo umieją czytać kod binarny.
<br/>To oczywiście problem, ponieważ jako programiści chcemy "porozumieć się" z komputerem.

${\color{gray} \textit{Na wypadek gdybyście zwątpili, to nie, ten kurs nie będzie o ręcznym zapisywaniu całych stron zer i jedynek.}}$
<br/>${\color{gray} \textit{Na całe szczęście.}}$

Zawdzięczamy to już istniejącym programom, które potrafią kod programistyczny, zapisany w zrozumiałym dla (niektórych) ludzi języku, przetłumaczyć na kod binarny.

Istnieją dwa główne podejścia do tłumaczenia kodu programistycznego na binarny - **kompilacja** oraz **interpretacja**.
<br/>Każdy język programowania zbudowany jest w oparciu o jedną z tych metod.

${\color{forestgreen} \textbf{Języki kompilowane}}$ - jest to starsze podejście do problemu. Po napisaniu kodu, programista przekazuje go do tzw. *kompilatora*, czyli programu, który tłumaczy go na kod binarny.
<br/>Powstaje program zapisany już w kodzie binarnym, który można uruchomić w dowolnej chwili i na dowolnym komputerze.
<br/>(o ile korzysta on z tego samego systemu operacyjnego. Np. program skompilowany w systemie Windows zadziała na innym komputerze z Windowsem, ale na Linuxie już nie)

${\color{forestgreen} \textbf{Języki interpretowane}}$ - nowszy i popularny ze względu na wygodę sposób. Po napisaniu kodu nie trzeba nic więcej robić.
<br/>Za to kiedy chcemy uruchomić program, musimy to zrobić poprzez tzw. *interpreter*, program, który na bieżąco tłumaczy kod programistyczny na binarny i od razu wykonuje przetłumaczone polecenia.
<br/>Aby uruchomić program, musimy mieć na swoim komputerze zainstalowany interpreter.

> Zaznaczę, że to uproszczone wyjaśnienie. W rzeczywistości oba procesy są znacznie bardziej skomplikowane, ale jeśli zależy ci, żeby poznać szczegóły, będziesz musiał/a poszukać bardziej technicznych żródeł wiedzy

<br/>${\color{blueviolet} \large \textbf{Główne różnice:}}$
- Proces kompilacji jest często czasochłonny. W rezultacie, po napisaniu kodu programista musi cierpliwie zaczekać aż dobiegnie on końca, zanim będzie mógł go wypróbować. Natomiast wykonywanie poprzez interpreter jest mniej wydajne.
- Jakkolwiek programista może uruchomić swój program od razu po napisaniu kodu, to za to program ten działa powoli w porównaniu do programu, który został już skompilowany.

- Jak wspomniałem powyżej, program skompilowany można uruchomić tylko na komputerze z tym samym systemem operacyjnym. Program interpretowany można uruchomić na dowolnym komputerze, pod warunkiem, że jest na nim zainstalowany interpreter.

- W przypadku języków interpretowanych kod źródłowy (czyli to co programista napisał) jest łatwo dostępny dla każdego użytkownika. Jeśli nie chcesz, żeby ktoś oglądał twój kod, możesz preferować języki kompilowane, w przypadku których użytkownik programu otrzymuje go tylko w postaci binarnej (a więc nieczytelnej).
<br/>Co prawda, zarówno odwrócenie procesu kompilacji jak i utrudnienie odczytania kodu interpretowanego są przedsięwzięciami wykonalnymi i stosowanymi, ale wymagają większego nakładu pracy.

<br/>

## Środowiska wirtualne
### [🠉](#spis-treści)
Masz już zainstalowanego "czystego" Pythona, ale czasem do stworzenia projektów potrzebne są różne modyfikacje i dodatkowe narzędzia.
<br/>Programiści nie zawsze chcą takie zasoby instalować bezpośrednio w swoim "głównym" Pythonie, dlatego korzystają z tzw. **środowisk wirtualnych**. (*virtual environment*)
<br/>Są to odizolowane "paczki", zawierające kopię (lub nawet inną wersję) interpretera oraz wybrane dodatkowe narzędzia czy biblioteki.

Środowisko wirtualne można aktywować, dzięki czemu programy, które uruchamiamy, korzystają ze znajdujących się w nim narzędzi.
<br/>Kiedy potrzebujemy innego zestawu narzędzi - możemy dezaktywować środowisko i aktywować inne.

Własne środwisko wirtualne można stworzyć z pomocą samego Pythona, lub też specjalnych narzędzi, takich jak np. conda - ale nie będę wdawał się w szczegóły w tym kursie.

${\color{green} \textbf{Jeśli chodzi o Pycharm:}}$
<br/>Pycharm domyślnie proponuje tworzenie oddzielnego środowiska wirtualnego dla każdego nowego projektu, który tworzysz.
<br/>Jako, że na razie nie będziesz korzystać z żadnych dodatkowych narzędzi, w trakcie lekcji "Przygotowanie do kursu" skonfigurowaliśmy twój pierwszy projekt tak, żeby zamiast tego korzystał z istniejącej podstawowej instalacji interpretera.
