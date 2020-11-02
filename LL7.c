//Revering a linked list through Iteration Method
#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node* next;
    };
    struct node* head=NULL;
//====================================================================================
    struct node* create_ll(struct node* head){
        struct node* temp=(struct node*)malloc(sizeof(struct node*));
        struct node* t;
        scanf("%d",&temp->data);
        temp->next=NULL;
        if (head==NULL){
            head=temp;
        }
        else{
            t=head;
            while(t->next!=NULL){
                t=t->next;
            }
            t->next=temp;
        }
        return head;
    }
//=====================================================================================
    void print_ll(struct node* print){
        while(print!=NULL){
            printf("%d ",print->data);
            print=print->next;
        }
    }
//================================================================================================
    struct node* reverse_LL(struct node* head){
        struct node *prev,*temp,*next;
        temp=head;
        prev=NULL;
        while(temp!=NULL){
            next=temp->next;
            temp->next=prev;
            prev=temp;
            temp=next;
        }   
        head=prev;
        return (head);
    }    
int main(){
     int nodes,count=0;
    printf("Enter the Number of nodes that you want to create:");
    scanf("%d",&nodes);
    while(count<nodes){
        head=create_ll(head);
        count++;
    }
    printf("List is :");
    print_ll(head);
    printf("\n");
    head=reverse_LL(head);
    printf("Reversed List is by Iteration :");
    print_ll(head);
    printf("\n");

    return 0;
}
