#include <iostream>
#include <vector>
#include <cmath>
#include <stdexcept>


struct Node{
    int value;
    Node* next;
    Node* prev;

    Node(int n){
        value = n;
        next = nullptr;
    }

    Node(int n, Node *p){
        value = n;
        next = p;
    }
};

class LinkedList{
private:
    Node* head;
    Node* tail;

    Node *get_node(int index){
        if (index < 0 or index >= size){
            throw std::range_error("IndexError: Index out of range");
        }
        else if (head == nullptr){
            throw std::invalid_argument("List is empty");
        }

        Node *current = head;
        for (int i = 0; i < index; i++){
            current = current->next;
        }
        return current;
    }

public: 
    int size;
    LinkedList(){
        head = nullptr;
        tail = nullptr;
        size = 0;
    }
    ~LinkedList(){
        Node *current;
        Node *next;

        current = head;

        while (current != nullptr){
            next = current->next;
            delete current;
            current = next;
        }
    }
    LinkedList(std::vector < int > initial){
        head = nullptr;
        tail = nullptr;
        for (int e : initial){
            append(e);
        }
    }

    int length(){
        return size;
    }

    void append(int val){
        if (head == nullptr){
            head = new Node(val);
            size++;
            return;
        }

        // Iterate to end of list
        Node *current;
        current = head;
        while (current->next != nullptr){
            current = current->next;
        }

        // Link new node to end of list
        current->next = new Node(val);
        size++;
    }
    void print(){
        Node *current = head;
        std::cout << "[";
        while (current->next != nullptr){
            std::cout << current->value;
            std::cout << ", ";
            current = current->next;
        }
        std::cout << current->value << "]" << std::endl;
    }
    int& operator[](int index){
        return get_node(index)->value;
    }
    void insert(int val, int index){
        if (index == 0){
            push_front(val);
        }
        else {
        Node *prev = get_node(index - 1);
        Node *next = prev->next;
        prev->next = new Node(val, next);
        }
    }
    void push_front(int val){
        head = new Node(val, head);
        size++;
    }
    void remove(int index)
    {
        (void)pop(index);
    }
    int pop(int index)
    {
        Node *current = head;
        Node *prev = current->prev;

        if (index == 0){
            delete current;
            current = current -> next;
        }
        else{
        for (int i = 0; i < index; i++){
            prev = current;
            current = current->next;
        }
        prev->next = prev->next->next;
        delete current;
        size--;
        }
        int value = current->value;
        return value;
        }
    int pop(){
        pop(length());
        return 0;
    }
        
};

void test_primes()
{
    LinkedList primes;
    primes.append(2);
    primes.append(3);
    primes.append(5);
    primes.append(7);
    primes.print();
}

void test_insert(){
    LinkedList l;
    l.append(1);
    l.append(2);
    l.insert(1, 1);
    l.push_front(0);
    l.print();
}

void test_pop(){
    LinkedList l({1, 2, 3, 4, 5});
    l.remove(3);
    l.pop(1);
    l.print();
}




int main(){
    test_primes();
    test_insert();
    test_pop();
    
}