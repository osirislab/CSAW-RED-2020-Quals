#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int trademark(char password[]) {

   char key[]="supersupersupersecretdrm";
   char keyy[]="nofreelunches-orsoftware";
   char keyyy[]="pleasegivemunneytousedis";

   char secret[sizeof(key)];

   for(int i=0; i<sizeof(secret); i++) {
      secret[i] = key[i] ^ keyy[i];
      secret[i] = secret[i] ^ keyyy[i];
   }
   
   return !strcmp(password, secret);

}

void give_flag()
{
    char buf[29];
    FILE *f;
    f = fopen("flag.txt", "r");
    if (f != NULL)
    {
        fgets(buf, sizeof(buf), f);
        printf("Flag: %s\n", buf);
    } else
    {
        printf("Missing flag.txt. If you're running this on the server, please message an admin\n");
    }
}

int main() {

   char password[25];

   puts("Welcome to FlagGiver™ Enterprises' FlagGiver™!\n");
   puts("Please input the Password™ to recieve™ a Flag™:\n");
   
   fgets(password, sizeof(password), stdin);

   if(trademark(password)) {
      puts("Thank you for using™ FlagGiver™ Enterprises' FlagGiver™!\n");
      puts("Here is your FlagGiver™ Flag™! Enjoy™!\n");
      give_flag();
   } else {
      puts("Sorry™, that was the Wrong™ Password™.");
   }
   return 0;
}


