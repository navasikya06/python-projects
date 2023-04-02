# A collection of Python projects

1. Hawkdove

A very simple ecosystem is simulated, without most of the complexities of the real world. The only active animals in our world will be birds. Each bird has a number representing its health, which starts at 100. If a bird eats, its health goes up. If it is injured, its health goes down. Birds also lose a small amount of health each unit of time. (This represents their normal rate of burning calories – a bird that doesn’t eat slowly gets less healthy over time.) If the health of a bird hits 0, it dies. If the health goes high – over 200 – then the bird reproduces. When it reproduces, its health goes down by 100, and a new bird of the same time is created.

Birds find food in one of two ways. Each time step, there are 10 units of food that are found by single birds on their own, who then get to eat the food without worry. There are also 50 units of food that are contested – one bird finds the food, but another approaches before they can eat it. In cases of contested food, each bird has two options – they can be passive or aggressive. 

Depending on what they choose, one of the following scenarios will occur:

* Two passive birds 
When both birds are passive, they will engage in displays meant to get the other bird to leave, and this will continue until one bird does so. The display costs a small amount of health for each bird, and it is random which of the birds ends up with the food.
* One aggressive and one passive bird 
If one bird is aggressive and the other is passive, the passive bird will flee and the aggressive bird will get the food.
* Two aggressive birds 
When both birds are aggressive, they will fight. One bird (chosen randomly) will win, and they will get the food. The loser instead is injured, reducing their health.

We will be modeling several types of birds. We’ll begin with hawks and doves. Hawks will always be aggressive, while doves will always be passive. Once we have that simulation working correctly, we’ll add other types of birds. Along the way we’ll get a bunch of interesting results.

2. Cipher

Three encryption schemes, each consisting of two algorithms. The first is the encryption algorithm. It takes two inputs, the plaintext, which is the readable text we want to encrypt, and the key, which is some piece of secret information that we need to do the encryption. The output of the encryption algorithm is called the ciphertext, and it is the encrypted message, supposedly unreadable by an adversary. The second algorithm is the decryption algorithm. It takes as input a ciphertext and a key. If the key is the same key that was used to create the ciphertext, then the decryption algorithm should output the original plaintext.

There are also algorithms for breaking a given encryption system. A break (or attack) is an algorithm that can recover the plaintext from a ciphertext without knowledge of the secret key.

* A working Caesar cipher
* A working Vigenère cipher
* A working substitution cipher
