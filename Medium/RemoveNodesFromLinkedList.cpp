//https://leetcode.com/problems/remove-nodes-from-linked-list/description/

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
    ListNode* removeNodes(ListNode* head) {
        ListNode* reverseHead = reverse(head);
        ListNode* newHead = reverseHead;

        while(reverseHead != nullptr){
            while((reverseHead->next != nullptr) && (reverseHead->next->val < reverseHead->val)){
                reverseHead->next = reverseHead->next->next;
            }
            reverseHead = reverseHead->next;
        }

        return reverse(newHead);
    }

    ListNode* reverse(ListNode* head){
        ListNode* newList = nullptr;
        ListNode* current = head;
        ListNode* next = nullptr;

        while(current != nullptr){
            next = current->next;
            current->next = newList;
            newList = current;
            current = next;
        }

        return newList;
    }
};