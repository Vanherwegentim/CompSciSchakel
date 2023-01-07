# Lineaire Algebra oefening assistentie

## Oefenbundel 1 (Les 1 2 3)

#### **Consistentie**

 Een stelsel is consistent als de matrix 1 of meerdere oplossing heeft. De uitgebreide matrix B
$$
\left(
\begin{array}{cc|c}
3 & 6 & 1\\
0 & 0 & 2\\
\end{array}
\right)
$$
Is inconsistent want 0x~1~ + 0x~2~ = 2 is niet mogelijk. De matrix B heeft dus geen oplossing.



#### **Span**

De span van vectoren is de verzameling van alle lineaire combinaties van die vectoren. Als je een matrix A (bestaande uit de kolomvectoren
 $a_1,a_2,a_3$) hebt dan is de kolomruimte ($Col(A)$) gelijk aan de span {${a_1,a_2,a_3}$}

**Extra info**

Als je een span hebt van 2 vectoren (v~1~, v~2~) en een derde vector (v~3~) ligt in die span dan kan je die v~3~ schrijven als een lineaire combinatie van v~1~ en v~2~



**Inverteerbaar (invertible)**

Een matrix is inverteerbaar als het aan de volgende voorwaarde voldoet:

- De matrix is vierkant m.a.w. eveneel kolommen als rijen
- De determinant van de matrix mag niet 0 zijn
- De matrix mag geen rijen hebben met alleen maar nullen

Als een matrix inverteerbaar is dan heeft deze een inverse matrix



#### **Lineaire Combinatie**

Gegeven de matrix multiplicatie van matrix A en B
$$
\left(
\begin{array}{cc}
a_1 & a_2 \\
a_3 & a_4 \\
\end{array}
\right)
.
\left(
\begin{array}{cc}
b_1 & b_2 \\
b_3 & b_4 \\
\end{array}
\right)
=
\left(
\begin{array}{cc}
a_1.b_1+a_2.b_3 & a_1.b_2+a_2.b_4 \\
a_3.b_1+a_4.b_3 & a_3.b_2+a_4.b_4 \\
\end{array}
\right)
$$
Zoals je kan zien hier zijn de kolommen van de matrix AB lineaire combinaties van de rijen van B want

$(b_1,b_2) + (b_3,b_4) = (b_1+b_3, b_2+b_4)$

want hetzelfde is als hieronder (buiten de scalar). Wat we hieronder hebben is recht uit de matrix AB hierboven gehaald.

$(a_1.b_1+a_2.b_3 , a_1.b_2+a_2.b_4)$



#### Echelon vorm

Een vierkante matrix is in echelon vorm als

- Alle niet-nul rijen zijn boven elke rij met alleen maar nullen staan
- Elke leidende entry van een rij is een kolom rechts van de leidende entry van de rij erboven
- Alle entries in een kolom onder leidende entry zijn nul.

**Gereduceerd echelon vorm**

Als het dan ook nog is voldoet aan de volgende voorwaarde dan is het in gereduceerd echelon vorm

- De leading entry in elke niet nul-rij is 1
- Elke leidende 1 is de enige niet nul entry in zijn kolom

Elke matrix heeft maar 1 gereduceerd echelon matrix

#### Homogeen

Een systeem van lineaire vergelijking is homogeen als het geschreven kan worden als $Ax=0$ waar A een $m\times n$ matrix is and 0 de zero vector. Zo een systeem $Ax=0$ heeft altijd een oplossing, namelijk $x=0$.

Dit noemen we de **triviale oplossing**. De vraag is of er een **nontriviale oplossing bestaat**.

De homogene vergelijking $Ax=0$ heeft een niet-triviale oplossing als en slechts als de vergelijking 1 vrije variable heeft.



#### Parametrische vector vorm

De oplossingsverzameling van $Ax=0$ (homogeen) kunnen we schrijven als $x=tv$ met $v$ een vector



We kunnen de oplossingsverzameling van $Ax=b$ schrijven in parametrische vector vorm en de algemene formule van dit ziet er zo uit: $x=p+tv$

Als de vergelijking $Ax=b$ consistent is voor een gegeven $b$ en $p$ is gelijk aan de oplossing. Dan is de oplossingsverzameling voor $Ax=b$ de verzameling van alle vectoren van de vorm $w=p+v_h$, waar $v_h$ gelijk is aan een oplossing van de homogene vergelijking $Ax=0$



#### Factorisaties

