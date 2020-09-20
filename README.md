# Cuckoo-Hashing--Python

Python3 Cuckoo Hash Table
- Python version 3.6
The purpose of this program is to visualize (as console) the cuckoo hashing method using different table sizes, and different number of tables.
In this program the number of tables (max 5 tables) and the size of tables (min 10 / max 30 cells) will be taken as input from the user. Also, the keys to be inserted, searched, and deleted will be taken from the user. Also the output shows total number of collisions and the load factor of each table after each insertion.

 Cuckoo hashing utilizes hash functions as much as size of table in order to minimize collisions.

Example, number of table is 2:
The hash table in this particular implementation contains 2 lists, each one using a different hash function. When inserting into a cuckoo hash table, hash the key twice to identify 2 possible "nests" (or "buckets") for the key pair. If both of its nests are already occupied, evict the occupant of 1 of the nests and then repeat the insertion step for the evicted occupant.

- This project's hash function calculates the ASCII values of the letters in a string and multiplies the ASCII value of each character by its index number. Thus, words consisting of the same letters giving the same ASCII value gives different result. Then, the id of each table is multiplied by the result, which ensures that each table has different hash functions.

Example for HASH FUNCTION:
Table size = 10
ASCII Values  [a] =97, [e] =101, [s] =115, [y]=121
Key = “ayse”
Hash Value for Table 1 = [(a*1 + y*2 + s*3 + e*4)*table_ID]%size_of_table 
                         [(97*1 + 121*2 + 115*3 + 101*4 )*1]%10 = 973%10 =3

Hash Value for Table 2 = [(97*1 + 121*2 + 115*3 + 101*4 )*2]%10 = 1946%10 =6
Key = “yase”

Hash Value for Table 1 = [(y*1 + a*2 + s*3 + e*4)*table_ID]%size_of_table
                         [(121*1 + 97*2 + 115*3 + 101*4 )*1]%10 = 949%10 =9
                         
Hash Value for Table 2 = [(121*1 + 97*2 + 115*3 + 101*4 )*2]%10 = 1898%10 =8

As seen in the example above, the words "ayse" and "yase", which consist of the same characters, give different hash values for each table.

- Cuckoo hashing is also very efficient for searching. It has a worst case lookup time of O(1).
- Furthermore, an infinite loop may be encountered while cuckoo hashing. This occurs if there are 2 or more items that are continuously displacing one another and are never able to find a permanent position. There is a certain threshold in the code to detect these infinite loops and deal with them. In this project, threshold value equals to number of table.

For example:
Table size = 10
If there is 10 cycle, the program will warn the user for unpositioned key. “Cycle here !!”.
Load factor = number of filled cells / size of table
Collision number = If the position where a key is to be placed as a result of the hash value is full, there is a collision in that table. 

#Running the tests
$python3 cuckoohashing.py 
