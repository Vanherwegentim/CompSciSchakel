# Examenvragen Gegevensstructuren en algoritmen



## Les 1 Analyse

### Vraag 1

**Gegeven één of andere tabel met probleemgroottes N en uitvoeringstijden (zie bvb. doubling experiment). Wat kan je besluiten ivm het gedrag van dit specifieke algoritme?**

Het volgende kan 1 van die voorbeelden tabellen zijn:

![image-20220410193741294](img/image-20220410193741294.png)

Op de moment heb ik echt geen idee, later nog op terugkomen



### Vraag 2

**Leg het verschil uit tussen grote-O en tilde-notatie om het stijgingsgedrag van functies te karakteriseren.**

De tilde-notatie gebruiken we als we een simple approximatie willen doen van een complexe functie. De termen met een lagere orde laten we dus vallen.

Vb: $x^3 + x^2 + x$ wordt dan $x^3$

De Big Oh/grote-O notatie geeft ons de worst case scenario m.a.w de upper bound.



### Vraag 3

**(*Augustus 2021*) Een algoritme heeft een tijdscomplexiteit ~c.n^3^. Stel dat we een computer aankopen die 10-maal zo snel is als onze huidige computer. Een hoeveel groter probleem (probleemgrootte n) kunnen we nu oplossen**
**met hetzelfde algoritme binnen dezelfde rekentijd?**

Dit staat in het boek *Algorithms 4 by Robert Sedgewick op p193-194 een beetje uitgelegd als mijn uitleg niet voldoende zou zijn.

Als een computer x keer sneller is dan de oude dan kan je de runtime verbeteren met een factor x.

Dus als je computer er ~c.n^3^ over doet en dan 10x sneller wordt. Dan gaat de nieuwe tijdscomplexiteit er zo uitzien

=> ~c.(10n)^3^

Als we dan de eerste tijdscomplexiteit delen door het tweede dan krijgen we:

$(c*n^3)/(c*(10n)^3) = 1000$ 

We kunnen dus een probleem oplossen dat 1000x groter is.



### Vraag 4

**(*Augustus 2021*) Veronderstel dat de uitvoeringstijd van een algoritme met een probleemgrootte n gelijk aan 1000, 2000, 3000, 4000 respectievelijk 5, 21, 44 en 82 seconden is. Wat is de geschatte uitvoeringstijd voor een probleemgrootte n = 5000?**

