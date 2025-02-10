
#include <pthread.h>
#include <unistd.h>
#include <iostream>
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond_consumer = PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_producer = PTHREAD_COND_INITIALIZER;
int number = 0;
int sleepTime = 0;
int value = 0;
int ready = 0;
int finish = 0;
int debugFlag = 0;

int get_tid(pthread_t nowThread, pthread_t* TSL) {
  int result = 0;
  for (int i = 0; i < number + 3; ++i) {
    if (TSL[i] == nowThread) {
      result = i;
      break;
    }
  }
  return result;
}

void* producer_routine(void* arg) {
  pthread_t now = pthread_self();
  int tid = get_tid(now, (pthread_t*)arg);
  while (scanf("%d", &value) > 0) {
    if (debugFlag) {
      std::cout << "( tid:" << tid << " ,set value:" << value << ")\n"
                << std::endl;
    }
    pthread_mutex_lock(&mutex);
    //        std::cout<<"get lock "<<pthread_self()<<'\n'<<std::endl;
    //        std::cin>>value;
    if (value == 0) {
      break;
    }
    //        std::cout<<"set number "<<value<<'\n'<<std::endl;
    pthread_cond_signal(&cond_consumer);
    ready = 1;
    while (ready) {
      pthread_cond_wait(&cond_producer, &mutex);
    }
    pthread_mutex_unlock(&mutex);
  }
  finish = 1;
  //  std::cout<<"producer thread exit "<<finish<<" "<<ready<<'\n';
  pthread_cond_signal(&cond_consumer);
  pthread_mutex_unlock(&mutex);
  pthread_exit(NULL);
  //    return NULL;
}

void* consumer_routine(void* arg) {
  pthread_t now = pthread_self();
  //  std::cout<<&now<<'\n';
  int tid = get_tid(now, (pthread_t*)arg);
  int* s = (int*)calloc(1, sizeof(int));
  pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, NULL);
  //  std::cout<<pthread_self()<<'\n'<<std::endl;
  while (1) {
    pthread_mutex_lock(&mutex);
    //    std::cout<<"get lock "<<pthread_self()<<'\n'<<std::endl;
    if (finish) {
      break;
    }
    if (!ready) {
      pthread_cond_wait(&cond_consumer, &mutex);
    }
    if (ready) {
      *s += value;
      if (debugFlag) {
        std::cout << "( tid:" << tid << " ,sum:" << *s << ")\n" << std::endl;
      }
      ready = 0;
      pthread_cond_signal(&cond_producer);
      pthread_mutex_unlock(&mutex);
      if (sleepTime == 0) {
        sleep(0);
      } else {
        sleep(rand() % sleepTime);
      }

    } else {
      pthread_cond_signal(&cond_producer);
      pthread_mutex_unlock(&mutex);
    }
  }
  //  std::cout<<pthread_self()<<" exit"<<'\n';
  pthread_cond_signal(&cond_consumer);
  pthread_mutex_unlock(&mutex);
  pthread_exit(s);
  //    return &s;
}

void* consumer_interruptor_routine(void* arg) {
  while (1) {
    if (finish) {
      break;
    }
    if (!ready) {
      int random = 3 + rand() % number;
      pthread_t thread = ((pthread_t*)arg)[random];
      if (thread != 0) {
        pthread_cancel(thread);
      }
      if (debugFlag) {
        //        std::cout<<"try to cancel
        //        "<<get_tid(((pthread_t*)arg)[random],(pthread_t*)arg)<<'\n';
      }
    }
  }

  // interrupt random consumer while producer is running
  pthread_exit(NULL);
  return NULL;
}

// the declaration of run threads can be changed as you like
int run_threads(int isDebug, int getNumber, int getSleepTime) {
  debugFlag = isDebug;
  // get the two params
  number = getNumber;
  sleepTime = getSleepTime;
  // create thread of producer
  pthread_t* TSL = (pthread_t*)calloc(3 + number, sizeof(pthread_t));
  //  std::cout<<TSL[0]<<'\n';
  pthread_create(&TSL[1], NULL, producer_routine, TSL);
  // create the thread of the interruptor
  pthread_create(&TSL[2], NULL, consumer_interruptor_routine, TSL);
  // create the consumers thread
  for (int i = 0; i < number; ++i) {
    pthread_create(&TSL[3 + i], NULL, consumer_routine, TSL);
  }
  pthread_join(TSL[1], NULL);
  int sum = 0;
  for (int i = 0; i < number; ++i) {
    void* a = NULL;
    pthread_join(TSL[3 + i], (void**)&a);
    sum += *(int*)a;
    free(a);
  }
  free(TSL);
  return sum;
}
