-- Drop and create the tables for Books and Authors Catalog Database. 

-- Switch to the book database.
USE `book`;

-- Drop the table if it exists.
DROP TABLE IF EXISTS `Books_Table`;

-- Create the table
CREATE TABLE IF NOT EXISTS `Books_Table`(
    `Book_ID` int(9) NOT NULL,
    `Title` varchar(150) NOT NULL,
    `Genre` varchar(100) NOT NULL,
    `Publication_Year` YEAR,
    `ISBN` varchar(20) UNIQUE
);

-- Designate the 'Book_ID` column as the primary key.
ALTER TABLE `Books_Table`
    ADD PRIMARY KEY(`Book_ID`);

-- Make `Book_ID` column auto increment on inserts.
ALTER TABLE `Books_Table`
    MODIFY `Book_ID` int(9) NOT NULL AUTO_INCREMENT;

-- Drop the `Authors_Table` if it exists.
DROP TABLE IF EXISTS `Authors_Table`;

-- Create `Authors_Table`.
CREATE TABLE `Authors_Table` (
    `Author_ID` int(9) NOT NULL,
    `First_Name` varchar(100) NOT NULL,
    `Last_Name` varchar(100) NOT NULL,
    `Birth_Year` YEAR,
    `Country` varchar(100) NOT NULL
);

-- Make the `Author_ID` the primary key.
ALTER TABLE `Authors_Table`
    ADD PRIMARY KEY(`Author_ID`);

-- Make `Author_ID` column auto increment on inserts.
ALTER TABLE `Authors_Table`
    MODIFY `Author_ID` int(9) NOT NULL AUTO_INCREMENT;

-- Drop the `Books_Authors_XREF` if it exists.
DROP TABLE IF EXISTS `Books_Authors_XREF`;

-- Create the `Books_Authors_XREF` table.
CREATE TABLE IF NOT EXISTS `Books_Authors_XREF` (
    bookID int(9) NOT NULL,
    authorID int(9) NOT NULL,
    PRIMARY KEY (bookID, authorID),
    FOREIGN KEY (bookID) REFERENCES Books_Table(Book_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (authorID) REFERENCES Authors_Table(Author_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