Een factorisatie van een matrix A is een vergelijking dat A uitdrukt als een product van 2 of meer matrices.

##### LU factorisatie

- **L** is een **l**ower triangular matrix met alleen maar 1 op de diagonaal

- **U** is de echelon vorm van A

Het algoritme voor LU factorisatie:

1. Reduceer a naar de echelon vorm U
2. Plaats de entries in L

De enige operatie die je mag doen is:

​	(Vervanging) Vervang een rij door de som van zichzelf en een veelvoud van een andere rij.



#### Inverse

Een $n\times n$ matrix $A$ is invertible als er een $n \times n$ matric $C$ bestaat zodat

​		$CA =I$ en $AC = I$

waar $I$ de identiteitsmatrix is

De inverse van een $2\times 2$ matrix kan berekend worden door de volgende formule:

$A^{-1} = \frac{1}{ad-bc} \begin{bmatrix}d &-b\\-c & a \end{bmatrix}$

Als $ad-bc=0$ dan is A niet inverseerbaar aangezien we dit ook gebruiken in de berekening van de determinant kunnen we zeggen dat een **matrix alleen een inverse heeft als **

- **$det(a) \ne0$**
- 0 is geen eigenvalue van A



**Eigenschappen:**

- $(A^{-1})^{-1}= A$
- $(AB)^{-1} = B^{-1}A^{-1}$
- $(A^T)^{-1}=(A^{-1})^T$



#### Partitionering

We kunnen matrices ook partitioneren. Dit wilt zeggen dat we een matrix gaan opdelen in kleinere submatrices. Er zijn 3 opties:

1. **Rij partitionering:** Hier gaan we een matrix A opspliten in 2 of meer matrices die telkens 1 of meer rijen bevat van onze originele matrix.
   - ![image-20221227184346499](img/image-20221227184346499.png)
2. **Kolom partitionering:** Hier gaan we een matrix A opsplitsen in 2 of meer matrices die telkens 1 of meer kolommen bevat van onze originele matrix
   - ![image-20221227184502635](img/image-20221227184502635.png)
3. **Block partitionering:** Hier gaan we de matrix A opsplitsen in kleinere matrices die telkens een vierkante blok bevatten van de matrix
   - ![image-20221227184611967](img/image-20221227184611967.png)

Dit kan handig zijn voor het berekenen van de inverse van een matrix.

Hier wat formules voor het berekenen van de determinant van een block partitionering (blok matrix). 
Als A B C D matrices zijn dan:

$$det \left(\begin{array}{cc}A & 0\\C & D\\\end{array}\right) = det(A)det(D) = det \left(\begin{array}{cc}A & B\\0 & D\\\end{array}\right)$$



#### Transpose

Gegeven een $m\times n$ matrix A, dan is the transpose de $n \times m$ matrix, genoteerd door A^T^, waarvan de kolommen gevormd worden door de overeenkomstige rijen van A

**Eigenschappen:**

- $(A^T)^T$ = A
- $(A+B)^T=A^T+B^T$
- Voor elke scalar $r,(rA)^T=rA^T$
- $(AB)^T=B^TA^T$

De transpose van een product van matrices is gelijk aan het product van de transpose in omgekeerd volgorde: $(AB)^T=B^TA^T$ 





#### Belangrijk voor examen:

- Vraag over inverse maar je mag het niet expliciet berekenen met rijreducties etc. Kijk dan of je het kan partitioneren. Vraag 13 in oefenbundel 1 is een goed voorbeeld
- 



## Oefenbundel 2



#### Basis

![image-20221228223436642](img/image-20221228223436642.png)



#### Lineaire Transformatie

**Definitie:** Een lineaire transformatie T van een vector ruimte V in een vector ruimte W is een regel die elke vector x in V een unieke vector T(x) in W toewijst zodat:

1. T(u+v) = T(u) + T(v) voor alle u , v in V
2. T(*c*u) = *c*T(u) voor alle u in V en alle scalars *c*



#### Determinant

De determinant van een matrix A is de schaal factor van de matrix. Afhankelijk van welke dimensie kan dit het volume of oppervlak zijn die de matrix spant.

**Eigenschappen:**

