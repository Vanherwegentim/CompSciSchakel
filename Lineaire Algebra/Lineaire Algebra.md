# Lineaire Algebra

## 1 Lineaire vergelijkingen

### 1.1 Systemen van lineaire vergelijkingen

Een lineaire vergelijkingen is een vergelijkingen die kan geschreven worden in de vorm van

$a_1x_1+a_2x_2+... +a_nx_n = b$



Een systeem van lineaire vergelijkingen is een verzameling van 1 of meerdere lineaire vergelijkingen met dezelfde variabelen als hierboven.



Een oplossing van een systeem is een lijst van getallen dat er voor zorgt dat elke vergelijking waar is. De set van alle mogelijke oplossing noemen we de **solution set of oplossing set**.

**Twee** lineaire systemen zijn equivalent als ze dezelfde oplossing set hebben.

Een systeem van lineaire vergelijkingen heeft:

1. **geen oplossing**
2. **1 oplossing**
3. **oneindig veel oplossingen**

Een systeem is consistent als er tenminste 1 of oneindig veel oplossingen bestaan. Als dit niet zo is dan is het systeem inconsistent.

De essentiele informatie van een linear systeem kunnen we compact neerzetten in een rechthoekige array, een matrix.

![image-20220901102945466](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901102945466.png)

Deze noemen we de coefficiente matrix.

Nu bestaat er ook de **augmented matrix**. Deze bestaat uit de coefficient matrix met een extra kolom, waarin de constanten van de rechterkant van de vergelijking in staan.

![image-20220901103444389](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901103444389.png)

Om dit soort van systemen op te lossen zijn er veel verschillende manieren maar wij gaan focussen op de elementaire rij-operaties waarvan er 3 zijn:

1. (Vervanging) Vervang een rij ddor de som van zichzelf en een veelvoud van een andere rij.
2. (Verwissel) Verwissel 2 rijen van plaats
3. (Scaling) Vermenigvuldig een hele rij door een niet-nul constante.

Twee matrices zijn rij equivalent als er een sequentie van elementaire rij-operaties is, die de ene matrix in de andere veranderd. Als de augmented matrices van 2 lineaire systemen rij-equivalent zijn dan hebben de 2 systemen dezelfde oplossing set.

**Example:** Kijk of het volgende systeem consistent is:

![image-20220901111125595](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901111125595.png)

![image-20220901111136271](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901111136271.png)

We verwisselen rij 1 en 2

![image-20220901111206213](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901111206213.png)

We elimineren de 5x~1~ in de derde rijd door -5/2 keer rij~1~ toe te voegen aan rij~3~

![image-20220901111318219](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901111318219.png)

We gebruiken rij~2~ om de -1/2 te elimineren in rij~3~

![image-20220901112028442](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901112028442.png)

De vergelijking 0 = 5/2 is een de korte vorm van 0x~1~ + 0x~2~+ 0x~3~ = 5 / 2. Dit kan niet dus is het systeem inconsistent

### 1.2 Rij reducties en echelon vorm

In de komende definities spreken we over een niet-nul rij of kolom. Dit betekent dat er tenminste 1 niet-nul entry is.



Een rechthoekige matrix is in **echelon vorm** of rij echelon vorm heeft 3 properties:

1. Alle niet-nul rijen zijn boven elke rij met alleen maar nullen
2. Elke leidende entry van een rij is een kolom rechts van de leidende entry van de rij erboven
3. Alle entries in een kolom onder leidende entry zijn nul.

Als een matrix in **echelon vorm** voldoet aan de volgende extra condities dan is deze in **reduced echelon form (row reduced echelon form) of gereduceerde echelon vorm**.

4. De leidende entry in elke niet-nul rij is 1
5. Elke leidende 1 is de enige niet-nul entry in zijn kolom.



**Theorem:**

Each matrix is rij equivalent aan maar 1 gereduceerde echelon matrix.



Stel we hebben de volgende gereduceerde echelon vorm gekregen door rij-operaties:

![image-20220901115414836](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901115414836.png)

Er zijn drie variables omdat de augmented matrix 4 kolommen had. We bekomen dan het volgende systeem van vergelijkingen

![image-20220901115550031](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901115550031.png)

De variabelen x~1~ en x~2~ in deze matrix zijn basic variables. De andere variable, x~3~ noemen we een vrije variable.

![image-20220901115715098](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901115715098.png)

De statement "x~3~ is vrij" betekent dat je vrij bent om eender welke waarde te kiezen voor x~3~. Eenmaal dat dit gedaan is kan je de waardes van x~1~ en x~2~ gaan vaststellen want deze hangen af van x~3~.



### 1.3 Vector vergelijkingen

**Vectors in $\R^2$ **

Een matrix met maar 1 kolom is een kolom vector of simpelweg een vector.



Geometrisch descriptie van $\R^2$

Denk aan een rechthoekig coordinaten systeem in een vlak. Elke punt in het vlak kan beschreven worden door een paar van getallen.

![image-20220901120431079](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901120431079.png)

### 1.4 The matrix vergelijking Ax = b

![image-20220901144035233](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901144035233.png)

Deze vergelijking heeft de vorm Ax = b. Dit soort vergelijkingen noemen we een matrix vergelijking. Dit is anders dan de vectov vergelijking hieronder.

![image-20220901144133497](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220901144133497.png)

### 1.5 Oplossing van sets van lineaire systemen.

Een systeem van lineaire vergelijkingen is **homogeen/homogeneous** als het kan geschreven worden in de vorm van Ax = 0, waar A een $m \times n$ matrix is en 0 de zero vector in $\R^m$

Zo een systeem Ax = 0 heeft altijd tenminste zo 1 oplossing, namelijk x = 0. Deze zero oplossing noemen we de triviale oplossing.

