//Minh Trinh
//1001705984
//C Standard 99
//Linux

#include <stdio.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

long traverse(char *direct)
{
    long sum = 0;

    DIR *dir;
    struct dirent *entry;
    struct stat pathStat;
    char path[255];

    dir = opendir(direct);
    while(entry = readdir(dir))
    {
        //if the entry, is a file (which is interpreted as ASCII so 8 = regular files)
        if(entry->d_type == 8)
        {
            //copy the parent directory into the path, add a / in front, and 
            //get the name of the file and concatenate it with the diretory path to get
            //the absolute path of the file and lastly get the size to add to 'sum'
            strcpy(path, direct);
            strcat(path, "/");
            strcat(path, entry->d_name);
            stat(path, &pathStat);
            sum += pathStat.st_size;
        }
        //if the entry, is a directory (which is interpreted as ASCII so 4 = directory)
        if(entry->d_type = 4)
        {
            //if the folder is just a '.' that is the parent directory and is to be ignored
            if(entry->d_name[0] != '.')
            {
                //copy the parent directory into the path, add a / in front, and 
                //get the name of the directory and concatenate it with the parent diretory path to get
                //the absolute path of the directory and lastly get the size to add to 'sum'
                strcpy(path, direct);
                strcat(path, "/");
                strcat(path, entry->d_name);
                //recall the recursion function to accomdate 'path' directory
                sum += traverse(path);
            }
        }
    }
    closedir(dir);
    return sum;
}

int main(void)
{
    long totSpace = 0;
    
    char CWD[255];
    //gets the current working directory and stores it in a buffer 'CWD'
    getcwd(CWD, 255);

    //calls the recursion function and stores the total byte size of the CWD and stores it in totSpace
    totSpace = traverse(CWD);

    printf("%ld\n", totSpace);
}

/*
Questions:
 1) Was one language easier or faster to write the code for this? If so, describe in detail
    why, as in what about the language made that case.
        - It was much easier and faster to write the code in java and python because they had
          various functions to easily find if something was a file or a directory and get the
          the size of them. Whereas C, required the usage of dirent which required pointers to
          be used to find the path of a file/folder and it's contents.
 2) Even though a language may not (e.g. FORTRAN) support recursion, describe how you could write
    a program to produce the same results without using recursion. Would that approach have any
    limitations and if so, what would they be?
        - You could store the contents of the CWD into arrays which will then go through each one
          adding up the sizes of each file, and recreating more arrays as more subdirectories show.
 */