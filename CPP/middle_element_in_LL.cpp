// code
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow;
        ListNode* fast;
        slow=head;
        int n=1;
        while(slow->next!=NULL){
            slow=slow->next;
            n++;
        }
        slow=head;
        fast=head;
        while(fast->next!=NULL && fast->next->next!=NULL) {
            fast=fast->next->next;
            slow=slow->next;
        }
        if(n%2==0) 
            return slow->next;
        return slow;
    }
};

// question link
// https://leetcode.com/problems/middle-of-the-linked-list/