Deze tering begint pas bij hoofdstuk 3, de rest is afval.

![Kulmomentje](C:\Users\timva\Pictures\Kulmomentje.png)

# Hoofdstuk 3 Talen, automaten en berekenbaarheid



## 3.1 Strings en talen

### 3.1.1 Strings

**Definitie 3.1:** Een alfabet is een niet-lege, eindige verzameling. De elementen van de verzameling worden symbolen genoemd.

**Voorbeeld 3.1** De verzameling {a,b,c...,z} is een alfabet. 

Wanneer het er niet toe doet wat het gebruikte alfabet precies is, gebruiken we vaak het symbool Σ om naar het alfabet te verwijzen, en noteren we de elementen als σ1, σ2, . . .



**Definitie 3.2** Een string s over een alfabet  Σ is een eindige rij symbolen uit Σ. Het aantal symbolen in die rij noemen we de lengte van de string, genoteerd |s|. De string die uit nul symbolen bestaat, noemen we de lege string, en noteren we λ. Elke andere string kan genoteerd worden door de symbolen waaruit de string bestaat achter elkaar op te schrijven. De verzameling van alle strings over een alfabet Σ noteren we Σ*.

**Voorbeeld 3.2** Met een alfabet Σ = {0,1} zijn 001101,1111,1101, en λ allemaal strings, met lengte 6,4,4 en 0. Met Σ = {A,B,C,...,Z,a,b,c,...,z} zijn goedemiddag en Leuven String over Σ, maar 120 niet.

Een string heeft steeds een eindige lengte (zie de definitie). Een string met oneindig veel symbolen bestaat dus niet. De verzameling van alle strings is dan wel oneindig, omdat er geen maximale lengte aan de strings opgelegd wordt.  Bijvoorbeeld: de verzameling van alle strings over het alfabet Σ = {a} is de verzameling {λ, a, aa, aaa, aaaa, aaaaa, . . .}.



### 3.1.2 Talen

**Definitie 3.3** Een taal over een alfabet Σ  is een verzameling strings over Σ. (Of nog: een taal over Σ is een deelverzameling van Σ*)

**Voorbeeld 3.3** De verzameling van alle Nederlandse woorden is een taal over Σ = {A,B,C,...,Z,a,b,c,...,z}. De verzameling van alle grammaticaal correcte Nederlandse zinnen en teksten is een taal over een alfabet dat bestaat uit letters, cijfers, leesteken, en de spatie. 







### 3.1.3 Reguliere talen.

Indien we een alfabet Σ vast kiezen, dan kunnen we de volgende bewerkingen uitvoeren op de strings uit Σ*:

- **De concatenatie of samenstelling. **
  Indien x = σ~1~ ,σ~2~  · · · σ~n~ ∈ Σ* en y = µ~1~,µ~2~ · · · µ~m~ ∈ Σ* dan is hun samenstelling 
  		xy = σ~1~,σ~2~ · · · σ~n~µ~1~µ~2~ · · · µ~m~ ∈ Σ*
  
  In het bijzonder hebben we ook voor elke x ∈ Σ* dat
  λx = xλ = x en λλ = λ. 
  
- Voor x ∈ Σ* definieren we 
  x^0^ = λ 
  ∀n ∈ N : x^n+1^ = xx^n^

  

**Voorbeeld 3.6** Als x = abba en y = abcd, dan is xy = abbaabcd. Indien x = abb, is x^3^ = abbabbabb.



We kunnen dezelfde bewerkingen uitbreiden tot talen. Zij A, B ⊆ Σ*, dan is 

- AB = {ab | a ∈ A, b ∈ B} 
- A^0^ = {λ}
- ∀n ∈ N(verzameling van natuurlijke getallen) : A^n+1^ = AA^n^ 

Verder definieren we 

- A* = A~0~ ∪ A~1~ ∪ A~2~ ∪ A~3~ ∪ · · · = ![image-20220216000111613](images\image-20220216000111613.png) 
  A∗ wordt de Kleenesluiting van A genoemd
- A+ = A~1~ ∪ A~2~ ∪ A~3~ ∪ · · · =![image-20220216000256605](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220216000256605.png)

**Definitie 3.4 (Reguliere Taal)** (kan worden gedefinieerd door een reguliere uitdrukking) Indien Σ een alfabet is, dan wordt de klasse van R van alle reguliere talen over Σ inductief als volgt gedefinieerd:

1. ∅ ∈ R, {λ} ∈ R en ∀σ ∈ Σ : {σ} ∈ R.
2. Indien A, B ∈ R, dan ook AB ∈ R, A ∪ B ∈ R en A∗ ∈ R

Elke taal uit R wordt een **reguliere taal** genoemd



**Voorbeeld 3.9** De taal L~3~ = {11,101,1001,10001,100001,...} op Σ = {0,1} is een reguliere taal, want

1. {1} en {0} zijn reguliere talen
2. {0}* is een reguliere taal
3. {1}{0}* is een reguliere taal
4. L~3~ = {1}{0}*{1} is een reguliere taal

### 3.1.4 Reguliere uitdrukkingen

Ook wel regular expression genoemd voor de duidelijkheid, is dus niks nieuws. Ze proberen natuurlijk weer speciaal te doen door het te vertalen naar het nederlands. godverdommse taalpuristen.

**Voorbeeld 3.10** Veronderstel dat Σ de verzameling van ASCII symbolen is, dan zijn de volgende strings reguliere uitdrukkingen over Σ:

- 123
- Hallo!
- Dag mevrouw.



**Voorbeeld 3.11** Met de reguliere uitdrukking ab∗ c duiden we alle strings aan bestaande uit een a, eventueel gevolgd door een aantal keer het symbool b en tenslotte een c. Voorbeelden van strings die aan dit patroon voldoen, zijn ac en abbbbbbbbbbbc, maar niet abbbbbbbbb. We kunnen ook gebruik maken van haakjes om bepaalde deeluitdrukkingen nul of meerdere keren te laten voorkomen. Zo komt met de reguliere uitdrukkingen b(ab)*c elke string overeen bestaande uit een b, dan een aantal keer ab en tenslotte gevolgd door een c. De strings bc en bababababababc voldoen aan dit patroon, de string bac niet. Tot slot is er ook nog een mechanisme dat alternatieven weergeeft. We kunnen namelijk in een reguliere expressie de notatie a|b gebruiken om aan te geven dat op die plaats een a of een b moet voorkomen. Ook bij | mogen we gebruik maken van haakjes.

Tenslotte kunnen we ∗ en | combineren. Zo komen met de reguliere uitdrukking d(a|i) ∗ t alle strings overeen bestaande uit een d gevolgd door nul of meerdere keren de letters a of i en ten slotte een t, zoals de string daiiiat.



**Voorbeeld 3.13**

| Reguliere uitdrukking |                                                              |
| --------------------- | ------------------------------------------------------------ |
| ab*\|c                | {ab^n^ \| n ∈ N} ∪ {c} = {a, ab, abb, abbb, abbbb, . . . , c} |
| a(b*\|c)              | {ab^n^ \|n ∈ N} ∪ {ac} = {a, ab, abb, abbb, abbbb, . . . , ac} |
| (ab)*\|c              | {(ab)^n^\|n ∈ N} ∪ {c} = {λ, ab, abab, abab, ababab, abababab, . . . , c} |



**Definitie 3.5 (Reguliere uitdrukking)** Indien Σ een alfabet is, dan wordt een reguliere uitdrukking over Σ op inductieve wijze als volgt gedefinieerd:

1. ∅ is een reguliere uitdrukking
2. λ is een reguliere uitdrukking
3. Voor elke σ ∈ Σ is σ een reguliere uitdrukking
4. Indien A en B reguliere uitdrukkingen zijn, dan zijn ook (A), A∗ , A|B en AB reguliere uitdrukkingen.

Zoals hierboven aangegeven bepaalt elke reguliere uitdrukking ω een verzameling van strings uit Σ∗ . Deze taal wordt de reguliere verzameling bepaald door ω genoemd.