- De determinant van een matrix is gelijk aan het product van zijn eigenvalues
- De determinant van een matrix is gelijk aan het volume van de parallellogram  die men krijgt door de kolommen van de matrix
- De determinant van een diagonaal matrix is gelijk aan het product van zijn diagonale entries
- De determinant van een (lower of upper) triangular matrix is gelijk aan het product van zijn diagonale entries.
- De determinant van een matrix is gelijk aan de determinant van zijn transpose
- $Det(A+B) \ne Det(A) + Det(B)$
- $Det(AB) = Det(A)Det(B)$
- Een rij-vervang operatie verandert de determinant niet
- Een rij-verwisseling operatie verandert het teken van de determinant
- Een rij-schaling (maal een scalar), schaalt de determinant met hetzelde getal



#### Row Space

Als A een $m \times x$ matrix is, dan heeft elke rij van A n entries en dus kan deze geïdentificeerd worden met een vector in $\R ^n$

De set van alle lineaire combinaties van de rij vectors noemen we de **row space** van A en noteren we met **Row A**

- Elke rij heeft $n$ entries dus is Row A een subspace van $\R^n$
- Aangezien de rijen van A geïdentificeerd worden met de kolommen van A^T^, we kunnen ook schrijven **Col A^T** in plaats van **Row A**

Als 2 matrices A en B rij-equivalent zijn dan zijn hun row spaces hetzelfde. Als B in echelon vorm dan vormen de niet-nul rijen van B een basis voor de row space van A en van B



#### Coördinaat Vector

De coördinaat vector [x]~B~ van een vector x ten opzichte van een gegeven basis B = {b~1~,.., b~n~} is een representatie van de vector x in termen van de basis B. 

Om deze coordinaat vector [x]~b~ te vinden, drukken we x uit als een **lineaire combinatie** van de vectoren van de basis B. Met andere woorden, we schrijven x als de som van de scalaire veelvouden van de vectors in basis B.

**Voorbeeld:**

Gegeven de vectoren: 
$$
x = 	 \left(\begin{bmatrix}8 \\ -9 \\ 6\end{bmatrix}\right), b_1=\left(\begin{bmatrix}1 \\ -1 \\ -3\end{bmatrix}\right), b_2=\left(\begin{bmatrix}-3 \\ 4 \\ 9\end{bmatrix}\right), b_3=\left(\begin{bmatrix}2 \\ -2 \\ 4\end{bmatrix}\right)
$$
Zoek de coordinaatvector $[x]_b$ van $x$ relatief ten opzichte van de basis B = ${b_1,...,b_3}$
$$
\left(
\begin{array}{ccc|c}
1 & -3 & 2 & 8\\
-1 & 4 & -2 &-9\\
-3 & 9 & 4 &6
\end{array}
\right) \widetilde\ \left(
\begin{array}{ccc|c}
1 & -3 & 2 & 8\\
0 & 1 & 0 &-1\\
0 & 0 & 10 &30
\end{array}
\right)  
$$
$C_1 -3C_2+2C_3=8 => C_1=-1$

$C_2=-1$

$C_3=3$

Thus:

$$[x]_b = 	 \left(\begin{bmatrix}8 \\ -9 \\ 6\end{bmatrix}\right)$$



#### Change of basis (Verandering van basis)



#### Rang

De rang van een matrix is gelijk aan de dimensie van $ColA$. $ColA$ is gelijk aan het aantal pivotkolommen. 

Gegeven een ($m × n$) matrix $A$ en een inverteerbare ($m × m$) matrix $P$, dan is de rang van $PA$ gelijk aan de rang van $A$



#### Rij-operaties

**De null space** van een matrix blijft hetzelfde wanneer we rij-operaties uitvoeren op deze matrix. Rij-operaties veranderen. Rij-operaties veranderen de hoeveelheid vrije variabelen in een matrix niet dus blijft de null space hetzelfde.



**De column space** van een matrix blijft niet hetzelfde wanneer we rij-operaties uitvoeren op de matrix. Rij-operaties veranderen de entries in de matrix, wat de lineaire combinaties van de kolommen kan veranderen.



**De row space** van een matrix blijft hetzelfde omdat we de rijen alleen scalen of dingen gaan bijtellen. Dus een matrix en zijn echelon vorm hebben dezelfde 



#### Belangrijk voor examen:

- De determinant van een matrix is gelijk aan de determinant van de transpose van die matrix
- Als $A$ en $B$, $n\times n$ matrices zijn dan is $det(AB)=det(A)det(B)$
- Als de determinant van een vierkante matrix 0 is dan is deze niet inverteerbaar
- Vraag 8 oefenbundel bekijken
- Vraag 19 herbekijken (d!!!)
- Quiz me again vraag a nog is bekijken





## Oefenbundel 3

#### Eigenvectors and eigenvalues

