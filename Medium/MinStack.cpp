// https://leetcode.com/problems/min-stack/description/

class MinStack
{

public:
    typedef struct Node
    {
        int val;
        Node *next;
        int minUpToNow;
    } Node;

    MinStack()
    {
        topNode = nullptr;
    }

    void push(int val)
    {
        if (topNode == nullptr)
        {
            topNode = new Node;
            topNode->val = val;
            topNode->next = nullptr;
            topNode->minUpToNow = val;
        }
        else
        {
            Node *temp = new Node;
            temp->val = val;
            temp->next = topNode;
            temp->minUpToNow = std::min(val, topNode->minUpToNow);
            topNode = temp;
        }
    }

    void pop()
    {
        Node *temp = topNode;
        topNode = topNode->next;
        delete temp;
        temp = nullptr;
    }

    int top()
    {
        return topNode->val;
    }

    int getMin()
    {
        return topNode->minUpToNow;
    }

private:
    Node *topNode;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */