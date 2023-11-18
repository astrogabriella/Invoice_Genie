CREATE TABLE clients (
client_id INTEGER PRIMARY KEY,
client_fname VARCHAR(225),
client_lname VARCHAR(225),
client_rate INTEGER,
total_hours INTEGER,
amount_paid INTEGER,
balance INTEGER
);

INSERT INTO clients (client_id, client_fname, client_lname, client_rate, total_hours, amount_paid, balance) VALUES
(1, 'John', 'Bib', 20, 40, 450, 800),
(2, 'Jane', 'Plop', 25, 30,  750, 750),
(3, 'Bob', 'Gib', 18, 50,  123, 900),
(4, 'Alice', 'Vib',22, 35,  890, 770);