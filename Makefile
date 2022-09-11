
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

clean:
	$(RM) *.o *~ $(MAIN) $(MAIN_AD) $(MAIN_LIB)

depend: $(SRCS)
	makedepend $(INCLUDES) $^

# DO NOT DELETE

app.o: /usr/include/stdint.h /usr/include/stdio.h /usr/include/string.h
app.o: /usr/include/stdlib.h /usr/include/time.h /usr/include/features.h
app.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
app.o: /usr/include/math.h /usr/include/unistd.h /usr/include/getopt.h
app.o: /usr/include/assert.h dhc.h
dhc.o: /usr/include/stdint.h /usr/include/stdio.h /usr/include/string.h
dhc.o: /usr/include/unistd.h /usr/include/features.h
dhc.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
dhc.o: /usr/include/time.h /usr/include/stdlib.h dhc.h
