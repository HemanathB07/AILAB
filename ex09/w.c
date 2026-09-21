Here is a **minimized version** of your singly linked-list code, with the search and delete issues corrected:

```
#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

struct Node* create(int d){
    struct Node *n=malloc(sizeof(struct Node));
    n->data=d;
    n->next=NULL;
    return n;
}

void insertEnd(struct Node **h,int d){
    struct Node *n=create(d),*t=*h;
    if(!*h){*h=n;return;}
    while(t->next)t=t->next;
    t->next=n;
}

void insertPos(struct Node **h,int d,int p){
    struct Node *n=create(d),*t=*h;
    if(p<0){free(n);return;}
    if(p==0){n->next=*h;*h=n;return;}
    for(int i=0;t&&i<p-1;i++)t=t->next;
    if(!t){free(n);return;}
    n->next=t->next;t->next=n;
}

int search(struct Node *h,int d){
    int p=0;
    while(h){
        if(h->data==d)return p;
        h=h->next;p++;
    }
    return -1;
}

void delete(struct Node **h,int p){
    if(!*h||p<0)return;
    struct Node *t=*h;
    if(p==0){*h=t->next;free(t);return;}
    for(int i=0;t&&i<p-1;i++)t=t->next;
    if(!t||!t->next)return;
    struct Node *x=t->next;
    t->next=x->next;
    free(x);
}

void display(struct Node *h){
    while(h){printf("%d->",h->data);h=h->next;}
    printf("NULL\n");
}

int main(){
    struct Node *head=NULL;
    int c,d,p,r;

    while(1){
        printf("\n1.Insert End\n2.Insert Position\n3.Search\n4.Delete\n5.Display\n6.Exit\n");
        printf("Enter choice: ");
        scanf("%d",&c);

        switch(c){
            case 1:
                scanf("%d",&d);
                insertEnd(&head,d);
                break;
            case 2:
                scanf("%d%d",&d,&p);
                insertPos(&head,d,p);
                break;
            case 3:
                scanf("%d",&d);
                r=search(head,d);
                printf("%d\n",r);
                break;
            case 4:
                scanf("%d",&p);
                delete(&head,p);
                break;
            case 5:
                display(head);
                break;
            case 6:
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }
}
```

 This keeps the same basic operations while removing unnecessary code and variables.
