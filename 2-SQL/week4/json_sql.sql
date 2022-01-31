--Let's begin by selecting a sample of 50 rows from the moma_artists table. This will give us a sense of the kind of data we are dealing with. 
SELECT * FROM moma_artists LIMIT 50;

--or example, let's examine what it looks like to format the info column using the jsonb_pretty() function.
SELECT jsonb_pretty(info) AS formatted_info
FROM moma_artists LIMIT 50;

-- Let's go ahead and grab those two fields for every artist. 
-- In order to access properties of the JSONB field, we must use arrow operators. 
-- Since these fields are both at the top level, we can use the basic arrow operator to key into the desired values, as shown below.

SELECT
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
ORDER BY id
LIMIT 50;


-- In order to query for American artists only, we'll have to provide a filter using a WHERE clause. 
-- However, there's a catch: We can't directly compare a JSONB value to a string.
-- Instead, we will first need to convert the JSONB value to string using the accessor operator with the double arrow head. 
-- That way, we can compare the extracted text value to the 'American' string literal.
-- To do this, update the query as follows:

SELECT
info -> 'display_name' AS name,
info -> 'nationality' AS nationality
FROM moma_artists
WHERE info ->> 'nationality' = 'American'
ORDER BY id
LIMIT 50;

-- As a final exercise, we will practice inserting JSON values.
-- The id column of moma_artists is of type SERIAL and will self-populate with an auto-incremented number when we insert a record.
-- So we just need to focus on the info column for this exercise.
-- Recall the jsonb_object function and the various forms it takes from the previous lesson. 
-- Choose one of these forms below to implement an INSERT statement that creates a new artist entry that contains a display_name and a nationality.
-- ONLY CHOOSE ONE of the three INSERT statements below - do not use them all:


INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, Ablade Glover, nationality, Ghanaian}')
);

INSERT INTO moma_artists (info) VALUES (
    json_object('{{display_name, Ablade Glover}, {nationality, Ghanaian}}')
);
INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, nationality}', '{Ablade Glover, Ghanaian}')
);
-- These three queries produce the same result, using each form of the json_object function. 
-- There is no benefit in choosing one over the other in a technical sense, so feel free to pick whichever you find easiest to understand. 
-- After you run the query, let's verify the row was inserted.
-- To do this, we'll write a query that orders the rows by IDs in descending order
SELECT info FROM moma_artists ORDER BY id DESC LIMIT 1;