//Minh Trinh
//1001705984
//OpenJDK Runtime Environment Version 17.0.1
//Linux

import java.util.Properties;
import java.io.File;
import java.lang.object;
 
public class mat5984_lab01 {
   public static void main(String []args)
    {
       long totSpace = 0;
 
       //stores the current working directory in 'CWD'
       String CWD = System.getProperty("user.dir");
 
       //stores the CWD as a file
       File dir = new File(CWD);
 
       //stores the byte size after calling the recursion function into totspace
       totSpace = traverse(dir);
 
       //prints the total byte size of the CWD and its files and subdirectories
       System.out.println(totSpace + "\n");
 
   }
 
   public static long traverse(File dir)
   {
       long sum = 0;
 
       //lists all of the contents within the CWD and stores it in 'pathnames'
       File[] files = dir.listFiles();
 
       for(File file : files)
       {
           //if it is a file, store the byte size of file into size
           if(file.isFile())
           {
               sum += file.length();
           }
           //if it is a directory, call the 'traverse' function again to get the size of files within that specified directory
           if(file.isDirectory())
           {
                sum += traverse(file);
           }
       }
       return sum;
   }
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
