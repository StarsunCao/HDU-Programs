%birth(father,mother,child,gender,year)

birth(yunba,yunma,yunmian,male,1939).
birth(yunba,yunma,yunyou,male,1941).
birth(yunba,yunma,yunfu,male,1943).
birth(chenba,linma,guiqin,female,1943).
birth(chenfu,linmu,qingguo,male,1944).
birth(linba,chenmu,lin,female,1946).
birth(yunyou,guiqin,xuelian,female,1965).
birth(yunyou,guiqin,xuefang,female,1967).
birth(yunyou,guiqin,fangyi,male,1971).
birth(qingguo,lin,minhua,female,1973).
birth(qingguo,lin,chenjie,male,1976).
birth(guihua,xuelian,honglu,female,1988).
birth(yanggen,xuefang,zixiang,male,1995).
birth(fangyi,minhua,xinyang,male,2001).
birth(chenjie,yiyi,yujia,male,2003).
birth(chenyan,honglu,zhilun,male,2012).
birth(zixiang,chenlin,haochen,male,2015).

%marriage(husband,wife,year)

marriage(yunba,yunma,1938).
marriage(chenba,linma,1940).
marriage(chenfu,linmu,1941).
marriage(linba,chenmu,1943).
marriage(yunyou,guiqin,1961).
marriage(qingguo,lin,1965).
marriage(guihua,xuelian,1986).
marriage(yanggen,xuefang,1990).
marriage(fangyi,minhua,1999).
marriage(chenjie,yiyi,2000).
marriage(chenyan,honglu,2010).
marriage(zixiang,chenlin,2013).

%divorce(husband,wife,year)

divorce(chenfu,linmu,1976).

%death(X,year)

death(chenfu,1990).
death(yunba,1994).
death(chenba,1999).
death(linba,2003).
death(yunma,2009).
death(chenmu,2013).

%rules

father(X,Y) :- birth(X,_,Y,_,_).
mother(X,Y) :- birth(_,X,Y,_,_).
male(X) :- birth(_,_,X,male,_).
female(X) :- birth(_,_,X,female,_).
son(X,Y) :- father(Y,X),male(X),!.
son(X,Y) :- mother(Y,X),male(X).
daughter(X,Y) :- father(Y,X),female(X),!.
daughter(X,Y) :- mother(Y,X),female(X).
brother(X,Y) :- father(Z,X), father(Z,Y), male(X), X\=Y,!.
brother(X,Y) :- mother(Z,X), mother(Z,Y), male(X), X\=Y.
sister(X,Y) :- father(Z,X), father(Z,Y), female(X), X\=Y,!.
sister(X,Y) :- mother(Z,X), mother(Z,Y), female(X), X\=Y.
younger_brother(X,Y) :- brother(X,Y), birth(_,_,X,_,Y1), birth(_,_,Y,_,Y2), Y1 < Y2.
elder_brother(X,Y) :- brother(X,Y), birth(_,_,X,_,Y1), birth(_,_,Y,_,Y2), Y1 > Y2.
younger_sister(X,Y) :- sister(X,Y), birth(_,_,X,_,Y1), birth(_,_,Y,_,Y2), Y1 < Y2.
elder_sister(X,Y) :- sister(X,Y), birth(_,_,X,_,Y1), birth(_,_,Y,_,Y2), Y1 > Y2.
grandfather(X,Y) :- father(X,Z), father(Z,Y),!.
grandfather(X,Y) :- father(X,Z), mother(Z,Y).
grandmother(X,Y) :- mother(X,Z), father(Z,Y),!.
grandmother(X,Y) :- mother(X,Z), mother(Z,Y).
cousin(X,Y) :- grandfather(Z,X), grandfather(Z,Y), X\=Y,!.
cousin(X,Y) :- grandmother(Z,X), grandmother(Z,Y), X\=Y.
uncle(X,Y) :- brother(Z,X), father(Z,Y),!.
uncle(X,Y) :- brother(Z,X), mother(Z,Y).
aunt(X,Y) :- sister(Z,X), father(Z,Y),!.
aunt(X,Y) :- sister(Z,X), mother(Z,Y).
nephew(X,Y) :- uncle(Y,X), male(X),!.
nephew(X,Y) :- aunt(Y,X), male(X).
niece(X,Y) :- uncle(Y,X), female(X),!.
niece(X,Y) :- aunt(Y,X), female(X).
married(X, Year) :- marriage(X,Y,YofMarriage), Year > YofMarriage,
    not(divorce(X,Y, _)), not(death(Y,_)).