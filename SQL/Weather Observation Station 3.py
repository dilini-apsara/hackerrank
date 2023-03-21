/* DISTINT statement is used to return only distinct values. */
SELECT DISTINCT city FROM station 
WHERE MOD(ID,2)=0 ;
