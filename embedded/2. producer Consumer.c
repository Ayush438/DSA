#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

#define size 5
int buffer[size];
int count=0;

pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond_full=PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_empty=PTHREAD_COND_INITIALIZER;


void* producer_fun(void *arg)
{
    char *id=(char*)arg;
    for (int i=0;i<5;i++)
    {
        pthread_mutex_lock(&mutex);
        
        while(count==size)
            pthread_cond_wait(&cond_empty, &mutex);
            
        buffer[count]=i+1;
        count++;
        printf("%s produced item=%d\n",id,i+1);
        
        pthread_cond_signal(&cond_full);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
}

void* consumer_fun(void *arg)
{
    char *id=(char*)arg;
    for (int i=0;i<5;i++)
    {
        pthread_mutex_lock(&mutex);
    
        while(count==0)
            pthread_cond_wait(&cond_full, &mutex);
     
        buffer[count]=0;
        count--;
        printf("%s consumeed item=%d\n",id,i+1);
        pthread_cond_signal(&cond_empty);
        pthread_mutex_unlock(&mutex);
        sleep(1);
    }
     
}

void main()
{
    pthread_t producer, consumer;
    pthread_create(&producer, NULL, producer_fun,"producer");
    pthread_create(&consumer, NULL, consumer_fun,"consumer");
    pthread_join(producer, NULL);
    pthread_join(consumer, NULL);
}
