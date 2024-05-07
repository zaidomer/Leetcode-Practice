// https://leetcode.com/problems/palindrome-linked-list/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // bool isPalindrome(ListNode* head) {    
    //     std::stack<int> stack; 
    //     ListNode* temp = head;
        
    //     while(temp != nullptr){
    //         stack.push(temp->val);
    //         temp = temp->next;
    //     }

    //     while(!stack.empty()){
    //         if(stack.top()!=head->val){
    //             return false;
    //         }
    //         stack.pop();
    //         head = head->next;
    //     }
    //     return true;
    // }

    ListNode *reverse(ListNode * head){
        ListNode* newHead = nullptr;
        ListNode* current = head;
        ListNode* temp = nullptr;

        while(current != nullptr){
            temp = newHead;
            newHead = current;
            current = current->next;
            newHead->next = temp;
        }

        return newHead;
    }

    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return true;
        }    
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast !=NULL && fast->next !=NULL){
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode *reverseHead = reverse(slow);
        ListNode *temp1 = head;
        ListNode *temp2 = reverseHead;
        while(temp2!=NULL){
            if(temp1->val != temp2->val){
                return false;
            }

            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        return true;
    }
};