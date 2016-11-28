#include <unordered_map>

using namespace std;

class DLLNode{
public:
    DLLNode* next;
    DLLNode* prev;
    int key;
    int value;

    DLLNode(int key, int value) : next(0),
        prev(0),
        key(key),
        value(value){}
};

class DLL{
public:
    DLLNode* front;
    DLLNode* back;
    int node_count;

    DLL(): front(0), back(0), node_count(0){}

    int size(){
        return node_count;
    }

    DLLNode* push(int key, int value){
        DLLNode* node = new DLLNode(key, value);
        if(front){
            front->next = node;
            node->prev = front;
        } else { //if front doesn't exit, list is empty
            back = node;
        }
        front = node;
        node_count++;
        return front;
    }

    int pop(){
        if(!back)
            return -1;
        //return the key so the item can be
        //deleted from the hashmap.
        int ret_key = back->key;
        if(back->next){
            back = back->next;
            delete back->prev;
            back->prev = 0;
        } else { //if back has no next, list only has 1 item
            delete back;
            front = 0;
            back = 0;
        }
        node_count--;
        return ret_key;
    }

    void moveToFront(DLLNode* node){
        if(front == node || !node)
            return;

        if(node->prev){
            node->prev->next = node->next;
            node->next->prev = node->prev;
        } else {
            //if node being passed in doesn't have
            //a next, it must be the back.
            back = node->next;
            back->prev = 0;
        }

        node->prev = front;
        front->next = node;
        node->next = 0;
        front = node;
    }
};


class LRUCache{
public:
    DLL* cache_list;
    unordered_map<int, DLLNode*> cache_hash;
    const int capacity;

    LRUCache(int capacity) : capacity(capacity) {
        cache_list = new DLL();
    }

    int get(int key) {
        if(cache_hash.count(key)){
            cache_list->moveToFront(cache_hash.at(key));
            return cache_hash.at(key)->value;
        }
        return -1;
    }

    void set(int key, int value) {
        if(!cache_hash.count(key)){
            if(cache_list->size() == capacity){
                cache_hash.erase(cache_list->pop());
            }
            cache_hash[key] = cache_list->push(key, value);

        } else {
            cache_hash.at(key)->value = value;
            cache_list->moveToFront(cache_hash.at(key));
        }
    }
};
