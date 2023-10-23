//https://leetcode.com/problems/remove-linked-list-elements/description/

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
    ListNode* removeElements(ListNode* head, int val) {
        while(head!=nullptr && head->val == val){
            head = head->next;
        }
        ListNode* temp = head;

        // while(temp != nullptr){
        //     while((temp->next != nullptr) && (temp->next->val == val)){
        //         temp->next = temp->next->next;
        //     }
        //     temp = temp->next;
        // }
        // return head;


        ListNode* prev = head;
        while(temp != nullptr){
            if(temp->val == val){
                prev->next = temp->next;
                // delete temp;
                temp = prev->next;
            }else{
                prev = temp;
                temp = temp->next;
            }
        }
        return head;

    }
};