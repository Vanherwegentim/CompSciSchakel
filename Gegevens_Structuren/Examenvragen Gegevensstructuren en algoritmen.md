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

### Vraag 1 

**(*Examenvraag Juni 2020*) Toon aan dat QuickSort een gemiddelde tijdscomplexiteit heeft ~1.39.n.log2(n). Verklaar duidelijk alle stappen in de redenering.**

Er zijn 2 aanpakken ma ik ga 1 geven die ik het simpelste vind.

**Aanpak 1**

Partitionering voor n elementen vraagt n+1 vergelijkingen (Cfr.Houre partitionering)

Verwacht aantal vergelijkingen nodig om n elementen met QS te sorteren:

![image-20220412151651761](img/image-20220412151651761.png)

$C(n) = (𝑛 + 1) + 1/n[𝐶(0) + 𝐶(𝑛 − 1)] + 1/𝑛  [𝐶(1) + 𝐶(𝑛 − 2)]+. . . + 1/n[𝐶(𝑛 − 1) + 𝐶(0)]$

​       	$= (n+1) + 2/n(c(0)+C(1)+C(2)...+C(n-1))$

En dus:
$nC(n)=n(n+1)+2(C(0)+C(1)+C(2)...+C(n-1))$

Vermits dit geldt voor alle waarden van n, geldt het ook voor n-1:

$(n-1)C(n-1) = (n-1)n+2(C(0)+C(1)+C(2)...+C(n-2))$

Om de lange som weg te werken, trekken we beide vorige vergelijkingen van elkaar af:

$𝑛C(𝑛) − (𝑛 − 1)𝐶(𝑛 − 1) = 𝑛(𝑛 + 1) − (𝑛 − 1)𝑛 + 2𝐶(𝑛 − 1)$

Herschrijven geeft:

$\frac{C(n)}{(n+1)}= \frac{2}{n+1}+\frac{C(n-1)}{n}$

​	Dit is een recursieve uitdrukking, die we gemakkelijk kunnen expanderen. We weten ook dat C(1) = 0 en C(2)=1, wat een stopconditie geeft voor de expansie.

$\frac{C(n)}{n+1}=\frac{2}{n+1}+\frac{2}{n}+\frac{2}{n-1}+\frac{2}{n-2}+...+\frac{2}{3}$

of ook:

$C(n)=2(n+1)(\frac{1}{n+1}+\frac{1}{n}+\frac{1}{n-1}+\frac{1}{n-2}+...+\frac{1}{3})$

Net zoals bij de benadering van Stirling, benaderen we de som door een integraal.

$(\frac{1}{n+1}+\frac{1}{n}+\frac{1}{n-1}+\frac{1}{n-2}+...+\frac{1}{3}) ≈ \int_2^{n+1}\frac{1}{x}dx $

=$[ln(x)]_2^{n+1}$

=$ln(n+1) - ln(2)$

![image-20220412165200251](img/image-20220412165200251.png)

Daarom kunnen we de integraal ook over een minder groot domein nemen, waardoor we 1 term verhuizen naar de lagere orde termen. Uiteindelijk maakt dit niet zoveel uit, vermist we enkel interesse hebben in de snelst stijgende term.

$(\frac{1}{n+1}+\frac{1}{n}+\frac{1}{n-1}+\frac{1}{n-2}+...+\frac{1}{3}) ≈ \int_2^{n}\frac{1}{x}dx + \frac{1}{n+1} $

= $[ln(x)]_2^{n+1} + \frac{1}{n+1}$

= $ln(n) - ln(2) + \frac{1}{n+1}$

Waaruit dan volgt:

$C(n) = 2(n+1)(ln(n)-ln(2) + \frac{1}{n+1})$

= $2nln(n)+...$

= $2nln(2)log_2n+...$

= $1.39nlog_2n+...$

~$1.39nlog_2n$

Algemene opmerking: sommigen zijn misschien verontrust door het “losjes” omspringen met het benaderen van de eindige som door een integraal, en een domein te kiezen zoals het ons uitkomt, maar andere benaderingen leveren dezelfde snelst stijgende term op, wat voldoende is voor de ~notatie.

### Vraag 2

**Indien we Quicksort zouden implementeren met 2 pivots (en 3 partities), hoe zou de tijdscomplexiteit zich gedragen? Let op: dit is niet hetzelfde als een 3-way Quicksort waarbij 1 van de partities enkel elementen bevat die gelijk zijn aan de pivot.**

