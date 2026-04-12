#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void* fun(void *arg)
{
    char *id=(char*)arg;
    
    for (int i=0;i<5;i++)
    {
        printf("%s itteration=%d", i+1);
        sleep(1);
    }
}
void main()
{
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, fun, "thread1");
    pthread_create(&thread2, NULL, fun, "thread1");
    
    pthread_join(thread1, NULL);
    pthread_join(thread1, NULL);
}
