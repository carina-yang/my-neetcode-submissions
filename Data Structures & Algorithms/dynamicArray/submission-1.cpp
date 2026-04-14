class DynamicArray {

private:
    int* arr;
    int capacity;
    int len;

public:

    DynamicArray(int capacity) {
        arr = new int[capacity];
        this->capacity = capacity;
        len = 0;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (len == capacity) {
            resize();
        }
        arr[len] = n;
        len++;
    }

    int popback() {
        len--;
        return arr[len];
    }

    void resize() {
        capacity = capacity * 2;
        int* temp_arr = new int[capacity];
        for (int i = 0; i < len; i++) {
            temp_arr[i] = arr[i];
        }
        delete[] arr;
        arr = temp_arr;
    }

    int getSize() {
        return len;
    }

    int getCapacity() {
        return capacity;
    }
};