**Stelling 3.1** Voor een gegeven alfabet Σ geldt dat de klasse van de reguliere talen op Σ precies samenvalt met de klasse van de reguliere verzamelingen. Voor elke reguliere taal L bestaat er bijgevolg een reguliere uitdrukking ω, waarvan de bijhorende reguliere verzameling precies L is



## 3.2 Eindige automaten

Deze shit is al direct kankeronduidelijk maar hopelijk zijn de 2 paginas tekst het waard.

### 3.2.1 Eindige automaten

![image-20220220190218276](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220220190218276.png)

Dit schema werkt door een serie van 0'en en 1'en af te gaan en te zien waar je belandt. Het schema zelf bepaalt een taal L. Als je belandt in de dubbele cirkel voldoet de serie aan de taal, als het er niet in belandt dan voldoet deze niet. 

**Beschouw het voorbeeld 11001.** We starten het schema bij de meest linkse cirkel. Omwille van de eerste 1 van de string verplaatsen we ons naar de bovenste cirkel. De tweede 1 uit de string zegt ons naar de rechter cirkel te gaan. Daarna doet de eerste nul ons naar de onderste cirkel gaan en de volgende nul en de laatste 1 doen ons telkens terugkeren naar de onderste cirkel. Op het einde bevinden we ons dus in de onderste cirkel.

Een eindige automaat is een computermodel dat door zo een schema kan worden voorgesteld. De basis-ingredienten van een eindige automaat zijn een eindig aantal toestanden (in het schema voorgesteld door cirkels) waarin de machine zich kan bevinden en vanuit elke toestand "overgangen" afhankelijk van de invoer op dat moment.

**Definitie 3.6 (Eindige automaat)** Een eindige automaat is een 5-tal A = (Q, Σ, δ, q0, F) met

- Q een eindige verzameling; we noemen de elementen van Q de toestanden van de automaat A.

- F ⊆ Q; F is de verzameling van de aanvaardbare eindtoestanden. (De letter F is de eerste letter van het Engelse Final).

- q~0~ ∈ Q; deze toestand wordt de begintoestand genoemd.

- Σ een alfabet

- • δ een afbeelding, de transitieafbeelding genoemd, 

  ​									δ : Q × Σ → Q.

Een eindige automaat (in het Engels a finite automaton of meer precies a finite state automaton, afgekort FSA) werkt als volgt: 

- Bij de start bevindt de machine zich in de begintoestand q~o~ . Op het moment dat we zullen starten zal er ook steeds een invoerstring x = σ~1~σ~2~ . . . σ~n~ gegeven zijn. (het is mogelijk dat x de lege string λ is).
- Per tijdseenheid voert de machine 1 instructie uit. Om de eerste instructie uit te voeren berekent de automaat de waarde van n δ(q~0~, σ~1~). Deze waarde is opnieuw een toestand, zeg q~i1~ 
- Als tweede stap bepaalt de automaat dan q~i2~
- ...
- Als n-de en laatste stap berekent de machine tenslotte q~in~ = δ(q~in−1~ , σ~n~)

Na deze n-de en laatste stap zijn er nu twee mogelijkheden: ofwel behoort q~i~~n~ tot de aanvaardbare eindtoestanden F, ofwel niet. In het eerste geval zeggen we dat de automaat de string x aanvaardt, in het andere geval wordt de string verworpen.

![image-20220220194243916](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220220194243916.png)

****

**WTF IS DIT MAN, IK HEB HIER WAT UITEG NODIG**

Misschien aanvullen als ge het wat beter begrijpt 

### 3.2.2 Eindige automaten en reguliere talen

Een automaat aanvaardt sommige strings wel, en andere niet. De verzameling van alle strings die aanvaard worden, vormt een taal. We noemen dit de taal bepaald door een automaat; we zeggen ook dat die taal herkend wordt door de automaat.

### 3.2.3 Niet-deterministische eindige automaten

effe uitleg hier, allemaal vrij logisch:

De eindige automaten we tot nu toe gezien hebben zijn zogenaamde deterministische machines. Dit betekent dat de machine op elk moment slechts 1 (ondubbelzinnige) instructie te verwerken krijgt en deze instructie slechts op 1 manier kan uitvoeren. We laten nooit de instructie “of ” toe (Doe A of Doe B). Indien we echter aannemen dat we over twee onafhankelijke processoren zouden beschikken, dan zou een opdracht als Doe A of Doe B parallel kunnen uitgevoerd worden. De ene processor zou A kunnen uitvoeren, terwijl de andere B zou kunnen uitvoeren.

Indien we maar over een processor beschikken, en we willen toch opdrachten met of-statements uitvoeren, dan moet de machine dus op bepaalde momenten een keuze maken welke van de twee (of meer) mogelijke opdrachten ze zal uitvoeren. Dergelijke machines noemt men niet-deterministische machines.

**Definitie 3.8 (Niet-deterministische eindige automaat)** Een niet-deterministische eindige automaat is een 5-tal A = (Q, Σ, δ, q~0~, F) met

- Q een eindige verzameling (de toestanden van de automaat A).

- F ⊆ Q de verzameling van de aanvaardbare eindtoestanden.

- q~0~ ∈ Q de begintoestand van de automaat.

- Σ het alfabet van de automaat.

- δ een afbeelding

  ​	δ : Q × (Σ ∪ {λ}) → P(Q).

Het eerste verschil tussen een gewone eindige automaat en een niet-deterministische ligt in het feit dat de transitieafbeelding δ geen toestanden als beelden heeft, maar verzameling van toestanden. Die verzamelingen kunnen leeg zijn.

Ook niet-deterministische eindige automaten kunnen we schematisch voorstellen met cirkels en pijlen. We laten bij een niet-deterministische machine echter toe dat er vanuit een cirkel meerdere pijlen met hetzelfde label vertrekken. Het label λ mag eveneens gebruikt worden.

**weer veel gezeik, kijk gewoon dit filmpje man**

https://www.youtube.com/watch?v=W8Uu0inPmU8

**Voorbeeld 3.19**

![image-20220320141055097](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220320141055097.png)

**TODO **

## 3.3 Turingmachines

### 3.3.1 Turingmachines

Eindige automaten zijn een wiskundig model voor een zeer eenvoudig soort computers. Ze hebben geen geheugencapaciteit; de enige informatie die ze hebben over de string die ze recent doorlopen hebben, is de toestand waarin ze zich bevinden, en er is maar een eindig aantal verschillende toestanden. Daardoor zijn ze beperkt qua berekeningen: ze kunnen enkel reguliere talen herkennen.

Turingmachines vormen een ander wiskundig model voor een bepaald soort computers, ditmaal wel met een grote geheugencapaciteit. Het model is niet te ingewikkeld, zodat het mogelijk is om bepaalde eigenschappen van dergelijke machines aan te tonen en te behandelen. Aan de andere kant is de klasse van Turingmachines toch krachtig genoeg om alle rekentaken te kunnen uitvoeren die een gewone computer kan uitvoeren.

We kunnen ons een Turingmachine voorstellen als een machine die voorzien is van een magneetband die in twee richtingen kan bewegen. In verschillende fasen van de berekening bevat de band (= het geheugen van dit computermodel!) de invoer voor de berekening, de tussenresultaten, en de uitvoer. De magneetband is een oneindig lange rij van symbolen die bestaat uit een eindige string voorafgegaan en gevolgd door oneindig veel blanco karakters (zie Figuur 3.1).

![image-20220222140950286](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220222140950286.png)

