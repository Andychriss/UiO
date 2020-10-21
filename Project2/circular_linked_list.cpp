#include <stdexcept>
#include <ostream>
#include <iostream>

using namespace std;

struct Node{
    int value;
    Node *next;
    Node *prev;
};

class CircLinkedList{
private:
    Node* head;
    Node* tail;

    Node *get_node(int index)
    {
        if (index < 0 or index >= size){
            throw range_error("IndexError: Index out of range");
        }
        else if (head == nullptr){
            throw invalid_argument("List is empty");
        }

        Node *current = head;
        for (int i = 0; i < index; i++){
            current = current->next;
        }
        return current;
    }

public:
    int size;

    CircLinkedList(){
        head = nullptr;
        size = 0;
    }

    CircLinkedList(int n){
        head = nullptr;
        size = 0;
        for (int i= 1; i<=n; i++){
            append(i);
        }
    }

    void append(int val){
        Node *initial = new Node;
        initial -> value = val;
        

        // Iterate to end of list
        int counter = 0;
        if (head != nullptr){
            initial -> next = head;
            Node *current = head;
            while (current->next != head){
                current = current->next;
                ++counter;
        }
        current->next = initial;
        }
        else {
            initial -> next = initial;
            head = initial;
        }
        size++;
    }
    int& operator[](int index){
        return get_node(index)->value;
    }
    void print(){
        Node *current = head;
        cout << "[";
        while (current->next != head)
        {
            cout << current->value;
            cout << ", ";
            current = current->next;
        }
        cout << current->value << "]" << std::endl;
    }
    
};



void test(){
    CircLinkedList clist;
    clist.append(0);
    clist.append(2);
    clist.append(4);
    clist.print();
}
int main(){
    test();
}