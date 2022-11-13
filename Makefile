
CC=gcc
CFLAGS=-O0 -g -Wall -std=gnu11 
INCLUDES=-I.
LIBS=-lm

SRCS=app.c dhc.c
OBJS = $(SRCS:.c=.o)
MAIN = app
MAIN_LIB = dhc_lib.so

SRCS_AD=audio_demo.c dhc.c
OBJS_AD = $(SRCS_AD:.c=.o)
MAIN_AD = audio_demo

.PHONY: depend clean

all: $(MAIN) $(MAIN_AD)
	@echo  Done

$(MAIN_AD): $(OBJS_AD) 
	$(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN_AD) $(OBJS_AD) $(LIBS)

$(MAIN): $(OBJS) 
	$(CC) $(CFLAGS) $(INCLUDES) -o $(MAIN) $(OBJS) $(LIBS) 

.c.o:
	$(CC) $(CFLAGS) $(INCLUDES) -c $<  -o $@

lib:
	$(CC) $(CFLAGS) $(INCLUDES) -shared -fPIC -o $(MAIN_LIB) dhc.c
	cp $(MAIN_LIB) ./python_bindings/

clean:
	$(RM) *.o *~ $(MAIN) $(MAIN_AD) $(MAIN_LIB)

depend: $(SRCS)
	makedepend $(INCLUDES) $^