**Definition**

An **eigenvector** of an $ n \times n$ matrix A is a nonzero vector $x$ such that $Ax = \lambda x$ for some scalar $\lambda$. A scalar $\lambda$ is called an **eigenvalue** of $A$ if there is a nontrivial solution $x$ of $Ax =\lambda x$; such that $x$ is called an eigenvector corresponding to $\lambda$.

The eigenvectors to put it simply are the vectors that given a transformation matrix $A$ keep the same values, so it isn't influenced by the transformations except for being stretched or squished in space. This is where the **eigenvalues** come in. The eigenvalues of a eigenvector is the amount the eigenvector gets stretched or squished in space by the transformation.

So if the **eigenvalue** is 2, the corresponding **eigenvector** has been made twice as long by the transformation.

Als een matrix de eigenvalue 0 heeft dan is deze **niet** inverteerbaar.

#### Karakteristieke polynomial

Als a een $n \times n$ matris is, dan is $det(A-\lambda I)$ gelijk aan een polynomial van graad $n$ die we de karakteristieke polynomial van $A$ noemen.



#### Similarity (Gelijkvormig)

Als $A$ en $B$, $n \times n$ matrices zijn, dan is A gelijkvormig aan B als er een inverteerbare matrix P bestaat zodat $P^{-1}AP = B$ of $A=PBP^{-1}$

Als $n \times n$ matrices $A$ en $B$ gelijkvormig zijn dan hebben ze dezelfde karakteristieke polynomial en dus dezelfde eigenvalues

#### Diagonalizatie

**De diagonalizatie theorem**

Een $n \times n$ matrix is diagonaliseerbaar als en slechts als $A$, $n$ lineair onafhankelijke eigenvectors heeft. In feite, $A = PDP^{-1}$, met $D$ een diagonaal matrix. als en slechts als de kolommen van $P$, $n$ lineair onafhankelijke eigenvectors  van $A$ zijn. In dit geval zijn de diagonale entries van $D$ de eigenvalues van $A$ die overeenkomen met de eigenvectors in $P$



#### Diagonale matrix representatie

Handig wanneer ze vragen voor een matrixvoorsteliing van iets die diagonaal is.

Stel $A = PDP^{-1}$, waar $D$ een diagonale $n \times n$ matrix is. Als $B$ de basis is voor $\R^n$ gevormed uit de kolommen van $P$, dan is $D$ de $B$-matrix voor de transformatie. p324

Dus met andere woorden. Als ze je vragen voor een basis van een matrix die diagonaal is, bereken dan de $D$ in $A=PDP^{-1}$ waar $P$ de matrix is met de eigenvectors en $D$ de matrix met de **eigenvalues** op de diagonaal



#### Inner product

Het inner product is iets anders dan onze typische matrix multiplicatie. Bij het inner product tussen matrices gaan we eigenlijk de transpose nemen van de eerste matrix en dan doen aan matrix multiplicatie. Voorbeeld:

$u.v = u^T.v =[2 -5 -1] \begin{bmatrix}3\\2 \\ -3 \end{bmatrix} = 2.3 + -5.2 + (-1).(-3) = -1$

Volgende eigenschappen gelden voor het **inner product**: 

- $u.v=v.u$
- $(u+v).w=u.w+v.w$
- $(cu).v = c(u.v)=u.(cv)$
- $u.u \ge 0,$ and $u.u=0$ if and only if $u=0$



#### Lengte van een vector

De lengte of norm van $v$ is de niet negatieve scalar $||v||$ gedefineerd door
$||v||= \sqrt{v.v} = \sqrt{v_1^2+v_2^2+...+v_n^2}$ and 



#### Normaliseren

Een vector met de lengte 1 noemen we de **unit vector**

Als we een niet-nul vector delen door zijn lengte dan krijgen we de unit vector $u$ omdat de lengte van $u$ = $(\frac{1}{||v||}||v||)$

Voorbeeld 

Let $v=(1,-2,2,0)$ Find a unit vector $u$ in the same direction as $v$

**Oplossing**: 
Bereken eerst de lengte van v:

$||v||=\sqrt9=3$

Doe dan $v$ maal ${\frac{1}{||v||}}$ om de unit vector te krijgen

$u=\begin{bmatrix}1/3\\-2/3 \\ 2/3\\0 \end{bmatrix} $



#### Afstand tussen vectoren

Voor $u$ en $v$ in $\R^n$, de afstand tussen de vectoren $u$ en $v$ is dan gelijk aan de lengte van de vector $u-v$ dus

