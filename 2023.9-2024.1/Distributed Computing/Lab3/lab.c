#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

#include "message.h"
#include "log.h"
#include "process.h"
#include "banking.h"

/** Value of this variable is unique for each process
 * Students can use it for implementation of Lamport's clock or remove it
 */
int lamport_time = 0;

void parent_work(int count_nodes)
{
    AllHistory all_history;
    all_history.s_history_len = count_nodes - 1;

    /* STUDENT IMPLEMENTATION STARTED */
    /* Implement starting synchronization */


    /* Useful work */
    bank_operations(count_nodes - 1);

    /* Implement finishing synchronization and collecting AllHistory */
}

void child_work(struct child_arguments args)
{
    /* Child arguments */
    local_id self_id = args.self_id;
    int count_nodes = args.count_nodes;
    uint8_t balance = args.balance;

    /* BalanceHistory initialization */
    BalanceHistory history;
    history.s_history_len = 1;
    history.s_id = self_id;
    memset(history.s_history, 0, sizeof(history.s_history));
    history.s_history[0].s_balance = balance;
    for (int i = 0; i < MAX_T; ++i) {
        history.s_history[i].s_time = i;
    }

    /* System process identifiers used for logs */
    pid_t self_pid = getpid();
    pid_t parent_pid = getppid();

    /* STUDENT IMPLEMENTATION STARTED */
}

void transfer(local_id src, local_id dst,
              balance_t amount)
{
    TransferOrder order = {src, dst, amount};

    /* STUDENT IMPLEMENTATION STARTED */
}

/* STUDENTS SHOULD NOT CHANGE THIS FUNCTION */
__attribute__((weak)) void bank_operations(local_id max_id)
{
    for (int i = 1; i < max_id; ++i) {
        transfer(i, i + 1, i);
    }
    if (max_id > 1) {
        transfer(max_id, 1, 1);
    }
}
