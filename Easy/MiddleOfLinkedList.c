//https://leetcode.com/problems/middle-of-the-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
    struct ListNode *mid = head;
    int count = 1;
    while(head != NULL){
        if(count%2==0){
            mid = mid->next;
        }
        count = count+1;
        head = head->next;
    }
    return mid;
}