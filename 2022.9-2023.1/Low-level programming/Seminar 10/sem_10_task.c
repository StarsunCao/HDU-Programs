#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>



#define DEFINE_LIST(type)                                               \
  typedef struct list_##type {                                          \
    type value;                                                         \
    struct list_##type* next; 											\
  }list_##type;


DEFINE_LIST(int64_t)
DEFINE_LIST(double)



#define print_list(x) \
  _Generic((x), \
           list_int64_t* : print_list_int64_t, \
           list_double* : print_list_double, \
           default : error("Unsupported operation"))(x)
		   
		   

 
#define push(x, y) \
  _Generic((x), \
           list_int64_t** : push_int64_t, \
           list_double** : push_double, \
           default : error("Unsupported operation"))(x, y)
		   
 
 
#define pop(x)                                                           \
  _Generic((x), list_int64_t**                                           \
           : pop_int64_t, list_double**                               \
           : pop_double, default                                      \
           : error("Unsupported operation"))(x)
		   
 

void error(const char *s) {
  fprintf(stderr, "%s", s);
  abort();
}


void push_int64_t(list_int64_t **head, int64_t data) {
    list_int64_t *tmp = (list_int64_t*) malloc(sizeof(list_int64_t));
    tmp->value = data;
    tmp->next = (*head);
    (*head) = tmp;
}


void push_double(list_double **head, double data) {
	list_double *tmp = (list_double*) malloc(sizeof(list_double));
    tmp->value = data;
    tmp->next = (*head);
    (*head) = tmp;
}

int pop_int64_t(list_int64_t **head) {
    list_int64_t* prev = NULL;
    int val;
    if (head == NULL) {
        exit(-1);
    }
    prev = (*head);
    val = prev->value;
    (*head) = (*head)->next;
    free(prev);
    return val;
}

int pop_double(list_double **head) {
    list_double* prev = NULL;
    int val;
    if (head == NULL) {
        exit(-1);
    }
    prev = (*head);
    val = prev->value;
    (*head) = (*head)->next;
    free(prev);
    return val;
}

void print_list_int64_t(list_int64_t *head) {
	    while (head) {
        printf("% " PRId64, head->value);
        head = head->next;
    }
    printf("\n");
}

void print_list_double(list_double *head) {
		while (head) {
         printf("%lf", head->value);
        head = head->next;
    }
    printf("\n");
}


int main(){
	
	// creating first linked list
	
	list_int64_t* head1 = NULL;
	int64_t x = 42;
	
	// adding values to first linked list
	push(&head1, x);
	push(&head1, 2*x);
	push(&head1, 8*x);
	
	print_list(head1);	
	// removing value from first linked list
	pop(&head1);
	print_list(head1);

	
	// creating second linked list
	
	list_double* head2 = NULL;
	double y = 42.5;
	
	// adding values to second linked list
	push(&head2, y);
	push(&head2, 2*y);
	push(&head2, 8*y);
	
	print_list(head2);	
	// removing value from second linked list
	pop(&head2);
	print_list(head2);	


	
	return 0;
}
