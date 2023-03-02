# Dalio, Brian A.
# dalioba
# 2023-02-15
#-----------------------------------------------------------------
CC       = gcc

SANFLAGS =

CFLAGS   = -g -Wall -Wextra $(SANFLAGS)
LDFLAGS  = $(SANFLAGS)
LDLIBS   = -lm

#-----------------------------------------------------------------
%.o : %.c
	$(CC) $(CFLAGS) -c $^

#-----------------------------------------------------------------
all : matrixTest transformsTest

matrixTest : matrix.o matrixTest.o
	$(CC) $(LDFLAGS) -o $@ matrix.o matrixTest.o $(LDLIBS)

transformsTest : matrix.o transforms.o transformsTest.o
	$(CC) $(LDFLAGS) -o $@ matrix.o transforms.o transformsTest.o $(LDLIBS)

#-----------------------------------------------------------------
clean:
	rm -f matrixTest transformsTest *.o

#-----------------------------------------------------------------
