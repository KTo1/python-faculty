#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/*
To compile:
$ gcc echo7.c -o echo7
To start
$ ./echo7
To connect
$ telnet 127.0.0.1 7
*/

int main()
{
    char buf[2048];
    int bytes_read;
    int sock, listener;
    struct sockaddr_in addr;
    struct sockaddr_in client;
    listener = socket(AF_INET, SOCK_STREAM, 0);
    if(listener < 0)
    {
        perror("socket");
        exit(1);
    }
    addr.sin_family = AF_INET;
    addr.sin_port = htons(7); //# 0x0007  0x0700
    addr.sin_addr.s_addr=htonl(INADDR_ANY);
    if(bind(listener, (struct sockaddr *)&addr, sizeof(addr)) < 0)
    {
        perror("bind");
        exit(2);
    }
    printf("The server is up and running.\n");
    listen(listener, 1);
    while(1)
    {
        size_t size = INET_ADDRSTRLEN;
        sock = accept(listener, (struct sockaddr *)&client, &size);
        if(sock < 0)
        {
            perror("accept");
            exit(3);
        }
        if (!fork())
        {
                        close(listener);
                char name[INET_ADDRSTRLEN];
                char port[6];
                char hello[81];
                sprintf(name, "%s", inet_ntoa(client.sin_addr));
                        sprintf(port, "%d", ntohs(client.sin_port));
                        sprintf(hello, "Echo server. Hello, %s:%s. Type your messages below:\n", name, port);
                        send(sock, hello, strlen(hello), 0);
                        while(1)
                        {
                                printf("\nAwaiting bytes from a client...\n");
                                bytes_read = recv(sock, buf, 2048, 0);
                                if(bytes_read <= 0)
                                {
                                        printf("%s:%s disconnected.\n", name, port);
                                        break;
                                }
                                printf("Received: %d bytes\tFrom: %s:%s\tMessage:\n%s", bytes_read, name, port, buf);
                                printf("Sending the message back to %s:%s...\n", name, port);
                                send(sock, buf, bytes_read, 0);
                                memset(buf, 0, bytes_read);  // bugfix: clear the received bytes from the buffer
                        }
                        close(sock);
                        exit(0);
        }
    }
    return 0;
}
