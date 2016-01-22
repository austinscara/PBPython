use dbd_copy


SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
;with names as (
select pe.FirstName, 
(select COUNT(pem.EntityID) from PersonEntity pem where pem.FirstName = pe.FirstName and pem.Gender = 1) as CountOfMale,
(select COUNT(pef.EntityID) from PersonEntity pef where pef.FirstName = pe.FirstName and pef.Gender = 2) as CountOfFemale
from PersonEntity pe
where pe.Gender = 1
) 


Select DISTINCT * , 
(Select  CAST(CountOfMale as DECIMAL(7,2))/(CountOfMale+CountOfFemale))*100 as PerCentMale,
(Select  CAST(CountOfFemale as DECIMAL(7,2))/(CountOfMale+CountOfFemale))*100 as PerCentFemale
from names
Where names.FirstName not like '.' and
      names.FirstName not like '-' and
      names.FirstName not like '_DNU%'
order by names.FirstName


