// /https://leetcode.com/problems/merge-two-sorted-lists/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    // if(list1==NULL){
    //     return list2;
    // }else if(list2==NULL){
    //     return list1;
    // }else{
    //     struct ListNode* main;
    //     struct ListNode* other;
    //     if(list1->val <= list2->val){
    //         main = list1;
    //         other = list2;
    //     }else{
    //         main = list2;
    //         other = list1;
    //     }

    //     struct ListNode* mainHead = main;
    //     while((other != NULL) && (mainHead != NULL)){
    //         struct ListNode* mainFuture = mainHead->next;
    //         if((mainFuture == NULL) || (mainFuture->val >= other->val)){
    //             struct ListNode* temp = malloc(sizeof(struct ListNode));
    //             temp->val = other->val;
    //             temp->next = mainFuture;
    //             mainHead->next = temp;
                
    //             other = other->next;
    //         }
    //         mainHead = mainHead->next;
    //     }
    //     return main;
    // }



    // if list1 happen to be NULL
    // we will simply return list2.
    if(list1 == NULL)
        return list2;
    
    // if list2 happen to be NULL
    // we will simply return list1.
    if(list2 == NULL)
        return list1;
    
    struct ListNode * ptr = list1;
    if(list1 -> val > list2 -> val)
    {
        ptr = list2;
        list2 = list2 -> next;
    }
    else
    {
        list1 = list1 -> next;
    }
    struct ListNode *curr = ptr;
    
    // till one of the list doesn't reaches NULL
    while(list1 &&  list2)
    {
        if(list1 -> val < list2 -> val){
            curr->next = list1;
            list1 = list1 -> next;
        }
        else{
            curr->next = list2;
            list2 = list2 -> next;
        }
        curr = curr -> next;
            
    }
    
    // adding remaining elements of bigger list.
    if(!list1)
        curr -> next = list2;
    else
        curr -> next = list1;
        
    return ptr;
}