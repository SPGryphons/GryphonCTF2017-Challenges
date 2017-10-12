
import java.util.Scanner;

/**
 *
 * @author chunyu
 */
public class soln {

    public static void main(String[] args) {
        // TODO code application logic here
        while(true){
          System.out.println("number => ");
          Scanner in = new Scanner(System.in);
          int num = in.nextInt();
          String[] a={"NSA","FBI","ABC","123","456","currently108elements","MD5","AES","CIA","ASD","KKK","GAK","286","420","BLA","ZEI","TXX","howslife?","idunnowhattowrite","d1ff1cul+","3e25y5y0u","1337","hax0r","whatsthis??????","iwonderthelengthofthisarray","magic","magi","mag","ma","mag","magi","magic","nothing","null","true","false","secret","agent","007","nowmuchmore","probablynotthatmuch","goodluck","longarrayislong","idontknowanymore","notascomplicatedasitlooks","orisitdifficult?","OUT","LINE","AVAIL","ABL","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","IWANTZEFLAG","FLAG","FLAGISNICEFLAG?","GIVEFLAGPLEASE","IAMHERE","MAGICALLY","IAMHERE","CHOOSEME","IAMHEREEE","HEREIAM","CHOOSEEMEEE","LINE14","ARRANGEME","WHOISTHEONE?","i am","isitme?","GCTF","admin","member","SHA512","WHATAMIDOING","IS","THIS","ASECR","ET","MESSAGE","???","ORISITNOT","IDONTACTUALLY","KNOW","HOWMANYELEMENTS","INTHIS","ARRAYOF","WORDS","NICESONGS","ILIKE","BADSONGS","IDONT","AN","EYEFO","RAN","EYE","303","8262017","PM","AM","SERVER","LOCA","LH","OST","LAST","ONE","DONE"};
          System.out.println(a[arrange(num)]);
        }
        
    }
    static int arrange(int i){
      i=i+3;
      i=(i/2);
      i=i*5-9*-11;
      i=i/2*4;
      i=i-200;
      i=i/2;
      i=i+100;
      i=i%100;
      i=i+20;

      if(i!=20){
        return i;

      }
      for(int k=0;k<4;k++)
        i=arrange(i);
      i=i+i;
      return i;
    }
    
}