De machine heeft een lees/schrijfkop en het symbool op de magneetband juist onder de kop noemen we het huidig symbool: de operatie van lezen is daarmee impliciet. De kop kan het huidig symbool overschrijven. Net als een eindige automaat heeft een Turingmachine een eindig aantal mogelijke toestanden, en op elk moment bevindt de machine zich in 1 van die toestanden. Een instructie voor de machine is een voorschrift voor de machine om, in 1 operatie, het huidig symbool te overschrijven met een nieuw symbool, de kop (of de magneetband) 1 positie naar links of naar rechts te bewegen, en naar een nieuwe toestand over te gaan. Welke instructie uitgevoerd wordt, hangt enkel af van de huidige toestand van de machine en het huidige symbool onder de leeskop. Eens gestart, blijft de machine instructies uitvoeren tot zij in een toestand komt waarbij 28 er voor het huidig gelezen symbool geen instructie meer voorhanden is. Op dat moment kan men controleren of de machine al dan niet in een aanvaardbare toestand gestopt is. We schrijven nu het bovenstaande neer in een formele definitie.

**Dit is een hele lang uitleg die ge zou kunnen begrijpen ma als ge het uzelf makkelijk wil maken, kijk dit filmpje: https://www.youtube.com/watch?v=dNRDvLACg5Q**



**Definitie 3.10 (Turingmachine)** Een Turingmachine is een 6-tal M = (Q, Σ, T, P, q~0~, F) met

- Q een eindige verzameling; we noemen de elementen van Q toestanden.

- F ⊂ Q de verzameling van aanvaardbare eindtoestanden

- q~0~ ∈ Q de begintoestand

- Σ het alfabet van de Turingmachine. Dit alfabet bevat, naast mogelijk andere symbolen, minstens een speciaal symbool, het blanco symbool of lege symbool, dat we noteren als #.

