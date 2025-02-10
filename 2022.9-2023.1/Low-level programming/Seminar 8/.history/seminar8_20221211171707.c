#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <sys/wait.h>
#include <sys/types.h>
int main()
{
    // pid_t is, like int, a numeric type for process IDs
    pid_t pid = fork();
    // depending on the return value that gets into pid, we will know if we are
    in the parent process or in the child.switch (pid)
    {
    case -1:
        perror("fork");
        return -1;
    case 0:
        // Child
        printf("Child: my pid = %i, returned pid = %i\n", getpid(), pid);
        break;
    default:
        // Parent
        printf("Parent: my pid = %i, returned pid = %i\n", getpid(),
               pid);
        break;
    }
    return 0;
}