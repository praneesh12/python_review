/*  Consider a table, Quotes, with the following columns:
-dealer_name
-instrument
-price_quote
-quote_date
*/

/* (a) Write a query that, for each instrument, returns the record with
 lowest quote received today. */

SELECT MIN(price_quote), instrument 
FROM Quotes 
WHERE DATE_FORMAT(quote_date, '%Y-%m-%d') = CURDATE()
GROUP BY instrument;


/* (b) Write a query that returns the 10 quotes with the 10 
 lowest prices recorded for today. */

SELECT TOP 10 price_quote 
FROM Quotes 
WHERE DATE_FORMAT(quote_date, '%Y-%m-%d') = CURDATE()
ORDER BY price_quote;