- dist($u,v$) = $||u-v||$

#### Orthogonaliteit

Twee vectoren $u$ en $v$ in $\R^n$ zijn orthogonaal(loodrecht op mekaar) als $u.v=0$ (inner product)

**Het pythagoras theorem**

Twee vectoren $u$ en $v$ zijn orthogonaal als en slechts als $||u+v||^2=||u||^2+||v||^2$

 

##### Orthonormale basis

Gegeven een basis $\{x_1,..,x_p \}$ for een niet-nul subruimte $W$ van $\R^n$, definieer dan



##### Orthogonale complementen

Als een vector $z$ orthogonaal staat op elke vector in subruimte $W$ van $\R^n$ dan is $z$ orthogonaal op $W$

De set van alle vectoren $z$ die orthogonaal staan op $W$ noemen we het orthogonaal complement van $W$ and dit noteren we met $W^{\perp}$.

De volgende eigenschappen gelden

- (Row A)$^{\perp}$ = Nul A
- (Col A)$^{\perp}$= Nul A^T^



##### Orthogonale sets

Een set vectoren $\{u_1,...,u_p\}$ in $\R^n$ is een orthogonale set als elk distinct paar vectoren uit de set orthogonaal is. Dus voor elk paar vector uit de geldt: $u.v=0$



##### Orthogonale basis

Een orthogonale basis for een subspace $W$ in $\R^n$ is een basis voor $W$ dat ook een orthogonale set is. 

Stel we willen een bepaalde vector $y$ schrijven als de lineaire combinatie van de vectoren in een subspace $W$. Dan kunnen we dat aan de hand van de volgende eigenschap

$y=c_1u_1+...+c_pu_p$

waar

$c_j=\frac{y.u_j}{u_j.u_j}$ (met j = 1,...,p)



##### Orthogonale projectie

Een orthogonale projectie is in essentie het pro jecteren van een vector op een andere vector zodat de projectie orthogonaal is op een subspace. Dit wordt gegeven door:

$\hat{y} = $ proj$_Ly=\frac{y.u}{u.u}u$ 



##### Gram-Schmidt process

Gegeven een basis $\{x_1,...,x_p\}$ voor een niet-nul subspace $W$ van $\R^n$, definieer

- $v_1=x_1$
- $v_2=x_2-\frac{x_2.v_1}{v_1.v_1}v_1$
- $v_3=x_3-\frac{x_3.v_1}{v_1.v_1}v_1-\frac{x_3.v_2}{v_2.v_2}v_2$
- ...
- $v_p=x_p-\frac{x_p.v_1}{v_1.v_1}v_1-\frac{x_p.v_2}{v_2.v_2}v_2-...-\frac{x_p.v_{p-1}}{v_{p-1}.v_{p-1}}v_{p-1}$

Dan is $\{v_1,...,v_p\}$ een orthogonale basis voor $W$

Stel we krijgen de vraag om een orthogonale basis te berekenen voor een bepaalde deelruimte $W$ van $\R^3$

$W= span\{\begin{bmatrix}0\\2 \\ 2 \end{bmatrix}\,\begin{bmatrix}6\\6 \\ -4 \end{bmatrix}\}$

Dan is de eerste vector van die basis simpelweg $x_1$. m.a.w. $v_1=x_1$. Nu berekenen we ook nog de tweede vector
$v_2=x_2-\frac{x_2.v_1}{v_1.v_1}v_1=\begin{bmatrix}6\\6 \\ -4 \end{bmatrix}-\frac{4}{8}\begin{bmatrix}0\\2 \\ 2 \end{bmatrix}=\begin{bmatrix}6\\5 \\ -5 \end{bmatrix}$

Dus is onze orthogonale basis voor $W$, $\{{\begin{bmatrix}0\\2 \\ 2 \end{bmatrix}\,\begin{bmatrix}6\\5 \\ -5 \end{bmatrix}\}}$

#### Diagonalisatie (extended)

Als $A$ een $m \times n$ matrix met lineair onafhankelijke kolommen is, dan kan $A$ gefactoriseerd worden als $A=QR$, waar $Q$ een $m \times n$ matrix is waarvan de kolommen een orthonormale basis vormen voor $Col~A$ en $R$ is een $n \times n$ upper driehoek inverteerbare matrix met positieve entries op zijn diagonaal.

#### Belangrijk voor examen

- Exercise 14,15,16, 17 oefenbundel 3 herbekijken
- 