use dbd
select *

FROM
(
SELECT *, ROW_NUMBER () OVER (PARTITION BY lvl4.[FundLPID], lvl4.[Fund ID], lvl4.[Quarters Since Close] ORDER BY lvl4.[FundLPID]) as [deduper2]

FROM
(
SELECT 

----	---- Report Date Info
lvl3.[Report Whole Date],
lvl3.[Report Date YYYY], 
lvl3.[Report Date Q],
lvl3.[Quarter Year Code Report Date],
lvl3.[Quarters Since Close],
lvl3.[Years Since Fund Close to Report Date],

----	---- Fund General Info
lvl3.[Fund ID],
lvl3.FundName,
lvl3.[Fund Type],
lvl3.[investor name],


----	---- Fund Close Date Info
lvl3.[Fund Close Date], 
lvl3.[Fund Close YYYY], 
lvl3.[Fund Close Q],
lvl3.[Global Region] ,

----	---- LP General Info
lvl3.[LP beid],
lvl3.[LP Name],

----	---- LP to Fund Specific Info
lvl3.FundLPID as [FundLPID],
lvl3.[Remaining Value],
lvl3.Contributed,
str(lvl3.[Distributed]) AS [Distributed],
lvl3.[Fund Initial Amount] as [Fund Initial Amount],
lvl3.[Returns with C D N IRR / Quarters Since Close] as [Consistency],
--ROW_NUMBER () OVER (PARTITION BY lvl3.fundname,  lvl3.[Quarter Year Code Report Date] ORDER BY lvl3.[Returns with C D N IRR / Quarters Since Close] DESC ) as [lpf duper],
----	---- add ins 
lvl3.Comitted as [Comitted]





FROM
(

SELECT *, 
CONVERT(float, lvl2.[LP Specific IRR], 4)/lvl2.[Top Return IRR] AS [Percentage of Top IRR], 
ROW_NUMBER () OVER (PARTITION BY lvl2.FundName, lvl2.[LP Name] ORDER BY lvl2.[Quarter Year Code Report Date] DESC) AS [duper]

FROM
(

SELECT  *,


(SELECT TOP 1 CONVERT(float, withirr.[Returns With C D N IRR], 4)/ CONVERT(float,(DATEDIFF(Q,infs.CloseDateActual, irrrs.ReportDate)), 4)
FROM InvestorFund infs
INNER JOIN InvestorFundLP iflp ON infs.EntityID = iflp.FundID
INNER JOIN IRRReturnsEntry irres ON iflp.EntityID = irres.FundLPID
INNER JOIN IRRReturnsReport irrrs ON irres.ReturnsReportId = irrrs.EntityID
WHERE irres.FundLPID = lvl1.fundpid
ORDER BY irrrs.ReportDate DESC)AS [Returns with C D N IRR / Quarters Since Close],


(SELECT TOP 1 irres.Irr
FROM InvestorFund infs
INNER JOIN InvestorFundLP iflp ON infs.EntityID = iflp.FundID
INNER JOIN IRRReturnsEntry irres ON iflp.EntityID = irres.FundLPID
INNER JOIN IRRReturnsReport irrrs ON irres.ReturnsReportId = irrrs.EntityID
WHERE irres.FundLPID = lvl1.fundpid
ORDER BY irrrs.ReportDate DESC) AS [Top Return IRR]


FROM (
SELECT inf.EntityID AS [Fund ID],
be2.EntityName as [investor name],
inf.FundName,

ft.Description AS [Fund Type],
CAST(inf.CloseDateActual AS DATE) AS [Fund Close Date], 
DATEPART(YYYY, inf.CloseDateActual) AS [Fund Close YYYY],
DATEPART(Q, inf.CloseDateActual) AS [Fund Close Q],
CONVERT(int, (CONVERT(varchar,DATEPART(YYYY,inf.CloseDateActual),4) + CONVERT(varchar,DATEPART(Q,inf.CloseDateActual), 1)),5) AS [Quarter Year Code Close],
inf.Amount,
inf.vintageYear,
CAST(irrr.ReportDate AS DATE) AS [Report Whole Date],
DATEPART(YYYY, irrr.ReportDate) AS [Report Date YYYY],
DATEPART(Q, irrr.ReportDate) AS [Report Date Q],
CONVERT(int, CONVERT(varchar,DATEPART(YYYY,irrr.ReportDate), 4) + CONVERT(varchar,DATEPART(Q, irrr.ReportDate),1), 5) AS [Quarter Year Code Report Date],
COALESCE(CONVERT(float,DATEDIFF(Q, inf.CloseDateActual, irrr.reportdate), 6),1) AS [Quarters Since Close],
DATEDIFF(YEAR, inf.CloseDateActual, irrr.ReportDate) AS [Years Since Fund Close to Report Date],
DATEDIFF(Q, inf.CloseDateActual, irrr.ReportDate) AS [Days Since Close],
be.EntityName AS [LP Name],
be.EntityID AS [LP beid],
irre.Irr AS [LP Specific IRR],
irre.RemainingValue/cer2.rate AS [Remaining Value],
irre.Contributed/cer2.rate AS [Contributed],
irre.Commited/cer2.rate as [Comitted],
irre.[Distributed]/cer2.rate AS [Distributed],
irre.EntityID as [entry id],
irrr.EntityID AS [report id],
irre.FundLPID AS [fundpid],
irre.Irr,
inf.Amount/cer.rate AS [Fund Initial Amount],
fc.Description AS [Fund Class],


CASE	
		WHEN es.countrycode IN (2,3,4,6,10,12,13,15,17,21,22,23,24,
								26,27,29,32,33,36,38,43,44,45,46,47,
								49,51,53,56,58,59,60,61,62,66,67,69,
								70,71,75,108,130,134,160,162,186,230,232)
		THEN 'Europe'
		WHEN es.countrycode IN (1,5,14,50, 134)
		THEN 'North America'
		WHEN es.countryCode IN (8, 11, 28, 102, 143, 196, 202, 205, 20, 31,
								72, 39, 172, 90, 161, 105, 110, 113, 34, 152, 
								167, 175, 191, 115, 99, 127, 35, 144, 48, 164, 
								57, 65, 73, 78, 20, 31, 72, 229)
		THEN 'Asia'
		WHEN es.countryCode IN (9, 55, 158, 98, 35, 168, 89, 189, 206, 159, 
								142, 154, 166, 173, 176, 179, 107, 125, 131, 
								171, 178, 183, 199, 200, 203, 208)
		THEN 'Oceania'
		WHEN es.countrycode IN (106, 25, 148, 52, 192, 201, 112, 116, 119, 
								141, 133, 136, 137, 147, 153, 155, 170, 103, 
								185, 188, 198, 117, 120, 121, 124, 182, 109, 
								118, 123, 126, 122, 129, 88, 150, 151, 156, 
								157, 163, 181, 182, 187, 190, 100, 204, 211, 
								212, 114, 146, 165, 68, 194, 239, 240, 241, 243)
		THEN 'Africa'
		WHEN es.countrycode IN (8, 81, 25, 139, 140, 40, 42, 145, 174, 180, 
								63, 195, 74, 76, 209, 210, 37, 132, 215)
		THEN 'Middle East'
		ELSE 'Rest of World'
		END AS [Global Region]

FROM InvestorFund inf
INNER JOIN InvestorFundRelation ifr ON inf.EntityID = ifr.fundId
INNER JOIN Investor i ON ifr.investorId= i.BusinessEntityID
INNER JOIN BusinessEntity be2 ON i.BusinessEntityID = be2.EntityID
INNER JOIN InvestorFundLP iflp ON inf.EntityID = iflp.FundID
INNER JOIN FundType ft ON inf.FundType = ft.ID
INNER JOIN FundClass fc ON inf.FundClass = fc.ID
INNER JOIN IRRReturnsEntry irre ON iflp.EntityID = irre.FundLPID
INNER JOIN IRRReturnsReport irrr ON irre.ReturnsReportId = irrr.EntityID
INNER JOIN LimitedPartner lp ON iflp.LimitedPartnerID = lp.EntityID
INNER JOIN BusinessEntity be ON lp.BusinessEntityId = be.EntityID
LEFT JOIN CurrencyExchangeRate cer ON cer.id = (SELECT TOP 1 cer1.id
                                                                        FROM CurrencyExchangeRate cer1 
                                                                        WHERE cer1.sourcecurrency = inf.CurrencyCode
                                                                        ORDER BY cer1.[date] DESC) 
LEFT JOIN CurrencyExchangeRate cer2 ON cer2.id = (SELECT TOP 1 cer1.id
                                                                        FROM CurrencyExchangeRate cer1 
                                                                        WHERE cer1.sourcecurrency = irre.CurrencyCodeId
                                                                        ORDER BY cer1.[date] DESC) 
                                                                        
lEFT JOIN EntitySite es ON i.BusinessEntityID = es.BusinessEntityId AND es.SiteType = 1 AND es.SiteStatus = 1
lEFT JOIN CountryCode cc ON es.countryCode = cc.ID


--- THIS IS WHERE YOU DECIDE WHICH FUNDS TO INCLUDE. CAN CUT IN PROGRAM, SO INCLUDE ALL YOU COULD WANT
WHERE inf.FundType in (2,7,11,17)

)lvl1




INNER JOIN
(SELECT irre1.FundLPID, Count(*) AS [Returns With C D N IRR]
FROM IRRReturnsEntry irre1

WHERE irre1.Contributed IS NOT NULL
AND irre1.[Distributed] IS NOT NULL
AND irre1.RemainingValue IS NOT NULL
GROUP BY irre1.FundLPID)withirr ON lvl1.fundpid = withirr.FundLPID)lvl2

WHERE lvl2.[Returns with C D N IRR / Quarters Since Close] > .8
AND lvl2.[Top Return IRR] IS NOT NULL 
AND lvl2.[Top Return IRR] > 0
AND lvl2.[Quarters Since Close] > 0)lvl3
WHERE lvl3.Contributed IS NOT NULL
AND lvl3.[Distributed] IS NOT NULL
AND lvl3.[Remaining Value] IS NOT NULL
AND lvl3.[Fund Initial Amount] IS NOT NULL
AND lvl3.Comitted IS NOT NULL
AND lvl3.Comitted > 0
)lvl4)lvl5
where lvl5.deduper2 = 1
--where lvl4.[lpf duper] = 
--and lvl3.[Fund Close YYYY] = 2014
--and lvl3.[Global Region] like 'Middle East'
--AND lvl3.duper = 1 dont use

--where lvl3.[report id] in (7377,
--12342,
--12674,
--11650,
--11295,
--11047,
--10007,
--9808,
--9583,
--8559,
--8298,
--5084,
--5032,
--110434,
--110435,
--177996,
--178240,
--204422,
--215096)

ORDER BY 8,  15, 4 desc

