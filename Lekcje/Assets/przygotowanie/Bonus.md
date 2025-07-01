# Tematy dodatkowe do lekcji "Przygotowanie do kursu"
<br/>

## Języki interpretowane vs kompilowane
Jak być może słyszałeś/aś, komputer "rozumie" tylko informacje w postaci kodu binarnego.
<br/>Jeśli natomiast kiedykolwiek widziałeś/aś jak wygląda zdanie zapisane w nim, to zapewne wiesz też, że z kolei ludzie nie za bardzo umieją czytać kod binarny.
<br/>To oczywiście problem, ponieważ jako programiści chcemy "porozumieć się" z komputerem.

<br/>*Na wypadek gdybyście zwątpili, to nie, ten kurs nie będzie o ręcznym zapisywaniu całych stron zer i jedynek.
<br/>Na całe szczęście.*

Zawdzięczamy to już istniejącym programom, które potrafią kod programistyczny, zapisany w zrozumiałym dla (niektórych) ludzi języku, przetłumaczyć na kod binarny.

Istnieją dwa główne podejścia do tłumaczenia kodu programistycznego na binarny - **kompilacja** oraz **interpretacja**.
<br/>Każdy język programowania zbudowany jest w oparciu o jedną z tych metod.

**Języki kompilowane** - jest to starsze podejście do problemu. Po napisaniu kodu, programista przekazuje go do tzw. *kompilatora*, czyli programu, który tłumaczy go na kod binarny.
<br/>Powstaje program zapisany już w kodzie binarnym, który można uruchomić w dowolnej chwili i na dowolnym komputerze.
<br/>(o ile korzysta on z tego samego systemu operacyjnego. Np. program skompilowany w systemie Windows zadziała na innym komputerze z Windowsem, ale na Linuxie już nie)

**Języki interpretowane** - nowszy i popularny ze względu na wygodę sposób. Po napisaniu kodu nie trzeba nic więcej robić.
<br/>Za to kiedy chcemy uruchomić program, musimy to zrobić poprzez tzw. *interpreter*, program, który na bieżąco tłumaczy kod programistyczny na binarny i od razu wykonuje przetłumaczone polecenia.
<br/>Aby uruchomić program, musimy mieć na swoim komputerze zainstalowany interpreter.

> Zaznaczę, że to uproszczone wyjaśnienie. W rzeczywistości oba procesy są znacznie bardziej skomplikowane, ale jeśli zależy ci, żeby poznać szczegóły, będziesz musiał/a poszukać bardziej technicznych żródeł wiedzy

**Główne różnice:**
- Proces kompilacji jest często czasochłonny. W rezultacie, po napisaniu kodu programista musi cierpliwie zaczekać aż dobiegnie on końca, zanim będzie mógł go wypróbować. Natomiast wykonywanie poprzez interpreter jest mniej wydajne.
- <br/>Jakkolwiek programista może uruchomić swój program od razu po napisaniu kodu, to za to program ten działa powoli w porównaniu do programu, który został już skompilowany.

- Jak wspomniałem powyżej, program skompilowany można uruchomić tylko na komputerze z tym samym systemem operacyjnym. Program interpretowany można uruchomić na dowolnym komputerze, pod warunkiem, że jest na nim zainstalowany interpreter.

- W przypadku języków interpretowanych kod źródłowy (czyli to co programista napisał) jest łatwo dostępny dla każdego użytkownika. Jeśli nie chcesz, żeby ktoś oglądał twój kod, możesz preferować języki kompilowane, w przypadku których użytkownik programu otrzymuje go tylko w postaci binarnej (a więc nieczytelnej).
<br/>Co prawda, zarówno odwrócenie procesu kompilacji jak i utrudnienie odczytania kodu interpretowanego są przedsięwzięciami wykonalnymi i stosowanymi, ale wymagają większego nakładu pracy.

<br/>

### Środowiska wirtualne
Masz już zainstalowanego "czystego" Pythona, ale czasem do stworzenia projektów potrzebne są różne modyfikacje i dodatkowe narzędzia.
<br>Programiści nie zawsze chcą takie zasoby instalować bezpośrednio 