Heel goeie vraag. Waarschijnlijk sneller, anders zouden ze de vraag niet stellen maar vraag me niet waarom : )



### Vraag 3

***(Examenvraag september 2016*) De worst-case tijdscomplexiteit van QuickSort is ~n^2^, indien men telkens voor elke partitionering, het kleinste dan wel het grootste element als pivot kiest. Men kan echter stellen dat QuickSort vrij vergevingsgezind is, en dat, zelfs al we toevallig enkele malen een slechte pivot kiezen gedurende de hele sortering, we toch een linearitmisch verloop van de rekentijd kunnen verwachten. Verklaar!**

We spreken hierover de tilde notatie van de tijdscomplexiteit. Dit betekent dus dat we niet geven om elementen met een kleinere orde.

![image-20220412183456862](img/image-20220412183456862.png)

Als we dan eenmaal een slechte split hebben, worden er n-1 aantal vergelijkingen toegevoegd. Als we dan naar de grote getallen gaan is deze n verwaarloosbaar. Zelfs een paar splits zijn ok. Daarom kunnen we toch nog een linearitmisch verloop van de rekentijd verwachten.



### Vraag 4

**(*Examenvraag September 2020*) Bij recursieve sorteeralgoritmen zoals MergeSort of QuickSort wordt de nog te behandelen deelrij vaak telkens in 2 delen gesplitst. Nochtans kan men zich eenvoudig inbeelden dat men de recursieve opsplitsing in 3 of 4 zelfs meer delen uitvoert (in geval van Quicksort vraagt dit dan meerdere pivots, bij MergeSort een merge-operatie van meerdere deelrijen). Is het over het algemeen een goed idee om recursieve sorteeralgoritmes zoals MergeSort en QuickSort (of eventueel anderen) in meer dan 2 delen op te splitsen? Waarom wel? Waarom niet? Wat zijn voor- en nadelen?**



**Quicksort**

Bij quicksort is er al een versie die het splits in 3 delen, namelijk 3 way partitioning. Dit is voordelig bij lijsten met veel duplicates omdat de middelste lijst alle elementen bevat die gelijk zijn aan de pivot.

Nog een voordeel dat voor kan kloppen is dat wanneer je splitst in 3 of meer delen en voor elk van deze delen een pivot kiest, de impact van een slechte pivot veel kleiner is. Nu zeg ik dit maar kan zijn dat ik de vraag fout heb begrepen en dit niet is wat ze bedoelen.

**MergeSort**

Hier kon ik niet direct iets voor vinden maar stackoverflow heeft hier wel een goed antwoord op.

In een normale merge, deelt ge de array door 2 tot je diepte van log~2~n bereikt en dan begin je te mergen. Elke merge van 2 arrays van grootte m neemt ook 2m operaties.

**Dit geeft ons de volgende formule(tijdscomplexiteit):**

```
n/2 * 2 + n/4 * 4 + ... 1 * n = n * log2n
```

Als je dan ipv een normale merge een three-way merge doet:

- De diepte is nu log~3~n
- Tijdens de merge moet je nu de minimum vinden van 3 getallen ipv 2.

**Dit betekent dat de formule er nu zo gaat uitzien:**

```
n/3 * 2*3 + n/9 * 2*9 + ... 1 * 2*n = 2 * n * log3n
```

Het is maal 2 omdat het minimum vinden van 3 elementen bestaat uit 2 operaties.

Asymptotische zijn deze beide Θ(nlogn) maar eenmaal naar de grootte getallen gaat dit wel een verschil geeven.



Voor de uitleg in het engels en nog een mooi voorbeeld wanneer een n-way merge sort handig kan zijn

https://stackoverflow.com/questions/14713468/why-should-we-use-n-way-merge-what-are-its-advantages-over-2-way-merge





## Les 5: Sorteren in lineaire tijd

### Vraag 1

Het antwoord op deze vraag is te vinden op p341 in het boek.

**Een aantal sorteeralgoritmes hebben de eigenschap "stabiel" te zijn.**

