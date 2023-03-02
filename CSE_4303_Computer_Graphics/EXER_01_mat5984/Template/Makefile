# Dalio, Brian A.
# dalioba
# 2022-08-22
#-----------------------------------------------------------------
CC       = gcc

SANFLAGS = -fsanitize=address

CFLAGS   = -g -Wall -Wextra $(SANFLAGS)
LDFLAGS  = $(SANFLAGS)
LDLIBS   = -lm

#-----------------------------------------------------------------
%.o : %.c
	$(CC) $(CFLAGS) -c $^

#-----------------------------------------------------------------
matrixTest : matrix.o matrixTest.o
	$(CC) $(LDFLAGS) -o $@ matrix.o matrixTest.o $(LDLIBS)

#-----------------------------------------------------------------
clean:
	rm -f matrixTest *.o

#-----------------------------------------------------------------
