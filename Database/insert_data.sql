-- Insert data into the book database.

-- Switch into the book database.
USE `book`

-- Insert data into the Books_Table.
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('The Great Gatsby', 'Literary Fiction', 1925, '9780333791035');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('One Hundred Years of Solitude', 'Epic Fiction', 1967, '9780060883287');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('In Search of Lost Time', 'Philosophical Fiction', 1913, '9781434105547');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('Frankenstein', 'Science Fiction', 1901, '978-0486282114');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('Twilight, Book 1', 'Young Adult Literature', 2005, '978-0-316-16017-9');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('Good Omens', 'Fantasy', 1990, '0-575-04800-X');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('The Talisman', 'Dark Fantasy', 1984, '978-0-670-69199-9');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('Why Nations Fail: The Origins of Power, Prosperity, and Poverty', 'Political Science', 2012, '0307719219');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('The Soul of a New Machine', 'Non-Fiction', 1981, '0316491977');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('Influence: Science and Practice', 'Psychology/Behavorial Science', 2008, '9780205609994');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('Breaking Down', 'Fantasy Fiction', 2008, '0-316-06792-X');
INSERT INTO `Books_Table` (Title, Genre, Publication_Year, ISBN)
    VALUES ('The Shining', 'Horror Fiction', 1977, '978-0-385-12167-5' );

-- Insert data into the Authors_Table.
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('F. Scott', 'Fitzgerald', 1901, 'United States');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Gabriel', 'García Márquez', 1927, 'Colombia');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Marcel', 'Proust', 1901, 'France');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Mary', 'Shelley', 1928, 'United Kingdom');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Stephenie', 'Meyer', 1973, 'United States');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Neil', 'Gaiman', 1960, 'United Kingdom');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Terry', 'Pratchett', 1948, 'United Kingdom');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Peter', 'Straub', 1943, 'United States');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Stephen', 'King', 1947, 'United States');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Daron', 'Acemoglu', 1967, 'Turkey');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('James', 'Robinson', 1960, 'United Kingdom');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Tracy', 'Kidder', 1945, 'United States');
INSERT INTO `Authors_Table` (First_Name, Last_Name, Birth_Year, Country)
    VALUES ('Robert', 'Cialdini', 1945, 'United States');

-- Insert data into the Books_Authors_XREF table.
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (1,1);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (2,2);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (3,3);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (4,4);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (5,5);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (6,6);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (6,7);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (7,8);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (7,9);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (8,10);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (8,11);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (9,12);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (10,13);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (11, 5);
INSERT INTO `Books_Authors_XREF` (bookID, authorID)
    VALUES (12,9);    



