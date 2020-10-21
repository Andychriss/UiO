#include <iostream>
#include <cmath>
#include <stdexcept>
#include <vector>
#include <math.h>

using namespace std;

class ArrayList{
private:
    int *data;
    int capacity;

    void resize(){
        capacity *= 2;
        int *tmp = new int[capacity];
        for (int i = 0; i < size; i++){
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    }

public:
    int size;
    ArrayList(){
        size = 0;
        capacity = 1;
        data = new int[capacity];
    }
    ~ArrayList(){
        delete[] data;
    }
    ArrayList(vector<int> initial){
        size = 0;
        capacity = initial.size();
        data = new int[capacity];

        for (int e : initial){
            append(e);
        }
    }
    int length(){
        return size;
    }
    void append(int n) {
        if (size >= capacity){
            resize();
        }
        data[size] = n;
        size ++;
        
        }
    void print() {
        cout << "[";
        if (size > 0) {
            cout << data[0];
        }
        for (int i = 1; i < size; i++) {
            cout << ", " << data [i];
        }
        cout << "]" << endl;
        cout << capacity << endl;
        }

    int& get(int i) {
        if ((0 <= i) and (i < size)) {
            return data[i];
                }
            else {
                throw range_error("Index out of range");
            }
        }
    int& operator[](int i){
            if (0 <= i and i < size){
                return data[i];
            }
            else{
                throw out_of_range("IndexError");
            }
        }
    void insert(int val, int index){
        if (size >= capacity){
            resize();
        }
        for (int i = 0; i < size - index; ++i){
            data[size - i] = data[size - i - 1];
            }
            size = size + 1;
            if (index <= size)
                data[index] = val;
                else{
                    throw range_error("Index is not in list");
                }
            }
    void remove(int index){
        for (int i = 0; i < size - index; ++i) {
            data[index + i] = data[index + i + 1];
        }
        size = size - 1;
        if (size > 0.25 * capacity)
            shrink_to_fit();
    }

    int pop(int index){
        remove(index);
        return data[index];
        if (size > 0.25 * capacity)
            shrink_to_fit();
    }
    int pop(){
        remove(size);
        return data[size];
        if (size > 0.25 * capacity)
            shrink_to_fit();
    }
    void shrink_to_fit()
    {
        int exponent = ceil(log2(size));
        capacity = pow(2, exponent);
        int *tmp = new int[capacity];
        for (int i = 0; i < size; i++)
        {
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    }
};

bool is_prime(int n){
    if (n == 1){
        return false;
    }
    for (int i = 2; i < n; i++){
        if (n % i == 0){
            return false;
            }
        }
    return true;
}

ArrayList find_primes(int n){
    ArrayList primes;
    int primes_found = 0;
    int i = 2;
    while (primes_found < 10){
        if (is_prime(i)){
            primes.append(i);
            primes_found++;
        }
        i++;
    }
    primes.print();
    return primes;
}

void test_print(){
    ArrayList l({1, 2, 3});
    l.print();
    cout << l[1] << endl;
    }
void test_insert(){
    ArrayList l({1, 2, 3, 4, 5});
    for (int i = 0; i < 10; i++){
        l.insert(4, 2);
        l.print();
        }
    };
void test_shrink(){
    ArrayList l({1, 2, 3, 4, 5});
    l.print();
    for (int i = 0; i < 100; i++){
        l.insert(2, 2);
        }
        l.print();
        for (int i = 0; i < 100; i++)
        {
            l.remove(1);
        
        }
        l.shrink_to_fit();
        l.print();
    }

int main(){
    //find_primes(30);
    //(test_print();
    //test_insert();
    test_shrink();
};