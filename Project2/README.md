# https://github.uio.no/IN1910/H20_project2_jmsomer_anderhc

# Makefile commands
ArrayList: array_list.cpp
	c++ -std=c++11 -Wall $< -o $@

LinkList: linked_list.cpp
	c++ -std=c++11 -Wall $< -o $@

CircularLinkedList: circular_linked_list.cpp
	c++ -std=c++11 -Wall $< -o $@

# Algoritmeanalyse ved store O-notasjonen

### Get element i by index:
* LinkedList     O(n): Bruker get_node som bruker en for-løkker til å iterere
* ArrayList      O(1): Får direkte tilgand til elementet

### Insert at front:
* LinkedList     O(1): Bruker push_fron
* ArrayList      O(n): Bruker en for-løkke

### Insert at back (aka append):
* LinkedList     O(1): Append-er direkte til halen
* ArrayList      O(n): Kan bruke resize som bruker en for-løkke til å iterere

### Insert into middle of list:
* LinkedList     O(n): Bruker get_node 
* ArrayList      O(n): Bruker resize eller en for-løkke 

### Remove element from front:
* LinkedList     O(n): Bruker en for-løkke 
* ArrayList      O(n): Bruker en for-løkke

### Remove element from back:
* LinkedList     O(n): 
* ArrayList      O(n): For-løkke 

### Remove element from middle:
* LinkedList     O(n): Refererer til pop som bruker for-løkke
* ArrayList      O(n): Kopierer hele lista 

### Print:
* LinkedList     O(n): Itererer gjennom listen
* ArrayList      O(n): Itererer gjennom listen


List of exercises compiled and run:
* 1a -> j
* 2a -> d
* 4a -> c
