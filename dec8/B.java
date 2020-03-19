package com.company;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

public class B {
    public static void main(String[] args) throws Exception {
        int x = 25;
        int y = 6;

        //Reading file
        String wd = System.getProperty("user.dir");
        System.out.println(wd);
        File file = new File(wd + "\\src\\com\\company\\input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st = br.readLine();

        //Do thing
        String[] list = st.split("(?<=\\G.{" + (x*y) + "})");

        char temp;
        ArrayList<Character> tempList = new ArrayList<Character>();
        for(int i = 0; i < (x*y); i++){
            for(int j = 0; j < (list.length); j++) {
                temp = list[j].charAt(i);
                if (temp != '2') {
                    tempList.add(temp);
                    break;
                }
            }
        }

        for(int i=0; i < y; i++){
            for(int j=0; j < x; j++){
                System.out.print(tempList.get(x*i+j));
            }
            System.out.println();
        }
    }
}

