//https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if(head == NULL){
        return head;
    }

    struct ListNode* iterator = head;
    struct ListNode* temp = NULL;
    
    while(iterator->next != NULL){
        if(iterator->val == iterator->next->val){
            temp = iterator->next;
            iterator->next = iterator->next->next;
            free(temp);
        }else{
            iterator = iterator->next;
        }
    }

    return head;
}