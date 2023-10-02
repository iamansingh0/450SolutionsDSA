// code

class Solution
{
    public:
    //Function to check if the linked list has a loop.
    bool detectLoop(Node* head)
    {
        if(head->next == NULL) return false;
        // your code here
        unordered_set<Node* > st;
        Node* temp = head;
        while(temp) {
            if(st.find(temp) != st.end()) return true;
            st.insert(temp);
            temp=temp->next;
        }
        return false;
    }
};

// question link:
// https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list