# what is the story?
I am going to make this program for a shop that cut steel for customers and needs a system to inventory steel. actually, it needs a subsystem for its business. 
so he has software that makes a nesting for cut steel and the software make a CVS file for a list of part name and rest of steels. and he needs a system for inventory of the rest of the steels to re-use. 
and also the program has to show if a part has been cut for a second time to avoid duplication. 
see below for an example of a nesting shape.
 
![image](https://user-images.githubusercontent.com/58405807/123320842-e93c8400-d4f7-11eb-8e29-48db37c4ec98.png)


Every nesting might have one or more rest steel(partial plate) and it is square or rectangle that has a length and width.

Below is the first revision of ER. 

![image](https://user-images.githubusercontent.com/58405807/123320379-47b53280-d4f7-11eb-869c-3336b119dd64.png)

But when I made it, I found it “rest steel” and “steel” should be the same. But if it is the same, it should be many-to-many relation. So I added a property between nesting and steel that shows what is the relation between those.
 
![image](https://user-images.githubusercontent.com/58405807/123320407-4edc4080-d4f7-11eb-9d22-b9eef5e764c6.png)
PostgresDB has used for the database and Pgadmin4 used to manage it. 
![Screenshot from 2021-06-29 12-47-40](https://user-images.githubusercontent.com/58405807/123846664-47dc7600-d8db-11eb-8a7c-d88d2267272d.png)
backup of the database has made. it is easy to restore it with pgadmin4. 
/database-backup/steel_inventory.tar



