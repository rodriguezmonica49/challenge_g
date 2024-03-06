--Challlenge 2 Result 1
drop table results1

SELECT department, job, [Q1], [Q2], [Q3], [Q4]
into results1
FROM  
    (SELECT d.[1] department, j.[1] job, concat( 'Q', datepart(quarter, e.[2])) Quarter, e.[0] employ
  FROM [Globant].[dbo].employees e
  left join jobs j on j.[0] = e.[4]
  left join departments d on d.[0]= e.[3]
  where year(e.[2]) = 2021
	 )   
    AS Sourcetable  
PIVOT
(
  count(employ)
  FOR Quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS PivotTable
order by department, job;
  