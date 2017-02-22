## Hash

- Every key has a hashcode, for the simplest version of hash table, each hashcode occupies a bracket. The value of that key is stored in such bracket.

  For example, for each word, the word itself is the key and the definition of that word is the value storing in the bracket.

  But such hash table has one problem that we may not have enough memory for such a huge hash table which map each word into a bracket.

- In order to solve this problem, we implement some method to compress the hashcode, for example:

  h(hashcode) = hashcode mod N

  where N is the actual capacity of our hash table. However, in this instance, we may suffer some other problem:

  h(hashcode1) = h(hashcode2)

  This is so called **"COLLISION"**

- Insert ()

  - compute the key's hash code

  - compress it to determine bucket

  - insert the entry into buckets chain.

    ​

- find()

  - hash the key

  - find the compressed index and find the bucket

  - find the key in the Linked list storing in that bucket.

  - if you find you key before reach the tail of the linked list, you return the value. Otherwise you return null

    ​

- remove()

  - hash the key

  - search the chain

  - remove from the linked list if found

  - return the Entry or null

    ​

- if your key have multiple value:

  - G&T: insert both; find() will return arbitrarily.
  - Replace old value with new one. find() will only return the new one.

- **Don't change your object after inserted into the hash table, **

- We implement **random** not for random choosing the bucket for a particular key. But for the first time of assigning a bucket for a key. Which means, after the first assignment, the key will always be mapped into a certain bucket.

- Compression functions:

  - ​