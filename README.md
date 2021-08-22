# Secured Database 💿
CoreX's database allows for secured data input and output. All the data that has been inputted will be safely stored using hash codes on the user's machine's memory, *creating a complete secured personal cloud only only the user can access and view*. The underlying Hashmap allows each of the user's results from the model to be saved under a custom cache, which is covered by a hash code. In other words, all the results from their use of the model will be saved under the hash code, which only can be accessed by them with a keyword. When the user first inputs a new "dataset" (financial status, fiscal year, etc), they will be prompted to type a name for that very dataset. That name will act as the key of that very dataset, which will allow the user to access that very dataset. No other key will work as the key will be saved under a hashcode, which is saves the dataset under it.

If users update their websites, when they view the log of the website, they will see all the results, dates, and updates made from them and the model. Moreover, users also have the ability to delete a website and the information embedded if they watn to. 


# Controls 🕹
 - `/feedback`: To update information about about your design (or add the website to the program if first time)
 - `/view_versions`: To see a log of past updates and reports of the website
 - `/delete`: To completely delete a design from the program
 - `/quit`: Quits the database 

Any other command that does not match the commands above, will result in the program outputting: `That command does not seem valid`. 


# More Info 📕
Each entry inputted by the user will be stored under a hashcode. 

The hashcodes are created by splitting the input into bytes and summing them. The index for the hashmap to store it under the hashcode it self is calculated by taking the *mod* of the array size.

The max amount of website analyses, and designs the user can have saved under the database is 1000.

  ## Time Complexities 📊
  Hashing Inputs (`.hash()`): `O(1)`
  Compreesing the Hashcode `.compressor()`: `O(1)`
  Setting the Input under a compressed hashcode `.setter() | /feedback`: `O(1)`
  Retrieving a value from the Hashmap `.retrieve()`: `O(1) | /view_versions`
  Deleting a website or its information from the database `.delete() | /delete`: `O(1)`

 Made in Python 🐍
