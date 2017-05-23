#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int seed;
int keys[256];
FILE *fp;

void cipher(char *flag) {
    int i,j;
    int l=strlen(flag);
    if (l>=256) {
        puts("Too long!");
        exit(-1);
    }
    keys[0]=seed%256;
    for (i=1;i<l;i++) 
        keys[i]=(keys[i-1]+1)%256;
    for (i=0;i<30;i++) {
        for (j=0;j<l;j++)
            if (i%2)
                flag[j]=flag[j]^keys[j];
            else
                flag[j]=(flag[j]+keys[j])%256;
        for (j=0;j<l;j++)
            keys[j]=(keys[j]*97+7)%256;
    }
    for (i=0;i<l;i++)
        putchar(flag[i]);
    putchar('\n');
}

int main() {
    char flag[46];
    char guess[46];
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    fp=fopen("/home/pwn3/flag1.txt", "r");
    fread(flag, 1, 46, fp);
    puts("key (0-255):");
    scanf("%d",&seed);
    puts("the encrypted flag is:");
    cipher(flag);
    puts("So show me the flag:");
    scanf("%s",guess);
    cipher(guess);
    if (strncmp(flag, guess, 46)==0) {
        puts("Great, here is your bonus:");
        system("cat bonus.txt");
        puts("but not a real bash");
    } else
        puts("Wrong!");
    fclose(fp);
    return 0;
}
