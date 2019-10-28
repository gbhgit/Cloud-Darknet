CC = g++
CFLAGS = -g -Wall
SRCS += src/main.cpp
PROG = script

CFLAGS_CPP= -std=c++11

$(PROG):$(SRCS)
	$(CC) $(CFLAGS_CPP) $(CFLAGS) -o $(PROG) $(SRCS)

clean:
	rm -rf $(PROG)
