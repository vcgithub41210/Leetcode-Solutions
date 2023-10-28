import java.io.*;
import java.util.Scanner;
import java.util.List;
import java.util.HashMap;

class VowelPermutation{
    public static int Permutation(int vowel,int n,int[][] Vowelint,HashMap <List<Integer>,Integer> memo){
        if(n == 1) return 1;
        if(n == 2){
            if (vowel == 0 || vowel == 4) return 1;
            else if(vowel == 1||vowel == 3) return 2;
            else return 4;
        }
        if (memo.containsKey(List.of(n,vowel))) return memo.get(List.of(n,vowel));

        int value = 0;
        for(int j = 0; j < Vowelint[vowel].length;j++)
        {
            value += Permutation(Vowelint[vowel][j],n-1,Vowelint,memo);
        }
        memo.put(List.of(n,vowel),value);
        return value;

    }
    public static void main(String args[]){
        int[][] Vowelint = {{1},{0,2},{0,1,3,4},{2,4},{0}};
        HashMap<List<Integer>,Integer> memo = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the shit nigga: ");
        int N = sc.nextInt();
        int permutation = 0;
        for(int i = 0; i < 5;i++)
        {
            permutation += Permutation(i,N,Vowelint,memo);
        }
        System.out.println(permutation);
    }
}