- **Wat wordt hiermee bedoeld?**

  Een sorteer methode is stabiel als de relatieve orde van gelijke keys in de array behouden wordt. Deze zin zegt wss weinig dus nu een voorbeeld voor wat duidelijkheid. Stel je hebt een internet commerce applicatie waar we een grote hoeveelheid events met een locatie en timestamps verwerken. Nu steken we deze in een array wanneer deze aankomen want dan zijn ze gesorteerd op de timestamp want de laatste timestamp is de laatste in de array. Als we deze lijst nu zouden sorteren op locatie gaan we zien dat bij een stabiel sorting method de timestamps nog correct staat per locatie en bij een instabiele sorting method niet. Hieronder een afbeelding ter verduidelijking.

  ![image-20220412202732408](img/image-20220412202732408.png)

- **Welke sorteeralgoritmes die we behandeld hebben in de lessen zijn stabiel?**

  **Stabiel:** insertion sort, merge sort

  **Niet-stabiel:** selection sort, quick sort

- **Waarom is stabiliteit een belangrijke eigenschap van een sorteeralgoritme?**

  Dit is enkel belangrijk als je er een nut voor hebt zoals bij het voorbeeld hierboven. Nog een voorbeeld van stackoverflow: *We are asked to sort "by last name, then by first". We could first sort (stable or unstable) by the first name, then stable sort by the last name. After these sorts, the list is primarily sorted by the last name. However, where last names are the same, the first names are sorted.*

  You can't stack unstable sorts in the same fashion.

  https://stackoverflow.com/questions/1517793/what-is-stability-in-sorting-algorithms-and-why-is-it-important

- **Kan een niet-stabiel sorteeralgoritme steeds stabiel gemaakt worden?**

  Ja maar niet zonder een serieuze extra hoeveelheid tijd of ruimte. Dit betekent dat de meeste programmers dus voor algoritmes gaan gaan die uit zichzelf stabiliteit garanderen.



### Vraag 2

**Hoe zou je counting sort kunnen wijzigen zodat het ook zou werken met data die geen positieve integers zijn? Bvb ook negatieve integers behandelen? Of ook getallen met decimale fracties (1.5, 2.5, 3.5, ... ?). Welke voorwaarden moeten er gelden voor de te sorteren data?**

Voor de negatieve integers zouden we de array, die we gebruiken om de hoeveelheid van dezelfde keys te tellen, kunnen opschuiven zodat het laagste getal op 0 staat en dan vandaar verder rekenen.

Voor decimale fracties kan je all getallen maal dezelfde bepaalde hoeveelheid doen zodat je een integer krijgt en dan op een normale manier kan sorteren.

is dit juist? Philly zeg het mij, amen.



### Vraag 3

**(*Examenvraag Juni 2020)* Leg uit: BucketSort. Wat is de kans dat we bij het BucketSort algoritme in de slechtst mogelijke situatie m.b.t. tijdscomplexiteit belanden?**

BucketSort is een sort waarbij elementen van een array in verschillende buckets gestoken worden, dit is meestal op basis van 1 of andere categorie. Daarna kunnen deze buckets op zichzelf gesorteerd worden door een ander algoritme of weer opnieuw gesorteerd in nieuwe buckets.

Geen idee wat de kans is, Phil. TODO



### Vraag 4

**(Examenvraag September 2020)** Op welke manier werkt het Least-Significant-Digit (LSD) sorteeralgoritme? Bespreek tevens de tijdscomplexiteit. 

LSD sort of Radix sort is een gebaseerd op counting sort. Het werkt als volgt; We nemen voor alle getallen het meest rechts gelegen getal, we sorteren dan op deze keys. Dan schuiven we 1 op naar rechts en sorteren op deze keys. Omdat counting sort stabiel is blijven deze getallen met dezelfde key in dezelfde volgorde, is dit niet het geval dan werkt LSD sort niet. Het sorteren op de keys blijven we toepassen tot we het grootste getal volledig behandeld hebben. Als we een getal hebben dat op een bepaalde plek geen cijfer meer heeft dan wordt daar simpelweg een 0 gezet, zoals hieronder.

![image-20220413115112630](img/image-20220413115112630.png)



De tijdscomplexiteit van LSD sort kan heel goed zijn.

![image-20220413115245923](img/image-20220413115245923.png)

Hierboven zien we probleemgrootte n, max grootte van de getallen d = 3 en base = 10(0-9)(dit kan ook binair of hexadecimaal).

Voor Counting sort eenmaal toe te passen hebben we een complexiteit van O(n+b). Voor elke d > 1 moeten we counting sort nog is toepassen dus dat betekent dat de complexiteit verandert naar O(d(n+b)).

Afhangend van bepaalde inputs kan LSD of radix sort het dus beter doen quick sort of merge sort.