Ik heb hier een berekening gedaan op basis van de slides [(les01)-analysis.pdf](https://p.cygnus.cc.kuleuven.be/bbcswebdav/pid-32517447-dt-content-rid-320242234_2/xid-320242234_2), slide 15. Geen idee of het juist is maar het lijkt in lijn te liggen met de vorige waarden.

**Eerste punt invullen:**

$log_25 = b.log_21000 + c$

**Tweede punt invullen:**

$log_21 = b.log_22000 + c$

**Gelijkstellen en uitrekenen:**

=> $log_25 - b.log_21000 + c = log_25 - b.log_21000 + c$

=> $log_25 - log_221 = b.log_21000 - b.log_22000$

=> $log_2(5/21) = b.log(1/2)$

=> $b=(log_2(5/21))/(log_2(1/2))$

=> $b = 2,070389327$

**b gebruiken om c uit te rekenen**

=> $log_25 = 2,070389327.log_21000+c$

=> $c = log_25 - 2,070389327.log_2(1000)$

=> $c = -18,3112317$



=> $T(N) = 2^{-18,3112317}.N^{2.070389327}$ 

**Nieuw punt invullen (5000,y)**

=> $T(N) =2^{-18,3112317}.5000^{2.070389327}$

=> $T(N) = 140$



Als we de uitgekomen functie plotten op de calculator komen de punten ongeveer overeen.

![image-20220411133029909](img/image-20220411133029909.png)



Niet de meeste accurate maar dat komt wss door de kommagetallen.



### Vraag 5

**(*Augustus 2021*) Stel dat de tijdscomplexiteit van Algoritme X heeft een tijdscomplexiteit ~c.n^2 (waarbij n een maat is voor de probleemgrootte). Voor algoritme Y, dat hetzelfde probleem oplost als algoritme X, is de**
**tijdscomplexiteit ~d.n^3. Geef twee valabele redenen waarom een programmeur toch zou kunnen kiezen voor algoritme Y i.p.v. algoritme X om het bewuste probleem op te lossen.**

Op de moment niet echt een idee? Misschien voor hele kleine N?



## Les 2 Selection Sort, Insertion Sort, Merge Sort

### Vraag 1

**Bewijs dat log~2~(n!) ~ n.log~2~(n)**

Dit is Stirling's benadering.

Nu vraagt ge u waarschijnlijk af, wat is dat nou die Stirling's benadering. Wel dus als je een faculteit wilt berekenen is dat best makkelijk voor kleine getallen maar eenmaal naar de grote getallen wordt dat best lastig. Dus was heeft Stirling gedaan, een formule gemaakt die het een stuk simpler maakt:

​		***Stirling’s formula:*** $n! ≈ √ (2πn).(n/e)^{±n}$

![image-20220411152540043](img/image-20220411152540043.png)

**Nu het bewijs:**

=> $log_2(n!)$
$n! = e^{ln(n!)}\space invullen$

=> $log_2(e)ln(n!)$

 => $log_2(e)[ln(n) + ln(n - 1) ... ln(2) ln(1)]$

**Som van natuurlijke logaritmes benaderen we door integraal:**

$ ln(n) + ln(n - 1) ... ln(2) ln(1) ≈ \int_1^nln(x)dx$ 

=> $\int_1^xln(x)dx$

=> $[xln(x)-x]_1^n$

=>  $nln(n)-n+1$

**En dus:**

=> $log_2(e)ln(n!)$

$≈ log2(𝑒)[𝑛ln(𝑛) −𝑛 + 1]$

$log_bx=log_ba⋅log_ax$ gebruiken

=> $𝑛log_2(𝑛) − 𝑛 log_2(𝑒) + log_2(𝑒)$

=> $nlog_2(n)- 1.443n+1443$

**==>**  $log_2(n!)~nlog_2(n)$

Bewezen!



### Vraag 2

**Toon aan dat een sorteeralgoritme, dat gebruik maakt van onderlinge vergelijkingen van elementen, steeds minstens log~2~(n!) vergelijkingen zal nodig hebben om algemeen een rij van n elementen te sorteren.**

De slides zeggen:

![image-20220411162155383](img/image-20220411162155383.png)

log~2~(n!) is eigenlijk n.log~2~(n), hebben we gezien in de vorige vraag.

A sorting algorithm using at most *h* comparisons on all inputs corresponds to a tree of height at most *h*. Such a tree has at most 2^h^ leaves. On the other hand, each permutation of 1,…,N must land at a different leaf, and so there must be at least N! leaves. Putting these together, we deduce that 2^h^≥N! and so h≥log~2~N!=Ω(NlogN) (using Stirling's approximation). So every sorting algorithm must use at least log~2~N!=Ω(NlogN) comparisons in the worst case (on some inputs it can use less).

![image-20220411181309011](img/image-20220411181309011.png)

![image-20220411181325976](img/image-20220411181325976.png)

**Het boek legt dit ook zeer uitgebreid en goed uit op p280.**

slides vanaf slide 28



### Vraag 3

**(*Examenvraag Juni 2020)***

1. **Hoeveel vergelijkingen tussen elementen heeft MergeSort maximaal nodig om een array van 6 elementen te sorteren? Hoeveel voor een array van 9 elementen? (geef enkel de aantallen)**

2. De slides zeggen dat mergesort nlog~2~n vergelijkingen doet. 

3. Dus voor een array van 6 elementen. 

4. => $6log_26=15.5097$
   => 16 vergelijkingen

5. Dus voor een array van 9 elementen

6. => $9log_29 =28.5293250129807$

7. => 29 vergelijkingen

8. 

9. **Stel dat ik bovenstaande wil berekenen voor om het even welk aantal elementen, m.a.w. ik zou willen weten hoeveel vergelijkingen tussen elementen MergeSort maximaal nodig heeft om een array van n elementen te sorteren. Ontwikkel een efficiënt algoritme om dit aantal te berekenen. Je hoeft enkel het aantal te berekenen, niet MergeSort zelf uit te voeren. Bespreek de algemene aanpak van je algoritme, geef pseudocode, en bespreek tevens de tijdscomplexiteit.**
   ***Opmerking: deze vraag veronderstelt ook kennis die in latere lessen aan bod zal komen ...***

### 		TODO



### Vraag 4

**(*Examenvraag Juni 2021*) Stel dat we een array van lengte 2n hebben, die bestaat uit de eerste n even positieve gehele getallen in oplopende volgorde, gevolgd door de eerste n oneven getallen, maar in aflopende volgorde. Bijvoorbeeld voor n = 5 is de array gelijk aan [0, 2, 4, 6, 8, 9, 7, 5, 3, 1]. Hoeveel vergelijkingen i.f.v. n hebben de respectievelijke sorteeralgoritmes [Selection, Insertion, Merge, Quick] nodig om dergelijke array te sorteren? Gebruik ~notatie, en geef ook een verklaring. Let op: n is de lengte van de halve array!**

Ik denk dat gewoon hun formules mogen gebruiken

**MergeSort:** weer nlog~2~n dus

=> $10log_210$

=> **33.219280948874**

**SelectionSort:** n.(n-1)/2 normaal maar we moeten de tilde notatie gebruiken dus ->  ~ n^2^/2

=> 10^2^/2

=> 50

**InsertionSort: **Half of elements to the left of the pivot are larger: ~n^2^/4

=> 10^2^/4

=> 25

**QuickSort:**TODO

![image-20220411213556547](img/image-20220411213556547.png)



## Les 3 & 4: Quicksort