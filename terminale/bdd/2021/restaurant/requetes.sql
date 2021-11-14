select nom
from Restaurant
join Evaluation
on Restaurant.rID = Evaluation.rID
where Evaluation.eID=1;

select E1.eID, E1.rID
from Evaluation as E1
where exists
(select *
from Evaluation as E2
where E1.rID = E2.rID and
E1.eID <> E2.eID);

select distinct W1.pseudonyme, W2.pseudonyme
from Evaluation as E1
join Evaluation as E2
on E1.rID = E2.rID
join Evaluateur as W1
on W1.eID = E1.eID
join Evaluateur as W2
on W2.eID = E2.eID
where E1.eID < E2.eID;

/*distinct utile si l'évaluateur est venu + de 2 fois
(pas clair dans l'énoncé)*/
select distinct nom, pseudonyme
from Restaurant
join Evaluation as E1
on Restaurant.rID = E1.rID
join Evaluateur
on Evaluateur.eID = E1.eID
where exists
(select *
from Evaluation as E2
where E1.rID = E2.rID and
E1.eID = E2.eID and
E1.dateEval < E2.dateEval and
E1.note < E2.note);

select pseudonyme
from Evaluateur
join Evaluation
on Evaluateur.eID = Evaluation.eID
group by Evaluation.eID
having count(Evaluation.eID) >= 4;