- T ⊆ Σ\{#} is de verzameling van invoersymbolen. De elementen van Σ\\(T ∪ {#}) worden hulpsymbolen genoemd.

- P een functie (niet noodzakelijk een afbeelding)

  ​			 P : (Q\F) × Σ → Q × Σ × {L, R, 0}

P wordt het programma of de instructieset van de Turingmachine genoemd. (In de verzameling {L, R, 0} staat L voor “Links”, R voor “Rechts” en 0 voor “Blijf staan”, waarmee de beweging van de schrijfkop aangegeven wordt.)

Wanneer we de machine starten bevindt deze zich in de begintoestand q0 en staat de leeskop boven het meest linkse, niet blanco symbool van de magneetband. De machine voert dan het programma P uit en dit moet als volgt geinterpreteerd worden: Noem q de toestand waarin de Turingmachine zich op een bepaald moment bevindt en zij σ ∈ Σ het symbool dat op datzelfde moment door de kop gelezen wordt. Nu zijn er twee mogelijkheden 

1. Het koppel (q, σ) behoort tot het definitiegebied van de functie P. Dit betekent dat P(q, σ) bestaat en gelijk is aan een drietal (q~0~ , σ~0~ , X) ∈ Q × Σ × {L, R, 0}. Het effect van de uitvoering van deze instructie is dat de Turingmachine haar toestand (eventueel) zal veranderen in toestand q~0~ , dat het huidig gescande symbool σ (eventueel) vervangen wordt door σ~0~ en dat de kop zich beweegt zoals X aangeeft, d.w.z. indien X = L, beweegt de kop zich naar links (of de band naar rechts), indien X = R beweegt de kop naar rechts en indien tenslotte X = 0 blijft de kop ter plaatse. 

2. Indien het koppel (q, σ) niet behoort tot het definitiegebied van P stopt het programma. De toestand q wordt de eindtoestand van de Turingmachine (voor die bepaalde invoer) genoemd. 

   

Indien de Turingmachine gestopt is en de eindtoestand q behoort tot F, dan zegt men dat de invoerstring aanvaard werd, in het andere geval zeggen we dat de invoerstring 29 verworpen werd. Indien een string aanvaard werd, dan beschouwen we de eindige string symbolen op de magneetband (dus zonder de twee oneindig lange uiteinden van blanco symbolen) als de uitvoer van de Turingmachine.

En dan nu een voorbeeld van de werking want deze 3 pagina's aan uitleg waren nog niet genoeg.

**Voorbeeld**

We illustreren deze begrippen aan de hand van een Turingmachine die als invoer een string van nullen en enen neemt en daarvan het meest rechtse symbool uitveegt (d.w.z. vervangt door een blanco symbool.)

De werking van een dergelijke Turingmachine zou er als volgt kunnen uitzien: 

- Bij het begin staat de leeskop op het meest linkse symbool van de string (toestand q0) 
- Daarna zoekt de machine het meest rechtse symbool van de string door de leeskop telkens een positie naar rechts te verschuiven (toestand q1). 
- Op het moment dat de leeskop het blanco symbool # leest, bevindt de kop zich ´e´en positie rechts van de string (toestand q2) en moet de kop weer een positie naar links bewegen. 
- Nu moet het ingescande symbool vervangen worden door het blanco symbool # en mag de machine stoppen (toestand h).

Hieronder zie je het hierboven gegeven voorbeeld grafisch voorgesteld.

![image-20220222143946966](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220222143946966.png)

### 3.3.2 Turingmachines en functies

Computers worden vaak gebruikt om berekeningen uit te voeren. Je kan denken dat de functie 'kwadraat', die van een natuurlijk getal zijn kwadraat bepaalt, berekenbaar is door middel van een computer. Nu heeft een computer geen oneindige opslagcapaciteit en is het dus onmogelijk om de waarde kwadraat(n of zelf het getal n zelf) voor elk natuurlijk getal kan opslaan in zijn geheugen. Toch zien we dit als mogelijk want we kunnen het geheugen van onze computer uitbreiden (in theorie althans). Daarom zeggen we vaak dat de functie **effectief berekenbaar is.** Algemeen noemen we elke functie die berekenbaar is op een machine met onbegrensde opslagcapaciteit effectief berekenbaar.

**Stelling 3.5 (These van Church)** Een functie is effectief berekenbaar als en slechts als die functie Turing-berekenbaar is.

Vanaf nu zullen we ons concentreren op functies (met 1 of meerdere veranderlijken) gedefinieerd op de natuurlijke getallen. Nu willen we dit zo simpel mogelijk gaan voorstellen. WE zouden de decimale voorstellingswijze kunnen gebruiken maar dan hebben we minstens 11 symbolen nodig (0,1,2...,#) nodig in onze TM. 

Daarom gaan we gebruiken maken van de binaire of zelfs unaire notatie. In de unaire notatie stellen we getal 0 voor door 1, het getal 1 door 11, het getal 2 door 111, . . . , het getal n door 111 · · · 111 | {z } n+1 enen . Bij deze laatste voorstellingswijze hebben we dus slechts 1 symbool nodig om de getallen zelf voor te stellen.



**Voorbeeld 3.23** De constante nulfunctie f : N → N : n → 0 is Turing-berekenbaar.

We kiezen voor de unaire representatie van de natuurlijke getallen. Een TM kan de constante nulfunctie als volgt berekenen: Bij om het even wat voor een invoerstring verplaatsen we de leeskop steeds een positie naar rechts waarbij we telkens het ingescande symbool wissen, tot we deze string voorbij zijn. Daarna schrijven we als uitvoer het symbool “1”, de unaire representatie voor 0 op de magneetband.

Een formele beschrijving van deze TM M = (Q, Σ, T, P, q~0~, F) wordt als volgt gegeven: 

- Q = {q0, q1, h}, F = {h} 
- Σ = {1, #}, T = {1} 
- P wordt gegeven door:   P(q0, 1) = (q1, #, R) 
  										                                             P(q1, 1) = (q1, #, R) 
                                                                										  P(q1, #) = (h, 1, 0)



**Opmerking** We merken hier op dat de bovenstaande TM niet minimaal is (in het aantal toestanden). Je hoeft namelijk niet meteen van toestand q0 over te gaan naar een nieuwe toestand. (We illustreren dit in het voorbeeld hieronder.)

**Voorbeeld 3.24** Het heeft geen zin om dit over te schrijven dus bekijk gewoon het boek op pagina 32.





**Stelling 3.6** Er bestaat een functie f: N → N diet niet Turing-berekenbaar is.

**Bewijs:** We zullen aant eonen dat er een manier bestaat om een oneindige rij Turingmachines te construeren, op zo'n manier dat elke denkbare Turingmachine ergens in die rij staat. Vervolgends zullen we aantonen dat er een functie bestaat waarvoor geldt dat geen enkele TM in die rij precies dezelfde functie berekent. Omdat de rij alle Turingmachines bevat, is de stelling dan bewezen.

Vooreerst stellen we nog dat we twee Turingmachines die precies hetzelfde zijn op de naamgeving van toestanden of symbolen na, als gelijk beschouwen. Het maakt immers niet uit of we de toestanden nu q~0~, q~1~, . . . noemen of p~0~, p~1~, etc., en hetzelfde geldt voor de symbolen.

**Deel 1:** De verzameling van alle Turingmachines met n toestanden en m symbolen is eindig (op naamgeving na). 

**Bewijs: ** Beschouw een Turingmachine (Q, Σ, T, P, q0, F) met n toestanden Q = {q0, q1, . . . , qn−1} en een alfabet van m symbolen Σ = {σ0, σ1, . . . , σm−1}. Het maakt niet uit welke naam die toestanden en symbolen precies krijgen; enkel de keuze van T, F en P maakt iets uit. Aangezien T ⊆ Σ, zijn er maar eindig veel keuzes mogelijk voor T (namelijk 2m). Hetzelfde geldt voor F ⊆ Q (2n mogelijkheden), en voor P ⊆ Q×Σ×Q×Σ×{L, R, 0} (23m2n 2 mogelijkheden). Het aantal mogelijke combinaties van T, F en P is dus eindig, en bijgevolg ook het aantal verschillende Turingmachines met n toestanden en m symbolen.

**Deel 2:** De volgende procedure kent aan elke Turingmachine een uniek volgnummer toe: Rangschik alle Turingmachines in een bepaalde volgorde waarbij eerst de Turingmachines met n + m = 2 komen (alle Turingmachines hebben minstens 1 toestand en minstens 1 invoersymbool),  dan de Turingmachines met n + m =3, enzovoort. Omdat het aantal Turingmachines met bepaalde n en m eindig is, is ook het aantal Turingmachines met n + m = k endig, voor eender welke k. Noem dit aantal N~k~ . Dan kunnen we alle Turingmachines met n+ m =2 een uniek volgnummer van 1 tot N~2~ geven (de precieze volgorde waarin we dat doen maakt niet uit); alle TM met n + m =3 een volgnummer van N~2~ + 1 tot N~2~ + N~3~ , enzovoort. Deze procedure kent aan elke TM een verschillend eindig getal i toe. Het is dus mogelijk om alle TMs op te lijsten in een oneindige opsomming, t~0~, t~1~,t~2~,... We noteren de fucntie die door t~i~ uitgerekend wordt als f~i~ . Aangezien {t~i~ | i∈ N } alle Turingmachines bevat, bevat {f~i~ | i∈ N } alle Turing-berekenbare functies.

**Deel 3:** definieer de functie g : N → N als volgt ∀i ∈ N : g(i) = fi(i) + 1. Het is duidelijk dat g niet gelijk kan zijn aan eender welke f~i~ , want voor elke f~i~ geldt dat g voor tenminste 1 invoerwaarde een ander resultaat geeft dan f~i~ namelijk voor i. Bijgevolg komt g niet voor in de verzameling van alle Turing-berekenbare functies.



### 3.3.3 Turingmachines en talen

Een TM kan met een bepaalde invoer een bepaalde uitvoer associeren en zo functies berekenen. Maar we kunnen een TM ook gebruiken om talen te herkennen. Als de machine eindigt in een aanvaardbare toestand dan is de invoerstring aanvaard. De taal bepaald door de TM is dan de verzameling van alle strings die aanvaard worden.

**Definitie 3.11** De taal bepaald door een Turingmachine M, genoteerd L(M), is de verzameling van alle invoerstrings waarvoor M in een aanvaardbare toestand eindigt. Gegeven een taal L, zeggen we dat L herkend wordt door M als L(M) = L.

**Definitie 3.12** Een taal L wordt Turing-herkenbaar genoemd, als er een TM bestaat die L herkent. Turing-herkenbare talen worden ook recursief opsombare talen genoemd.

**Definitie 3.13** Een TM beslist een taal, als voor elk string s ∈ L de TM in een aanvaardbare toestand eindigt, en voor elke string s \∈ L de TM in een onaanvaardbare toestand eindigt.

Merk het verschil op tussen herkennen en beslissen. Als een TM de taal L herkent, dan betekent dat dat de TM alle en alleen de strings in L aanvaardt. Strings buiten L kunnen verworpen worden, of onbeslist blijven (omdat de machine niet stopt)

**Definitie 3.14** Een taal L wordt Turing-beslisbaar of kortweg beslisbaar genoemd, als er een TM bestaat die L beslist. Turing-beslisbare talen worden ook recursieve talen genoemd.



### 3.3.4 Niet-deterministische Turingmachines

Als we spreken over TMs zonder verdere uitleg, bedoelen we steeds deterministische Turingmachines. We kunnen ook hier een niet-deterministische versie definieren. Deze zullen een belangrijke rol spelen in de analyse van de complexiteit van beslissingsproblemen.

**Definitie 3.15** (Niet-deterministische Turingmachine) Een niet-deterministische Turingmachine M bestaat uit een zestal M = (Q, Σ, T, P, q~0~, F) dat aan precies dezelfde voorwaarden voldoet als in definitie 3.10, behalve dat P nu geen functie meer hoeft te zijn, maar slechts een relatie tussen (Q\F) × Σ en Q × Σ × {L, R, 0}.

Concreet betekent dit voor een NDTM M dat wanneer deze machine zich in een bepaalde toestand q bevindt en de leeskop boven een bepaald symbool σ staat, er meerdere koppels ((q, σ),(q'  , σ' , X)) tot P kunnen behoren. Dit wil zeggen dat de NDTM M meerdere acties kan ondernemen. We maken dit duidelijker aan de hand van een concreet voorbeeld



**Voorbeeld 3.27** Een NDTM die voor een invoerstring bestaande uit a's en b's nagaat of die string een even aantal a's of b's bevat.

- Toestanden van M: Q = {q~0~,p~0~,p~1~,r~0~,r~1~,h}, F = {h}

- symbolen van M: Σ = {#, a, b}, T = {a, b}

- De instructieset P bestaat uit de koppels:

  ​				![image-20220301144947675](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220301144947675.png)		

In de instructieset hierboven worden de p–toestanden gebruikt om het even of oneven zijn van het aantal a’s bij te houden, de r toestanden doen hetzelfde voor het aantal b’s. Toestand p0 (resp. r0) duidt een even aantal a’s (resp. b’s) aan, toestand p1 (resp. r1) een oneven aantal.

![image-20220301150307968](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220301150307968.png)

Er zijn twee mogelijke wegen die de NDTM M kan volgen en deze zijn samen geschetst in figuur 3.3. Zoals je ziet op de figuur heeft de NDTM bij de eerste stap de keuze tussen twee opdrachten (namelijk ((q0, a),(p0, a, 0)) of ((q0, a),(r0, a, 0))). We nemen aan dat een NDTM telkens wanneer er meerdere opdrachten mogelijk zijn, elk van deze mogelijkheden apart maar tegelijkertijd (parallel) behandelt. We zeggen dat een NDTM M met succes stopt bij een bepaalde invoer of ook nog dat de NDTM M een bepaalde string aanvaardt, indien ´e´en van de gevolgde wegen (en misschien ook meer) in een aanvaardbare eindtoestand stopt. De rekentijd van de NDTM komt overeen met het aantal stappen in de kortste van al die wegen.



## 3.4 Analyse van algoritmen

Hoeveel berekeningsstappen heeft een algoritme nodig om de uitkomst te berekenen, hoeveel geheugenruimte is er nodig? Het analyseren van een algoritme om deze vragen te beantwoorden noemen we "complexiteitsanalyse". Dergelijke vragen zijn van velang als we de keuze hebben tussen verschillende algoritmen voor het oplossen van een probleem. 

Hoe hangt de benodigde tijd of geheugenruimte af van de "grootte" of de moeilijkheidsgraad van de invoer? Om dat te beantwoorden, moeten we eerst die grootte kwantitatief kunnen uitdrukken met een of andere paramter. Het verband tussen die parameter en de benodigde rekentijd en geheugenruimte noemen we de respectievelijk de tijdscomplexiteit en de ruimtecomplexiteit van het algoritme.



### 3.4.1 tijdscomplexiteit van algoritmen

De tijd nodig om een probleem op te lossen hangt af van de "grootte" van het probleem dat moet worden opgelost. Deze grootte wordt gemeten aan de hand van de grootte van de invoer van het "specifieke geval". Ter illustratie bekijken we even het vermenigvuldigen van twee n x n matrices voor welbepaalde n.

Voor de “grootte” van dit specifieke probleem kunnen we n als maat nemen. We zouden echter natuurlijk evengoed n 2 of 2n 2 kunnen voorstellen als maat voor de omvangsgrootte. Veronderstel dat we een algoritme beschouwen dat de standaardmethode voor het vermenigvuldigen van matrices gebruikt. Zo’n algoritme berekent voor alle 1 ≤ i, j ≤ n de (i, j)–de term uit het product door de i–de rij met de j-de kolom te vermenigvuldigen. Voor de berekening van deze (i, j)–de term moet de computer 2n leesoperaties, n vermenigvuldigingen en n − 1 optellingen en tenslotte nog een schrijfoperatie uitvoeren. In het totaal hebben we voor de berekening van deze term 4n bewerkingen nodig. Aangezien er n 2 termen te berekenen zijn, voert het algoritme dus 4n 3 bewerkingen uit.

**Logisch toch? : )**

**Als ge hierna geen zenuwinzinking hebt dan zijt ge een echte winees**

**Definitie 3.16 (Tijdscomplexiteit)** De tijdscomplexiteit van een bepaald algoritme A is een functie tijd~A~(n):  N → N die voor een gegeven invoeromvang n het maximum aantal elementaire bewerkingen aangeeft, die door het algoritme A bij een invoeromvang van grootte n zullen worden uitgevoerd.

Uit de definitie volgt onmiddelijk dat tijd~A~(n) een slechtste geval maat is. Het kan goed zijn dat het in de meeste gevallen veel minder dan tijd~A~(n) elementaire bewerkingen moet uitvoeren om tot een resultaat te komen. Dus maakt men vaak analyses van algoritmen met betrekking tot de gemiddelde complexiteit. Dit is wel wat moeilijker dus beperken wij ons tot het slechtste geval.

#### O-notatie

**Definitie 3.17 (De O-notatie)** Indien f en g functies zijn van  R^+^, dan zeggen we "f(n) is O(g(n))" of "f is O(g)" als

​			∃c ∈ R + 0 , ∃N ∈ N, ∀n ∈ N : n ≥ N ⇒ f(n) ≤ c g(n)

Men zegt ook wel: f is van orde g, of f wordt asymptotisch gedomineerd door g.

Merk op dat het mogelijk is dat “f is O(g)” en “g is O(f)” allebei gelden.



# Hoofdstuk 4 Grafentheorie

Dit is echt een cools momentje, altijd plezierig.

## 4.1 Inleiding

### **4.1.3** Voorbeeld

Snel voorbeeld aan de hand van een voorbeeld dat iedereen wel kent. De boer, de wolf, de kool en de geit.

![image-20220308150719811](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220308150719811.png)

Hierboven zie je de graaf die alle mogelijke opties geeft. Als je dan links vanboven begint en dan naar rechts boven probeert te gaan, is dat je oplossing. 

Zie boek voor meer voorbeelden uwu

## 4.2 Grafen

### 4.2.1 Basisdefinities

**Multiverzameling:** Een multiverzameling lijkt op een verzameling, met als enige verschil dat het zelfde element meerdere keren kan voorkomen in een multiverzameling.

**Multipaar:** Een multipaar is een multiverzameling met 2 elementen.

Bv. {1,1,2,3,5,5,5} is een multiverzameling waarin 1 twee keer voorkomt, en 5 zelfs drie keer. {1,2} is een multipaar, {2,2} ook. De volgorde van de elementen in een multiverzameling heeft geen belang.

Met M~2~(V) bedoelen we de verzameling van alle multiparen die elementen uit V bevatten. M~2~(V ) is bijna hetzelfde als V^2^ = V × V , maar de volgorde waarin we de elementen schrijven heeft bij een multipaar geen belang.

**Definitie 4.1 Graaf** Een graaf is een drietal (V, E,φ), met V een verzameling waarvan de elementen knopen genoemd worden; E een verzameling waarvan de elementen bogen genoemd worden; en φ: E → M~2~(V) een functie die met elke boog twee knopen associeert. 

**Voorbeeld 4.1** De graaf G = (V, E, φ) met V = {a, b, c, d}, E = {e~1~, e~2~, e~3~, e~4~}, en φ(e~1~) = (a, b), φ(e~2~) = (b, c), φ(e~3~) = (b, c), φ(e~4~) = (d, d) kan als volgt getekend worden:

![image-20220308174521128](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220308174521128.png)

We zeggen dat een boog e invalt op een knoop v als v ∈ φ(e). Twee knopen v en w zijn buren van elkaar (of: zijn adjacent) als er een boog e bestaat zodat φ(e) = (v, w).

**Definitie 4.2 (Lus)** Een lus is een boog e waarvoor geldt dat er een v ∈ V bestaat zo dat φ(e) = (v, v). M.a.w. een lus is een boog die een knoop met zichzelf verbindt.

**Definitie 4.3 (Parallelle bogen)** In een graaf G(V, E, φ) noemen we de bogen e~1~ en e~2~ parallelle bogen als en slechts als φ(e1) = φ(e2). M.a.w. twee bogen zijn parallel als en slechts als ze dezelfde knopen met elkaar verbinden.

**Definitie 4.4 (Enkelvoudige graaf)** Een enkelvoudige graaf is een graaf die noch lussen, noch parallelle bogen bevat. M.a.w.: G(V, E, φ) is enkelvoudig als en slechts als (1) ∀e ∈ E : φ(e) = (v, w) ⇒ v 6= w, en (2) ∀e1, e2 ∈ E : e1 6= e2 ⇒ φ(e1) 6= φ(e2).

Vaak zullen we de bogen in een graaf direct met het bijhorende multipaar aanduiden; dus als er een boog e is waarvoor φ(e) = (x, y), dan duiden we die gewoon aan met (x, y). Bij grafen zonder parallelle bogen is dat nooit een probleem. Bij grafen met parallelle 78 bogen is het met deze notatie niet altijd duidelijk welke boog we bedoelen, maar dat is vaak ook niet echt nodig. Daarom wordt die eenvoudiger notatie heel vaak gebruikt, en dat leidt dan tot de volgende, eenvoudigere, definitie van een graaf. 

TLDR: we korten die shit gewoon af omdat we anders teveel nutteloze stuff hebben, dus onze definitie van hierboven wordt dan:

**Definitie 4.5 (Graaf)** Een graaf is een koppel (V, E), met V een verzameling knopen, en E een multiverzameling van multiparen uit V.

**Definitie 4.6 (Graad)** De graad van een knoop v, genoteerd δ(v), is het aantal bogen dat op v invalt. Een lus telt hierbij voor twee (omdat de lus twee keer op de knoop invalt).

**Stelling 4.1** Het aantal bogen in een graaf is steeds de helft van de som van de graden.

**Stelling 4.2** De som van de graden van alle knopen in een graaf is steeds even.

**Stelling 4.3** Het aantal knopen met oneven graad in een graaf is altijd even.

---> De laatste 3 stellingen zijn allemaal eigenlijk triviaal en is gewoon een logisch van het geval dat als ge een boog toevoegt dat deze verbonden is met 2 knopen en dus de some van de graden stijgt met 2. Maar natuurlijk moeten we moeilijk doen dus hieronder het bewijs van deze schijt.



**Bewijs:** Merk vooreerst op: de som van even getallen is altijd even; de som van een even en een oneven getal is altijd oneven; de som van twee oneven getallen is altijd even. Hieruit volgt algemener dat de som van een even aantal oneven getallen altijd even is, en de som van een oneven aantal oneven getallen altijd oneven.

Zij V~o~ de verzameling knopen met oneven graad en V~e~ de verzameling knopen met even graad. Elke knoop in V heeft ofwel even ofwel oneven graad, dus we hebben

![image-20220311143600466](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220311143600466.png)

![image-20220311144242489](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220311144242489.png)



### 4.2.2 Paden

**Definitie 4.7 (Pad)** Een pad in een graaf G(V,E) is een rij bogen van de vorm (v~0~,v~1~),(v~1~,v~2~),...,(v~n-1~,v~n~) waarbij ∀i : (v~i~ , v~i+1~) ∈ E.

We noteren een pad (v~0~,v~1~),(v~1~,v~2~),...,(v~n-1~,v~n~) soms ook als (v~0~,v~1~,...,v~n-1~,v~n~). Het aantal bogen in het pad noemen we de lengte van het pad. Het pad van lengte 0 noemen we het lege pad.

**Definitie 4.8 (Enkelvoudig pad)** Een enkelvoudig pad is een pad (v~0~,v~1~,...,v~n-1~,v~n~) waarvan alle knopen verschillend zijn, d.w.z, ∀i, j : i /= j ⇒ v~i~ /= v~j~ .

**Definitie 4.9 (Kring, enkelvoudige kring)** Een kring is een pad ((v~0~,v~1~),(v~1~,v~1~),...,(v~n-1~,v~n~)) waarin alle bogen verschillend zijn, en waarvoor v~0~ = V~n~(eerste en laatse knoop uwu). Een enkelvoudige kring is een kring waarin ook alle knopen verschillend zijn, afgezien van v~0~ = v~n~.

**Definitie 4.10 (Samenhangende grafen)** Een graaf is samenhangend als en slechts als tussen elke twee knopen van de graaf een pad bestaat.

**Definitie 4.11 (Hamiltoniaans pad, Hamiltoniaanse kring)** Zij gegeven een graaf G. Een Hamiltoniaans pad van G is een pad waarin elke knoop van G precies 1 keer voorkomt. Een Hamiltoniaanse kring van G is een enkelvoudige kring waarin elke knoop van G voorkomt.

![image-20220311151148390](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220311151148390.png)

 **Definitie 4.12 (Euleriaans pad, Euleriaanse kring)** Zij gegeven een graaf G. Een Euleriaans pad van G is een pad waarin elke knoop van G minstens 1 keer, en elke boog van G precies 1 keer voorkomt. Een Euleriaanse kring van G is een Euleriaans pad dat ook een kring is.

  **Stelling 4.4** Een graaf G heeft een Euleriaanse kring als en slechts als de graaf samenhangend is en elke knoop een even graaf heeft.

Okay nu komt er echt een muur van tekst gewoon om de bovenstaande stelling te bewijzen. Is het te laat om uit te schrijven?

**Bewijs:** De bewering is van de vorm “A als en slechts als B” (wiskundig genoteerd: A ⇔ B). Dit wil zeggen dat wanneer A waar is, B ook waar moet zijn (A ⇒ B), en omgekeerd, wanneer B waar is, moet A ook waar zijn (A ⇐ B). We bewijzen beide delen afzonderlijk. ⇒: Als G een Euleriaanse kring heeft, is G samenhangend (1) en heeft elke knoop een even graad (2). Bewijs: (1) G heeft een Euleriaanse kring ⇒ er bestaat een kring die alle knopen van G bevat (bij definitie van Euleriaanse kring) ⇒ tussen elke twee knopen bestaat een pad (volg gewoon de kring) ⇒ G is samenhangend (bij definitie van “samenhangend”). (2) Neem een willekeurige knoop v, van waaruit je stap voor stap een pad construeert dat in v begint, alle bogen precies 1 keer aandoet, en in v eindigt (zo’n pad is een Euleriaanse kring). Zij w een willekeurige knoop verschillend van v. Telkens we w passeren, hebben we een boog nodig om in w aan te komen, en een andere om te vertrekken; het aantal ongebruikte bogen invallend op w vermindert dus met 2. Als w nu een oneven graad zou hebben, zullen we op een bepaald moment in w aankomen via de laatste ongebruikte boog, waarna we niet meer verder kunnen, en de Euleriaanse kring niet kunnen afmaken. Elke knoop behalve v moet dus een even graad hebben. Dat v zelf ook een even graad moet hebben, volgt uit het feit dat we in het begin 1 boog gebruiken om uit v te vertrekken, en op het einde 1 boog om er aan te komen, dus 2 in totaal, en bij elke tussentijdse passage door v precies 2 bogen opgebruiken. ⇐: Als G samenhangend is en elke knoop een even graad heeft, heeft G een Euleriaanse kring. Bewijs: Neem een willekeurige knoop in G; we duiden die knoop aan met v0. Construeer een pad vanuit v0 door een willekeurige boog te kiezen naar een andere knoop, vanuit die knoop weer een willekeurige boog te kiezen, enz. Omdat elke knoop een even graad heeft, heeft elke knoop waarin je aankomt nog een boog over om verder te gaan. De enige uitzondering is de beginknoop v0, die na vertrek een oneven aantal ongebruikte bogen overhoudt. Dus als we vanuit v0 zo’n pad construeren en blijven verdergaan tot we niet meer kunnen, eindigen we gegarandeerd weer in v0. We hebben dan een kring 82 (v0, v1, . . . , vn, v0). Er zijn nu twee mogelijkheden: ofwel zijn alle bogen opgebruikt, dan is de kring Euleriaans en zijn we klaar; ofwel niet. In dat laatste geval is er ergens een boog (x, y) die niet op het pad voorkomt. Stel dat x en y niet in de kring zitten. Omdat de graaf samenhangend is, moet er een pad bestaan tussen x en eender welke knoop op de geconstrueerde kring, en daarom moet er een knoop vi zijn in die kring van waaruit er een boog vertrekt die niet in de kring zit. Als x en/of y wel in de kring zitten, kunnen we gewoon vi = x of vi = y nemen. Vanuit vi kunnen we nu een nieuwe kring construeren met ongebruikte bogen, op dezelfde manier als daarnet. (Zij G0 de graaf G zonder de reeds gebruikte bogen; omdat in G elke knoop even graad had en de graden in G0 een veelvoud van 2 lager zijn dan die in G, heeft G0 ook enkel even graden.) De nieuw geconstrueerde kring kan tussengevoegd worden in de oorspronkelijke: (v0, v1, . . . , vi , w1, . . . , wm−1, vi , vi+1, . . . , vn, v0). Telkens er nog ongebruikte bogen over zijn, kunnen we op deze manier de kring uitbreiden. Dit blijven we doen tot er geen ongebruikte bogen meer zijn; het resultaat is een Euleriaanse kring.

Ik kan echt niet eens de moeite doen om hier een tl;dr van te schrijven.

**Stelling 4.5** Een graaf G heeft een Euleriaans pad als en slechts als de graaf samenhangend is en hoogstens 2 knopen een oneven graad hebben.

**Bewijs:**⇐: Het aantal knopen met oneven graad is steeds even (Stelling 4.3). “Hoogstens 2” betekent dus 0 of 2. In het geval dat het er 0 zijn, is er een Euleriaanse kring, en dus een Euleriaans pad. Zij G een samenhangende graaf waarin twee knopen een oneven graad hebben. Noem die twee knopen v en w. Voeg nu een boog (v, w) toe: G0 = G ∪ {(v, w)}. G0 heeft enkel knopen met even graad, en heeft dus een Euleriaanse kring. Beschouw de Euleriaanse kring die in v begint en (w, v) als laatste boog gebruikt: (v, v1),(v1, v2), . . . ,(w, v). Deze kring doet alle bogen van G aan, en op het einde ook (w, v). Wanneer we nu die laatste boog weer weghalen, hebben we een pad van v naar w dat alle bogen van G aandoet, dus een Euleriaans pad. ⇒: Als er een Euleriaans pad bestaat, is de graaf zeker samenhangend. Als er in deze graaf meer dan 2 knopen een oneven graad hebben, waaronder v en w, dan heeft G0 = G ∪ {(v, w)} nog steeds knopen met oneven graad, dus heeft G0 geen Euleriaanse kring, en G geen Euleriaans pad.



### 4.2.3 Deelgrafen en componenten

**Definitie 4.13 (Deelgraaf)** Een graaf G'(V' , E' ) is een deelgraaf van een graaf G(V, E), genoteerd G'' ⊆ G, als en slechts als V' ⊆ V en E' ⊆ E.

**Definitie 4.14** (Geinduceerde deelgraaf) Gegeven een graaf G(V, E) en een deelverzameling V' ⊆ V noemen we G' (V' , E' ) de deelgraaf van G geinduceerd door V' als en slechts E' = {(v, w) ∈ E|v, w ∈ V'}.

**Definitie 4.15 (Component)** Een graaf G(V, E) is een component van een graaf G' (V' , E' ) als en slechts als G ⊆ G' , G is niet leeg, G is samenhangend, en er bestaat geen samenhangende graaf G'' waarvoor G ⊂ G'' ⊆ G' .

De componenten van een graaf G vormen een partitie van G, d.w.z.: elke knoop en boog komt voor in precies 1 component van G.



Als ge hier niks van begrijpt, bekijk dan eerst de afbeelding hieronder!

![image-20220315153351486](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220315153351486.png)

![image-20220315153612564](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220315153612564.png)

**Hieronder vind je alles van hierboven uitgelegd in voorbeelden.**

![image-20220315153733323](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220315153733323.png)



### 4.2.4 Gerichte grafen

Bij een gewone graaf geven de bogen een symmetrische relatie aan: als v verbonden is met w, is w automatisch ook verbonden met v. Soms hebben we grafen nodig waarin de bogen een richting hebben. Er kan dan een boog van v naar w zijn zonder dat er een boog van w naar v is. Dat leidt tot het concept van een gerichte graaf.

**Definitie 4.16 (Gerichte graaf)** Een gerichte graaf (Eng. directed graph of digraph) is een koppel (V, E), met V een verzameling waarvan de elementen knopen genoemd worden, en E ⊆ V^2^ een verzameling koppels

**Definitie 4.17 (Gericht pad, ongericht pad)** Een gericht pad in een gerichte graaf G(V, E) is een pad (v~0~, v~1~, . . . , v~n~) met ∀~i~ : (v~i~ , v~i+1~) ∈ E. Een ongericht pad is een pad (v~0~, v~1~, . . . , v~n~) met ∀~i~ : (v~i~ , v~i+1~) ∈ E ∨ (v~i+1~, v~i~) ∈ E.

![image-20220322144305488](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220322144305488.png)

## 4.3 Voorstellingen van grafen

We hebben grafen tot nog toe gewoonlijk als tekeningen voorgesteld, of als koppels (V, E) met V een verzameling knopen en E een verzameling bogen. Er zijn nog andere voorstellingen mogelijk. In deze sectie bekijken we matrixvoorstellingen van grafen. Een voordeel van deze voorstellingswijze is dat allerlei nuttige berekeningen met grafen dan met behulp van matrixoperaties kunnen gebeuren.

### 4.3.1 Buurmatrix

**Definitie 4.18 (Buurmatrix)** Gegeven een enkelvoudige graaf G(V,E), met V = {v~1~, v~2~, . . . , v~n~}, is de buurmatrix van G een n × n-matrix A met A~ij~ = 1 <=> (v~i~,v~j~) ∈ E, en A~ij~ = 0 ⇔ (v~i~ , v~j~ ) /∈ (geen element van) E.

Ik had eerst echt totaal niet door wat er met een buurmatrix bedoelt werd ma das gewoon een matrix van een graaf en als ge een 1 hebt op een plek betekent dat die 2 noden verboden zijn op de graaf. Eigenlijk niet zo moeilijk.

![image-20220322144519388](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220322144519388.png)

**Stelling 4.7** Als A de buurmatrix van een enkelvoudige graaf G(V,E) is, geldt voor A^k^ het volgende: voor alle i en j is A^k^~ij~ gelijk aan het aantal verschillende paden van lengte k tussen v~i~ en v~j~



**Bewijs:** We bewijzen dit door inductie

**Basis:** Voor k = 1 is A^k^ =A. Bewijs: Er is een pad van lengte 1 tussen v~i~ en v~k~ als en slechts als er een boog tussen v~i~ en v~j~ is. Het aantal paden van lengte 1 tussen v~i~ en v~j~ is. Het aantal paden van lengte 1 tussen v~i~ en v~j~ is dus 1 als er een boog tussen die knopen is (in dit geval is A~ij~ = 1), en 0 als er geen is (dan is A~ij~ = 0). A~ij~ is dus steeds gelijk aan het aantal paden van lengte 1 tussen v~i~ en v~j~ .



**Inductiestap:** als de stelling geldt voor een bepaalde k ≥ 1, dan ook voor k + 1. Bewijs: Elk pad van lengte k + 1 van vi naar vj begint met een boog van vi naar een knoop vl , en vervolgt met een pad van lengte k van v~l~ naar v~j~ . Het aantal paden van lengte k + 1 met als eerste boog (v~i~ , v~l~) is gelijk aan 0 als de boog (v~i~ , v~l~) niet bestaat (d.w.z. als A~il~ = 0), en anders (als A~il~ = 1) gelijk aan het aantal paden van lengte k van v~l~ naar v~j~ . Dat laatste is vanwege de inductieveronderstelling gelijk aan A^k^ ~lj~ . Het totaal aantal paden van lengte k + 1 is de som van al deze aantallen voor de verschillende v~l~ die gekozen kunnen worden, dus gelijk aan ![image-20220322151223540](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220322151223540.png) . Dit laatste is bij definitie gelijk aan A^k+1^~ij~



### 4.3.2 Booleaanse buurmatrix

4.3.2 Booleaanse buurmatrix In plaats van matrices met getallen kunnen we ook booleaanse matrices definieren. Booleaanse matrices hebben booleaanse waarden in hun cellen staan. Som en product van dergelijke matrices worden op de gebruikelijke manier gedefinieerd, met dit verschil dat de som van twee getallen hier een disjunctie van twee booleaanse waarden wordt, en het product van twee getallen een conjunctie van booleaanse waarden. Dit wil zeggen dat het product van twee Booleaanse matrices A en B gedefinieerd wordt als P = A · B ⇔ ∀~i, j~ : P~ij~ = A~i1~ ∧ B~1j~ ∨ A~i2~ ∧ B~2~ ∨ · · · ∨ A~in~ ∧ B~nj~ = ![image-20220322153136114](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220322153136114.png)

en hun som als 

​					S = A + B ⇔ ∀i, j : S~ij~ = A~ij~ ∨ B~ij~

 We kunnen van de buurmatrix een booleaanse versie definieren

**Stelling 4.8** Als B de booleaanse buurmatrix van G(V, E) is, geldt voor B^k^ het volgende: voor alle i en j is B^k^~ij~ equivalent met “er bestaat een pad van lengte k van v~i~ naar v~j~”.

**Bewijs:** Wordt als oefening gelaten. Dit kan bewezen worden op dezelfde manier als de vorige stelling, of je kan gebruik maken van de vorige stelling en van de eigenschap dat “er bestaat een pad” overeenkomt met “het aantal paden is strikt groter dan 0”.

**Stelling 4.9** Als B de booleaanse buurmatrix van G(V, E) is, geldt voor S = ![image-20220322154125827](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220322154125827.png) het volgende: voor alle i en j is S~ij~ equivalent met “er bestaat een pad van lengte l of korter tussen v~i~ en v~j~”.

**Bewijs:** Wordt als oefening gelaten. 

### **4.3.3 Incidentiematrix**

**Definitie 4.20 (Incidentiematrix) **Gegeven een enkelvoudige graaf G(V, E), met V = {v~1~, v~2~, . . . , v~n~} en E = {e~1~, e~2~, . . . , e~m~}, is de incidentiematrix van G een n × mmatrix A met A~ij~ = 1 als ej invalt op v~i~ , en A~ij~ = 0 in alle andere gevallen.

![image-20220326170328823](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220326170328823.png)

## 4.4 Isomorfisme

**Defintie 4.21 (Graaf-isomorfisme)** Twee grafen G(V, E) en G' (V' , E') zijn isomorf als en slechts als er een bijectie h : V → V' bestaat, zo dat {h(x)|x ∈ V } = V' en {(h(x), h(y))|(x, y) ∈ E} = E'

De functie h stelt een “hernoeming” van de knopen voor; ze beeldt elementen van V af op elementen van V'. Als twee grafen isomorf zijn, moeten de knopen van de eerste graaf hernoemd kunnen worden, zo dat, na toepassing van die hernoeming op V en E, V' en E' bekomen wordt

**Isomorfisme** komt er eigenlijk op neer dat V en E van beide grafen gelijk zijn, op de namen van de elementen na.



![image-20220326182606980](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220326182606980.png)

**Al deze grafen zij isomorf!**

**Stelling 4.10** Twee enkelvoudige grafen zijn isomorf als en slechts als er een ordening van de knopen bestaat zodat hun buurmatrix gelijk is.

**Bewijs: =>** Beschouw twee isomorfe grafen G(V, E) en G' (V' , E') met buurmatrices A en A' ; zij h de bijectie die bij het isomorfisme hoort. Beschouw de knopen van V in de volgorde v~1~, v~2~, . . . , v~n~. Beschouw nu de knopen van V' in de volgorde h(v~1~), h(v~2~), . . . , h(v~n~). Als we voor A en A' deze volgordes aanhouden, dan hebben we A~ij~ = 1 ⇔ (v~i~ , v~j~ ) ∈ E ⇔ (h(v~i~), h(v~j~)) ∈ E' ⇔ A'~ij~ = 1 en analoog A~ij~ = 0 ⇔ (v~i~ , v~j~ ) /∈ E ⇔ (h(v~i~), h(v~j~)) /∈ E' ⇔ A'~ij~ = 0. ⇐: als de buurmatrices gelijk zijn, definieer dan h zo dat de i-de knoop in V overeenkomt met de i-de knoop in V' . A~ij~ = A'~ij~ impliceert dan dat (v~i~ , v~j~) ∈ E ⇔ (h(v~i~), h(v~j~)) ∈ E' , m.a.w. de grafen zijn isomorf. 

**Stelling 4.11** Twee grafen G en G' zijn isomorf als en slechts als er een ordening van de knopen en bogen bestaat waarvoor de incidentiematrices van G en G' gelijk zijn.

**Bewijs**: Het bewijs wordt als oefening gelaten.

### 4.4.1 Graaf-isomorfisme testen



Gegeven twee grafen G~1~(V~1~) en G~2~(V~2~, E~2~) , hoe kunnen we testen of ze isomorf zijn? Het is duidelijk dat als |V~1~| /= |V~2~|, er geen bijectie tussen de knopen bestaat, en de grafen dus zeker niet isomorf zijn. In het volgende gaan we ervan uit dat |V~1~| = |V~2~| = n. Een eenvoudig algoritme is het volgende: beschouw alle mogelijke bijecties f van V~1~ naar V~2~, en test voor elke f of E~2~ = {(f(v), f(w))|(v, w) ∈ E~1~}. Van zodra een f gevonden wordt waarvoor dit het geval is, eindigt het algoritme met “ja” als antwoord. Er zijn eindig veel bijecties; als ze allemaal geprobeerd zijn zonder een bijectie met de vermelde eigenschap te vinden, eindigt het algoritme met “nee”. Als de grafen n knopen hebben, zijn er n! bijecties uit te testen. Dit algoritme heeft dus een exponentiele complexiteit. Het nagaan of een bijectie voldoet aan de vermelde eigenschap is relatief eenvoudig, dit kan in polynomiale tijd. Dat betekent dat het probleem in NP zit. Voor dit probleem is momenteel niet bekend of het in P zit, en er is ook niet aangetoond dat NP-compleet is. In principe is het dus mogelijk dat het representatief is voor een complexiteitsklasse die “tussen” P en NPC in zit. 

**P = Polynomial time**

**NP = Non-deterministic polynomial time**



Een verwant probleem is het beslissen van subgraaf-isomorfisme: 

Gegeven twee grafen G1 en G2, bestaat er een subgraaf G ⊆ G2 zo dat G1 isomorf is met G? 

Van subgraaf-isomorfisme is bekend dat het **NP**-compleet is. Hoewel graaf-isomorfisme moeilijk is, bestaan er algoritmen die gemiddeld vrij snel beslissen of twee grafen isomorf zijn. Het is vrij eenvoudig om voorwaarden te definieren waaraan twee isomorfe grafen altijd voldoen, en die snel na te gaan zijn: 

- Het aantal knopen moet gelijk zijn. 
- Het aantal bogen moet gelijk zijn. 
- Het aantal knopen met graad i moet gelijk zijn, voor elke i ∈ N. 
- . . . 

Een algoritme kan bv. gemakkelijk een tabel opstellen met voor elke i het aantal knopen met graad i in G1, en hetzelfde voor G2, en dan nagaan of die tabellen gelijk zijn; dit kan in polynomiale tijd. Wanneer twee grafen aan alle voorwaarden voldoen, dan pas is het nodig om een algoritme met hogere complexiteit te gebruiken. Dan nog kan het aantal bijecties dat bekeken moet worden, sterk gereduceerd worden: het is bv. niet zinvol om bijecties te bekijken die een knoop met graad g afbeelden op een knoop met graad g' > g. ==Het totaal aantal bijecties wordt dan gereduceerd van n! naar n~1~!n~2~! · · · n~k~!, met n~i~ het aantal knopen met graad i. Dat is een veel kleiner getal.==

effe uitleg voor het gearceerde deel, n is het aantal knopen. Dus wat ze willen zeggen is dat de faculteit van n kleiner is dan het product van de faculteiten van het aantal knopen met een bepaalde graad.



## 4.5 Gewogen grafen

In dit gedeelte bekijken we grafen waarvoor aan elke boog e een gewicht w(e) ∈ R + 0 toegekend is. Het gewicht van een graaf, en het gewicht van een pad, defini¨eren we als de som van de gewichten van de bogen in die graaf (op dat pad). Het kortste pad tussen a en b is bij definitie het pad tussen a en b met het kleinste gewicht. classic gps dus.



### 4.5.1 Het kortste-pad-algoritme van Dijkstra

We beginnen met een lichtjes vereenvoudigde versie van het **Dijkstra** algoritme. Dit algoritme berekent enkel het gewicht van het kortste pad, niet het pad zelf. Daarna zullen we het uitbreiden zodat het ook het pad zelf aanduidt.

### 4.5.2 Dijkstra, versie 1

Het volgende algoritme berekent het gewicht van het kortste pad van een gegeven knoop a naar een gegeven knoop z in een enkelvoudige, samenhangende, gewogen graaf G(V, E) met a, z ∈ V .

![image-20220326214021018](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220326214021018.png)

